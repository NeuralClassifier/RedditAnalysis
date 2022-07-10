# RedditAnalysis
In this assignment I have scrapped the reddit posts from two popular reddit repositories: [r/vim](https://www.reddit.com/r/vim/) and [r/emacs](https://www.reddit.com/r/emacs/) by considering that the number of posts each day by any subreddit is less than 1000, and did a comprehensive graphical analysis. Another special graphical analysis has been conducted by measuring the subjectivity scores and polarity scores of the extracted texts.

# Installation
For Installing [PRAW](https://praw.readthedocs.io/en/latest/): The Python Reddit API Wrapper
```javascript
pip install praw
```
For Installing [PSAW](https://pypi.org/project/psaw/): Pushshift API Wrapper
```javascript 
pip install psaw
```
For Installing [TextBlob](https://textblob.readthedocs.io/en/dev/)
```javascript
pip install -U textblob
```

# *Note
Please use this code if the plot is getting saved with no axis
```javascript
matplotlib.pyplot.savefig(/.../,bbox_inches = "tight")
```

# Contributors

* Kushankur Ghosh, [kushanku@ualberta.ca](mailto:kushanku@ualberta.ca)
