import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    # Check if an argument is provided, otherwise default to 5
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])  # Read the number from the command-line argument
        except ValueError:
            print("Error: Please provide a valid integer.")
            sys.exit(1)
    else:
        n = 5  # Default value

    print(f"First {n} prime numbers: {generate_primes(n)}")

