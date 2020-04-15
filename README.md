# SQLAlchemy Challenge - Surfs Up!

## Project development
For completing this assignment the following files have been developed:

1. HonoluluHI_weather.py - main library that contains the all the methods used for querying the database and processing data into dataframes or dictionaries;
2. Climate_Analysis_and_Exploration.ipynb - Jupyter Notebook file used for analysis and visualization of the dataframes resulted from calling methods in HonoluluHI_weather.py;
3. application.py - Flask application used to query database through HonoluluHI_weather.py and return API's in the form of list of dictionaries.

Also, a virtual environment has been created locally (in the project folder), to allow the execution of the files.

## Climate analysis and exploration
After displaying all the precipitation data from the last year recoded in the database, it seems that precipitation in Hawaii overall doesn't have any periodic behavior, reason why it cannot be used as a criteria to choose the vacation date.

<img src=Images/Precipitation_chart.png >|
:-------------------------:|
Chart 1: Last year precipitation data from all stations|

Considering the observed temperature in the most active station (WAIHEE 837, HI US), it seems that the distribution is biased towards the highest value, which means that there are only short periods of low temperature.

<img src=Images/Temp_hist.png >|
:-------------------------:|
Chart 2: Temperature distribution for Waihee 837 weather station|

By making a benchmark of average monthly temperatures between July and December, it seems that there is a difference of about 5 degrees Fahreinheit. The inequality is also proved by performing the two tail T-test, without assumption of equal variability, which yields a P-value much less than the alfa value of 5%, which leads us to reject the null hypothesis of equal averages.

<img src=Images/Ttest.png >|
:-------------------------:|
Chart 3: Differences between June and December temperatures|
### T-test result
Ttest_indResult(statistic=7.570096659210406, pvalue=5.3283128862831936e-05)


Considering the previous analysis, my personal preference would be to go in Hawaii at the beginning of June (Jun 1'st 2018 to Jun 7'th 2018), when there is a warmer weather. Therefore, when considering the exact same period in 2017, I should be expecting roughly a temperature within 74 and 81 F.

<img src=Images/TripTemp_bar.png >|
:-------------------------:|
Chart 4: Last year's temp for the same period

By further calculating the min, max and avg temperature for the same past intervals (Jun 1'st to Jun 7'th), considering all the data from the db, it can be confirmed that also going deeper in the past the temperatures are within the same range.
<img src=Images/WeatherRainfall_area.png >|
:-------------------------:|
Chart 5: Temperature estimation for my trip

