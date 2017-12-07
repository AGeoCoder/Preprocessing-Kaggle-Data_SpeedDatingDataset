# SpeedDatingExperimentPreprocessing
Preprocessing for Speed Dating Experiment Data from Kaggle

A short preprocessing script to divide a dataset (CSV format) into a training set CSV and a test set CSV for use with machine learning algorithms. The test set will be comprised with 50/50 matches and not matches (i.e. regarding 0s or 1s in the "match" column). Originally, there are 6998 "no match" rows and 1380 "match" rows. From this, 628 randomly selected "matches" and 628 "no matches" are taken out to make the test set. The remaning rows comprise the training set.

The original dataset with speed dating experiment information was downloaded from Kaggle. The experiment data and their metadata are also included here for convenience.

(https://www.kaggle.com/annavictoria/speed-dating-experiment)
(The original CSV has 8378 rows and about 195 columns.)
