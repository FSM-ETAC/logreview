import os
from pandas import DataFrame
from datetime import datetime
import pytz
import logreview.load as load

folder = "tests/data"
excel_file = "test_Error Codes.xlsx"
log_file = "mAOLogs/AOLogs/backend/phoenix.log"
ssl_access_file = "mAOLogs/AOLogs/system/var_log_httpd_log/ssl_access_log"


def test_get_excel_sheet_returns_DataFrame_object():
    sheetname = "backend"
    result = load.get_excel_sheet(folder, excel_file, sheetname)
    assert isinstance(result, DataFrame)


def test_get_excel_sheet_uses_row0_as_headers():
    sheetname = "backend"
    list_of_columns = [
        "Error Code",
        "Description",
        "example",
        "Root Cause",
        "How to Fix/KB",
        "Associated Tickets",
    ]
    result = load.get_excel_sheet(folder, excel_file, sheetname)
    assert len(result.columns) == len(list_of_columns)
    assert all(a == b for a, b in zip(result.columns, list_of_columns))


def test_get_backend_phoenix_log_returns_DataFrame_object():
    result = load.get_backend_phoenix_log(folder, log_file)
    assert isinstance(result, DataFrame)


def test_get_backend_phoenix_log_date_first_column():
    result = load.get_backend_phoenix_log(folder, log_file)
    assert load.verify_backend_phoenix_date(result.date[0])


def test_get_ssl_access_log_returns_DataFrame_object():
    result = load.get_ssl_access_log(folder, ssl_access_file)
    assert isinstance(result, DataFrame)


def test_parse_string_returns_string():
    result = load.parse_string("[test_string]")
    assert isinstance(result, str)


def test_parse_string_removes_first_last_delimiters():
    result = load.parse_string("[test_string]")
    assert result == "test_string"


def test_parse_datetime_returns_datetime():
    result = load.parse_datetime("[12/Apr/2022:01:00:02 -0700]")
    assert isinstance(result, datetime)


def test_parse_datetime_parses_dates():
    result = load.parse_datetime("[12/Apr/2022:01:00:02 -0700]")
    assert result == datetime(2022, 4, 2, 1, 0, tzinfo=pytz.FixedOffset(70))


def test_verify_backend_phoenix_date_fails_wrong_format():
    date_string = "12/Apr/2022:01:00:02 -0700"
    assert not load.verify_backend_phoenix_date(date_string)
