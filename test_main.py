from main import taxable_income, tax, net_income
import pytest

def test_taxable_income():
    assert taxable_income(200000) == 200000

def test_negative_income():
    with pytest.raises(ValueError):
        taxable_income(-1000)

def test_no_tax():
    assert tax(200000) == 0

def test_tax_5_percent():
    assert tax(400000) == 7500

def test_tax_20_percent():
    assert tax(800000) == 72500

def test_tax_30_percent():
    assert tax(1200000) == 142500

def test_net_income():
    assert net_income(800000) == 727500