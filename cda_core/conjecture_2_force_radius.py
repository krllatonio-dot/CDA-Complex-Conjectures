import cmath
import math
from cda_core.complex_engine import cda_step_standard


def measure_basin_radius(c_terms: dict, target_root: complex, num_samples: int = 36) -> float:
    """
    Estimates effective geometric attraction radius around a target root
    by radially scanning outwards until CDA convergence breaks.
    """
    max_radius = 0.0
    angles = [2.0 * math.pi * i / num_samples for i in range(num_samples)]

    for angle in angles:
        # Radial search outwards from root
        r = 0.01
        last_valid_r = 0.0
        while r < 2.0:
            z0 = target_root + r * cmath.rect(1.0, angle)
            z = z0
            converged = False
            for _ in range(25):
                z = cda_step_standard(z, c_terms)
                if abs(z - target_root) < 1e-4:
                    converged = True
                    break

            if converged:
                last_valid_r = r
                r += 0.02
            else:
                break
        max_radius += last_valid_r

    return max_radius / num_samples


def evaluate_conjecture_2(n_degree: int = 50):
    """
    Verifies Conjecture II (Polynomial Force-Radius Conjecture):
    Compares effective basin radius of 1-term polynomial vs multi-term polynomial.
    Multi-term configurations should exhibit larger mean attraction radii.
    """
    print("=" * 65)
    print(f"VERIFYING CONJECTURE II: Polynomial Force-Radius (Degree n = {n_degree})")
    print("=" * 65)

    c = complex(1.0, 0.8)

    # 1-Term Polynomial: z^n - c
    terms_1term = {n_degree: 1.0, 0: -c}
    root_1term = (abs(c) ** (1.0 / n_degree)) * cmath.rect(1.0, math.atan2(c.imag, c.real) / n_degree)
    r_1term = measure_basin_radius(terms_1term, root_1term)

    # Multi-Term Polynomial: z^n + 0.3*z^(n//2) - c
    terms_multiterm = {n_degree: 1.0, n_degree // 2: 0.3, 0: -c}
    root_multiterm = root_1term  # Approximation near primary branch
    r_multiterm = measure_basin_radius(terms_multiterm, root_multiterm)

    print(f"Single-Term (z^{n_degree} - c)        Mean Basin Radius: {r_1term:.5f}")
    print(f"Multi-Term  (z^{n_degree} + 0.3z^{n_degree//2} - c) Mean Basin Radius: {r_multiterm:.5f}")

    if r_multiterm > r_1term:
        print("\nVerdict: CONFIRMED — Multi-term distribution expands effective basin radius.")
    else:
        print("\nVerdict: REQUIRES FURTHER REFINEMENT.")

    print("-" * 65 + "\n")


if __name__ == "__main__":
    evaluate_conjecture_2()
