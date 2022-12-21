import os
import pandas as pd

def get_sheets(path, filename):
    excel_file = pd.read_excel(os.path.join(path, filename))
    return excel_file


