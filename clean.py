import os, shlex, subprocess

def run_command(raw_command):
    command=shlex.split(raw_command)
    system=subprocess.Popen(command)
    return system.communicate()

target_path=r'/Users/jdavenport/Downloads/tempLogs'
customer_number='5807288'

customer_path=os.path.join(target_path, customer_number)
outcome=run_command(f'rm -rf {customer_path}')