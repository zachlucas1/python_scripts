from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest


def test_names():
    """Test the chemistry.get_name function."""
    assert get_name("H") == "Hydrogen"
    assert get_name("Fe") == "Iron"
    assert get_name("Rf") == "Rutherfordium"
    # TODO: write this function.

def test_atomic_masses():
    """Test the chemistry.get_atomic_mass function."""
    assert get_atomic_mass("H") == 1.01
    assert get_atomic_mass("Fe") == 55.845
    assert get_atomic_mass("Rf") == 267
    # TODO: write this function.

def test_parse():
    """Test the chemistry.parse_formula function."""
    assert parse_formula("O3") == {"O":3}
    assert parse_formula("H2O") == {"H":2, "O":1}
    assert parse_formula("C6H12O6") == {"C":6, "H":12, "O":6}
    assert parse_formula("PO4H2(CH2)12CH3") == {'P': 1, 'O': 4, 'H': 29, 'C': 13}

    try:
        parse_formula("L")
        parse_formula("4H")
        parse_formula("H2L4")
        parse_formula("-H")
        parse_formula("(H2O")
        parse_formula("H2)O3")
        assert False

    except FormulaError as ex:
        assert True
    # TODO: write this function.

def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    assert molar_mass(parse_formula("H2O")) == approx(18.01528, 0.01)
    assert molar_mass(parse_formula("C6H6")) == approx(78.11184, 0.01)
    assert molar_mass(parse_formula("PO4H2(CH2)12CH3")) == approx(280.34072, 0.01)
    # TODO: write this function.

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "test_chemistry.py"])