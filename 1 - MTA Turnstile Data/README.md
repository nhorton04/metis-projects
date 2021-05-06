### Metis Project 1: MTA turnstile data 

# Sunny Futures STEM Project

## Context
Sunny Futures STEM is an organization which wishes to create long-term improvement in the lives of underprivileged kids, by exposing them to exciting science events and getting them interested in STEM. They are looking for the best location to host their events in NYC such that they will reach the maximum number of at-risk kids. 

## Goal
Provide recommendations as to the ideal location to place a STEM outreach event, such that it would reach and benefit the maximum number of at-risk students. 

## Methodologies
1. ) Obtain and analyze NYC Department of Education school performance data to identify the highest-risk and worst-performing schools in NYC. 
2. ) Use Google Maps to locate these schools, and their nearest subway stations. 
3. ) Obtain and clean MTA turnstile data by removing outliers, and use it to analyze afternoon weekday ridership at stations nearby schools, to determine at which of these stations there is highest traffic to see the demonstrations. 

## Findings and Conclusions
Analysis indicated that many of the lowest-performing schools are located close together, centralized in lower-income neighborhoods. Among those, the Harlem neighborhood’s at-risk schools were most numerous, closest to subway stations, and the aggregate ridership of those  stations was the highest. Students at these schools will commute from several stations on 3 main subway lines, so we recommend Sunny Futures hosts one event at the highest traffic station on each line to reach the maximum number of at-risk students.

## Deliverables
* [EDA](https://github.com/anterra/mta-data/blob/master/FINAL%20PROJECT.ipynb)
* [Presentation Slide](https://github.com/anterra/mta-data/blob/master/Sunny%20Futures%20STEM%20Project.pdf)

## Project Team
* [Anterra Kennedy](github.com/anterra)
* [Sasha Prokhorova](github.com/sasha-talks-tech)
* [Nick Horton](github.com/nhorton04)

## Technologies Used
* Jupyter Notebook
* Python
* Pandas
* Matplotlib
* Seaborn
