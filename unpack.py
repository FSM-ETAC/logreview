from time import strftime
import pandas as pd
import fnmatch
import os, gzip, tarfile, sys
import shlex, subprocess, shutil


def run_command(raw_command):
    command=shlex.split(raw_command)
    system=subprocess.Popen(command)
    return system.communicate()


def prepare_target_path(target_path, customer_number):
    customer_path=os.path.join(target_path, customer_number)
    try:
        os.mkdir(customer_path)
    except FileExistsError:
        date_string=strftime('%Y%m%d_%H%M%S')
        customer_path=os.path.join(customer_path, date_string)
        os.mkdir(customer_path)
    except:
        raise
    return customer_path

def unpack(root_path, target_path, customer_number, sample_tar):
    pattern= '*.gz'
    customer_path = prepare_target_path(target_path, customer_number)

    with tarfile.open(os.path.join(root_path, sample_tar)) as tar:
        tar.extractall(customer_path)

    for root, dirs, files in os.walk(customer_path):
        for filename in fnmatch.filter(files, pattern):
            current_file=os.path.join(root, filename)
            target_file=os.path.join(root, os.path.splitext(filename)[0])
            with gzip.open(current_file, 'rb') as zip_in:
                with open(target_file, 'wb') as zip_out:
                    shutil.copyfileobj(zip_in, zip_out)
            _=run_command(f'rm -f {current_file}')





root_path=r'/Users/jdavenport/Downloads'
target_path=r'/Users/jdavenport/Downloads/tempLogs'
customer_number='5900299'
tar_filename='collector-AOLogs-3.tar'
unpack(root_path, target_path, customer_number, tar_filename)
                






print('done')
