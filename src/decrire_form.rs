#[derive(Debug, Clone)]
pub struct DescriptionForme {
    pub nom: String,
    pub description: String,
    pub parametres_attendus: Vec<String>,
    pub formules: Vec<String>,
}

pub fn decrire_forme(
    forme: &str,
) -> DescriptionForme {
    let mut result = DescriptionForme {
        nom: forme.to_string(),
        description: String::new(),
        parametres_attendus: vec![],
        formules: vec![],
    };

    let key = forme.to_lowercase();

    match key.as_str() {
        // ---------------------------
        // CERCLE
        // ---------------------------
        "cercle" | "circle" => {
            result.description = "Ensemble des points à distance fixe (rayon r) d'un centre.".into();
            result.parametres_attendus = vec!["r (rayon)".into(), "centre (x,y)".into()];
            result.formules = vec![
                "Aire = π · r²".into(),
                "Périmètre = 2 · π · r".into(),
                "Diamètre = 2 · r".into(),
            ];

        }

        // ---------------------------
        // RECTANGLE
        // ---------------------------
        "rectangle" => {
            result.description =
                "Quadrilatère avec côtés opposés égaux et angles droits.".into();
            result.parametres_attendus = vec!["a (côté horizontal)".into(), "b (côté vertical)".into()];
            result.formules = vec![
                "Aire = a · b".into(),
                "Périmètre = 2 · (a + b)".into(),
                "Diagonale = sqrt(a² + b²)".into(),
            ];

        }

        // ---------------------------
        // CARRE
        // ---------------------------
        "carre" | "square" => {
            result.description = "Carré : 4 côtés égaux, angles droits.".into();
            result.parametres_attendus = vec!["a (côté)".into(), "(option) x,y coin sup.gauche".into()];
            result.formules = vec![
                "Aire = a²".into(),
                "Périmètre = 4 · a".into(),
                "Diagonale = a · √2".into(),
            ];

        }

        // ---------------------------
        // TRIANGLE
        // ---------------------------
        "triangle" => {
            result.description = "Polygone à 3 côtés.".into();
            result.parametres_attendus = vec![
                "a.x,a.y; b.x, b.y; c.x,c.y".into(),
                "(les points de chaque côté)".into(),
            ];

            result.formules = vec![
                "Aire (Heron) = √(s(s-a)(s-b)(s-c))".into(),
                "Périmètre = a + b + c".into(),
            ];

        }

        // =====================================================
        // LOSANGE
        // =====================================================
        "losange" | "rhombus" | "rhomb" => {
            result.description = "Losange : 4 côtés égaux, diagonales perpendiculaires.".into();
            result.parametres_attendus = vec![
                "a (côté)".into(),
                "diagonales d1, d2".into(),
            ];
            result.formules = vec![
                "Aire = (d1 · d2) / 2".into(),
                "Périmètre = 4 · a".into(),
            ];

        }

        // =====================================================
        // POLYGONE RÉGULIER
        // =====================================================
        "polygone" | "polygone_regulier" | "regular polygon" | "polygon" => {
            result.description = "Polygone régulier à n côtés égaux.".into();
            result.parametres_attendus = vec![
                "n (nombre de côtés, ≥ 3)".into(),
                "a (longueur du côté)".into(),
            ];
            result.formules = vec![
                "Aire = (n · a²) / (4 · tan(π/n))".into(),
                "Périmètre = n · a".into(),
            ];

        }

        // ---------------------------
        // AUTRE / NON RECONNU
        // ---------------------------
        _ => {
            result.description = "Forme inconnue. Formes supportées : cercle, rectangle, carre, triangle, losange, polygone.".into();
        }
    }

    result
}

fn pretty_print(desc: &DescriptionForme) {
    // Nom de la forme avec █ des deux côtés
    println!("█ {} █", desc.nom.to_uppercase());
    println!("{}", desc.description);
    println!("┌─────────────────────────────┬─────────────────────────────┐");
    println!("│ Paramètre utilisateur       │ Formule                     │");
    println!("├─────────────────────────────┼─────────────────────────────┤");

    let max_rows = std::cmp::max(desc.parametres_attendus.len(), desc.formules.len());

    for i in 0..max_rows {
        // Utiliser une chaîne statique pour le fallback
        let propriete = desc.parametres_attendus.get(i).map(|s| s.as_str()).unwrap_or("");
        let formule = desc.formules.get(i).map(|s| s.as_str()).unwrap_or("");
        println!("│ {:<27} │ {:<27} │", propriete, formule);
    }

    println!("└─────────────────────────────┴─────────────────────────────┘");
}



fn main() {

    let desc = decrire_forme("carre");
    pretty_print(&desc);

    let desc = decrire_forme("cercle");
    pretty_print(&desc);

    let desc = decrire_forme("polygon");
    pretty_print(&desc);

    let desc = decrire_forme("losange");
    pretty_print(&desc);

    let desc = decrire_forme("triangle");
    pretty_print(&desc);

    let desc = decrire_forme("rectangle");
    pretty_print(&desc);
}
