use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;
use crate::helpers::Point;

use crate::distances::rectangle_distance::dist_rect_rect;
use crate::distances::rectangle_distance::dist_point_rectangle;

use pyo3::prelude::*;

/// Convertit un carré → rectangle
pub fn carre_to_rect(c: &Carre) -> Rectangle {
    Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    }
}

#[pyfunction]
pub fn dist_point_carre(p: &Point, c: &Carre) -> f64 {
    let rect = carre_to_rect(c);
    dist_point_rectangle(p, &rect)
}


#[pyfunction]
pub fn dist_carre_cercle(c: &Carre, cercle: &Cercle) -> f64 {
    let rect = carre_to_rect(c);

    let min_x = rect.x;
    let max_x = rect.x + rect.largeur;
    let min_y = rect.y;
    let max_y = rect.y + rect.hauteur;

    let closest_x = cercle.centre_x.clamp(min_x, max_x);
    let closest_y = cercle.centre_y.clamp(min_y, max_y);

    let dx = cercle.centre_x - closest_x;
    let dy = cercle.centre_y - closest_y;

    let d = (dx * dx + dy * dy).sqrt();

    (d - cercle.rayon).max(0.0)
}

#[pyfunction]
pub fn dist_carre_rectangle(c: &Carre, r: &Rectangle) -> f64 {
    let rc = carre_to_rect(c);
    dist_rect_rect(&rc, r)
}

#[pyfunction]
pub fn dist_carre_carre(c1: &Carre, c2: &Carre) -> f64 {
    let r1 = carre_to_rect(c1);
    let r2 = carre_to_rect(c2);
    dist_rect_rect(&r1, &r2)
}

#[pyfunction]
pub fn dist_carre_triangle(c: &Carre, t: &Triangle) -> f64 {
    let rect = carre_to_rect(c);

    // Points du triangle
    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let cpt = Point { x: t.cx, y: t.cy };

    let d1 = dist_point_rectangle(&a, &rect);
    let d2 = dist_point_rectangle(&b, &rect);
    let d3 = dist_point_rectangle(&cpt, &rect);

    d1.min(d2).min(d3)
}

#[pyfunction]
pub fn dist_carre_polygone(c: &Carre, poly: &crate::polygon::Polygone) -> f64 {
    let rect = carre_to_rect(c);

    let mut min_dist = f64::INFINITY;

    // Parcours des sommets du polygone
    for &(x, y) in &poly.points {
        let p = Point { x, y };
        let d = dist_point_rectangle(&p, &rect);
        if d < min_dist {
            min_dist = d;
        }
    }

    min_dist
}

