from time import strftime
from tqdm import tqdm
import pandas as pd
import fnmatch, os, gzip, tarfile, shutil


def prepare_target_path(target_path, customer_number):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    customer_path=os.path.join(target_path, customer_number)
    try:
        os.mkdir(customer_path)
    except FileExistsError:
        #if the file already exists create a new folder using the date and time string
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

    for root, _, files in os.walk(customer_path):
        total_files=len(files)
        for filename in tqdm(fnmatch.filter(files, pattern), desc='unpacking - ', total=total_files, unit=' files', leave=True):
            current_file=os.path.join(root, filename)
            target_file=os.path.join(root, os.path.splitext(filename)[0])
            with gzip.open(current_file, 'rb') as zip_in:
                with open(target_file, 'wb') as zip_out:
                    shutil.copyfileobj(zip_in, zip_out)
            os.remove(current_file)



if __name__== '__main__':

    root_path=r'/Users/jdavenport/Projects/LogReview/tests/data'
    target_path=r'/Users/jdavenport/Projects/LogReview/tests/data/tempLogs'
    customer_number='2200299'
    tar_filename='AOLogs.tar'
    unpack(root_path, target_path, customer_number, tar_filename)
    print('done')
