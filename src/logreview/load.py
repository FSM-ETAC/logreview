import os
import re
import pandas as pd
import pytz
from datetime import datetime

def get_sheets(path, filename, sheetname):
    excel_file = pd.read_excel(os.path.join(path, filename), sheet_name=sheetname)
    return excel_file

def get_logs(path, filename):
    log_file = os.path.join(path, filename)
    df = pd.DataFrame(columns=['date','hostname','pid','error_code','severity','process','file','line','detail'])

    with open(log_file) as f:
        for line in f:

            spaces = line.split(' ')
            remaining=' '.join(spaces[3 : ]).strip('\n').partition(':')
            final=remaining[2].split(',', 4)

            date=spaces[0]
            hostname=spaces[1]
            pid=spaces[2].replace(':','')
            error_code=remaining[0].strip('[]')
            severity=final[0].partition('=')[2]
            process=final[1].partition('=')[2]
            file_name=final[2].partition('=')[2]
            line=final[3].partition('=')[2]
            detail=final[4].partition('=')[2]


            df = df.append({'date':date,
                            'hostname':hostname,
                            'pid':pid,
                            'error_code':error_code,
                            'severity':severity,
                            'process':process,
                            'file':file_name,
                            'line':line,
                            'detail':detail},
                            ignore_index=True)

    return df

def parse_string(x):
    return x[1:-1]

def parse_datetime(x):
    x=parse_string(x)
    dt=datetime.strptime(x[1:-7], '%d/%b/%Y:%H:%M:%S')
    dt_tz=int(x[-6:-3])*60+int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))

def get_ssl_access_logs(path, filename):
    data = pd.read_csv(
    os.path.join(path, filename),
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0, 3, 4, 5, 6],
    names=['ip', 'time', 'request', 'status', 'size'],
    converters={'time': parse_datetime,
                'request': parse_string,
                'status': int,
                'size': int})

    return data
