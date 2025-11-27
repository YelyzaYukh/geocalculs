use crate::helpers::Point;
use crate::polygon::Polygone;

use pyo3::prelude::*;
use pyo3::types::{PyAny, PyAnyMethods};

use crate::triangle_plat::TrianglePlat;
use crate::distances::segment_distance::dist_segment_point;

use crate::triangle::Triangle;

use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;

use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::cercle_distance::dist_point_cercle;
use crate::distances::point_distance::dist_point_point;

/// Convert polygone → Points
fn points_polygone(poly: &Polygone) -> Vec<Point> {
    poly.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}

/// Ray casting
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


/// ------------------ CARRE ↔ POLYGONE ------------------
#[pyfunction]
pub fn dist_carre_polygone(c: &Carre, poly: &Polygone) -> f64 {
    let rect = Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    };

    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, &rect))
        .fold(f64::INFINITY, f64::min)
}


/// ------------------ RECTANGLE ↔ POLYGONE ------------------
#[pyfunction]
pub fn dist_rectangle_polygone(rect: &Rectangle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, rect))
        .fold(f64::INFINITY, f64::min)
}


/// ------------------ CERCLE ↔ POLYGONE ------------------
#[pyfunction]
pub fn dist_cercle_polygone(c: &Cercle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_cercle(p, c))
        .fold(f64::INFINITY, f64::min)
}


/// ------------------ SEGMENT ↔ POLYGONE ------------------
fn distance_segment_polygone(t: &TrianglePlat, poly: &Polygone) -> f64 {
    let mut best = f64::INFINITY;

    for (x, y) in &poly.points {
        best = best.min(dist_segment_point(t.ax, t.ay, t.cx, t.cy, *x, *y));
    }

    best
}


/// ------------------ TRIANGLE ↔ POLYGONE ------------------
fn distance_triangle_polygone(t: &TrianglePlat, poly: &Polygone) -> f64 {
    let mut best = f64::INFINITY;

    for (x, y) in &poly.points {
        let p = Point { x: *x, y: *y };
        best = best.min(t.dist_point(&p));
    }

    best
}



#[pyfunction]
pub fn distance_triangle_polygone(tri: &TrianglePlat, poly: &Polygone) -> f64 {
    let pts = [
        Point { x: tri.ax, y: tri.ay },
        Point { x: tri.bx, y: tri.by },
        Point { x: tri.cx, y: tri.cy },
    ];

    let mut best = f64::INFINITY;

    for p in pts {
        best = best.min(dist_point_polygone(&p, poly));
    }

    best
}




/// ------------------ POLYGONE ↔ POLYGONE ------------------
#[pyfunction]
pub fn dist_poly_poly(p1: &Polygone, p2: &Polygone) -> f64 {
    let pts1 = points_polygone(p1);
    let pts2 = points_polygone(p2);

    // Overlap
    for a in &p1.points {
        if point_in_poly(a.0, a.1, &p2.points) {
            return 0.0;
        }
    }
    for b in &p2.points {
        if point_in_poly(b.0, b.1, &p1.points) {
            return 0.0;
        }
    }

    // Sinon distance min
    let mut min = f64::INFINITY;

    for a in &pts1 {
        for b in &pts2 {
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = (dx*dx + dy*dy).sqrt();
            min = min.min(dist);
        }
    }

    min
}


/// ------------------ POINT ↔ POLYGONE ------------------
#[pyfunction]
pub fn dist_point_polygone(p: &Point, poly: &Polygone) -> f64 {

    if point_in_poly(p.x, p.y, &poly.points) {
        return 0.0;
    }

    let mut best = f64::INFINITY;

    for (x, y) in &poly.points {
        let q = Point { x: *x, y: *y };
        best = best.min(dist_point_point(p, &q));
    }

    best
}

pub fn dist_segment_polygone(seg: &TrianglePlat, poly: &Polygone) -> f64 {
    let (x1, y1, x2, y2) = seg.segment();

    let p1 = Point { x: x1, y: y1 };
    let p2 = Point { x: x2, y: y2 };

    let mut best = f64::INFINITY;

    for (x, y) in &poly.points {
        let q = Point { x: *x, y: *y };
        best = best.min(dist_segment_point(&p1, &p2, &q));
    }

    best
}

