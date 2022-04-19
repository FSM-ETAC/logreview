
from testing_utilities.testing_utilities import LRtest_session, get_path_list, compare_dirs


def test_get_path_list():
    #get_path_list takes a path and returns a list of relative path names 
    path1=r'./tests/data/tempLogs/1100299'
    paths= ['AOLogs/backend/svnlite.log',
        'AOLogs/backend/phoenix.log',
        'AOLogs/backend/phxctl.log',
        'AOLogs/backend/phoenix.log-2022-04-12-1649750401',
        'AOLogs/backend/completed_discovery_results.tgz',
        'AOLogs/backend/archiver.log',
        'AOLogs/system/top',
        'AOLogs/system/proc_cpuinfo',
        'AOLogs/system/messages',
        'AOLogs/system/df',
        'AOLogs/system/sa11',
        'AOLogs/system/ph-show-version.txt',
        'AOLogs/system/phstatus',
        'AOLogs/system/sss',
        'AOLogs/system/AO_VERSION',
        'AOLogs/system/sa12',
        'AOLogs/system/etc_snmp_snmpd.conf',
        'AOLogs/system/vmstat',
        'AOLogs/system/var_log_httpd_log/ssl_access_log',
        'AOLogs/system/var_log_httpd_log/ssl_request_log',
        'AOLogs/system/var_log_httpd_log/ssl_error_log-20220412',
        'AOLogs/system/var_log_httpd_log/ssl_error_log',
        'AOLogs/system/var_log_httpd_log/ssl_access_log-20220412',
        'AOLogs/system/var_log_httpd_log/ssl_request_log-20220412',
        'AOLogs/postgres/postgresql.log',
        'AOLogs/postgres/postgresql.log-2022-04-12-1649797201.gz',
        'AOLogs/appsvr/phoenix.log',
        'AOLogs/appsvr/server.log'
        ]

    assert get_path_list(path1) == paths

def test_compare_dirs():
    path1=r'./tests/data/tempLogs/1100299'
    path2=r'./tests/data/mAOLogs'
    assert compare_dirs(path1, path2) == True

