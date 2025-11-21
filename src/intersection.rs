use pyo3::prelude::*;
use crate::cercle::Cercle;
use crate::carre::Carre;
use crate::rectangle::Rectangle;

/// Type enum pour identifier ce que l'utilisateur envoie
enum Geometrie {
    Cercle(Cercle),
    Rect(Rectangle),
}

/// Helper pour convertir un Carré en Rectangle (car la logique est la même)
fn carre_vers_rect(c: &Carre) -> Rectangle {
    Rectangle { x: c.x, y: c.y, largeur: c.cote, hauteur: c.cote }
}

/// Helper pour extraire la forme depuis un objet Python générique
fn extraire_forme(obj: &Bound<'_, PyAny>) -> PyResult<Geometrie> {
    // 1. Est-ce un Cercle ?
    if let Ok(c) = obj.extract::<Cercle>() {
        return Ok(Geometrie::Cercle(c));
    }
    // 2. Est-ce un Rectangle ?
    if let Ok(r) = obj.extract::<Rectangle>() {
        return Ok(Geometrie::Rect(r));
    }
    // 3. Est-ce un Carré ? (On le convertit en Rectangle)
    if let Ok(c) = obj.extract::<Carre>() {
        return Ok(Geometrie::Rect(carre_vers_rect(&c)));
    }
    
    Err(pyo3::exceptions::PyTypeError::new_err(
        "Type de forme non supporté pour l'intersection"
    ))
}

// --- ALGORITHMES DE COLLISION ---

fn collide_rect_rect(r1: &Rectangle, r2: &Rectangle) -> bool {
    // Logique AABB (Axis-Aligned Bounding Box)
    r1.x < r2.x + r2.largeur &&
    r1.x + r1.largeur > r2.x &&
    r1.y < r2.y + r2.hauteur &&
    r1.y + r1.hauteur > r2.y
}

fn collide_cercle_cercle(c1: &Cercle, c2: &Cercle) -> bool {
    let dx = c1.centre_x - c2.centre_x;
    let dy = c1.centre_y - c2.centre_y;
    let distance_sq = dx*dx + dy*dy;
    let rayons_sum = c1.rayon + c2.rayon;
    distance_sq < rayons_sum * rayons_sum
}

fn collide_rect_cercle(rect: &Rectangle, cerc: &Cercle) -> bool {
    // Trouver le point du rectangle le plus proche du centre du cercle
    // clamp(value, min, max)
    let closest_x = cerc.centre_x.max(rect.x).min(rect.x + rect.largeur);
    let closest_y = cerc.centre_y.max(rect.y).min(rect.y + rect.hauteur);

    let dx = cerc.centre_x - closest_x;
    let dy = cerc.centre_y - closest_y;

    (dx*dx + dy*dy) < (cerc.rayon * cerc.rayon)
}

/// LA SUPER FONCTION UNIQUE
#[pyfunction]
#[pyo3(signature = (forme_a, forme_b, mode="bool"))] // mode par défaut = "bool"
pub fn intersecte(forme_a: &Bound<'_, PyAny>, forme_b: &Bound<'_, PyAny>, mode: &str) -> PyResult<bool> {
    
    // Pour l'instant, on ne gère que le mode "bool" (Vrai/Faux)
    if mode != "bool" {
        return Err(pyo3::exceptions::PyValueError::new_err("Seul le mode 'bool' est supporté pour le moment."));
    }

    let geom_a = extraire_forme(forme_a)?;
    let geom_b = extraire_forme(forme_b)?;

    let resultat = match (geom_a, geom_b) {
        // Rectangle vs Rectangle
        (Geometrie::Rect(r1), Geometrie::Rect(r2)) => collide_rect_rect(&r1, &r2),
        
        // Cercle vs Cercle
        (Geometrie::Cercle(c1), Geometrie::Cercle(c2)) => collide_cercle_cercle(&c1, &c2),
        
        // Mixte : Rectangle vs Cercle
        (Geometrie::Rect(r), Geometrie::Cercle(c)) => collide_rect_cercle(&r, &c),
        (Geometrie::Cercle(c), Geometrie::Rect(r)) => collide_rect_cercle(&r, &c),
    };

    Ok(resultat)
}