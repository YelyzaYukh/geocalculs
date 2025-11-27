use crate::helpers::Point;
use crate::cercle::Cercle;
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::triangle::Triangle;
use crate::polygon::Polygone;

use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::carre_distance::dist_carre_cercle;
use crate::distances::point_distance::dist_point_segment;

use pyo3::prelude::*;

/// Distance point ↔ cercle
#[pyfunction]
pub fn dist_point_cercle(p: &Point, c: &Cercle) -> f64 {
    let dx = p.x - c.centre_x;
    let dy = p.y - c.centre_y;
    let d = (dx*dx + dy*dy).sqrt();
    (d - c.rayon).max(0.0)
}

/// Distance cercle ↔ cercle
#[pyfunction]
pub fn dist_cercle_cercle(c1: &Cercle, c2: &Cercle) -> f64 {
    let dx = c1.centre_x - c2.centre_x;
    let dy = c1.centre_y - c2.centre_y;
    let d = (dx*dx + dy*dy).sqrt();
    (d - c1.rayon - c2.rayon).max(0.0)
}

/// Distance cercle ↔ rectangle
#[pyfunction]
pub fn dist_cercle_rectangle(c: &Cercle, r: &Rectangle) -> f64 {
    let cx = c.centre_x.clamp(r.x, r.x + r.largeur);
    let cy = c.centre_y.clamp(r.y, r.y + r.hauteur);

    let dx = c.centre_x - cx;
    let dy = c.centre_y - cy;

    let d = (dx*dx + dy*dy).sqrt();
    (d - c.rayon).max(0.0)
}

/// Distance cercle ↔ carré
#[pyfunction]
pub fn dist_cercle_carre(c: &Cercle, car: &Carre) -> f64 {
    dist_carre_cercle(car, c)
}

/// Distance cercle ↔ triangle
#[pyfunction]
pub fn dist_cercle_triangle(c: &Cercle, t: &Triangle) -> f64 {
    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let cc = Point { x: t.cx, y: t.cy };

    let centre = Point { x: c.centre_x, y: c.centre_y };
    let r = c.rayon;

    // 1) distance sommet–cercle
    let mut best = dist_point_cercle(&a, c)
        .min(dist_point_cercle(&b, c))
        .min(dist_point_cercle(&cc, c));

    // 2) distance centre–segment - rayon
    let d1 = dist_point_segment(&centre, &a, &b) - r;
    let d2 = dist_point_segment(&centre, &b, &cc) - r;
    let d3 = dist_point_segment(&centre, &cc, &a) - r;

    best = best.min(d1).min(d2).min(d3);

    if best < 0.0 {
        0.0
    } else {
        best
    }
}

/// Distance cercle ↔ polygone
#[pyfunction]
pub fn dist_cercle_polygone(c: &Cercle, p: &Polygone) -> f64 {
    let mut best = f64::INFINITY;

    for (x, y) in &p.points {
        let pt = Point { x: *x, y: *y };
        best = best.min(dist_point_cercle(&pt, c));
    }

    best
}
