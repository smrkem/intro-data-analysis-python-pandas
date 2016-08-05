import pickle
from helpers import SOURCES_PATH

# Grab our X_test and y_test data from previously:
pickle_in = open(SOURCES_PATH + 'x_test.pickle', 'rb')
X_test = pickle.load(pickle_in)
print(X_test)

pickle_in = open(SOURCES_PATH + 'y_test.pickle', 'rb')
y_test = pickle.load(pickle_in)
print(y_test)

# Grab the pickled classifier:
pickle_in = open(SOURCES_PATH + 'classifier.pickle', 'rb')
clf = pickle.load(pickle_in)

# And check how it does! The result is the exact same as from the time we ran it and pickled it. Makes sense!
print('======================')
print(clf.score(X_test, y_test))
