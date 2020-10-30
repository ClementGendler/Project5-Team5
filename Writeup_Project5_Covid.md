# Problem Statement

Identify potential Covid hotspots at the US state level, attempt to utilize government response, mobility, and population data, even weather.

Data sets we usee:  
- Covid19 database on GitHub - https://github.com/GoogleCloudPlatform/covid-19-open-data
- Shape files from US Census - CLEMENT
- Covid-related Google search trends - COIVD-cast from Carnegie-Mellon's Delphi Group, https://covidcast.cmu.edu/?sensor=ght-smoothed_search&level=state&date=20201025&signalType=value&encoding=color&mode=export&region=42003


# Executive Summary

This study utilizes Covid19 daily data on confimed cases, population, weather, and Covid-related search activity to create a model which predicts future Covied19 hotspots.  The breadth of the data (over 6 months of daily data for 50 US states) introduces a not-inconsequential amount of complexity.  After testing SARIMA and ARIMA models, we tried two additional models:  Facebook Prophet, and "IID" Model.  Ultimately, we determined that the IID Model yielded the most specific predictions, as it allowed us to fit models specific to each state.  Our docuementation includes heatmaps which visualize for the reader the difference in predictions.  


# Data Description and Data Dictionary

For data collection, we used selected several fields available from the Covid 19 Open Data site.  Of the 108 fields offered, we honed in on the fields listed in the data dictionary below.   



| Item | Description |
| --- | --- |
| date | date pertaining to the observation |
| subregion1_name | US state name |
| new_confirmed | number of new confirmed infections daily |
| new_deceased | number of deaths due to Covid19 |
| total_confirmed | total cumulative confirmed infections for each state |
| total_deceased | total cumulative deaths due to Covid19 per state | 
| population | total state population, includes detail on age brackets from 0 to 80 years and older | 
| population_male | total state population of males only |   
| population_female | total state population of females only |
| mobility_workplaces | categorical variable for the amount of time spent in workplaces* |
| average_temperature | temperature (F), including detail on max and min temperature | 
| rainfall | amount of rain | 
| dew_point | dew point (F) |
| relative_humidity | humidity level |
  
  
  
...

| Item | Description |
| --- | --- |
| title | The headline of each post |


We used data from Covid 19 Open Data site, which compiles data for countries world wide, including select provinces such as US states. 
Details on this data source are below:
@article{Wahltinez2020,
  author = "Oscar Wahltinez and Matt Lee and Anthony Erlinger and Mayank Daswani and Pranali Yawalkar and Kevin Murphy and Michael Brenner",
  year = 2020,
  title = "COVID-19 Open-Data: curating a fine-grained, global-scale data repository for SARS-CoV-2",
  url = {https://github.com/GoogleCloudPlatform/covid-19-open-data},
}

To supplement our quantitative data, we utilized posts from Facebook to understand if they serve as leading indicator of infection.  
[Clement description of FB data]
- how were the FB posts collected (API?)
- parameters and other pre-processing steps
- how incorporated into modeling visualization



# Exploratory Data Analysis and Key Findings

Exploratory Data Analysis (EDA) revealed ...  


# Model Construction and Evaluation

### Quantitative Modeling for EDA

...


### Quantitative Modeling for Prediction

For the first pass, we created a rough model assess how well the data would predict, as well as which type of classifier would work best.  

**Model Score Results**


| Model type | Train   | Test    | Delta  (Test - Train) |  Other parameters
|-------------------------------|---------|---------|-----------------------|


...

### Natural Language Processing of Facebook posts

Clement input? ...


# Conclusions, Recommendations, Further Steps


1. ...
1. ...
1. ...


# Appendix
**Table of Contents**

| Item | Description |
| --- | --- |

