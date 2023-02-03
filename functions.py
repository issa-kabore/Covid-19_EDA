from termcolor import colored as cl  # text customization
import pandas as pd
from pandas_profiling import ProfileReport
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
    print(cl('NULL VALUES', attrs=['bold'], color='green'))
    print(null_column_report_df(dataframe))
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
    print(cl('SUMMARY OF STATISTICS', attrs=['bold'], color='green'))
    print(dataframe.describe())
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
