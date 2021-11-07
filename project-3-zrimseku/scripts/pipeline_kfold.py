import pandas as pd
import numpy as np
import joblib
from sklearn.decomposition import PCA

from sklearn.model_selection import KFold, cross_validate, GridSearchCV, RandomizedSearchCV

from sklearn import svm
from sklearn.pipeline import make_pipeline

pd.options.mode.chained_assignment = None

usage = pd.read_csv('data/Celtra platform usage data.csv')
sessions = pd.read_csv('data/Celtra sessions data.csv')

known_user = usage[usage['USER'] != '(anonymous)']

known_user['DATE'] = pd.to_datetime(known_user['TIMESTAMP']).dt.dayofyear
known_user['HOUR'] = pd.to_datetime(known_user['TIMESTAMP']).dt.hour
known_user['MIN'] = pd.to_datetime(known_user['TIMESTAMP']).dt.hour * 60 + pd.to_datetime(known_user['TIMESTAMP']).dt.minute
known_user = known_user.drop(['TIMESTAMP', 'ACTIVITY'], axis=1)


no_log_in = ['campaignExplorer', 'comments', 'adBuilder', 'previewPage', 'socialLinkDialog', 'demoPage', 'creativeExport']
# no_log_in = [actloc_dict[act] for act in no_log_in_text]
np.random.seed(0)
test_idx = []
for user in known_user['USER'].unique():
    test_idx.append(known_user[(known_user['USER'] == user) & (known_user['ACTIVITYLOCATION'].isin(no_log_in))]
                    .sample(frac=0.25).index.values)
test_idx = np.concatenate(test_idx)

df1 = pd.get_dummies(known_user[['ACCOUNT', 'USER', 'ACTIVITYLOCATION', 'DATE', 'MIN']], columns=['ACCOUNT', 'ACTIVITYLOCATION'])

np.random.seed(0)
sample_users = np.random.choice(df1['USER'].unique(), 20, replace=False)

usage_test = df1.loc[test_idx]
usage_test = usage_test[usage_test['USER'].isin(sample_users)]
usage_train = df1.drop(test_idx)
usage_train = usage_train[usage_train['USER'].isin(sample_users)]

X = usage_train.loc[:, usage_train.columns != 'USER']
y = usage_train['USER']
X_test = usage_test.loc[:, usage_test.columns != 'USER']
y_test = usage_test['USER']


kf = KFold(n_splits=10)

# SVM
param_distributions = {'gamma': [0.001, 0.1, 1], 'kernel': ['rbf', 'linear'], 'C': [0.1, 1, 5]}

clf = make_pipeline(PCA(n_components=5), RandomizedSearchCV(svm.SVC(), param_distributions, n_iter=6, cv=kf,
                                                            random_state=0, n_jobs=4))

tmp = clf.fit(X, y)


joblib.dump(tmp, 'pipeline_results.joblib')
