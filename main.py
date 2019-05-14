from __future__ import print_function

import os
import argparse
import sys
import multiprocessing
import csv

import requests
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

parser = argparse.ArgumentParser(description='Runs a kmeans cluster analysis for anomaly detection')
parser.add_argument("--url_in", help="remote address for the input data")
parser.add_argument("--url_out", help="remote address for the output data")

args = parser.parse_args()

input = pd.read_csv(args.url_in)

print(input)

requests.put(args.url_out, data=input.to_csv())