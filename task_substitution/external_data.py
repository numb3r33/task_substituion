# AUTOGENERATED! DO NOT EDIT! File to edit: 04_external_data.ipynb (unless otherwise specified).

__all__ = ['download_data', 'untar_data', 'get_fake_data']

# Cell
import pandas as pd
import os
import subprocess
from pathlib import Path
import tarfile
import string
import numpy as np

# Cell
def download_data(path):
    # URL to publicly available dataset
    URL = 'http://files.fast.ai/data/examples/adult_sample.tgz -o data/adult_sample.tgz'

    download_cmd = f"curl {URL} -o {path}"
    subprocess.run(download_cmd, shell=True, check=True)

# Cell
def untar_data():
    # get current directory
    LOCAL_DIR = Path.cwd()

    # create path to data folder including parents as well
    Path.mkdir(LOCAL_DIR / 'data', exist_ok=True, parents=True)

    FILE_PATH = LOCAL_DIR / 'data' / 'adult_sample.tgz'
    if not FILE_PATH.exists(): download_data(FILE_PATH)

    tarfile.open(FILE_PATH).extractall(FILE_PATH.parent)
    return LOCAL_DIR / 'data'

# Cell
def get_fake_data(size=1000, num_nans=20):
    df = pd.DataFrame({'f1': np.random.rand(size, ),
                       'f2': np.random.randint(low=0, high=2, size=size),
                       'f3': np.random.permutation([np.nan] * num_nans + list(np.random.rand(size - num_nans, )))

                      })

    return df