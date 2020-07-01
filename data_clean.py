import kaggle_download
from kaggle_download import df
import pandas as pd
import time

start_time = time.time()

if __name__ == "__main__":
    print('Main Program.')

    #### Change Data Types ####
    df["ObservationDate"] = pd.to_datetime(df["ObservationDate"]).dt.date
    df["Last Update"] = pd.to_datetime(df["Last Update"], exact=True).dt.date

    ## Convert String Columns ##
    lst = list(df)[2:4]
    df[lst] = df[lst].astype(str)

    ## Only US ##
    is_US = df["Country/Region"] == "US"
    US = df[is_US]

    ##### Summary Info ####
    type(US)
    list(US)
    US = US.drop(columns=["SNo"])

    #### GroupBy Pandas ####
    # df.groupby('Id', as_index=False)
    daily_totals = US.groupby(["ObservationDate"], as_index=False).sum()

else:
    print('1: {} module imported...'.format(__name__))
    

    # Logging Message
    print('\n2: {} module initiating data cleansing...\n'.format(__name__))

    #### Change Data Types ####
    df["ObservationDate"] = pd.to_datetime(df["ObservationDate"]).dt.date
    df["Last Update"] = pd.to_datetime(df["Last Update"], exact=True).dt.date

    ## Convert String Columns ##
    lst = list(df)[2:4]
    df[lst] = df[lst].astype(str)

    ## Only US ##
    is_US = df["Country/Region"] == "US"
    US = df[is_US]

    ##### Summary Info ####
    type(US)
    list(US)
    US = US.drop(columns=["SNo"])

    #### GroupBy Pandas ####
    # df.groupby('Id', as_index=False)
    daily_totals = US.groupby(["ObservationDate"], as_index=False).sum()

    print('\n3: Cleaning completed in {} seconds.'.format(time.time() - start_time))
