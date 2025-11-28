use crate::helpers::Point;
use crate::polygon::Polygone;

use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;
use crate::losange::Losange;

use crate::distances::rectangle_distance::{
    dist_point_rectangle,
    dist_rect_rect,
};



use crate::distances::carre_distance::carre_to_rect;

use pyo3::prelude::*;


fn losange_to_rect(l: &Losange) -> Rectangle {
    Rectangle {
        x: l.x - l.largeur / 2.0,
        y: l.y - l.hauteur / 2.0,
        largeur: l.largeur,
        hauteur: l.hauteur,
    }
}

/// Convertit Polygone → Vec<Point>
fn points_polygone(p: &Polygone) -> Vec<Point> {
    p.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}


#[pyfunction]
pub fn dist_point_losange(p: &Point, l: &Losange) -> f64 {
    let rect = losange_to_rect(l);
    dist_point_rectangle(p, &rect)
}


#[pyfunction]
pub fn dist_losange_cercle(l: &Losange, c: &Cercle) -> f64 {
    // On convertit le losange en rectangle
    let rect = losange_to_rect(l);

    // Distance cercle ↔ rectangle déjà correcte :
    // = distance du centre au rectangle – rayon
    let closest_x = c.centre_x.clamp(rect.x, rect.x + rect.largeur);
    let closest_y = c.centre_y.clamp(rect.y, rect.y + rect.hauteur);

    let dx = c.centre_x - closest_x;
    let dy = c.centre_y - closest_y;

    let d = (dx * dx + dy * dy).sqrt();

    (d - c.rayon).max(0.0)
}


#[pyfunction]
pub fn dist_losange_rectangle(l: &Losange, r: &Rectangle) -> f64 {
    let rect_l = losange_to_rect(l);
    dist_rect_rect(&rect_l, r)
}


#[pyfunction]
pub fn dist_losange_carre(l: &Losange, c: &Carre) -> f64 {
    let rect_l = losange_to_rect(l);
    let rect_c = carre_to_rect(c);
    dist_rect_rect(&rect_l, &rect_c)
}


#[pyfunction]
pub fn dist_losange_triangle(l: &Losange, t: &Triangle) -> f64 {
    let rect = losange_to_rect(l);

    let pts = vec![
        Point { x: t.ax, y: t.ay },
        Point { x: t.bx, y: t.by },
        Point { x: t.cx, y: t.cy },
    ];

    pts.iter()
        .map(|p| dist_point_rectangle(p, &rect))
        .fold(f64::INFINITY, f64::min)
}


#[pyfunction]
pub fn dist_losange_polygone(l: &Losange, p: &Polygone) -> f64 {
    let rect = losange_to_rect(l);

    points_polygone(p)
        .iter()
        .map(|pt| dist_point_rectangle(pt, &rect))
        .fold(f64::INFINITY, f64::min)
}


#[pyfunction]
pub fn dist_losange_losange(l1: &Losange, l2: &Losange) -> f64 {
    let r1 = losange_to_rect(l1);
    let r2 = losange_to_rect(l2);

    dist_rect_rect(&r1, &r2)
}
