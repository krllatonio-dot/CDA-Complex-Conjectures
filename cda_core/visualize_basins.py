from verification.conjecture_1_force_strength import evaluate_conjecture_1
from verification.conjecture_2_force_radius import evaluate_conjecture_2


def main():
    print("Running Full CDA Appendix F Verification Suite...\n")
    evaluate_conjecture_1(n_degree=100)
    evaluate_conjecture_2(n_degree=50)


if __name__ == "__main__":
    main()
