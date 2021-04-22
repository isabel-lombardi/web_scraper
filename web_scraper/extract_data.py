import os

import camelot  # to Extract Tabular Data from PDFs
import pandas as pd
import numpy as np


class ExtractData:
    def __init__(self, filename):
        self.filename = filename