import math


def is_prime(n: int) -> bool:
    if n == 0 or n == 1:
        return False

    for val in range(2, n // 2 + 1):
        if n % val == 0:
            return False

    return True


def passes_fermat_primality_test(n: int) -> bool:
    if n <= 1:
        return False

    for a in range(2, n):
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False

    return True


def is_carmichael(n: int) -> bool:
    if passes_fermat_primality_test(n) and not is_prime(n):
        return True

    return False


def main() -> None:
    print(passes_fermat_primality_test(561))
    print(is_prime(561))
    print(is_carmichael(561))


if __name__ == '__main__':
    main()
