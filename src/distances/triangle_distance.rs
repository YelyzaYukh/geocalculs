use crate::triangle::Triangle;
use crate::helpers::Point;

use crate::distances::point_distance::{dist_point_point, dist_point_polygone, dist_point_segment};
use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::cercle_distance::dist_point_cercle;

use crate::rectangle::Rectangle;
use crate::carre::Carre;
use crate::cercle::Cercle;
use crate::polygon::Polygone;

use pyo3::prelude::*;

/// Convertit triangle → liste de points
fn tri_pts(t: &Triangle) -> [Point; 3] {
    [
        Point { x: t.ax, y: t.ay },
        Point { x: t.bx, y: t.by },
        Point { x: t.cx, y: t.cy },
    ]
}

/// ----------------------------------------------
///  VERSION PURE RUST : ORIENTATION
/// ----------------------------------------------
fn orient(a: &Point, b: &Point, c: &Point) -> f64 {
    (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
}

/// ----------------------------------------------
///  Test point inside triangle
/// ----------------------------------------------
fn point_in_triangle(p: &Point, a: &Point, b: &Point, c: &Point) -> bool {
    let v0 = (c.x - a.x, c.y - a.y);
    let v1 = (b.x - a.x, b.y - a.y);
    let v2 = (p.x - a.x, p.y - a.y);

    let dot00 = v0.0 * v0.0 + v0.1 * v0.1;
    let dot01 = v0.0 * v1.0 + v0.1 * v1.1;
    let dot02 = v0.0 * v2.0 + v0.1 * v2.1;
    let dot11 = v1.0 * v1.0 + v1.1 * v1.1;
    let dot12 = v1.0 * v2.0 + v1.1 * v2.1;

    let inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01);

    let u = (dot11 * dot02 - dot01 * dot12) * inv_denom;
    let v = (dot00 * dot12 - dot01 * dot02) * inv_denom;

    // inside si u >= 0, v >= 0 et u + v <= 1
    u >= 0.0 && v >= 0.0 && (u + v) <= 1.0
}


/// ========== DISTANCE POINT ↔ TRIANGLE ==========
#[pyfunction]
pub fn dist_point_triangle(p: &Point, t: &Triangle) -> f64 {
    let pts = tri_pts(t);
    let (a, b, c) = (&pts[0], &pts[1], &pts[2]);

    // Si le point est dedans → 0
    if point_in_triangle(p, a, b, c) {
        return 0.0;
    }

    // Sinon distance segment
    dist_point_segment(p, a, b)
        .min(dist_point_segment(p, b, c))
        .min(dist_point_segment(p, c, a))
}

/// ========== TRIANGLE ↔ TRIANGLE ==========
#[pyfunction]
pub fn dist_triangle_triangle(t1: &Triangle, t2: &Triangle) -> f64 {
    let p1 = tri_pts(t1);
    let p2 = tri_pts(t2);

    // collision ?
    for p in &p1 {
        if dist_point_triangle(p, t2) == 0.0 {
            return 0.0;
        }
    }
    for p in &p2 {
        if dist_point_triangle(p, t1) == 0.0 {
            return 0.0;
        }
    }

    // distance segment-segment complète
    let seg1 = [(&p1[0], &p1[1]), (&p1[1], &p1[2]), (&p1[2], &p1[0])];
    let seg2 = [(&p2[0], &p2[1]), (&p2[1], &p2[2]), (&p2[2], &p2[0])];

    let mut best = f64::INFINITY;

    for (a1, b1) in seg1 {
        for (a2, b2) in seg2 {
            best = best
                .min(dist_point_segment(a1, a2, b2))
                .min(dist_point_segment(b1, a2, b2))
                .min(dist_point_segment(a2, a1, b1))
                .min(dist_point_segment(b2, a1, b1));
        }
    }

    best
}


/// ========== TRIANGLE ↔ CERCLE ==========
#[pyfunction]
pub fn dist_triangle_cercle(t: &Triangle, c: &Cercle) -> f64 {
    let pts = tri_pts(t);

    let cx = c.centre_x;
    let cy = c.centre_y;
    let r = c.rayon;

    let centre = Point { x: cx, y: cy };

    // distance sommet–cercle
    let mut best = pts
        .iter()
        .map(|p| dist_point_cercle(p, c))
        .fold(f64::INFINITY, f64::min);

    // distance centre–segments - rayon
    let d1 = dist_point_segment(&centre, &pts[0], &pts[1]) - r;
    let d2 = dist_point_segment(&centre, &pts[1], &pts[2]) - r;
    let d3 = dist_point_segment(&centre, &pts[2], &pts[0]) - r;

    best = best.min(d1).min(d2).min(d3);

    if best < 0.0 {
        0.0
    } else {
        best
    }
}

/// ========== TRIANGLE ↔ CARRE ==========
#[pyfunction]
pub fn dist_triangle_carre(t: &Triangle, c: &Carre) -> f64 {
    let rect = Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    };
    dist_triangle_rectangle(t, &rect)
}

/// ========== TRIANGLE ↔ RECTANGLE ==========
#[pyfunction]
pub fn dist_triangle_rectangle(t: &Triangle, r: &Rectangle) -> f64 {
    let pts = tri_pts(t);

    pts.iter()
        .map(|p| dist_point_rectangle(p, r))
        .fold(f64::INFINITY, f64::min)
}

/// ========== TRIANGLE ↔ POLYGONE ==========
#[pyfunction]
pub fn dist_triangle_polygone(t: &Triangle, poly: &Polygone) -> f64 {
    let tri = [
        Point { x: t.ax, y: t.ay },
        Point { x: t.bx, y: t.by },
        Point { x: t.cx, y: t.cy },
    ];

    let pts = &poly.points;
    let mut best = f64::INFINITY;

    // collision ? (un sommet du polygone dans le triangle)
    for (x, y) in pts {
        if dist_point_triangle(&Point { x: *x, y: *y }, t) == 0.0 {
            return 0.0;
        }
    }

    // distance sommet triangle → polygone
    for tp in &tri {
        best = best.min(dist_point_polygone(tp, poly));
    }

    // distance sommet polygone → triangle
    for (x, y) in pts {
        let p = Point { x: *x, y: *y };
        best = best.min(dist_point_triangle(&p, t));
    }

    best
}

