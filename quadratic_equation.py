from math import sqrt


def get_roots(coefficient_a, coefficient_b, coefficient_c):
    discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
    if discriminant < 0:
        return None, None
    root1 = (-coefficient_b - sqrt(discriminant)) / (2 * coefficient_a)
    root2 = (-coefficient_b + sqrt(discriminant)) / (2 * coefficient_a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
