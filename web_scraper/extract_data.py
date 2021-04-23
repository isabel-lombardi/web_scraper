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
        df_tables = [tab.df for tab in tables]

        # concatenate all dataframe into one
        df = pd.concat(df_tables, ignore_index=True)

        # fix dataframe header
        df.columns = df.iloc[0]
        df = df[1:]

        # replace No-Break
        # Missing data in the document was represented by a "-", turn it into a NaN value
        df = df.replace({"\u00A0": " ", "-": np.nan}, regex=True)
        df.columns = df.columns.str.replace("\u00A0", " ")

        for i in range(2, 4):
            # remove currency symbols
            df.iloc[:, i].replace(to_replace="[^0-9\.-]", value="", regex=True, inplace=True)

            # df column from object to float
            df.iloc[:, i] = pd.to_numeric(df.iloc[:, i])


        # save dataframe
        # remove file extension (PDF) and save csv with the same filename
        filename = os.path.splitext(self.filename)[0]
        df.to_csv(filename + ".csv", index=False)

        path, filename = os.path.split(filename)
        print("\n-The file '{}.csv' is available in the folder '{}'".format(filename, path))