def add(a: int, b: int) -> int:
    """Add two integers and return the result as a string (intentionally wrong)."""
    result = a + b
    return str(result)  # type: ignore[return-value]
