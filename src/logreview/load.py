import os
import re
import pandas as pd
import pytz
from datetime import datetime


def get_excel_sheet(path, filename, sheetname):
    excel_file = pd.read_excel(os.path.join(path, filename), sheet_name=sheetname)
    return excel_file


def verify_backend_phoenix_date(date_string):
    """date should be in format:
    2022-11-29T01:15:31.976088-08:00
    """
    try:
        valid_date = re.match(
            r"^(\d{4})[-](\d{2})[-](\d{2})[T](\d{2})[:](\d{2})[:](\d{2})[.](\d{6})[-](\d{2})[:](\d{2})",
            date_string,
        )
        if valid_date is not None:
            return True
    except ValueError as e:
        print(f"Invalid Date: {date_string}")
    return False


def get_backend_phoenix_log(path, filename):
    log_file = os.path.join(path, filename)
    df = pd.DataFrame(
        columns=[
            "date",
            "hostname",
            "pid",
            "error_code",
            "severity",
            "detail",
        ]
    )

    with open(log_file) as f:
        for line in f:

            spaces = line.split(" ")
            date = spaces[0]
            hostname = spaces[1]
            pid = spaces[2].replace(":", "")

            remaining = " ".join(spaces[3:]).strip("\n").partition(":")
            error_code = remaining[0].strip("[]")
            if error_code == error_code.upper():
                severity = remaining[2].split(",", 4)[0].partition("=")[2]
                detail = remaining[1:]
            else:
                error_code = "NONE"
                severity = "NONE"
                detail = remaining

            df = df.append(
                {
                    "date": date,
                    "hostname": hostname,
                    "pid": pid,
                    "error_code": error_code,
                    "severity": severity,
                    "detail": detail,
                },
                ignore_index=True,
            )

    return df


def parse_string(x):
    return x[1:-1]


def parse_datetime(x):
    x = parse_string(x)
    dt = datetime.strptime(x[1:-7], "%d/%b/%Y:%H:%M:%S")
    dt_tz = int(x[-6:-3]) * 60 + int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))


def get_ssl_access_log(path, filename):
    data = pd.read_csv(
        os.path.join(path, filename),
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine="python",
        na_values="-",
        header=None,
        usecols=[0, 3, 4, 5, 6],
        names=["ip", "time", "request", "status", "size"],
        converters={
            "time": parse_datetime,
            "request": parse_string,
            "status": int,
            "size": int,
        },
    )

    return data
