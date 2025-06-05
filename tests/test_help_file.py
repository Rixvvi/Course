import pytest

from src.help_file import get_search_str, top_transactions


@pytest.fixture
def list_dict():
    return [
        {"id": 1, "description": "Python Developer"},
        {"id": 2, "description": "Data analyst with Python knowledge"},
        {"id": 3, "description": "Java developer"},
        {"id": 4, "description": ""},
        {"id": 5},
    ]


def test_match_found(list_dict):
    result = get_search_str(list_dict, "Python")
    assert len(result) == 2
    assert list_dict[0] in result
    assert list_dict[1] in result


def test_no_match(list_dict):
    result = get_search_str(list_dict, "Rust")
    assert result == []


def test_empty_description(list_dict):
    result = get_search_str(list_dict, "Python")
    assert list_dict[3] not in result


def test_missing_description_key(list_dict):
    result = get_search_str(list_dict, "Python")
    assert list_dict[4] not in result


def test_case_insensitive_search(list_dict):
    result = get_search_str(list_dict, "python")
    assert len(result) == 2


def test_special_characters_in_search():
    data = [{"description": "C++ developer"}]
    result = get_search_str(data, r"C\+\+")
    assert len(result) == 1
    assert result[0] == data[0]


def test_invalid_input_type():
    result = get_search_str("not a list", "Python")
    assert result == []


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "salary": {"from": 1000, "to": 2000}},
        {"id": 2, "salary": {"from": 3000}},
        {"id": 3, "salary": {"to": 2500}},
        {"id": 4, "salary": None},
        {"id": 5, "salary": {"from": 2000, "to": 4000}},
        {"id": 6},
    ]


def test_top_3_transactions(sample_data):
    result = top_transactions(sample_data, 3)
    expected_ids = [2, 5, 3]
    assert [r["id"] for r in result] == expected_ids


def test_top_1_transaction(sample_data):
    result = top_transactions(sample_data, 1)
    assert result[0]["id"] in [2, 5]


def test_top_0_transactions(sample_data):
    result = top_transactions(sample_data, 0)
    assert result == []


def test_all_transactions_returned_if_n_exceeds(sample_data):
    result = top_transactions(sample_data, 10)
    assert len(result) == len(sample_data)
