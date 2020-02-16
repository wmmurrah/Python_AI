# explore_housing_data.py
"""
Explore Housing Data
Author: William Murrah
Description: from chapter 2 of Hands-On ML.
"""
import sys
import matplotlib.pyplot as plt
import pandas as pd

housing = pd.read_csv('data/housing/housing.csv')

housing.hist(bins=50, figsize=(20,15))
plt.show()
