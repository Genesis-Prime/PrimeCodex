#!/usr/bin/env python3
"""GenesisPrime Examples - Advanced usage demonstrations."""

import time

from genesis_prime import GenesisPrime


def performance_demo() -> None:
    """Demonstrate timing characteristics of large prime checks."""

    print("=== Performance Demo ===")
    gp = GenesisPrime()

    large_primes = [982_451_653, 982_451_707, 982_451_761, 982_451_817]

    start_time = time.time()
    for candidate in large_primes:
        label = "prime" if gp.is_prime(candidate) else "composite"
        print(f"{candidate:,} is {label}")
    elapsed = time.time() - start_time

    print(f"Checked {len(large_primes)} large numbers in {elapsed:.3f}s")
    print()


def twin_prime_analysis(limit: int = 100) -> None:
    """Analyze twin prime distribution up to ``limit``."""

    print("=== Twin Prime Analysis ===")
    gp = GenesisPrime()

    primes = gp.generate_primes_sieve(limit)
    twin_pairs = [
        (value, value + 2)
        for value in primes
        if value + 2 <= limit and gp.is_twin_prime(value)
    ]

    print(f"Twin prime pairs up to {limit}:")
    for left, right in twin_pairs:
        print(f"  {left} and {right}")

    print(f"\nTotal twin prime pairs: {len(twin_pairs)}")
    print(f"Total primes up to {limit}: {len(primes)}")
    denominator = max(len(primes), 1)
    percentage = len(twin_pairs) * 2 / denominator * 100
    print(f"Twin prime percentage: {percentage:.1f}%")
    print()


def factorization_analysis() -> None:
    """Explore factorization patterns across representative numbers."""

    print("=== Factorization Analysis ===")
    gp = GenesisPrime()

    samples = [
        (60, "Highly composite"),
        (128, "Power of 2"),
        (243, "Power of 3"),
        (210, "Product of first 4 primes"),
        (97, "Prime number"),
        (221, "Semiprime (product of 2 primes)"),
    ]

    for value, description in samples:
        factors = gp.prime_factors(value)
        unique_factors = sorted(set(factors))

        print(f"{value} ({description}):")
        print(f"  Factors: {' × '.join(map(str, factors))}")
        print(f"  Unique primes: {unique_factors}")
        print(f"  Number of prime factors: {len(factors)}")
        print(f"  Number of distinct primes: {len(unique_factors)}")

        if len(factors) == 1:
            print("  Type: Prime")
        elif len(unique_factors) == 1:
            print(f"  Type: Prime power ({unique_factors[0]}^{len(factors)})")
        elif len(factors) == 2 and len(unique_factors) == 2:
            print("  Type: Semiprime")
        else:
            print("  Type: Composite")
        print()


def prime_gaps_analysis(count: int = 50) -> None:
    """Inspect gaps between the first ``count`` prime numbers."""

    print("=== Prime Gaps Analysis ===")
    gp = GenesisPrime()

    primes = gp.generate_primes_sequence(count)
    gaps = [primes[index + 1] - primes[index] for index in range(len(primes) - 1)]

    print("First 20 prime gaps:")
    for index, gap in enumerate(gaps[:20]):
        print(f"  {primes[index]} → {primes[index + 1]}: gap = {gap}")

    print("\nGap statistics for first 50 primes:")
    print(f"  Average gap: {sum(gaps) / len(gaps):.2f}")
    print(f"  Minimum gap: {min(gaps)}")
    print(f"  Maximum gap: {max(gaps)}")

    gap_frequency: dict[int, int] = {}
    for gap in gaps:
        gap_frequency[gap] = gap_frequency.get(gap, 0) + 1

    print("  Gap frequency:")
    for gap in sorted(gap_frequency):
        print(f"    Gap {gap}: {gap_frequency[gap]} times")
    print()


def prime_density_analysis() -> None:
    """Display prime density within several numeric ranges."""

    print("=== Prime Density Analysis ===")
    gp = GenesisPrime()

    ranges = [(1, 100), (100, 200), (200, 300), (500, 600), (900, 1000)]

    print("Prime density by range:")
    for start, end in ranges:
        all_primes = gp.generate_primes_sieve(end)
        window = [value for value in all_primes if start <= value <= end]
        density = len(window) / (end - start + 1) * 100

        summary = f"  [{start:3d}, {end:3d}]: {len(window):2d} primes ({density:5.1f}%)"
        print(summary)
    print()


def goldbach_demo() -> None:
    """Illustrate Goldbach's conjecture for even numbers up to 30."""

    print("=== Goldbach's Conjecture Demo ===")
    gp = GenesisPrime()

    print("Every even number > 2 can be expressed as sum of two primes:")

    primes = gp.generate_primes_sieve(100)
    prime_set = set(primes)

    for value in range(4, 31, 2):
        pairs = []
        for candidate in primes:
            if candidate > value // 2:
                break
            complement = value - candidate
            if complement in prime_set:
                pairs.append((candidate, complement))

        if pairs:
            displays = [f"{left}+{right}" for left, right in pairs[:3]]
            remainder = f" (+{len(pairs) - 3} more)" if len(pairs) > 3 else ""
            print(f"  {value:2d} = {', '.join(displays)}{remainder}")
    print()


def main() -> None:
    """Run all demonstrations."""

    print("GenesisPrime - Advanced Examples")
    print("=" * 40)
    print()

    performance_demo()
    twin_prime_analysis()
    factorization_analysis()
    prime_gaps_analysis()
    prime_density_analysis()
    goldbach_demo()

    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
