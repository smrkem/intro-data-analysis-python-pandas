from sklearn import svm, preprocessing, cross_validation
import pandas as pd, numpy as np
from helpers import SOURCES_PATH
import pickle

# Grab our prepped data from last time
HPI_Plus = pd.read_pickle(SOURCES_PATH + 'prepped_US_HPI_Plus.pickle')
# print(HPI_Plus.head())

# create features (X) and labels (y)

# We don't want any label stuff in our features:
# The second argument to drop 1 specifies the axis, 1 = columns
X = np.array(HPI_Plus.drop(['US_AVE_Future', 'label'], 1))
# print(X)
# preprocessing scales all values from -1 to 1 - better for ML? In this case it doesn't
# seem to do that...
X = preprocessing.scale(X)
# print(X)

y = np.array(HPI_Plus['label'])

# create our training and testing sets:
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# looking at the data at this point isn't very helpful. It's all jumbled and scaled and unlabeled. RAW!!!
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

# Can we 'pickle' the classifier at this point for later? We should also pickle the test data:
pickle_out = open(SOURCES_PATH + 'x_test.pickle', 'wb')
pickle.dump(X_test, pickle_out)
pickle_out.close()

pickle_out = open(SOURCES_PATH + 'y_test.pickle', 'wb')
pickle.dump(y_test, pickle_out)
pickle_out.close()

pickle_out = open(SOURCES_PATH + 'classifier.pickle', 'wb')
pickle.dump(clf, pickle_out)
pickle_out.close()


# Let's see how it does on the remaining test data:
print(clf.score(X_test, y_test))

# average results seem to be ~74% accurate. not bad.