import cmath
import math
from cda_core.complex_engine import cda_step_standard, generate_seed


def evaluate_conjecture_1(n_degree: int = 100, v_thresholds: list = None, max_steps: int = 30):
    """
    Verifies Conjecture I (Complex Force-Strength Conjecture):
    Measures spin accuracy and sector classification across varying imaginary parts |v|.
    Transitions/anomalies are expected when |v| < 0.6.
    """
    if v_thresholds is None:
        v_thresholds = [0.1, 0.3, 0.55, 0.65, 0.8, 1.2]

    print("=" * 65)
    print(f"VERIFYING CONJECTURE I: Complex Force-Strength (Degree n = {n_degree})")
    print("=" * 65)

    num_spins = min(n_degree, 20)

    for v in v_thresholds:
        c = complex(1.0, v)
        c_terms = {n_degree: 1.0, 0: -c}

        correct_count = 0

        for k in range(num_spins):
            z = generate_seed(n_degree, c, k)

            for _ in range(max_steps):
                z = cda_step_standard(z, c_terms)

            # Reconstructed angle from converged root
            actual_angle = cmath.phase(z)
            if actual_angle < 0:
                actual_angle += 2.0 * math.pi

            expected_angle = (math.atan2(v, 1.0) + 2.0 * math.pi * k) / float(n_degree)
            expected_angle = expected_angle % (2.0 * math.pi)

            # Angle deviation threshold relative to sector width
            sector_width = (2.0 * math.pi) / n_degree
            diff = abs(actual_angle - expected_angle)
            diff = min(diff, 2.0 * math.pi - diff)

            if diff < (sector_width / 2.0):
                correct_count += 1

        accuracy = (correct_count / num_spins) * 100.0
        status = "ANOMALOUS / SENSITIVE" if v < 0.6 else "STABLE"
        print(f"|v| = {v:.2f} | Spin Accuracy = {accuracy:5.1f}% ({correct_count}/{num_spins}) | Region: {status}")

    print("-" * 65 + "\n")


if __name__ == "__main__":
    evaluate_conjecture_1()
