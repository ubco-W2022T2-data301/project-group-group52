## Question 3/4 + Results

### Question 3

In [Cody's analysis](https://github.com/ubco-W2022T2-data301/project-group-group52/blob/main/analysis/analysis3.ipynb), we examined two research questions. The first question was "Does a movie's popularity correlate with it's quality?" In this analysis, Cody used a weighted rating score taken as an average of a movie's IMDb, Letterboxd, and Rateyourmusic adjusted rating. He then separated movies into 'bad', 'average', 'good', and 'great' categories based on that weighted score. The baseline score which was used to define 'average' was a 6/10 movie. Two key visualizations which were utilized to answer this question were a boxplot of weighted rating and a histogram of movie quality.

![Boxplot of Top 449 Movies by Weighted Rating](project-group-group52/images/cody_final_analysis/boxplot.JPG)

In this visualization, we can see that the midpoint is significantly higher than 6/10, but still within what is defined as an 'average' movie. We can see that 25% of the observations fall below a rating of 5.63 with the lowest rating being 3.50. 25% of the observations are above a rating of 7.14 with the highest rating being 8.99. By our definitions, the majority of these popular movies are 'average' or 'good'. Furthermore, when we narrow the range to include only the top 150 highest rated movies, the distribution seems to shift to the right.

![Boxplot of Top 150 Movies by Weighted Rating](project-group-group52/images/cody_final_analysis/boxplot_150.JPG)

This seems to imply that popular movies tend to be of higher quality than average movies. To further demonstrate this, we can see this histogram of the frequency of movie quality.

![Frequency Distribution of Movie Quality](project-group-group52/images/cody_final_analysis/quality dist.JPG)

From this graph, we can see that 'good' and 'average' movies are the most frequent. 'Bad' movies are significantly rarer, with 'great' movies being an outlier. From these visualizations as well as the deeper analysis, we concluded that popular movies tend to be rated higher than the average movie, but the correlation between popularity and 'great' movies is not that strong. In other words, we can expect a popular movie to be above average or even good, but not necessarily amazing.

### Question 4

The second research question was "Does a movie's release year correlate with its quality?" This question was simpler to answer. Initially, it seemed that there was a correlation between release year and quality, however these older years tended to have significantly fewer observations. A filter was applied to only account for years with a large amount of observations (2000-2021), and this scatterplot was obtained. 

![Scatterplot of Movie Weighted Rating by Release Year (2000-2021)](project-group-group52/images/cody_final_analysis/scatterplot.JPG)

As we can see, when eliminating the years which had few observations, there appeared to be much less of a correlation between release year and quality. We concluded that there is no significant correlation between release year and quality. 

## Summary/Conclusion

In our analysis, we have learned that by investigating runtime, sales, ratings, and genres, popular movies tend to have these characteristics. Movies have been growing in popularity steadily. Sales tend to increase over the years and amount of movies made within a genre also increases. We found that the 2 most popular movie genres are 'Adventure' and 'Action'. We found that popular films tend to have longer runtimes. We found that there is a positive correlation between a movie's quality and its popularity. Finally, we found that there isn't a significant correlation between a movie's release year and it's quality. In conclusion, we can see that popular movies tend to be more recent, longer, action or adventure-oriented, and higher quality. 