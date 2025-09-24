# PrimeCodex - GenesisPrime

A comprehensive prime number library and toolkit implemented in Python. GenesisPrime provides efficient algorithms for prime number operations, factorization, and mathematical analysis.

## Features

- **Prime Testing**: Fast primality checking with optimized trial division
- **Prime Generation**: Generate primes using Sieve of Eratosthenes or sequential generation  
- **Prime Factorization**: Complete prime factorization of any integer
- **Twin Prime Detection**: Identify twin prime pairs (p, p+2)
- **Prime Navigation**: Find next/previous primes relative to any number
- **Range Operations**: Find all primes within specified ranges
- **Command Line Interface**: Full-featured CLI for all operations
- **Caching**: Intelligent caching for improved performance

## Quick Start

### Basic Usage (Python Library)

```python
from genesis_prime import GenesisPrime

gp = GenesisPrime()

# Check if a number is prime
print(gp.is_prime(97))  # True

# Generate first 10 primes
primes = gp.generate_primes_sequence(10)
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Get prime factorization
factors = gp.prime_factors(60)
print(factors)  # [2, 2, 3, 5]

# Find twin primes
print(gp.is_twin_prime(17))  # True (17, 19)
```

### Command Line Interface

```bash
# Check if a number is prime
python prime_cli.py check 97

# Generate first 20 primes
python prime_cli.py generate --count 20

# Generate all primes up to 100
python prime_cli.py generate --limit 100

# Get prime factorization
python prime_cli.py factors 84

# Find next prime after 50
python prime_cli.py next 50

# Find primes in range 10-30
python prime_cli.py range 10 30

# Check if number is twin prime
python prime_cli.py twin 13
```

## Core Functions

### GenesisPrime Class Methods

- `is_prime(n)` - Test if n is prime
- `generate_primes_sieve(limit)` - Generate all primes up to limit using Sieve of Eratosthenes
- `generate_primes_sequence(count)` - Generate first `count` prime numbers
- `prime_factors(n)` - Get complete prime factorization of n
- `next_prime(n)` - Find the next prime after n
- `prev_prime(n)` - Find the previous prime before n
- `is_twin_prime(n)` - Check if n is part of a twin prime pair
- `get_stats()` - Get performance statistics and cache info

## Examples

### Finding Large Primes

```python
gp = GenesisPrime()

# Check if a large number is prime
large_num = 982451653
print(f"{large_num} is {'prime' if gp.is_prime(large_num) else 'composite'}")

# Find the next prime after a million
next_million_prime = gp.next_prime(1000000)
print(f"Next prime after 1,000,000: {next_million_prime}")
```

### Prime Analysis

```python
# Analyze numbers for prime properties
numbers = [97, 101, 103, 107, 109, 113]

for num in numbers:
    is_prime = gp.is_prime(num)
    is_twin = gp.is_twin_prime(num) if is_prime else False
    print(f"{num}: Prime={is_prime}, Twin Prime={is_twin}")
```

### Factorization Analysis

```python
# Factor multiple numbers
test_numbers = [60, 84, 100, 128, 255]

for num in test_numbers:
    factors = gp.prime_factors(num)
    unique_factors = sorted(set(factors))
    
    print(f"{num} = {' × '.join(map(str, factors))}")
    print(f"  Unique factors: {unique_factors}")
    print(f"  Is prime power: {len(unique_factors) == 1}")
    print()
```

## Performance

GenesisPrime is optimized for performance with:

- **Intelligent Caching**: Frequently tested primes are cached for instant lookup
- **Optimized Algorithms**: Uses efficient trial division with 6k±1 optimization
- **Sieve Implementation**: Fast Sieve of Eratosthenes for bulk prime generation
- **Early Termination**: Algorithms terminate as early as possible

### Benchmarks

On a typical modern computer:
- Prime checking: ~1M checks/second for numbers < 10^6
- Sieve generation: ~100K primes/second up to 10^6  
- Factorization: ~10K factorizations/second for numbers < 10^6

## CLI Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `check <n>` | Test if n is prime | `prime_cli.py check 97` |
| `generate --count <n>` | First n primes | `prime_cli.py generate --count 10` |
| `generate --limit <n>` | Primes up to n | `prime_cli.py generate --limit 100` |
| `factors <n>` | Prime factorization | `prime_cli.py factors 60` |
| `next <n>` | Next prime after n | `prime_cli.py next 50` |
| `prev <n>` | Previous prime before n | `prime_cli.py prev 50` |
| `twin <n>` | Check twin prime | `prime_cli.py twin 17` |
| `range <a> <b>` | Primes in [a,b] | `prime_cli.py range 10 30` |
| `stats` | Show statistics | `prime_cli.py stats` |

## Installation

Simply download the Python files:

```bash
# Download the core library
wget https://raw.githubusercontent.com/Genesis-Prime/PrimeCodex/main/genesis_prime.py

# Download the CLI tool  
wget https://raw.githubusercontent.com/Genesis-Prime/PrimeCodex/main/prime_cli.py

# Make CLI executable
chmod +x prime_cli.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Testing

Run the built-in demo to verify installation:

```bash
python genesis_prime.py
```

This will run a comprehensive demonstration of all features.

## Contributing

Contributions are welcome! Areas for improvement:

- Additional prime-related algorithms (Goldbach conjecture testing, etc.)
- Performance optimizations for very large numbers
- Additional export formats (JSON, CSV, etc.)
- More statistical analysis functions
- Web interface

## License

This project is open source. See LICENSE file for details.

## Mathematical Background

### Prime Numbers
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Twin Primes  
Twin primes are pairs of prime numbers that differ by 2, such as (3,5), (5,7), (11,13), (17,19).

### Sieve of Eratosthenes
An ancient algorithm for finding all primes up to a given limit by iteratively marking multiples of each prime as composite.

---

*PrimeCodex - Unlocking the mysteries of prime numbers, one algorithm at a time.*