#**************************************************************************
# Title: prepare_housing_data.R
# Author: William Murrah
# Description:
# Created: Wednesday, 11 March 2020
# R version: R version 3.6.3 (2020-02-29)
# Directory: /home/wmmurrah/Learning/Python_AI/Projects/HousingProject
#**************************************************************************
# packages used -----------------------------------------------------------

housing <- read.csv("data/housing/housing.csv", header = TRUE)


split_train_test <- function(data, test_ration, id_column){
  ids <- data[, id_column]
  in_test_set <- apply()
}