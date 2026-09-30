# CDA Appendix F Verification Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

This repository provides the official implementation and numerical verification scripts for **Conjecture I (Complex Force-Strength Conjecture)** and **Conjecture II (Polynomial Force-Radius Conjecture)**, as formulated in Appendix F of the *Complex Displacement Architecture (CDA)* manuscript.

---

## Overview

The routines in this repository verify two key mathematical dynamics near high-degree complex polynomial roots ($f(z) = z^n - c$ and multi-term variations):

1. **Conjecture I (Complex Force-Strength Conjecture):** Tests seed localization and spin sector capture accuracy across varying magnitude thresholds of the coefficient imaginary part $\vert{}v\vert{}$ ($c = u + iv$). Demonstrates the transition into anomalous/sensitive spin-to-basin dynamics when $\vert{}v\vert{} < 0.6$.
2. **Conjecture II (Polynomial Force-Radius Conjecture):** Evaluates and compares the effective geometric attraction radii surrounding root basins in single-term ($z^n - c$) versus multi-term ($z^n + a_k z^k - c$) polynomial systems.

---

## Project Structure

```text
cda_conjectures/
│
├── cda_core/
│   ├── __init__.py
│   └── complex_engine.py      # Core CDA displacement operator & seed generator
│
├── verification/
│   ├── __init__.py
│   ├── conjecture_1_force_strength.py   # Test suite for Conjecture I (|v| transitions)
│   └── conjecture_2_force_radius.py     # Test suite for Conjecture II (Attraction radii)
│
├── visualize_basins.py        # Master execution script for full verification
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

Installation & Setup
Prerequisites
 * Python 3.8+
 * pip package manager
Installation Steps
 * Clone the repository:
   git clone [https://github.com/YOUR-USERNAME/cda-conjectures-verification.git](https://github.com/YOUR-USERNAME/cda-conjectures-verification.git)
cd cda-conjectures-verification

 * Install dependencies:
   pip install -r requirements.txt

Execution & Usage
Running the Full Verification Suite
To run both numerical verification suites sequentially:
python visualize_basins.py

Running Individual Verification Modules
 * Verify Conjecture I (Force-Strength / Sensitivity Threshold |v| < 0.6):
   python -m verification.conjecture_1_force_strength

 * Verify Conjecture II (Force-Radius / 1-Term vs Multi-Term Basins):
   python -m verification.conjecture_2_force_radius

Mathematical Formulation
The core iteration step evaluates the unconstrained complex displacement operator:
where:
 * S(z) = \frac{f'(z)}{f(z)} (First-order logarithmic derivative / logarithmic field ratio)
 * K(z) = \frac{f''(z)}{2 f'(z)} (Second-order curvature ratio)
Citation
If you use this verification code or reference Conjectures I & II in your research, please cite:
@article{cda2026appendixf,
  title={Complex Displacement Architecture: Appendix F Conjectures},
  author={Latonio, Karl Arvin},
  year={2026},
  journal={Manuscript Appendix F}
}
