#!/usr/bin/env python3
"""
Prime CLI - Command line interface for GenesisPrime

A command-line tool for prime number operations using the GenesisPrime library.
"""

import argparse
import sys
from genesis_prime import GenesisPrime


def format_list(numbers, max_per_line=10):
    """Format a list of numbers for display"""
    if not numbers:
        return "None"
    
    lines = []
    for i in range(0, len(numbers), max_per_line):
        chunk = numbers[i:i + max_per_line]
        lines.append(", ".join(map(str, chunk)))
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="GenesisPrime - Prime number operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s check 17              # Check if 17 is prime
  %(prog)s generate --count 10   # Generate first 10 primes
  %(prog)s generate --limit 50   # Generate primes up to 50
  %(prog)s factors 60            # Get prime factors of 60
  %(prog)s next 20               # Find next prime after 20
  %(prog)s prev 20               # Find previous prime before 20
  %(prog)s twin 17               # Check if 17 is a twin prime
        """)
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Check command
    check_parser = subparsers.add_parser('check', help='Check if a number is prime')
    check_parser.add_argument('number', type=int, help='Number to check')
    
    # Generate command
    gen_parser = subparsers.add_parser('generate', help='Generate prime numbers')
    gen_group = gen_parser.add_mutually_exclusive_group(required=True)
    gen_group.add_argument('--count', type=int, help='Generate first N primes')
    gen_group.add_argument('--limit', type=int, help='Generate primes up to limit')
    
    # Factors command
    factors_parser = subparsers.add_parser('factors', help='Get prime factorization')
    factors_parser.add_argument('number', type=int, help='Number to factorize')
    
    # Next prime command
    next_parser = subparsers.add_parser('next', help='Find next prime after number')
    next_parser.add_argument('number', type=int, help='Starting number')
    
    # Previous prime command
    prev_parser = subparsers.add_parser('prev', help='Find previous prime before number')
    prev_parser.add_argument('number', type=int, help='Starting number')
    
    # Twin prime command
    twin_parser = subparsers.add_parser('twin', help='Check if number is a twin prime')
    twin_parser.add_argument('number', type=int, help='Number to check')
    
    # Range command
    range_parser = subparsers.add_parser('range', help='Find primes in a range')
    range_parser.add_argument('start', type=int, help='Start of range (inclusive)')
    range_parser.add_argument('end', type=int, help='End of range (inclusive)')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    gp = GenesisPrime()
    
    try:
        if args.command == 'check':
            result = gp.is_prime(args.number)
            print(f"{args.number} is {'prime' if result else 'not prime'}")
        
        elif args.command == 'generate':
            if args.count:
                primes = gp.generate_primes_sequence(args.count)
                print(f"First {args.count} primes:")
                print(format_list(primes))
            else:
                primes = gp.generate_primes_sieve(args.limit)
                print(f"Primes up to {args.limit} ({len(primes)} found):")
                print(format_list(primes))
        
        elif args.command == 'factors':
            factors = gp.prime_factors(args.number)
            if factors:
                factors_str = " × ".join(map(str, factors))
                print(f"{args.number} = {factors_str}")
                
                # Show unique factors
                unique_factors = list(set(factors))
                unique_factors.sort()
                if len(unique_factors) != len(factors):
                    print(f"Unique prime factors: {', '.join(map(str, unique_factors))}")
            else:
                print(f"{args.number} has no prime factors (less than 2)")
        
        elif args.command == 'next':
            result = gp.next_prime(args.number)
            print(f"Next prime after {args.number}: {result}")
        
        elif args.command == 'prev':
            result = gp.prev_prime(args.number)
            if result:
                print(f"Previous prime before {args.number}: {result}")
            else:
                print(f"No prime before {args.number}")
        
        elif args.command == 'twin':
            result = gp.is_twin_prime(args.number)
            if result:
                # Show the twin pair
                if gp.is_prime(args.number + 2):
                    print(f"{args.number} is a twin prime (pair: {args.number}, {args.number + 2})")
                elif gp.is_prime(args.number - 2):
                    print(f"{args.number} is a twin prime (pair: {args.number - 2}, {args.number})")
            else:
                if gp.is_prime(args.number):
                    print(f"{args.number} is prime but not a twin prime")
                else:
                    print(f"{args.number} is not prime")
        
        elif args.command == 'range':
            if args.start > args.end:
                print("Error: Start must be less than or equal to end")
                return
            
            all_primes = gp.generate_primes_sieve(args.end)
            range_primes = [p for p in all_primes if args.start <= p <= args.end]
            
            print(f"Primes in range [{args.start}, {args.end}] ({len(range_primes)} found):")
            print(format_list(range_primes))
        
        elif args.command == 'stats':
            stats = gp.get_stats()
            print("GenesisPrime Statistics:")
            print(f"  Cached primes: {stats['cached_primes']}")
            print(f"  Largest cached: {stats['largest_cached']}")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()