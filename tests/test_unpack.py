import os
from testing_utilities.testing_utilities import LRtest_session, compare_dirs
from logreview.unpack import unpack


def test_unpack():
    root_path = r"./tests/data"
    target_path = r"./tests/data/tempLogs"
    customer_number = "3300299"
    tar_filename = "AOLogs.tar"
    baseline_path = os.path.join(target_path, "1100299")
    customer_path = os.path.join(target_path, customer_number)
    unpack(root_path, target_path, customer_number, tar_filename)
    assert compare_dirs(baseline_path, customer_path) == True
