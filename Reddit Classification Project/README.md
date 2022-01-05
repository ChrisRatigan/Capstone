## Problem Statement

Are Dad Jokes technically the truth? Can we build a model to distinguish between the highest scoring posts on r/dadjokes and r/technicallythetruth?

## Executive Summary

Comparing data from r/technicallythetruth (TTT) and r/dadjokes is not a simple task. The two reddits have different posting policies. For posts which had selftext, we used this to analyze them. However, while r/dadjokes generally has purely text posts, TTT is usually a repost of a meme or image from elsewhere on the internet. As such, pytesseract, an OCR library was used to read in data from TTT. We then compiled this text together into a dataframe.

Doing a stratified train/test split, we were able to correctly classify 66% of the data. This is a nearly 1/3 increase from the baseline. We compared this with a logistic regression based solely on the lengths of the titles of the posts and found that a model based solely on text length actually performed slightly worse than the 50% baseline, showing that our model is uncovering meaningful features of the data.

While our model performed well, it struggled far more with classifying TTT posts as dadjokes than dadjokes as TTT. This means, from our model's perspective, it is unclear what the difference between TTT posts and dadjokes are and a more detailed model would need to be used to be able to tell the difference.



## File Directory

The code, EDA, and analysis can all be found in project_3.py.
A copy of the presentation I gave at GA is saved as project_3_presentation.pdf

## Data Dictionaries

There are two separate data dictionaries for this project. One for cleaning and processing the data and the other for modeling the data. In addition to cleaning vs. processing the data can also be divided into the categories

1) Features given by Pushshift vs. Engineered features
2) Features I could find documentation for vs. features at whose meaning I am making educated guesses.

Engineered Features are marked with an asterisk in the tables below. For features in category (2) I have written presumably in the description, to make clear that the exact meaning of these features is conjecture.

The following data dictionary is for features used to clean the data.

Cleaning Data Dictionary

| Feature           | Type       | Description                                        |
|-------------------|------------|----------------------------------------------------|
| full_link            | str object | the full url for the Reddit post                   |
| url                  | str object | Same as full_link, unless there is embedded media, then the url for that media |
| is_self              | boolean    | Binary value: Presumably 1 if url equals full_link, 0 otherwise     |
|removed_by_category   | str object | title of the entity that removed the post from reddit, NA if the post still exists |
|image_text*           | str object | The text content of an image after being processed through pytesseract |
|cleaned_text*         | str object | If is_self is false, the finalized "clean" text. Otherwise selftext |
| media                | str object | Link to media embedded in the post, otherwise NAN                   |


The following features were used directly in a text-based<sup>1</sup> model for our classification problem.

Modeling Data Dictionary

| Feature           | Type       | Description                                        |
| ------------------|------------|----------------------------------------------------|
| title             | str object | Post title                                         |
| selftext          | str object | Post text Note this is empty for image/media posts |
| over_18           | boolean    | Binary value: 1 if tagged NSFW, 0 otherwise        |
| spoiler           | boolean    | Binary value: 1 if tagged spoiler, 0 otherwise     |
| subreddit         | str object | The full title of the subreddit (dadjokes or technically the truth) |
| is_dadjoke*       | boolean    | Binary value: 1 if from dadjokes, 0 otherwise     |
| score             | int        | The number of upvotes the post recieved           |
| view_count        | int        | The total number of view on the post              |
| "word"*           | int        | The counts of words in cleaned_texts after passing through CountVectorizer |

<b>Note:</b> for both score and view_count, these may differ slightly from the exact values on Reddit due to pushshift not updating frequently. Interestingly, the pushshift API gives different dictionaries depending on both the subreddits and posts obtained. In particular the length of the dictionary for dadajokes was different from the one for TTT.

## Conclusions

While we were able to create a model that did significantly better than the baseline, our model made many type 1 errors in classifying technicallythetruth posts as coming from r/dadjokes. As such, while it is possible to use NLP to aid in classifying posts, it is not a silver bullet and it is unclear whether there is a strong distinction between dad jokes and technically the truth posts. 

I would recommend caution in using NLP as a model for flagging posts on TTT as being off-topic. However, further tuning of the model and processing of the text could yield useful insights as to the distinction between these two reddits and when a post from one really belongs in the other.

While using more data could improve the model, a more complex model and some more data cleaning/filtering might yield better results. The use of OCR in this model means the TTT data was much messier than the dadjoke data and this could have skewed some of the model's results.

### Sources:

https://www.reddit.com/r/dadjokes/
https://www.reddit.com/r/technicallythetruth/
https://www.reddit.com/r/pushshift/

https://stackoverflow.com/questions/43767289/cant-seem-to-run-tesseract-from-command-line-despite-adding-path
https://pypi.org/project/pytesseract/