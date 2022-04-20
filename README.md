# Log Review

## Install

1. Clone project to new folder
2. within that folder install with:

```bash
pip install -e .
```

3. set default paths in ./configs/logreview.ini

## Usage

```bash
usage: unpack.py [-h] [-c CUSTOMER] [-f FILENAME]

options:
  -h, --help            show this help message and exit
  -c CUSTOMER, --customer CUSTOMER
                        Customer Number
  -f FILENAME, --filename FILENAME
                        Filename of tar file
```

## Example

```bash
python unpack.py -c 5723255 -f AOLogs_5723255_Collector_DEBUG.tar
