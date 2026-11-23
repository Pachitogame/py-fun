"""Arithmetic on numbers, numeric strings, number words and Roman numerals."""

_DIGITS = (
    "zero one two three four five six seven eight nine ten",
    "null eins zwei drei vier fünf sechs sieben acht neun zehn",
    "cero uno dos tres cuatro cinco seis siete ocho nueve diez",
    "ноль один два три четыре пять шесть семь восемь девять десять",
    "零 一 二 三 四 五 六 七 八 九 十",
)
_VALUES = {word: n for row in _DIGITS for n, word in enumerate(row.split())}
_VALUES.update(zip("i ii iii iv v vi vii viii ix x".split(), range(1, 11)))
_VALUES["fuenf"] = 5


def _number(value):
    if isinstance(value, (int, float)):
        return value
    if not isinstance(value, str):
        return 0
    word = value.strip().casefold()
    if word in _VALUES:
        return _VALUES[word]
    try:
        return int(word)
    except ValueError:
        try:
            return float(word)
        except ValueError:
            return 0


class Calculator:
    """A single shared calculator. Unrecognized inputs count as zero."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a, b):
        """Return the sum of two operands."""
        return _number(a) + _number(b)

    def sub(self, a, b):
        """Subtract b from a."""
        return _number(a) - _number(b)

    def mul(self, a, b):
        """Return the product of two operands."""
        return _number(a) * _number(b)

    def div(self, a, b):
        """Divide a by b, returning positive infinity for a zero divisor."""
        divisor = _number(b)
        return _number(a) / divisor if divisor else float("inf")

    def factorize(self, n):
        """Return prime factors in order. Zero and one have empty results."""
        n = _number(n)
        if n < 0 or (isinstance(n, float) and not n.is_integer()):
            raise ValueError("factorization requires a nonnegative integer")
        n = int(n)
        factors = []
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor = 3 if divisor == 2 else divisor + 2
        if n > 1:
            factors.append(n)
        return factors
