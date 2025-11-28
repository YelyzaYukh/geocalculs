use crate::helpers::Point;
use crate::triangle::Triangle;
use crate::rectangle::Rectangle;
use crate::carre::Carre;
use crate::cercle::Cercle;
use crate::polygon::Polygone;

use crate::distances::rectangle_distance::{
    dist_point_rectangle,
    dist_rect_rect,
    dist_rectangle_cercle,
};

use crate::distances::point_distance::{
    dist_point_point,
    dist_point_polygone,
};

use pyo3::prelude::*;

/// ----------------------------------------------------------
///  Bounding box (AABB) du triangle
/// ----------------------------------------------------------
fn tri_aabb(t: &Triangle) -> Rectangle {
    let xs = [t.ax, t.bx, t.cx];
    let ys = [t.ay, t.by, t.cy];

    let xmin = xs.iter().cloned().fold(f64::INFINITY, f64::min);
    let xmax = xs.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    let ymin = ys.iter().cloned().fold(f64::INFINITY, f64::min);
    let ymax = ys.iter().cloned().fold(f64::NEG_INFINITY, f64::max);

    Rectangle {
        x: xmin,
        y: ymin,
        largeur: xmax - xmin,
        hauteur: ymax - ymin,
    }
}

/// ----------------------------------------------------------
///   1) DISTANCE POINT ↔ TRIANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_point_triangle(p: &Point, t: &Triangle) -> f64 {
    let r = tri_aabb(t);
    dist_point_rectangle(p, &r)
}

/// ----------------------------------------------------------
///   2) TRIANGLE ↔ TRIANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_triangle(t1: &Triangle, t2: &Triangle) -> f64 {
    let r1 = tri_aabb(t1);
    let r2 = tri_aabb(t2);
    dist_rect_rect(&r1, &r2)
}

/// ----------------------------------------------------------
///   3) TRIANGLE ↔ CERCLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_cercle(t: &Triangle, c: &Cercle) -> f64 {
    let r = tri_aabb(t);
    dist_rectangle_cercle(&r, c)
}

/// ----------------------------------------------------------
///   4) TRIANGLE ↔ RECTANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_rectangle(t: &Triangle, r: &Rectangle) -> f64 {
    let rt = tri_aabb(t);
    dist_rect_rect(&rt, r)
}

/// ----------------------------------------------------------
///   5) TRIANGLE ↔ CARRE (via rect)
/// ----------------------------------------------------------
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

/// ----------------------------------------------------------
///   6) TRIANGLE ↔ POLYGONE (via AABB rectangle)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_polygone(t: &Triangle, poly: &Polygone) -> f64 {
    let tri_box = tri_aabb(t);

    // Distance du rectangle contenant le triangle ↔ polygone
    crate::distances::polygon_distance::dist_rectangle_polygone(&tri_box, poly)
}
