#!/usr/bin/env python3
"""
GenesisPrime Examples - Advanced usage demonstrations

This file contains examples of how to use GenesisPrime for various
prime number analysis tasks.
"""

from genesis_prime import GenesisPrime
import time


def performance_demo():
    """Demo performance characteristics"""
    print("=== Performance Demo ===")
    gp = GenesisPrime()
    
    # Time prime checking
    large_primes = [982451653, 982451707, 982451761, 982451817]
    
    start_time = time.time()
    for prime in large_primes:
        result = gp.is_prime(prime)
        print(f"{prime:,} is {'prime' if result else 'composite'}")
    end_time = time.time()
    
    print(f"Checked {len(large_primes)} large numbers in {end_time - start_time:.3f}s")
    print()


def twin_prime_analysis():
    """Analyze twin prime distribution"""
    print("=== Twin Prime Analysis ===")
    gp = GenesisPrime()
    
    # Find twin primes up to 100
    primes_100 = gp.generate_primes_sieve(100)
    twin_pairs = []
    
    for p in primes_100:
        if gp.is_twin_prime(p):
            if p + 2 in primes_100:  # p is the smaller of the pair
                twin_pairs.append((p, p + 2))
    
    print(f"Twin prime pairs up to 100:")
    for pair in twin_pairs:
        print(f"  {pair[0]} and {pair[1]}")
    
    print(f"\nTotal twin prime pairs: {len(twin_pairs)}")
    print(f"Total primes up to 100: {len(primes_100)}")
    print(f"Twin prime percentage: {len(twin_pairs) * 2 / len(primes_100) * 100:.1f}%")
    print()


def factorization_analysis():
    """Analyze factorization patterns"""
    print("=== Factorization Analysis ===")
    gp = GenesisPrime()
    
    # Analyze numbers with different factorization patterns
    test_cases = [
        (60, "Highly composite"),
        (128, "Power of 2"),  
        (243, "Power of 3"),
        (210, "Product of first 4 primes"),
        (97, "Prime number"),
        (221, "Semiprime (product of 2 primes)")
    ]
    
    for num, description in test_cases:
        factors = gp.prime_factors(num)
        unique_factors = sorted(set(factors))
        
        print(f"{num} ({description}):")
        print(f"  Factors: {' × '.join(map(str, factors))}")
        print(f"  Unique primes: {unique_factors}")
        print(f"  Number of prime factors: {len(factors)}")
        print(f"  Number of distinct primes: {len(unique_factors)}")
        
        # Classification
        if len(factors) == 1:
            print(f"  Type: Prime")
        elif len(unique_factors) == 1:
            print(f"  Type: Prime power ({unique_factors[0]}^{len(factors)})")
        elif len(factors) == 2 and len(unique_factors) == 2:
            print(f"  Type: Semiprime")
        else:
            print(f"  Type: Composite")
        print()


def prime_gaps_analysis():
    """Analyze gaps between consecutive primes"""
    print("=== Prime Gaps Analysis ===")
    gp = GenesisPrime()
    
    # Generate first 50 primes and analyze gaps
    primes = gp.generate_primes_sequence(50)
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    
    print("First 20 prime gaps:")
    for i, gap in enumerate(gaps[:20]):
        print(f"  {primes[i]} → {primes[i+1]}: gap = {gap}")
    
    # Gap statistics
    print(f"\nGap statistics for first 50 primes:")
    print(f"  Average gap: {sum(gaps) / len(gaps):.2f}")
    print(f"  Minimum gap: {min(gaps)}")
    print(f"  Maximum gap: {max(gaps)}")
    
    # Gap frequency
    gap_freq = {}
    for gap in gaps:
        gap_freq[gap] = gap_freq.get(gap, 0) + 1
    
    print(f"  Gap frequency:")
    for gap in sorted(gap_freq.keys()):
        print(f"    Gap {gap}: {gap_freq[gap]} times")
    print()


def prime_density_analysis():
    """Analyze prime density in different ranges"""
    print("=== Prime Density Analysis ===")
    gp = GenesisPrime()
    
    ranges = [(1, 100), (100, 200), (200, 300), (500, 600), (900, 1000)]
    
    print("Prime density by range:")
    for start, end in ranges:
        all_primes = gp.generate_primes_sieve(end)
        range_primes = [p for p in all_primes if start <= p <= end]
        density = len(range_primes) / (end - start + 1) * 100
        
        print(f"  [{start:3d}, {end:3d}]: {len(range_primes):2d} primes ({density:5.1f}%)")
    print()


def goldbach_demo():
    """Demonstrate Goldbach's conjecture for small even numbers"""
    print("=== Goldbach's Conjecture Demo ===")
    gp = GenesisPrime()
    
    print("Every even number > 2 can be expressed as sum of two primes:")
    
    # Test even numbers from 4 to 30
    primes_100 = gp.generate_primes_sieve(100)
    prime_set = set(primes_100)
    
    for n in range(4, 31, 2):
        # Find pairs of primes that sum to n
        pairs = []
        for p in primes_100:
            if p > n // 2:
                break
            complement = n - p
            if complement in prime_set:
                pairs.append((p, complement))
        
        if pairs:
            # Show first few pairs
            pair_strs = [f"{p}+{q}" for p, q in pairs[:3]]
            more = f" (+{len(pairs)-3} more)" if len(pairs) > 3 else ""
            print(f"  {n:2d} = {', '.join(pair_strs)}{more}")
    print()


def main():
    """Run all demonstrations"""
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