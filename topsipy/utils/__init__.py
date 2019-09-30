import pandas as pd


def slice_in_chunks(dataframe, chunks):
    return [dataframe[i:i+chunks] for i in range(0,dataframe.shape[0],chunks)]