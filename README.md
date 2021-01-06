# Exploratory Analysis of Movies Released from 1915 to 2019

**Author**: Chi Bui

## Overview

The objective of this project is to use *exploratory data analysis* and *visualization* to identify current trends and key parameters of a successful movie. Using data science, we can potentially predict customer preference and determine how to construct and optimize content for our product to reach its maximum potential.

## Business Problem

The filmmaking industry is currently dominated by 6 big players 'Warner Bros', 'Walt Disney', '20th Century Fox', 'Paramount', 'Sony', and 'Universal', which accounted for over 75% of the market share altogether. Planning for a debut into a highly competitive market for a new company would therefore require thorough analysis of the current landscape of the film industry.

The objective of this project is to use *exploratory data analysis* and *visualization* to investigate the relations between certain attributes like **genres**, **directors**, **production company**, **month of release** on a movie’s commercial success, as well as the correlation between **ratings** and **box office gross**. Using data collected from two main sources, [**Rotten Tomatoes**](https://www.rottentomatoes.com/) and [**thenumber.org**](https://www.the-numbers.com/market/), to study market trends from 1915 to 2019 with a special focus on the 2000-2019 period would certainly provide insights on how to optimize a debut into the movie industry for a new company in 2021.

## Data

We are provided with 11 movie datasets from various sources:
- [Box Office Mojo](https://www.boxofficemojo.com/) (1)
- [IMDb](https://www.imdb.com/) (6)
- [Rotten Tomatoes](https://www.rottentomatoes.com/) (2)
- [The Movie Database](https://www.themoviedb.org/) (1)
- [The Numbers](https://www.the-numbers.com/market/) (1)

The final dataframe used for the majority of analyses this project (`tn_rotten_tomatoes`) is a merge between datasets from <b>the-numbers.com</b> and <b>Rotten Tomatoes</b>. This dataset contains 4348 entries for movies released in the span of 105 years from 1915-02-08 to 2019-12-31.

The goal of this project is to weigh the impacts of attributes like genres, directors, production company, and month of release on the commercial success of movies as well as the correlation between ratings and worldwide gross. More specifically, commercial success of movies are evaluated based on:
- <b>box office gross</b>
- <b>profit</b> = worldwide gross - production budget 
- <b>rate of return</b> = profit / production budget

## Methods

This project uses **descriptive analysis** including the analysis of trends and market distribution over time, which would provide a useful overview of the landscape of the filmmaking industry. 

Tools used primarily for this analysis:
- NumPy
- Pandas
- Matplotlib
- Seaborn


## Results

1. The number of movies released seems to have hit its peak in 2008, which coincides with Netflix's expansion to offering streaming services in 2007. In the span of 12 years, streaming media seem to have quickly taken over movie theaters.

![graph1](./images/viz1.png)

2. Movies with high commercial success are rarely categorized solely as one single genre. Based on historical data, a combination of <b>Action & Adventure</b> and <b>Science Fiction & Fantasy</b> with some <b>Comedy</b> and <b>Drama</b> elements tend to do relatively well. Although the number of movies released seems to have reduced since 2008, the percentage of movies tagged with <b>Action & Adventure</b> and <b>Science Fiction & Fantasy</b> are still on the rise, which indicates an upward trend for these.

![graph1](./images/viz1.png)

3. In general, <b>May</b> and <b>June</b> are the best months to release a movie for potential profit. However, the best time to release a <b>Horror</b> and <b>Mystery & Suspense</b> movie would be <b>October</b>. Some of the movies with highest rates of return (profit/budget) in the last 20 years are categorized as <b>Horror</b> and <b>Mystery & Suspense</b>. 

## Conclusions

Some recommendations for a new company to break into the movie production industry can be derived from this exploratory analysis as follows:
<br>
- Combining different genres generally boosts profit and return on investment as it helps attract more demographics. Some of the most profitable combinations include <b>Action & Adventure</b>, <b>Science Fiction & Fantasy</b> with some elements of <b>Drama</b>, <b>Comedy</b> and <b>Mystery & Suspense</b>. However, producing movies based too directly on past success could also lead to potentially over-saturating the market. Therefore, it is always important to incorporate elements of novelty into the movies and take into consideration how the audience might have evolved over time.  


- <b>May</b> and <b>June</b> are the best months to release a movie for potential profit. The best time to release a <b>Horror</b> and <b>Mystery & Suspense</b> movie would be <b>October</b>. Some of the movies with highest rate of return (profit/budget) in the last 20 years are categorized as <b>Horror</b> and <b>Mystery & Suspense</b>.  


- Since the introduction of media streaming services in 2007 by Netflix, less movies are being released in movie theaters. This demonstrates the importance of the distributors and distributing methods in the movie industry. Investing in a partnership/licensing deal with Netflix and/or other streaming platforms might help your product reach more audience, and eventually success, which should no longer be measured primarily by box office gross. 

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-movie-exploratory-analysis.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **Chi Bui at [chibui191@gmail.com](mailto:chibui191@gmail.com)**

## Repository Structure

```
├── README.md                                             
├── dsc-phase1-project-movie-exploratory-analysis.ipynb   
├── DS_Project_Presentation.pdf                           
├── data                                                  
└── images                                                
```
