# Predicting Income from Census Data

### Introduction:

The US Census is an decennial survey dating back to 1790. Article 1, Section 2 of the Constitution states that the country must conduct a count of its population once every 10 years (although the census began occurring annually starting in the year 2000). The chief purpose of the census is to count every person living in the United States, in order to determine the number of seats each state will have in the House of Representatives. It's also used to draw congressional and state legislative districts.

The results of the census determine how billions of dollars in federal funding are allocated every year - to hospitals, fire departments, schools, roads, and other resources. Far more than just a simple tally of the population, the census provides a treasure trove of demographic and economic data.

### Objective:

Using classification, can we predict an individual's income bracket by looking at their answers to the questions on the census? (Excluding those regarding income, of course). We will use a classification algorithm to make predictions, and try to determine the most suitable model for this specific question.

### Methodology:

Data was downloaded from IPUMS (Integrated Public Use Microdata Series) for the year 2018. In csv format, the dataset initially had 269 features, but many were technical codes for tracking data across different years. Per the website's "About" section: `"Our signature activity is harmonizing variable codes and documentation to be fully consistent across datasets. This work rests on an extensive technical infrastructure developed over more than two decades, including the first structured metadata system for integrating disparate datasets."`

The sklearn random forest `feature_importances` module was used to visualize the features by importance. The exact order of features varied each time the code was run (maybe because it's based off the results of random forest, which introduces some randomness / variability into the equation?) but followed the same general pattern, with 'UHRSWORK' (usual hours worked per week) consistently coming in first or second place. 'EDUCD' was also removed, because it is the same as 'EDUC' but the 'D' stands for detailed, which just means there were more 'outlier' codes added as possible values for the column, but mostly identical to the non-detailed row. Next!

### Feature Engineering:

All 58 features chosen initially (out of 269 available - many of which were technical variables regarding data consistency from one year to the next):

![Features](https://i.imgur.com/GTFiw9L.png)

Selected important features:

![Features](https://i.imgur.com/YD5TK4I.png)

We can see from the feature importance graphs above that exact ranking of feature importance changes as we remove features. While there is some discrepancy, the relative feature importances are **generally** similar to before, and R2 scores improve considerably.

*Education level, usual number of hours worked per week, occupation, value of home, bachelor's degree major, age, sex, and travel time to work.*

The dataset was undersampled using "Near Miss" undersampling.

![Before](https://i.imgur.com/psbG7sX.png)

---
![After](https://i.imgur.com/iMPgJ1M.png)


However, R2 scores plummeted with Near Miss balanced data input to the models. The minority class is about 1/2 the size of the majority class, so the imbalance isn't as extreme as it could be. Another attempt at correcting class imbalance was passing the parameter `class_weight='balanced'` to each model, with varying results. Balancing the classes in this way greatly improved the r2 score of the logistic regression model*, but passing the parameter in the same way to Random Forest actually *decreased* the r2 score slightly.

\*Note - `class_weight='balanced'` was inconsistent - sometimes it improved the r2 for Logistic Regression, other times it decimated it... not sure why this was happening.

---

I also had mixed results with standardization using sklearn's `StandardScaler()`. In preliminary testing, it made R2 scores worse. But in my final model tests, it improved the Linear Regression score from 66% to 82% (wow!) I was unable to use it on KNN in time, though. The scaled features took longer on every model they were used in, but with KNN the time was too much.

### Results: <br>

The Random Forest model got the best results - R2 values of 97.55% train, 81.40% test. Precision = 72.72% and recall = 67.17%. The ROC curve looks smooth instead of "stepped" - possibly due to the large amount of observations in the data.

![ROC](https://i.imgur.com/t4Uo337.png)

Extra Trees Classifier got very similar results because it's based on the same decision tree algorithm as random forest. R2 values of 97.55% train, 80.64% test. Precision = 71.25% and recall = 66.41%.

![ROC](https://i.imgur.com/Pzsaab3.png)

Logistic Regression gets the title of Most Improved! Before scaling: After scaling: R2 values of 97.55% train, 80.64% test. Precision = 71.25% and recall = 66.41%.

![ROC](https://i.imgur.com/5iUJW1m.png)
The curve has the "steps" because this plot was generated from the sample dataset with less observations (50,000 vs 1,800,000. The plot for the full set was not ready by the deadline)

K Nearest Neighbors came in last place with R2 scores of 96.50% train, 74.61% test. Precision = 84.93% and recall = 74.95%. The ROC curve has a pointy shape - something to do with how the algorithm works?

![ROC](https://i.imgur.com/xrPOWLL.png)

### Conclusion

In conclusion, classification modelling with Random Forest Classification is a decent predictor of income with the Census data. Next steps would be to figure out why scaling and class weighting were inconsistent and sometimes worsened results.

## Citations
#### Census info:
https://2020census.gov/en/what-is-2020-census.html

#### Dataset:
Steven Ruggles, Sarah Flood, Ronald Goeken, Josiah Grover, Erin Meyer, Jose Pacas and Matthew Sobek. IPUMS USA: Version 10.0 [dataset]. Minneapolis, MN: IPUMS, 2020. https://doi.org/10.18128/D010.V10.0
