# explore_housing_data.py
"""
Explore Housing Data
Author: William Murrah
Description: from chapter 2 of Hands-On ML.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit

os.chdir('Projects/HousingProject')

housing = pd.read_csv('data/housing/housing.csv')

housing.hist(bins=50, figsize=(20, 15))
plt.show()

housing.describe()

housing['income_cat'] = pd.cut(housing['median_income'],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])
# Create test set
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2,
                               random_state=42)
for train_index, test_index in split.split(housing,
                                           housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

#strat_test_set['income_cat'].value_counts() /len(strat_test_set)

for set_ in (strat_train_set, strat_test_set):
    set_.drop('income_cat', axis=1, inplace=True)

# Impute median for missing total_bedrooms

imputer = SimpleImputer(strategy="median")

housing_num = housing.drop("ocean_proximity", axis=1)

imputer.fit(housing_num)

imputer.statistics_

housing_num.median().values

X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index=housing_num.index)
