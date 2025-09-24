#!/usr/bin/env python3
"""
GenesisPrime Quick Start Demo

A simple demonstration of GenesisPrime capabilities for new users.
Run this to see the library in action!
"""

from genesis_prime import GenesisPrime


def quickstart_demo():
    """Quick demonstration of key features"""
    print("🚀 Welcome to GenesisPrime!")
    print("=" * 50)
    print()

    # Initialize the library
    gp = GenesisPrime()

    # 1. Prime checking
    print("1️⃣  Prime Number Checking")
    test_numbers = [17, 18, 97, 100]
    for num in test_numbers:
        result = "✅ PRIME" if gp.is_prime(num) else "❌ Not prime"
        print(f"   {num:3d} → {result}")
    print()

    # 2. Generate primes
    print("2️⃣  Prime Generation")
    first_10 = gp.generate_primes_sequence(10)
    print(f"   First 10 primes: {first_10}")

    primes_50 = gp.generate_primes_sieve(50)
    print(f"   Primes up to 50: {len(primes_50)} found")
    print(f"   They are: {primes_50}")
    print()

    # 3. Prime factorization
    print("3️⃣  Prime Factorization")
    numbers_to_factor = [12, 30, 97, 100]
    for num in numbers_to_factor:
        factors = gp.prime_factors(num)
        if factors:
            factors_str = " × ".join(map(str, factors))
            print(f"   {num:3d} = {factors_str}")
        else:
            print(f"   {num:3d} = No prime factors (< 2)")
    print()

    # 4. Twin primes
    print("4️⃣  Twin Prime Detection")
    candidates = [3, 5, 11, 13, 17, 19, 23]
    twin_pairs = []
    for num in candidates:
        if gp.is_twin_prime(num):
            if gp.is_prime(num + 2):
                twin_pairs.append(f"({num}, {num + 2})")
            elif gp.is_prime(num - 2):
                twin_pairs.append(f"({num - 2}, {num})")

    print(f"   Twin prime pairs found: {', '.join(twin_pairs)}")
    print()

    # 5. Prime navigation
    print("5️⃣  Prime Navigation")
    for num in [10, 50, 100]:
        next_p = gp.next_prime(num)
        prev_p = gp.prev_prime(num)
        print(f"   Around {num:3d}: ← {prev_p} | {next_p} →")
    print()

    # 6. Quick math facts
    print("6️⃣  Fun Prime Facts")
    print(f"   📊 Largest prime we've cached: {max(gp._cache)}")
    print(f"   📈 Total primes cached: {len(gp._cache)}")

    # Calculate prime density for first 100 numbers
    primes_100 = gp.generate_primes_sieve(100)
    density = len(primes_100)
    print(f"   🎯 Prime density in 1-100: {density}% ({density}/100)")

    # Find the largest gap in first 100 primes
    gaps = []
    for i in range(len(primes_100) - 1):
        gaps.append(primes_100[i + 1] - primes_100[i])
    max_gap = max(gaps)
    gap_index = gaps.index(max_gap)
    gap_message = (
        f"   📏 Largest prime gap in 1-100: {max_gap} "
        f"(between {primes_100[gap_index]} and {primes_100[gap_index + 1]})"
    )
    print(gap_message)
    print()

    # 7. Try it yourself
    print("7️⃣  Try It Yourself!")
    print("   Run these commands to explore more:")
    print("   📝 python prime_cli.py check 1009")
    print("   📝 python prime_cli.py generate --count 20")
    print("   📝 python prime_cli.py factors 2310")
    print("   📝 python prime_cli.py twin 101")
    print("   📝 python examples.py")
    print()

    print("🎉 That's GenesisPrime in action!")
    print("   Check the README.md for complete documentation.")
    print("   Happy prime hunting! 🔍✨")


if __name__ == "__main__":
    quickstart_demo()
