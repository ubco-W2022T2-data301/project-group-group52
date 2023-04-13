The second question our project addressed was: "Does the length of a film affect its popularity, as assessed by sales and ratings?" In order to answer this question, our main dataset - which provided domestic, international, and worldwide sales for each film - was supplemented by our own dataset containing ratings for each film. This dataset was filled manually and pulled ratings from three sites - IMDb, Letterboxd, and Rate Your Music. Based on the size of the later dataset, 450 films were used for this analysis. The ratings from these sites were standardized to percentages and averaged to calculate the average rating for each film. The worldwide popularity of each film was then calculated based on worldwide sales and average rating, as the following equation describes: (0.5)(world sales/maximum world sales) + (0.5)(average rating).

Linear regressions were performed on the following pairs of variables: domestic sales vs. runtime, international sales vs. runtime, world sales vs. runtime, average rating vs. runtime, and worldwide popularity vs. runtime. To ensure the data fulfilled the assumptions for linear regression, residual plots were graphed for each variable pairing. Where heteroscedasticity was observed, the independent variable was log<sub>2</sub>-transformed. This log-transformation successfully solved all cases of heteroscedasticity. There were some cases where further data manipulation was required, such as removal of major outliers.

<br />

<img src="./images/kyla_worldsalesvsruntime.png" alt="Trulli" style="width:60%">
<figcaption align = "left"><font size = 2><b>Fig 1. Worldwide sales (in U.S. dollars) are plotted against runtime (in minutes). </b>  Worldwide sales were log<sub>2</sub>-transformed due to heteroscedasticity. The equation for the trendline is as follows: log<sub>2</sub>(World Sales) = (0.01106)(Runtime) + 27.5667. P-value was 7.9933e-13. R<sup>2</sup> value was 0.3291. Standard error was 0.0015. Based on a P-value of < 0.0001, the positive correlation is significant at p <= 0.05.</font></figcaption>
</figure>

<br />

<img src="./images/kyla_averageratingvsruntime.png" alt="Trulli" style="width:60%">
<figcaption align = "left"><font size = 2><b>Fig 2.Average rating (in percentage) is plotted against runtime (in minutes). </b> Ratings from three sites - IMDb, Letterboxd, and Rate Your Music - were standardized and averaged. The equation for the trendline is as follows: Average Rating = (0.1031)(Runtime) + 51.5159. P-value was 1.4572e-07. R<sup>2</sup> value was 0.2448. Standard error was 0.0193. Based on a P-value of < 0.0001, the positive correlation is significant at p <= 0.05.</font></figcaption>
</figure>

<br />

<img src="./images/kyla_worldpopularityvsruntime.png" alt="Trulli" style="width:60%">
<figcaption align = "left"><font size = 2><b>Fig 3. Popularity (in percentage) is plotted against runtime (in minutes). </b> Popularity score takes into acount both worldwide sales and average rating [calculated as: 0.5 (worldwide sales/maximum worldwide sales) + 0.5 (average rating)]. The equation for the trendline is as follows: Worldwide Popularity = (0.1456)(Runtime) + 24.575. P-value was 1.3668e-18. R<sup>2</sup> value was 0.3986. Standard error was 0.0158. Based on a P-value of < 0.0001, the positive correlation is significant at p <= 0.05.</font></figcaption>
</figure>

<br />

Linear regression found significant positive correlations between all variable pairings (Fig. 1, Fig. 2, Fig. 3; figures for domestic sales vs. runtime and international sales vs. runtime are not shown here). In all cases, p-values were less than 0.0001, implying signicance at p <= 0.05. Therfore, the analysis found that film runtime does have an effect on popularity, as well as sales and ratings individually. Specifically, longer movies are more popular and perform better in sales and ratings. The regression line for worldwide popularity vs. runtime suggests that a movie's popularity score increases by around 0.15 for every minute its runtime is increased. There are several hypotheses for why this may be the case. One possibility is that longer runtimes are associated with bigger budget or higher production value projects. Another may be that longer runtimes allow for better story and character development.

Two confounding variables considered were genre and distributor. Longer runtime may be correlated with certain genres or distributors, which in turn were more popular. Although box plots were produced for a base level assessment, the scope of this analysis did not allow for in-depth statistical analysis to test for confounding correlations between runtime and genre or distributor. Therefore, this analysis was unable to determine with certainty whether the positive correlations observed between popularity and runtime were the result of confounding variables.