use crate::helpers::Point;
use crate::polygon::Polygone;

use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;

use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::cercle_distance::dist_point_cercle;
use crate::distances::point_distance::dist_point_point;

use pyo3::prelude::*;

/// Transforme un Polygone en liste de Points
fn points_polygone(poly: &Polygone) -> Vec<Point> {
    poly.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}

/// ---------------------------------------------------------
///   Test si un point est à l’intérieur d’un polygone (ray casting)
/// ---------------------------------------------------------
fn point_in_poly(px: f64, py: f64, pts: &[(f64, f64)]) -> bool {
    let mut inside = false;
    let n = pts.len();

    for i in 0..n {
        let (x1, y1) = pts[i];
        let (x2, y2) = pts[(i + 1) % n];

        let intersects = ((y1 > py) != (y2 > py))
            && (px < (x2 - x1) * (py - y1) / (y2 - y1 + 1e-12) + x1);

        if intersects {
            inside = !inside;
        }
    }

    inside
}

//
// ---------------------------------------------------------
//         POLYGONE ↔ CARRE
// ---------------------------------------------------------
//
#[pyfunction]
pub fn dist_carre_polygone(carre: &Carre, poly: &Polygone) -> f64 {
    let rect = Rectangle {
        x: carre.x,
        y: carre.y,
        largeur: carre.cote,
        hauteur: carre.cote,
    };

    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, &rect))
        .fold(f64::INFINITY, f64::min)
}

//
// ---------------------------------------------------------
//         POLYGONE ↔ RECTANGLE
// ---------------------------------------------------------
//
#[pyfunction]
pub fn dist_rectangle_polygone(rect: &Rectangle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, rect))
        .fold(f64::INFINITY, f64::min)
}

//
// ---------------------------------------------------------
//         POLYGONE ↔ CERCLE
// ---------------------------------------------------------
//
#[pyfunction]
pub fn dist_cercle_polygone(cercle: &Cercle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_cercle(p, cercle))
        .fold(f64::INFINITY, f64::min)
}

//
// ---------------------------------------------------------
//         POLYGONE ↔ TRIANGLE
// ---------------------------------------------------------
//
#[pyfunction]
pub fn dist_triangle_polygone(tri: &Triangle, poly: &Polygone) -> f64 {

    let tri_pts = vec![
        Point { x: tri.ax, y: tri.ay },
        Point { x: tri.bx, y: tri.by },
        Point { x: tri.cx, y: tri.cy },
    ];

    let poly_pts = points_polygone(poly);

    let mut min = f64::INFINITY;

    for tp in &tri_pts {
        for pp in &poly_pts {
            let dx = tp.x - pp.x;
            let dy = tp.y - pp.y;
            let d = (dx * dx + dy * dy).sqrt();
            if d < min {
                min = d;
            }
        }
    }

    min
}

/// ---------------------------------------------------------
///     POLYGONE ↔ POLYGONE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_poly_poly(p1: &Polygone, p2: &Polygone) -> f64 {

    let pts1 = points_polygone(p1);
    let pts2 = points_polygone(p2);

    // 1) Vérif : si un point de p1 est dans p2 → overlap
    for a in &p1.points {
        if point_in_poly(a.0, a.1, &p2.points) {
            return 0.0;
        }
    }
    // 2) Vérif : si un point de p2 est dans p1 → overlap
    for b in &p2.points {
        if point_in_poly(b.0, b.1, &p1.points) {
            return 0.0;
        }
    }

    // 3) sinon distance minimale des sommets
    let mut min = f64::INFINITY;

    for a in &pts1 {
        for b in &pts2 {
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = (dx*dx + dy*dy).sqrt();
            if dist < min {
                min = dist;
            }
        }
    }

    min
}


/// ===============================================================
///     DISTANCE POINT → POLYGONE
/// ===============================================================
#[pyfunction]
pub fn dist_point_polygone(p: &Point, poly: &Polygone) -> f64 {

    // 1) TEST : si point à l'intérieur → distance = 0
    if point_in_poly(p.x, p.y, &poly.points) {
        return 0.0;
    }

    // 2) Distance minimale aux sommets
    let mut best = f64::INFINITY;

    for (x, y) in &poly.points {
        let q = Point { x: *x, y: *y };
        best = best.min(dist_point_point(p, &q));
    }

    best
}
