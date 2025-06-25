import pytest
import csv
from main import isNumber, get_filter_values, get_aggregate_values, get_filtered_products, get_aggregation_result, main


# Фикстура для тестовых данных
@pytest.fixture
def sample_products():
    return [
        {"name": "Product1", "price": "10.5", "rating": "4.5"},
        {"name": "Product2", "price": "20.0", "rating": "4.7"},
        {"name": "Product3", "price": "15.0", "rating": "4.9"},
    ]

# Тесты для isNumber
def test_isNumber():
    assert isNumber('4') is True 
    assert isNumber('4.7') is True
    assert isNumber('asd23') is False

# Тесты для get_filter_values
def test_get_filter_values_greater_than():
    column, value, symb = get_filter_values("rating>4.7")
    assert column == "rating"
    assert value == "4.7"
    assert symb == ">"

def test_get_filter_values_less_than():
    column, value, symb = get_filter_values("price<20")
    assert column == "price"
    assert value == "20"
    assert symb == "<"

def test_get_filter_values_equals():
    column, value, symb = get_filter_values("name=iphone 15 pro")
    assert column == "name"
    assert value == "iphone 15 pro"
    assert symb == "="

def test_get_filter_values_invalid():
    column, value, symb = get_filter_values("invalidfilter")
    assert column == ""
    assert value == ""
    assert symb == ""

# Тесты для get_aggregate_values
def test_get_aggregate_values_min():
    column, value = get_aggregate_values("rating=min")
    assert column == "rating"
    assert value == "min"

def test_get_aggregate_values_max():
    column, value = get_aggregate_values("price=max")
    assert column == "price"
    assert value == "max"

def test_get_aggregate_values_avg():
    column, value = get_aggregate_values("rating=avg")
    assert column == "rating"
    assert value == "avg"

def test_get_aggregate_values_invalid():
    column, value = get_aggregate_values("rating=invalid")
    assert column == ""
    assert value == ""

# Тесты для get_filtered_products
def test_get_filtered_products_gt(sample_products):
    result = get_filtered_products(sample_products, "rating", "4.6", ">")
    assert len(result) == 2
    assert result[0]["name"] == "Product2"

def test_get_filtered_products_lt(sample_products):
    result = get_filtered_products(sample_products, "price", "20", "<")
    assert len(result) == 2
    assert result[0]["name"] == "Product1"

def test_get_filtered_products_eq_number(sample_products):
    result = get_filtered_products(sample_products, "rating", "4.7", "=")
    assert len(result) == 1
    assert result[0]["name"] == "Product2"

def test_get_filtered_products_eq_string(sample_products):
    result = get_filtered_products(sample_products, "name", "Product1", "=")
    assert len(result) == 1
    assert result[0]["name"] == "Product1"

# Тесты для get_aggregation_result
def test_get_aggregation_result_min(sample_products):
    result = get_aggregation_result(sample_products, "price", "min")
    assert result == ["10.5"]

def test_get_aggregation_result_max(sample_products):
    result = get_aggregation_result(sample_products, "rating", "max")
    assert result == ["4.9"]

def test_get_aggregation_result_avg(sample_products):
    result = get_aggregation_result(sample_products, "rating", "avg")
    assert result == [pytest.approx((4.5 + 4.7 + 4.9) / 3)]
