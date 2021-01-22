#************************************************************************
# Title: explore_housing_data.R
# Author: William Murrah
# Description: Explore housing data in Chapter 2 of HOML
# Created: Tuesday, 22 December 2020
# R version: R version 4.0.3 (2020-10-10)
# Project(working) directory: /Users/wmm0017/Projects/Learning/Python_AI/Projects/HousingProject
#************************************************************************
library(data.table)
library(psych)


# Load and prepare data ---------------------------------------------------
hdat <- fread("data/housing/housing.csv")
names(hdat)

# Explore data ------------------------------------------------------------
hist(hdat$median_house_value, breaks = 'fd')

hist(log(hdat$median_house_value), breaks = 'fd')

pairs.panels(hdat)

with(hdat, plot(longitude, latitude))
