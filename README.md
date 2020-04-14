# SQLAlchemy Challenge - Surfs Up!

## Project development
For completing this assignment the following files have been developed:

1. HonoluluHI_weather.py - main library that contains the all the methods used for querying the database and processing data into dataframes or dictionaries;
2. Climate_Analysis_and_Exploration.ipynb - Jupyter Notebook file used for analysis and visualization of the dataframes resulted from calling methods in HonoluluHI_weather.py;
3. application.py - Flask application used to query database through HonoluluHI_weather.py and return API's in the form of list of dictionaries.

Also, a virtual environment has been created locally (in the project folder), to allow the execution of the files.

## Climate analysis and exploration
After displaying all the precipitation data from the last year recoded in the database, it seems that precipitation in Hawaii overall doesn't have any periodic behavior, reason why it cannot be used as a criteria to choose the vacation date.

Considering the observed temperature in the most active station (WAIHEE 837, HI US), it seems that the distribution is biased towards the highest value, which means that there are only short periods of low temperature.

By making a benchmark of average monthly temperatures between July and December, it seems that there is a difference of about 5 degrees Fahreinheit. The inequality is also proved by performing the two tail T-test, without assumption of equal variables, which yields a P-value much less than the alfa = 5%.
