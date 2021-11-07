import time
import pandas as pd
import joblib

from sklearn import svm

pd.options.mode.chained_assignment = None

usage = pd.read_csv('data/Celtra platform usage data.csv')


known_user = usage[usage['USER'] != '(anonymous)']

known_user['DATE'] = pd.to_datetime(known_user['TIMESTAMP']).dt.dayofyear
known_user['HOUR'] = pd.to_datetime(known_user['TIMESTAMP']).dt.hour
known_user['MIN'] = pd.to_datetime(known_user['TIMESTAMP']).dt.hour * 60 + pd.to_datetime(known_user['TIMESTAMP']).dt.minute
known_user = known_user.drop(['TIMESTAMP', 'ACTIVITY'], axis=1)


no_log_in = ['campaignExplorer', 'comments', 'adBuilder', 'previewPage', 'socialLinkDialog', 'demoPage', 'creativeExport']

SPLITING_BY_TIME = True
if SPLITING_BY_TIME:
    test_idx = joblib.load('test_index_timesplit.joblib')
else:
    test_idx = joblib.load('test_index.joblib')

df1 = pd.get_dummies(known_user[['ACCOUNT', 'USER', 'ACTIVITYLOCATION', 'DATE', 'MIN']], columns=['ACTIVITYLOCATION', 'ACCOUNT'])

if SPLITING_BY_TIME:
    usage_train = df1.loc[df1.index < test_idx[0], :]
else:
    usage_train = df1.drop(test_idx)


X = usage_train.loc[:, usage_train.columns != 'USER']
y = usage_train['USER']

# SVM
t = time.time()
model = svm.SVC(gamma=0.1, C=5, kernel='rbf')
model.fit(X, y)
print(time.time() - t)

if SPLITING_BY_TIME:
    joblib.dump(model, 'svm_users_timesplit.joblib')
else:
    joblib.dump(model, 'svm_users.joblib')

