import json
from unittest.mock import mock_open, patch

from src.reader_json import ReaderJson

vacancy_sample = {
    "name": "Python Developer",
    "link": "https://example.com",
    "salary": 150000,
    "responsibility": "Write code",
    "requirements": "Python"
}


def test_read_file_success():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        result = reader._read_file()
        assert result == [vacancy_sample]


def test_read_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        reader = ReaderJson("not_exist.json")
        result = reader._read_file()
        assert result == []


def test_save_file_success():
    with patch("builtins.open", mock_open()) as file:
        reader = ReaderJson("test.json")
        reader._save_file([vacancy_sample])
        file.assert_called_once_with("test.json", "w", encoding="utf-8")
        handle = file()
        handle.write.assert_called()


def test_add_vacancy_new():
    mock_data = json.dumps([])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        with patch("json.dump") as mock_dump:
            reader.add_vacancies(vacancy_sample)
            mock_dump.assert_called_once()


def test_add_vacancy_duplicate_not_added():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        with patch("json.dump") as mock_dump:
            reader.add_vacancies(vacancy_sample)
            mock_dump.assert_not_called()


def test_get_vacancies_all():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        result = reader.get_vacancies()
        assert result == [vacancy_sample]


def test_get_vacancies_filtered_match():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        result = reader.get_vacancies({"name": "Python Developer"})
        assert result == [vacancy_sample]


def test_get_vacancies_filtered_no_match():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        result = reader.get_vacancies({"name": "Java Developer"})
        assert result == []


def test_delete_vacancy_exists():
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        with patch("json.dump") as mock_dump:
            result = reader.delete_vacancies(vacancy_sample)
            assert result == []
            mock_dump.assert_called_once()


def test_delete_vacancy_not_found():
    another = dict(vacancy_sample)
    another["name"] = "Another"
    mock_data = json.dumps([vacancy_sample])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        reader = ReaderJson("test.json")
        with patch("json.dump") as mock_dump:
            result = reader.delete_vacancies(another)
            assert result == [vacancy_sample]
            mock_dump.assert_called_once()
