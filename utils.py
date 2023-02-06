from termcolor import colored as cl  # text customization
import pandas as pd
# from pandas_profiling import ProfileReport
import logging


# create logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
LOGGER.addHandler(ch)


def data_info(dataframe: pd.DataFrame):
    LOGGER.info("Getting dataframe information")
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
    print(cl('COLUMNS INFORMATION', attrs=['bold'], color='green'))
    print(cl('The dataset has {} cases and {} features'.format(*dataframe.shape), attrs=['bold']))
    print(dataframe.info(verbose=True, show_counts=False))
    print(cl('------------------------------------------------------------------------', attrs=['bold']))


def null_column_report_df(df):
    """
    Searches a dataframe for null columns and returns a dataframe of the format
    Column | Total Nulls | Percent Nulls
    """
    num_null_columns = df.shape[1] - df.dropna(axis=1).shape[1]
    print(cl('Number of columns with null values:\n{}\n'.format(num_null_columns), attrs=['bold']))
    null_columns = df.columns[df.isnull().any()].tolist()
    null_info_records = []
    for col in null_columns:
        total_null_records = df[col].isnull().sum()
        percent_null_records = round(total_null_records / df.shape[0], 2)
        null_info_records.append({
            'Column': col,
            'Total_Null_Records': total_null_records,
            'Percent_Null_Records': percent_null_records
        })
    return pd.DataFrame(null_info_records)