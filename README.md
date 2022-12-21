# Log Review

## Install

1. Clone project to new folder
2. within that folder install with:

    ```bash
    pip install .
    ```

3. set default paths tar files and extracted logs in ./configs/logreview.ini
4. add a custom alias replacing <path_to_installed_unpack.py> with the path where step 2 was performed:

    ```bash
    echo "alias unpack=$(which python3) <path_to_installed_unpack.py>" >> ~/.zshrc
    ```

### Install with testing

```bash
pip install -r requirements_dev.txt
```

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
unpack -c 5723255 -f AOLogs_5723255_Collector_DEBUG.tar
