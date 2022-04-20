import argparse
from configparser import ConfigParser
from logreview.unpack import unpack

def config(filename: str = './configs/logreview.ini', section: str = 'logreview'):
    parser: ConfigParser = ConfigParser()
    parser.read(filename)

    configs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configs[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return configs

def app():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--customer', type=str, help='Customer Number')
    parser.add_argument('-f', '--filename', type=str, help='Filename of tar file')
    args = parser.parse_args()
    defaults=config()

    root_path=defaults['root_path_default']
    target_path=defaults['target_path_default']
    customer_number= args.customer
    tar_filename= args.filename
    unpack(root_path, target_path, customer_number, tar_filename)