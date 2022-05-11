"""Module responsible for reading in Rrs samples."""

import glob
import numpy as np
import pathlib
import os

def read_rrs_samples(params):

    # read Rrs samples
    resolved_rrs_path=os.path.join(pathlib.Path(__file__).parent.resolve(), params["Rrs_samples"]["sample_dir"],'*.txt')
    rrs_files = glob.glob(resolved_rrs_path)
    rrs_samples = []
    for rrs_file in rrs_files:
        this_sample = np.genfromtxt(rrs_file, comments="#", delimiter=',', dtype=float)
        this_sample[this_sample <0] = np.nan
        rrs_samples.append(this_sample)

    return rrs_files, rrs_samples