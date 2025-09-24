#!/usr/bin/env python3
"""
GenesisPrime - A comprehensive prime number library

This module provides essential prime number operations including:
- Prime number validation
- Prime number generation 
- Prime factorization
- Prime number sequences
"""

import math
from typing import List, Iterator, Set


class GenesisPrime:
    """Main class for prime number operations"""
    
    def __init__(self):
        """Initialize GenesisPrime with basic cached primes"""
        self._cache: Set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    
    def is_prime(self, n: int) -> bool:
        """
        Check if a number is prime using optimized trial division
        
        Args:
            n: The number to check
            
        Returns:
            bool: True if n is prime, False otherwise
        """
        if n < 2:
            return False
        if n in self._cache:
            return True
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Check for divisors up to sqrt(n)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        
        # Cache the result if it's prime
        if n not in self._cache:
            self._cache.add(n)
        return True
    
    def generate_primes_sieve(self, limit: int) -> List[int]:
        """
        Generate all prime numbers up to a limit using Sieve of Eratosthenes
        
        Args:
            limit: Upper limit (inclusive)
            
        Returns:
            List[int]: List of prime numbers up to the limit
        """
        if limit < 2:
            return []
        
        # Initialize sieve
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        
        # Sieve of Eratosthenes
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        
        # Collect primes
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        
        # Update cache
        self._cache.update(primes)
        
        return primes
    
    def generate_primes_sequence(self, count: int) -> List[int]:
        """
        Generate the first 'count' prime numbers
        
        Args:
            count: Number of primes to generate
            
        Returns:
            List[int]: First 'count' prime numbers
        """
        if count <= 0:
            return []
        
        primes = []
        candidate = 2
        
        while len(primes) < count:
            if self.is_prime(candidate):
                primes.append(candidate)
            candidate += 1
        
        return primes
    
    def prime_factors(self, n: int) -> List[int]:
        """
        Find prime factorization of a number
        
        Args:
            n: The number to factorize
            
        Returns:
            List[int]: List of prime factors (with repetition)
        """
        if n < 2:
            return []
        
        factors = []
        
        # Check for factor 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check for odd factors
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If n is a prime greater than 2
        if n > 2:
            factors.append(n)
        
        return factors
    
    def next_prime(self, n: int) -> int:
        """
        Find the next prime number after n
        
        Args:
            n: Starting number
            
        Returns:
            int: The next prime number after n
        """
        candidate = n + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate
    
    def prev_prime(self, n: int) -> int:
        """
        Find the previous prime number before n
        
        Args:
            n: Starting number
            
        Returns:
            int: The previous prime number before n, or None if n <= 2
        """
        if n <= 2:
            return None
        
        candidate = n - 1
        while candidate > 1 and not self.is_prime(candidate):
            candidate -= 1
        
        return candidate if candidate > 1 else None
    
    def is_twin_prime(self, n: int) -> bool:
        """
        Check if n is part of a twin prime pair (n, n+2) or (n-2, n)
        
        Args:
            n: The number to check
            
        Returns:
            bool: True if n is part of a twin prime pair
        """
        if not self.is_prime(n):
            return False
        
        return self.is_prime(n + 2) or self.is_prime(n - 2)
    
    def get_stats(self) -> dict:
        """
        Get statistics about the current state
        
        Returns:
            dict: Statistics including cache size
        """
        return {
            "cached_primes": len(self._cache),
            "largest_cached": max(self._cache) if self._cache else None
        }


def main():
    """Demo function showing GenesisPrime capabilities"""
    gp = GenesisPrime()
    
    print("=== GenesisPrime Demo ===")
    print()
    
    # Test prime checking
    test_numbers = [2, 3, 4, 17, 25, 97, 100, 101]
    print("Prime checking:")
    for num in test_numbers:
        print(f"  {num} is {'prime' if gp.is_prime(num) else 'not prime'}")
    print()
    
    # Generate first 10 primes
    first_primes = gp.generate_primes_sequence(10)
    print(f"First 10 primes: {first_primes}")
    print()
    
    # Generate primes up to 50
    primes_50 = gp.generate_primes_sieve(50)
    print(f"Primes up to 50: {primes_50}")
    print()
    
    # Prime factorization
    test_factors = [12, 17, 60, 97]
    print("Prime factorization:")
    for num in test_factors:
        factors = gp.prime_factors(num)
        print(f"  {num} = {' × '.join(map(str, factors))}")
    print()
    
    # Twin primes
    print("Twin prime checking:")
    for num in [3, 5, 11, 13, 17, 19]:
        twin = gp.is_twin_prime(num)
        print(f"  {num} is {'a twin prime' if twin else 'not a twin prime'}")
    print()
    
    # Next/previous primes
    print("Next/previous primes:")
    for num in [10, 20, 30]:
        next_p = gp.next_prime(num)
        prev_p = gp.prev_prime(num)
        print(f"  Around {num}: previous = {prev_p}, next = {next_p}")
    print()
    
    # Statistics
    stats = gp.get_stats()
    print(f"Cache statistics: {stats}")


if __name__ == "__main__":
    main()