use crate::helpers::Point;

#[derive(Debug, Clone)]
pub struct TrianglePlat {
    pub ax: f64,
    pub ay: f64,
    pub bx: f64,
    pub by: f64,
    pub cx: f64,
    pub cy: f64,
}

impl TrianglePlat {

    pub fn new(ax: f64, ay: f64, bx: f64, by: f64, cx: f64, cy: f64) -> Self {
        TrianglePlat { ax, ay, bx, by, cx, cy }
    }

    /// Test : triangle dégénéré (les 3 points alignés)
    pub fn is_degenerate(&self) -> bool {
        let area = (self.bx - self.ax) * (self.cy - self.ay)
                 - (self.cx - self.ax) * (self.by - self.ay);
        area.abs() < 1e-12
    }

    /// Distance d'un point au triangle (ou segment si dégénéré)
    pub fn dist_point(&self, p: &Point) -> f64 {
        // Distance au segment AB
        let d1 = crate::distances::segment_distance::dist_segment_point(
            self.ax, self.ay, self.bx, self.by, p.x, p.y
        );

        // Distance au segment BC
        let d2 = crate::distances::segment_distance::dist_segment_point(
            self.bx, self.by, self.cx, self.cy, p.x, p.y
        );

        // Distance au segment CA
        let d3 = crate::distances::segment_distance::dist_segment_point(
            self.cx, self.cy, self.ax, self.ay, p.x, p.y
        );

        d1.min(d2).min(d3)
    }
    pub fn segment(&self) -> (f64, f64, f64, f64) {
        // On renvoie le segment A–C (parfait pour distance minimale)
        (self.ax, self.ay, self.cx, self.cy)
    }
}
