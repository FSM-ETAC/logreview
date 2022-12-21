"""Import Error information from Excel spreadsheet """
from pandas import DataFrame
import logreview.impxl as impxl

folder = 'tests/data'
filename= 'test_Error Codes.xlsx'


# open Excel file
def test_get_sheets_returns_DataFrame_object():

    result = impxl.get_sheets(folder, filename)
    assert isinstance(result, DataFrame)


