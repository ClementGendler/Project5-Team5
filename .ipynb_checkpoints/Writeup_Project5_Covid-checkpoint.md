## Problem Statement

Identify potential Covid hotspots at the US state level, attempt to utilize government response, mobility, and population data, even weather.

Data sets we usee:  
- Covid19 database on GitHub - https://github.com/GoogleCloudPlatform/covid-19-open-data
- Shape files from US Census - CLEMENT
- Covid-related Google search trends - COVID-cast from Carnegie-Mellon's Delphi Group, https://covidcast.cmu.edu/?sensor=ght-smoothed_search&level=state&date=20201025&signalType=value&encoding=color&mode=export&region=42003


## Executive Summary

This study utilizes Covid19 daily data on confimed cases, population, weather, and Covid-related search activity to create a model which predicts future Covied19 hotspots.  The breadth of the data (over 6 months of daily data for 50 US states) introduces a not-inconsequential amount of complexity.  After testing SARIMA and ARIMA models, we tried two additional models:  Facebook Prophet, and "IID" Model.  Ultimately, we determined that the IID Model yielded the most specific predictions, as it allowed us to fit models specific to each state.  Our docuementation includes heatmaps which visualize for the reader the difference in predictions.  


## Data Description and Data Dictionary

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


We used data from Covid 19 Open Data site, which compiles data for countries world wide, including select provinces such as US states: 
>  author = "Oscar Wahltinez and Matt Lee and Anthony Erlinger and Mayank Daswani and Pranali Yawalkar and Kevin Murphy and Michael Brenner",
>  year = 2020,
>  title = "COVID-19 Open-Data: curating a fine-grained, global-scale data repository for SARS-CoV-2",
>  url = {https://github.com/GoogleCloudPlatform/covid-19-open-data}

To supplement our quantitative data, we utilized count of COVID-related search data from Google to understand if they search could be a  leading indicator of infection.  The list from COVID-cast from Carnegie-Mellon's Delphi Group proved quite useful: https://covidcast.cmu.edu/?sensor=ght-smoothed_search&level=state&date=20201025&signalType=value&encoding=color&mode=export&region=42003



## Exploratory Data Analysis 

Our original objective was to work at the county level, as it is provides a more relevant report to individuals about trends in their immediate community.  Exploration of the data source revealed however, that many of the causal variables existed only at the state level, and not more granular. 



## Model Construction and Evaluation

### Quantitative Modeling for Prediction

For the first pass, we tried SARIMA and ARIMA models, however, the high error levels motivated us to look elsewhere for other modeling options.  This study utilizes the Facebook Prophet model and the "IID Model", based on assumptions of multivariate normal distribution.  


**Facebook Prophet model** is used by the financial industry, and has the benefit of seasonality assumptions embedded in the model. However, there are some downsides to the Prophet model as well:  
- It overweights recent observations such that large increases/decreases in the prior week can yield astronomical error.  
- Moreover, it's vulnerable to data publication dates, as we saw in Alabama. You’ll see that Alabama is a hotspot, and the news confirms it, but when we dug in, we saw that the spike was due to a publication of several months of data at once.
- Taking a step back, the Phophet model is a classic sales models with pronounced seasonal spikes that occur regularly:  weekly, and for major holidays.  The model is not tuned to the more exogenous and epedemiological nature of the Covid-19 virus.  


**The IID model** offers more precision in several ways:
- enables us to use traditional modeling techniques (regression in particular)
- allows us to model each individual state using Gridsearch to find the best fitting model for each state. 



### Modeling for Prediction
With so many variables, we turned to models to help us understand which of the inputs was more determanative of the model.  Using Random Forest, we generated a feature importance plot.



# Conclusions, Recommendations, Further Steps


1. ...
1. ...
1. ...


# Appendix
**Table of Contents**

| Item | Description |
| --- | --- |

