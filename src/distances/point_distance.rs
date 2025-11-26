use crate::helpers::Point;
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::triangle::Triangle;
use crate::cercle::Cercle;
use crate::polygon::Polygone;
use crate::losange::Losange;

/// ------------------------------------------------------
/// DISTANCE POINT ↔ POINT
/// ------------------------------------------------------
#[inline]
pub fn dist_point_point(a: &Point, b: &Point) -> f64 {
    ((b.x - a.x).powi(2) + (b.y - a.y).powi(2)).sqrt()
}

/// ------------------------------------------------------
/// DISTANCE POINT ↔ SEGMENT
/// ------------------------------------------------------
pub fn dist_point_segment(p: &Point, a: &Point, b: &Point) -> f64 {
    let abx = b.x - a.x;
    let aby = b.y - a.y;

    let apx = p.x - a.x;
    let apy = p.y - a.y;

    let ab_len2 = abx*abx + aby*aby;

    if ab_len2 == 0.0 {
        return ((p.x - a.x).powi(2) + (p.y - a.y).powi(2)).sqrt();
    }

    let t = (apx*abx + apy*aby) / ab_len2;

    if t <= 0.0 {
        return ((p.x - a.x).powi(2) + (p.y - a.y).powi(2)).sqrt();
    }
    if t >= 1.0 {
        return ((p.x - b.x).powi(2) + (p.y - b.y).powi(2)).sqrt();
    }

    let projx = a.x + t * abx;
    let projy = a.y + t * aby;

    ((p.x - projx).powi(2) + (p.y - projy).powi(2)).sqrt()
}


/// ------------------------------------------------------
/// DISTANCE POINT ↔ RECTANGLE (AABB)
/// ------------------------------------------------------
pub fn dist_point_rectangle(p: &Point, r: &Rectangle) -> f64 {
    let dx = if p.x < r.x {
        r.x - p.x
    } else if p.x > r.x + r.largeur {
        p.x - (r.x + r.largeur)
    } else {
        0.0
    };

    let dy = if p.y < r.y {
        r.y - p.y
    } else if p.y > r.y + r.hauteur {
        p.y - (r.y + r.hauteur)
    } else {
        0.0
    };

    (dx * dx + dy * dy).sqrt()
}

/// ------------------------------------------------------
/// DISTANCE POINT ↔ CARRE
/// ------------------------------------------------------
pub fn dist_point_carre(p: &Point, c: &Carre) -> f64 {
    // On traite le carré comme rectangle
    let rect = Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    };
    dist_point_rectangle(p, &rect)
}

/// ------------------------------------------------------
/// DISTANCE POINT ↔ CERCLE
/// ------------------------------------------------------
pub fn dist_point_cercle(p: &Point, c: &Cercle) -> f64 {
    let centre = Point {
        x: c.centre_x,
        y: c.centre_y,
    };
    let d = dist_point_point(p, &centre);
    (d - c.rayon).max(0.0)
}

/// ------------------------------------------------------
/// DISTANCE POINT ↔ TRIANGLE
/// ------------------------------------------------------

fn point_in_triangle(p: &Point, a: &Point, b: &Point, c: &Point) -> bool {
    let v0 = (c.x - a.x, c.y - a.y);
    let v1 = (b.x - a.x, b.y - a.y);
    let v2 = (p.x - a.x, p.y - a.y);

    let dot00 = v0.0*v0.0 + v0.1*v0.1;
    let dot01 = v0.0*v1.0 + v0.1*v1.1;
    let dot02 = v0.0*v2.0 + v0.1*v2.1;
    let dot11 = v1.0*v1.0 + v1.1*v1.1;
    let dot12 = v1.0*v2.0 + v1.1*v2.1;

    let inv = 1.0 / (dot00*dot11 - dot01*dot01);

    let u = (dot11*dot02 - dot01*dot12) * inv;
    let v = (dot00*dot12 - dot01*dot02) * inv;

    u >= 0.0 && v >= 0.0 && u + v <= 1.0
}

pub fn dist_point_triangle(p: &Point, t: &Triangle) -> f64 {
    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let c = Point { x: t.cx, y: t.cy };

    // 1) Vérifier si triangle dégénéré (aligné)
    let orient = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);

    if orient == 0.0 {
        // DISTANCE AU SEGMENT LE PLUS PROCHE (triangle plat = segment)
        return dist_point_segment(p, &a, &b)
            .min(dist_point_segment(p, &b, &c))
            .min(dist_point_segment(p, &c, &a));
    }

    // 2) Triangle non aligné → test standard
    if point_in_triangle(p, &a, &b, &c) {
        return 0.0;
    }

    // 3) Distance aux segments sinon
    dist_point_segment(p, &a, &b)
        .min(dist_point_segment(p, &b, &c))
        .min(dist_point_segment(p, &c, &a))
}



/// ------------------------------------------------------
/// DISTANCE POINT ↔ POLYGONE
/// ------------------------------------------------------
pub fn dist_point_polygone(p: &Point, poly: &Polygone) -> f64 {
    let pts = &poly.points;

    // Si moins de 2 points → aucun bord
    if pts.len() < 2 {
        // si un seul point → distance simple
        if pts.len() == 1 {
            let a = Point { x: pts[0].0, y: pts[0].1 };
            return dist_point_point(p, &a);
        }
        return f64::INFINITY;
    }

    let mut min = f64::INFINITY;

    for i in 0..pts.len() {
        let (x1, y1) = pts[i];
        let (x2, y2) = pts[(i + 1) % pts.len()];
        let a = Point { x: x1, y: y1 };
        let b = Point { x: x2, y: y2 };
        min = min.min(dist_point_segment(p, &a, &b));
    }

    min
}

/// ------------------------------------------------------
/// DISTANCE POINT ↔ LOSANGE (approx. par rectangle bounding)
/// ------------------------------------------------------
pub fn dist_point_losange(p: &Point, l: &Losange) -> f64 {
    // approximation : le losange est vu comme rectangle extérieur
    let rect = Rectangle {
        x: l.x - l.largeur / 2.0,
        y: l.y - l.hauteur / 2.0,
        largeur: l.largeur,
        hauteur: l.hauteur,
    };
    dist_point_rectangle(p, &rect)
}
