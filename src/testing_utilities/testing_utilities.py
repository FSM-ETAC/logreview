
import tarfile
import pytest
import os
from shutil import rmtree
from filecmp import cmp



@pytest.fixture(autouse=True)
def LRtest_session():
    #setup
    base_path=r'./tests/data'
    tempLogs_path = r'./tests/data/tempLogs'
    if os.path.exists(tempLogs_path):
        rmtree(tempLogs_path)
    baseline_path = os.path.join(tempLogs_path, '1100299','AOLogs')
    baseline_log = 'aAOLogs.tar'
    os.makedirs(baseline_path)
    with tarfile.open(os.path.join(base_path,baseline_log)) as tar:
        tar.extractall(baseline_path)


    yield   #test
    #teardown
    rmtree(tempLogs_path)


def get_path_list(path1):
    paths=[]
    for root, _, files in os.walk(path1):
        for filename in files:
            paths.append(os.path.relpath(os.path.join(root, filename), start=path1))
    return paths

def compare_dirs(path1, path2):
    p1 = get_path_list(path1)
    matched_paths=[]
    for root, _, files in os.walk(path2):
        for filename in files:
            current_file=os.path.relpath(os.path.join(root, filename), start=path2)
            if current_file in p1:
                p1file_index=p1.index(current_file)
                p1file=os.path.join(path1, p1[p1file_index])
                p2file=os.path.join(path2, current_file)

                if cmp(p2file, p1file):
                    matched_paths.append(current_file)
            else:
                return False

    if (len(p1) == len(matched_paths)):
        return True
    else:
        return False