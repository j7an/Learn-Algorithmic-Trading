# loading the class data from the package pandas_datareader
from pandas_datareader import data
import pandas as pd

pd.set_option('display.max_columns', 1000)
# pd.set_printoptions('max_colwidth', 1000)
pd.set_option('display.width', 1000)
# First day
start_date = '2014-01-01'
# Last day
end_date = '2020-01-01'
# Call the function DataReader from the class data
goog_data = data.DataReader('AAPL', 'yahoo', start_date, end_date)
print((goog_data))