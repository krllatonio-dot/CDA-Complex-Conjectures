import cmath
import math

try:
    import gmpy2
    from gmpy2 import mpc, mpfr
    HAS_GMPY2 = True
except ImportError:
    HAS_GMPY2 = False


def cda_step_standard(z: complex, c_terms: dict) -> complex:
    """
    Evaluates one CDA displacement step for f(z) = sum(a_k * z^k):
    z_{t+1} = z_t - 1 / (S(z) - K(z))
    where S = f'/f and K = f''/(2f')
    """
    f = sum(coeff * (z**deg) for deg, coeff in c_terms.items())
    f_prime = sum(deg * coeff * (z**(deg - 1)) for deg, coeff in c_terms.items() if deg > 0)
    f_double_prime = sum(deg * (deg - 1) * coeff * (z**(deg - 2)) for deg, coeff in c_terms.items() if deg > 1)

    if abs(f_prime) == 0 or abs(f) == 0:
        return z

    s = f_prime / f
    k = f_double_prime / (2.0 * f_prime)

    denom = s - k
    if abs(denom) == 0:
        return z

    delta = 1.0 / denom
    return z - delta


def generate_seed(n: int, c: complex, k_spin: int) -> complex:
    """
    Generates spin-dependent seed z_0 using Appendix F localization rule:
    angle = (2*pi*k + atan2(v, u)) / n
    """
    u, v = c.real, c.imag
    phi = math.atan2(v, u)
    r0 = abs(1.0 - c)
    angle = (2.0 * math.pi * k_spin + phi) / float(n)
    return r0 * cmath.rect(1.0, angle)
