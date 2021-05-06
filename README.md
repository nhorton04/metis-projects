# Metis_Projects

These are my projects from the [Metis](https://www.thisismetis.com/) data science bootcamp. Project 1 was a group project, which I completed with the help of [Anterra Kennedy](https://github.com/anterra) and [Sasha Prokhorova](https://github.com/sasha-talks-tech).

---

#### (Group) Project 1: MTA Turnstile Data

- Proposed science fair type events at subway stations to get kids from underprivileged schools interested in STEM
- Analyzed MTA entry/exit turnstile data to determine which subway station had the highest foot traffic on weekday afternoons to coincide with students' commute home from school
- Analyzed NYC school data to find 20 lowest performing schools according to funding and test scores, then cross referenced these schools with nearby subway stations with highest traffic in after-school hours to find 3 optimal locations to recommend

---

#### Project 2: Predicting Movie Sales from Metacritic Reviews

- Used BeautifulSoup and Selenium to scrape movie data from BoxOfficeMojo and Metacritic
- Fed this data into classification algorithms including Random Forest, XGBoost, and Logistic Regression to predict a movie's box office sales based on its Metacritic review score 
- Metacritic review scores were actually negatively correlated with box office sales
- Number of audience ratings was by far the most influental feature on box office sales (positive correlation)

---

#### Project 3: Predicting Income from US Census Data

- Explored whether predicting someone's income was possible given their answers to related census questions (such as number of average hours worked per week, occupation, education, age, etc)
- Used classification algorithms including Logistic Regression, Random Forest, Extra Trees, K Nearest Neighbor, and XGBoost
- These algorithms generally did a good job of predicting whether someone's income was above or below 50k per year, with Random Forest and K Nearest Neighbor having the best results
- Random Forest predicted with 81% test accuracy, 73% precision and 67% recall
- K Nearest Neighbor predicted slightly less accurately at 75% on testing data, but with 12% higher precision and 8% higher recall than Random Forest (85% precision, 75% recall)
---

#### Project 4: Analyzing Reddit Comments with NLP

Used Natural Language Processing tools including Spacy, Gensim, Textblob, and Word2Vec for:
- Sentiment analysis
- Word embeddings
- Topic modeling with Latent Dirichlet Allocation
- Alternative topic modeling with K-Means clustering

---

#### Project 5: Creating Images with Generative Adversarial Networks
- Capstone project to familiarize myself with the inner workings of neural networks, specifically in the context of Computer Vision
- Created web apps for Face Swap, Style Transfer, StyleGAN Encoding
- Used the "Flickr Faces" dataset with 168,000 aligned facial images to train the models
  - For Style Transfer, 10,000 iterations of training was optimal - fewer iterations had low resolution and noise, while more gave diminishing returns
- Used OpenCV to detect faces, PyTorch and Tensorflow to generate optimized images according to style and content loss functions, and Streamlit for a simple, effective user interface

