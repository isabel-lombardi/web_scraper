import os

import camelot  # to Extract Tabular Data from PDFs
import pandas as pd
import numpy as np


class ExtractData:
    def __init__(self, filename):
        self.filename = filename

    def data_from_pdf(self):

        # Increase line_scale to detect smaller lines in the table
        tables = camelot.read_pdf(self.filename, pages="1-end", line_scale=30, strip_text=";\n")

        # convert each table in a dataframe
        df_table = [tab.df for tab in tables]

        # concatenate all dataframe into one
        df = pd.concat(df_table, ignore_index=True)

        # fix dataframe header
        df.columns = df.iloc[0]
        df = df[1:]

        # Missing data in the document was represented by a "-"
        # I turn it into a NaN value
        df = df.replace("-", np.nan)

        # save dataframe
        # remove file extension (PDF) and save csv with the same filename
        filename = os.path.splitext(self.filename)[0]
        df.to_csv(filename + ".csv", index=False)

        path, filename = os.path.split(filename)
        print("\n-The file '{}.csv' is available in the folder '{}'".format(filename, path))