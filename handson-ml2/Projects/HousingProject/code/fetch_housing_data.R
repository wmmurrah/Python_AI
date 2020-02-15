# fetch_housing_data.R
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = "data/housing/"
TARFILENAME = "housing.tgz"
HOUSING_URL = paste0(DOWNLOAD_ROOT,"datasets/housing/",TARFILENAME)

fetch_housing_data <- function(housing_url = HOUSING_URL, 
                               dest_folder = HOUSING_PATH,
                               tarfilename =TARFILENAME) {
  # Download and unpack 1990 California Housing Prices data
  dir.create(HOUSING_PATH, 
                                                                 recursive = TRUE)
    download.file(url = housing_url, 
                  destfile = paste0(HOUSING_PATH, 
                                    tarfilename))
    untar(tarfile = paste0(dest_folder,tarfilename), exdir = dest_folder)
}


