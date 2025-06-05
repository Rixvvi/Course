from unittest.mock import MagicMock, patch

import pytest

from src.api import HhApi


@pytest.fixture
def mock_vacancy():
    return {
        "name": "Python Developer",
        "url": "https://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {
            "responsibility": "Develop web apps",
            "requirement": "Python, Django"
        }
    }


@patch("src.api.requests.get")
@patch("builtins.open")
def test_load_vacancies_success(mock_open, mock_get, mock_vacancy):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [mock_vacancy]}
    mock_get.return_value = mock_response

    api = HhApi()
    vacancies = api.load_vacancies("Python")

    assert isinstance(vacancies, list)
    assert len(vacancies) > 0
    assert vacancies[0]["name"] == "Python Developer"
    assert "description" in vacancies[0]
    assert "requirements" in vacancies[0]
    assert mock_get.call_count > 1
    assert mock_open.called


@patch("src.api.requests.get")
def test_load_vacancies_connection_fail(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    api = HhApi()
    result = api.load_vacancies("Python")

    assert result == []
    assert mock_get.call_count == 1


@patch("src.api.requests.get")
def test_load_vacancies_invalid_json(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response

    api = HhApi()
    result = api.load_vacancies("Python")

    assert result == []
