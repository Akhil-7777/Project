# tests/test_calculator.py
from app.calculator import add, subtract
import pytest  # Add this import

def test_add():  # Note the test_ prefix
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3
