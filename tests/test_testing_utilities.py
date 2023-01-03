from sys import platform
from testing_utilities.testing_utilities import (
    LRtest_session,
    get_path_list,
    compare_dirs,
)


def test_get_path_list():
    # get_path_list takes a path and returns a list of relative path names
    path1 = r"./tests/data/tempLogs/1100299"
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # linux or OS X
        paths = [
            "AOLogs/backend/svnlite.log",
            "AOLogs/backend/phoenix.log",
            "AOLogs/backend/phxctl.log",
            "AOLogs/backend/phoenix.log-2022-04-12-1649750401",
            "AOLogs/backend/completed_discovery_results.tgz",
            "AOLogs/backend/archiver.log",
            "AOLogs/system/top",
            "AOLogs/system/proc_cpuinfo",
            "AOLogs/system/messages",
            "AOLogs/system/df",
            "AOLogs/system/sa11",
            "AOLogs/system/ph-show-version.txt",
            "AOLogs/system/phstatus",
            "AOLogs/system/sss",
            "AOLogs/system/AO_VERSION",
            "AOLogs/system/sa12",
            "AOLogs/system/etc_snmp_snmpd.conf",
            "AOLogs/system/vmstat",
            "AOLogs/system/var_log_httpd_log/ssl_access_log",
            "AOLogs/system/var_log_httpd_log/ssl_request_log",
            "AOLogs/system/var_log_httpd_log/ssl_error_log-20220412",
            "AOLogs/system/var_log_httpd_log/ssl_error_log",
            "AOLogs/system/var_log_httpd_log/ssl_access_log-20220412",
            "AOLogs/system/var_log_httpd_log/ssl_request_log-20220412",
            "AOLogs/postgres/postgresql.log",
            "AOLogs/postgres/postgresql.log-2022-04-12-1649797201.gz",
            "AOLogs/appsvr/phoenix.log",
            "AOLogs/appsvr/server.log",
        ]
    elif platform == "win32":
        # Windows...
        paths = [
            r"AOLogs\backend\svnlite.log",
            r"AOLogs\backend\phoenix.log",
            r"AOLogs\backend\phxctl.log",
            r"AOLogs\backend\phoenix.log-2022-04-12-1649750401",
            r"AOLogs\backend\completed_discovery_results.tgz",
            r"AOLogs\backend\archiver.log",
            r"AOLogs\system\top",
            r"AOLogs\system\proc_cpuinfo",
            r"AOLogs\system\messages",
            r"AOLogs\system\df",
            r"AOLogs\system\sa11",
            r"AOLogs\system\ph-show-version.txt",
            r"AOLogs\system\phstatus",
            r"AOLogs\system\sss",
            r"AOLogs\system\AO_VERSION",
            r"AOLogs\system\sa12",
            r"AOLogs\system\etc_snmp_snmpd.conf",
            r"AOLogs\system\vmstat",
            r"AOLogs\system\var_log_httpd_log\ssl_access_log",
            r"AOLogs\system\var_log_httpd_log\ssl_request_log",
            r"AOLogs\system\var_log_httpd_log\ssl_error_log-20220412",
            r"AOLogs\system\var_log_httpd_log\ssl_error_log",
            r"AOLogs\system\var_log_httpd_log\ssl_access_log-20220412",
            r"AOLogs\system\var_log_httpd_log\ssl_request_log-20220412",
            r"AOLogs\postgres\postgresql.log",
            r"AOLogs\postgres\postgresql.log-2022-04-12-1649797201.gz",
            r"AOLogs\appsvr\phoenix.log",
            r"AOLogs\appsvr\server.log",
        ]

    assert get_path_list(path1) == paths


def test_compare_dirs():
    path1 = r"./tests/data/tempLogs/1100299"
    path2 = r"./tests/data/mAOLogs"
    assert compare_dirs(path1, path2) == True
