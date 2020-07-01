

# import pandas as pd


# def extract_kaggle(urlpath):
#     # Find your desired dataset urlpath
#     # Enter that argument into 'extract_kaggle'

#     # Login to local kaggle
#     user = kaggle.KaggleApi()
#     user.authenticate()

#     # Download files from Kaggle Webpage
#     user.dataset_download_cli(dataset=urlpath,
#                               unzip=True)


# # Dataset URL Path
# dataset_urlpath = 'sudalairajkumar/novel-corona-virus-2019-dataset'

# extract_kaggle(dataset_urlpath)

# # Store Pandas Dataframe
# df = pd.read_csv(
#     "C:/Users/jwill/OneDrive/Desktop/Python/Coronavirus/covid_19_data.csv")

if __name__ == "__main__":
    print("Run from Main Program")


else:
    print('{} module imported...'.format(__name__))
    import os
    import pandas as pd
    os.environ['KAGGLE_USERNAME'] = "jwill93"
    os.environ['KAGGLE_KEY'] = "9d13bc6586379f81d5c7530d72964f1d"
    os.system('kaggle datasets download -d sudalairajkumar/novel-corona-virus-2019-dataset --unzip')


    # import kaggle
    # import pandas as pd

    # # Dataset URL Path. Change path for different data extraction
    # dataset_urlpath = 'sudalairajkumar/novel-corona-virus-2019-dataset'

    # extract_kaggle(dataset_urlpath)

    # Store Pandas Dataframe
    df = pd.read_csv(
        "/home/jwstats/Coronavirus_us/covid_19_data.csv")
