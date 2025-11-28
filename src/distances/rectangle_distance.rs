use crate::rectangle::Rectangle;
use crate::helpers::Point;
use pyo3::prelude::*;

#[pyfunction]
pub fn dist_point_rectangle(p: &Point, r: &Rectangle) -> f64 {
    let x = p.x;
    let y = p.y;

    let closest_x = x.clamp(r.x, r.x + r.largeur);
    let closest_y = y.clamp(r.y, r.y + r.hauteur);

    let dx = x - closest_x;
    let dy = y - closest_y;

    (dx*dx + dy*dy).sqrt()
}

#[pyfunction]
pub fn dist_rect_rect(r1: &Rectangle, r2: &Rectangle) -> f64 {

    let dx = if r1.x > r2.x + r2.largeur {
        r1.x - (r2.x + r2.largeur)
    } else if r2.x > r1.x + r1.largeur {
        r2.x - (r1.x + r1.largeur)
    } else {
        0.0
    };

    let dy = if r1.y > r2.y + r2.hauteur {
        r1.y - (r2.y + r2.hauteur)
    } else if r2.y > r1.y + r1.hauteur {
        r2.y - (r1.y + r1.hauteur)
    } else {
        0.0
    };

    (dx*dx + dy*dy).sqrt()
}
#[pyfunction]
pub fn dist_rectangle_carre(r: &Rectangle, c: &crate::carre::Carre) -> f64 {
    let rc = Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    };
    dist_rect_rect(r, &rc)
}
#[pyfunction]
pub fn dist_rectangle_cercle(r: &Rectangle, cercle: &crate::cercle::Cercle) -> f64 {
    let min_x = r.x;
    let max_x = r.x + r.largeur;

    let min_y = r.y;
    let max_y = r.y + r.hauteur;

    let closest_x = cercle.centre_x.clamp(min_x, max_x);
    let closest_y = cercle.centre_y.clamp(min_y, max_y);

    let dx = cercle.centre_x - closest_x;
    let dy = cercle.centre_y - closest_y;

    let d = (dx*dx + dy*dy).sqrt();

    (d - cercle.rayon).max(0.0)
}
#[pyfunction]
pub fn dist_rectangle_triangle(r: &Rectangle, t: &crate::triangle::Triangle) -> f64 {
    use crate::helpers::Point;

    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let c = Point { x: t.cx, y: t.cy };

    let d1 = dist_point_rectangle(&a, r);
    let d2 = dist_point_rectangle(&b, r);
    let d3 = dist_point_rectangle(&c, r);

    d1.min(d2).min(d3)
}
#[pyfunction]
pub fn dist_rectangle_polygone(r: &Rectangle, poly: &crate::polygon::Polygone) -> f64 {
    use crate::helpers::Point;

    let mut min_dist = f64::INFINITY;

    for &(x, y) in &poly.points {
        let p = Point { x, y };
        let d = dist_point_rectangle(&p, r);
        if d < min_dist {
            min_dist = d;
        }
    }

    min_dist
}
