## Problem Statement

Is it possible to classify CNN articles by author?

### Executive Summary

Cable News Network (CNN) is a global 24/7 news organization whose website does not requite a subscription to access. This makes it the perfect candidate for webcrawling. We are intested in classifying the authors of articles by their text. Since often times multiple authors contribute to the same article, we restricted the scope of articles to ones that were written by seven authors who had written at lesat 100 articles in our sample. This worked well because these seven authors rarely collaborated with each other. While this makes for a nice classification problem, there was a lot of cleaning of text and HTML that had to be done.

Restricting to these authors drastically reduced the number of articles in our sample (from 7000+ to a bit more than 1000), the articles in this sample were generally higher quality.

In the end we found that a baseline model of guessing the mode had a 22% accuracy. Fitting a logistic regression model on our data gave a test accuracy of 85%. While more complex classification models could have been used, in the spirit of occam's razor, the simplest model is often the best. More complexity would bring diminishing returns since our model already accounts for 85% of the variance.

It was also of note that authors who specialized into a particular topic tended to be easier to classify than generalizists who covered a wider range of subjects.

| Author | Title | Accuracy | Articles Scraped |
| --- | --- | --- | ---|
|Jen Christensen | Health & Climate Unit| 93% | 312 |
|Zachary Cohen | National Security Reporter| 96% | 263 |
|Eliott C. McLaughlin | Senior Writer| 83% | 248 |
|Jill Martin | Sports News Editor| 87% | 145 |
|Konstantin Toropin | News Editor| 70% | 111 |
|Ivana Kottasova | Digital News Producer| 70% | 105 |
|Paul P. Murphy | Producer / Writer| 66% | 167 |

The imbalance of classes also seems to have had an effect on our model's accuracy. Another way to expand this project would be to scrape more data and refine the parameters for how to scrape.


## File Directory

The code, EDA, and analysis can all be found in Capstone.py.
The spider used for scraping was in the folder raw_spider, but due to concerns about bad actors using such a spider to DDOS CNN, it has been omitted from this public repository. The scraped data was ready into a large .csv file which due to size restraints is also omitted from this public repository.
A copy of the presentation I gave at GA is saved as Capstone.pdf

## Data Dictionaries

There are two separate data dictionaries for this project. The raw one read in by the .csv file and the final one used for modeling

Raw Data Dictionary

'author', 'author3', 'author4', 'profile_url', 'title', 'profile_picks',
       'content1', 'content2', 'content3', 'content4', 'url'

| Feature           | Type       | Description                                        |
|-------------------|------------|----------------------------------------------------|
| author            | str object |     paragraph tags containing author information from certain articles               |
| atuhor3, author 4                  | str object | text containing author information from other articles |
| profile_url              | str object    | url to the author's profile, used to scrape all articles on their profile page    |
| title   | str object | title of the news article, if successfully scraped, nan otherwise |
| profile_picks           | str object | article urls scraped from the profile_url, if applicable |
| content1         | str object | full text of successfully scraped article, nan otherwise |
| content2               | str object | unsuccessful scraping: nan                   |
| content3               | str object | paragraph tags containing article contents, nan otherwise |
| content4               | str object | full text of successfully scraped article, nan otherwise |
| url                    | str object | the url which was attempted to be scraped |

All nan values represent articles that were not successfully scraped using a particular attribute of the spider. E.g. if author is nan, then the article was formatted in such a way that the spider could not retrieve the author by that method (but may have retrieved it using author3 or author 4).


Modeling Data Dictionary

| Feature           | Type       | Description                                        |
| ------------------|------------|----------------------------------------------------|
| individualwords             | int | binary value for Countvectorized text,                    |
| total_word_length          | int | number of words in article |
| average_word_length           | int    | length of the average word in article       |
| target           | str    | author of the article, what we want to classify    |

## Conclusions

While we were able to classify article text by author quite easily and outperform the baseline quite well, our model does not take into account other contributors to the articles we scraped. Our sampling method is also biased both by the fact that news articles which were successfully scraped tended towards certain content types (recent articles and those that had certain layouts) and that we did a convenience sample of authors who had both collaborated on an article and had profiles on CNN.

More data could be used to improve the model's performance as our model struggled to classify the authors with the fewest articles scraped. This also does not bode well for classify more casual cnn writers and contributors.

While using more data could improve the model, a more complex model seems unnecessary at this point. Better sampling methodology would likely be the best place to look to improve this model.

### Sources:

http://cnn.com (and a bunch of other urls)

https://stackoverflow.com/questions/29034928/pandas-convert-a-column-of-list-to-dummies 

https://docs.scrapy.org/en/latest/intro/tutorial.html
