import math
from typing import List, Tuple, Optional

def arithmetic(a, b, op):
    """Perform simple arithmetic. Returns result or 'Tundmatu tehe'."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Tundmatu tehe"
        return a / b
    return "Tundmatu tehe"


def is_year_leap(year: int) -> bool:
    """Return True if year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def square(side: float) -> Tuple[float, float, float]:
    """Return perimeter, area and diagonal of a square."""
    perimeter = 4 * side
    area = side * side
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal


def season(month: int) -> Optional[str]:
    """Return Estonian season name for month (1-12): talv, kevad, suvi, sügis."""
    if month in (12, 1, 2):
        return "talv"
    if 3 <= month <= 5:
        return "kevad"
    if 6 <= month <= 8:
        return "suvi"
    if 9 <= month <= 11:
        return "sügis"
    return None


def bank(a: float, years: int) -> float:
    """Compound a with 10% annual interest for years years."""
    return a * (1.1 ** years)


def is_prime(n: int) -> bool:
    """
    Return True if n is prime, otherwise print its divisors and return False.
    Divisors printed are the proper divisors >1 and <n.
    """
    if n < 2:
        print("Jagajad:", [])
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        divisors = [i for i in range(2, n) if n % i == 0]
        print("Jagajad:", divisors)
        return False
    limit = int(math.sqrt(n))
    divisors = []
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if divisors:
        print("Jagajad:", sorted(divisors))
        return False
    return True


def date(day: int, month: int, year: int) -> bool:
    """Return True if given day, month, year form a valid calendar date."""
    if month < 1 or month > 12 or day < 1:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12):
        return day <= 31
    if month in (4, 6, 9, 11):
        return day <= 30
    # February
    if is_year_leap(year):
        return day <= 29
    return day <= 28


def XOR_cipher(text: str, key: str) -> str:
    """XOR-encrypt text with key (key is cycled)."""
    if not key:
        raise ValueError("Key must not be empty")
    out_chars = []
    kl = len(key)
    for i, ch in enumerate(text):
        kch = key[i % kl]
        out_chars.append(chr(ord(ch) ^ ord(kch)))
    return "".join(out_chars)


def XOR_uncipher(cipher_text: str, key: str) -> str:
    """Recover original text (XOR is symmetric)."""
    return XOR_cipher(cipher_text, key)


def average(numbers: List[float]) -> Optional[float]:
    """Return arithmetic mean of numbers or None if empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def min_max(numbers: List[float]) -> Tuple[Optional[float], Optional[float]]:
    """Return (min, max) of numbers; (None, None) if empty."""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


def unique_elements(seq: List) -> List:
    """Return list with duplicates removed preserving order."""
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out