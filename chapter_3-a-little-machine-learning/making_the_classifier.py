from sklearn import svm, preprocessing, cross_validation
import pandas as pd
from helpers import SOURCES_PATH


HPI_Plus = pd.read_pickle(SOURCES_PATH + 'prepped_US_HPI_Plus.pickle')
print(HPI_Plus.head())

