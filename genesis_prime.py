#!/usr/bin/env python3
"""GenesisPrime - A comprehensive prime number library."""

from __future__ import annotations

import math


class GenesisPrime:
    """Main class for prime number operations."""

    def __init__(self) -> None:
        """Initialise GenesisPrime with a basic cache of primes."""

        self._cache: set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

    def is_prime(self, value: int) -> bool:
        """Return ``True`` if ``value`` is prime using an optimised trial division."""

        if value < 2:
            return False
        if value in self._cache:
            return True
        if value < 4:
            return True
        if value % 2 == 0 or value % 3 == 0:
            return False

        divisor = 5
        while divisor * divisor <= value:
            if value % divisor == 0 or value % (divisor + 2) == 0:
                return False
            divisor += 6

        self._cache.add(value)
        return True

    def generate_primes_sieve(self, limit: int) -> list[int]:
        """Return all primes up to and including ``limit`` using a sieve."""

        if limit < 2:
            return []

        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        for candidate in range(2, int(math.sqrt(limit)) + 1):
            if sieve[candidate]:
                for multiple in range(candidate * candidate, limit + 1, candidate):
                    sieve[multiple] = False

        primes = [index for index, is_prime in enumerate(sieve) if is_prime]
        self._cache.update(primes)
        return primes

    def generate_primes_sequence(self, count: int) -> list[int]:
        """Return the first ``count`` prime numbers."""

        if count <= 0:
            return []

        primes: list[int] = []
        candidate = 2

        while len(primes) < count:
            if self.is_prime(candidate):
                primes.append(candidate)
            candidate += 1

        return primes

    def prime_factors(self, value: int) -> list[int]:
        """Return the prime factorisation of ``value``."""

        if value < 2:
            return []

        factors: list[int] = []
        remainder = value

        while remainder % 2 == 0:
            factors.append(2)
            remainder //= 2

        divisor = 3
        while divisor * divisor <= remainder:
            while remainder % divisor == 0:
                factors.append(divisor)
                remainder //= divisor
            divisor += 2

        if remainder > 2:
            factors.append(remainder)

        return factors

    def next_prime(self, value: int) -> int:
        """Return the first prime strictly greater than ``value``."""

        candidate = value + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate

    def prev_prime(self, value: int) -> int | None:
        """Return the largest prime strictly less than ``value`` if it exists."""

        if value <= 2:
            return None

        candidate = value - 1
        while candidate > 1 and not self.is_prime(candidate):
            candidate -= 1
        return candidate if candidate > 1 else None

    def is_twin_prime(self, value: int) -> bool:
        """Return ``True`` if ``value`` is part of a twin-prime pair."""

        if not self.is_prime(value):
            return False

        return self.is_prime(value + 2) or self.is_prime(value - 2)

    def get_stats(self) -> dict[str, int | None]:
        """Return statistics about the cached primes."""

        largest = max(self._cache) if self._cache else None
        return {"cached_primes": len(self._cache), "largest_cached": largest}


def main() -> None:
    """Demonstrate GenesisPrime capabilities."""

    gp = GenesisPrime()

    print("=== GenesisPrime Demo ===")
    print()

    test_numbers = [2, 3, 4, 17, 25, 97, 100, 101]
    print("Prime checking:")
    for number in test_numbers:
        verdict = "prime" if gp.is_prime(number) else "not prime"
        print(f"  {number} is {verdict}")
    print()

    first_primes = gp.generate_primes_sequence(10)
    print(f"First 10 primes: {first_primes}")
    print()

    primes_50 = gp.generate_primes_sieve(50)
    print(f"Primes up to 50: {primes_50}")
    print()

    print("Prime factorisation:")
    for number in [12, 17, 60, 97]:
        factors = gp.prime_factors(number)
        print(f"  {number} = {' × '.join(map(str, factors))}")
    print()

    print("Twin prime checking:")
    for number in [3, 5, 11, 13, 17, 19]:
        verdict = "a twin prime" if gp.is_twin_prime(number) else "not a twin prime"
        print(f"  {number} is {verdict}")
    print()

    print("Next/previous primes:")
    for number in [10, 20, 30]:
        next_prime = gp.next_prime(number)
        prev_prime = gp.prev_prime(number)
        print(f"  Around {number}: previous = {prev_prime}, next = {next_prime}")
    print()

    stats = gp.get_stats()
    print(f"Cache statistics: {stats}")


if __name__ == "__main__":
    main()
