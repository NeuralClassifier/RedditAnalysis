from textblob import TextBlob as tb
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
import itertools
import collections
from nltk.tokenize import WordPunctTokenizer
import csv
import re
import sklearn
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize 
from nltk.util import ngrams
from statistics import mean 
from collections import Counter
import matplotlib.pyplot as plt
from google.colab import drive # This is used to connect with the google drive to save the generated datasets
drive.mount('/gdrive/')




#Declaring a function to clean the texts

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))
def tweet_cleaner(text):
    #soup = BeautifulSoup(text, 'lxml')
    #souped = soup.get_text()
    stripped = re.sub(combined_pat, '', text)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    #lower_case = letters_only.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(letters_only)
    return (" ".join(words))#.strip()
def scrub_words(text):
    """Basic cleaning of texts."""
    
    # remove html markup
    text=re.sub("(<.*?>)","",text)
    
    #remove non-ascii and digits
    text=re.sub("(\\W|\\d)"," ",text)
    
    #remove whitespace
    text=text.strip()
    return text
#removing abbreviations

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        # File path which consists of Abbreviations.
        fileName = "/gdrive/My Drive/DrAdams_Task3_Files/abbr.txt"
        # File Access mode [Read Mode]
        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            # Removing Special Characters.
            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:
                # Check if selected word matches short forms[LHS] in text file.
                if _str.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    # Replacing commas with spaces for final output.
    #print(type(user_string))
    print(' '.join(user_string))
    #print('===================================================')
    #print('')
    return ' '.join(user_string)
    
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text




####r/vim####

vim_df = pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/vim_fd_refined.csv')
vim_df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1,inplace=True)
vim_df


#r/vim: Removing Special Characters

print(vim_df['title'])
print('------Remove____SpecialChars------')
vim_df['t1'] = vim_df['title'].apply(lambda x: ' '.join([tweet_cleaner(word) for word in x.split()]))
print(vim_df['t1'])

#r/vim: Scrubbing

print(vim_df['t1'])
print('------Remove____SpecialChars------')
vim_df['t2'] = vim_df['t1'].apply(lambda x: ' '.join([scrub_words(word) for word in x.split()]))
vim_df.drop(['t1'],axis=1,inplace=True)
print(vim_df['t2'])


#r/vim: Converting to lower-case
print(vim_df['t2'])
print('------Lower-Case------')
vim_df['t3'] = vim_df['t2'].apply(lambda x: ' '.join([word.lower() for word in x.split()]))
vim_df.drop(['t2'],axis=1,inplace=True)
print(vim_df['t3'])


#r/vim: Removing stopwords

stop = stopwords.words("english")
print(vim_df['t3'])
print('------Remove____Stopwords------')
vim_df['t4'] = vim_df['t3'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
vim_df.drop(['t3'],axis=1,inplace=True)
print(vim_df['t4'])


#r/vim: Converting to upper-case
print(vim_df['t4'])
print('------Upper-Case------')
vim_df['t5'] = vim_df['t4'].apply(lambda x: ' '.join([word.upper() for word in x.split()]))
vim_df.drop(['t4'],axis=1,inplace=True)
print(vim_df['t5'])


#r/vim: Using the full form of abbreviations
print(vim_df['t5'])
print('------Removing Abbreviations------')
vim_df['t6']=vim_df['t5'].apply(lambda x: translator(x))
vim_df.drop(['t5'],axis=1,inplace=True)
print(vim_df['t6'])


#r/vim: Counting word Frequency
words = [tweet.lower().split() for tweet in vim_df['t6']]
words[:2]
#r/vim: Listing word frequency
# List of all words across tweets
wordsN = list(itertools.chain(*words))
# Create counter
counter_count = collections.Counter(wordsN)
#r/vim: Keyword Frequeny (Top 5)
list_freq = pd.DataFrame(counter_count.most_common(15),columns=['words', 'count'])
print(list_freq.head())


#Lemmatizing

lmtzr=WordNetLemmatizer()
print(vim_df['t6'])
print('------Lemmatization------')
vim_df['t7'] = vim_df['t6'].apply(lambda x: ' '.join([lmtzr.lemmatize(word,'v') for word in x.split()]))
vim_df.drop(['t6'],axis=1,inplace=True)
print(vim_df['t7'])


#Converting to upper-case
print(vim_df['t7'])
print('------Upper-Case------')
vim_df['t8'] = vim_df['t7'].apply(lambda x: ' '.join([word.upper() for word in x.split()]))
vim_df.drop(['t7'],axis=1,inplace=True)
print(vim_df['t8'])


#Polarity~Subjectivity change in January: Vim
polarity_vim_jan=[]
subjectivity_vim_jan=[]
janVim = vim_df[vim_df['month']=='Jan']
day=[]

#iterating over 31 days
for i in range(1,32):

  janvimTemp=janVim[janVim['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(janvimTemp)):

    pol_day.append(tb(janvimTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(janvimTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_vim_jan.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_vim_jan.append(mean(subj_day)) #Taking the average scores per day
  day.append(i)


#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day,polarity_vim_jan, '-.r')
ax.plot(day,subjectivity_vim_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Scores')
plt.legend(['Polarity','Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/Special Analysis/PolaritySubjectivity_JanVim_daywise.png')
plt.show()


#Polarity~Subjectivity change in February: Vim
polarity_vim_feb=[]
subjectivity_vim_feb=[]
febVim = vim_df[vim_df['month']=='Feb']
day_feb=[]

#iterating over 29 days
for i in range(1,30):

  febvimTemp=febVim[febVim['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(febvimTemp)):

    pol_day.append(tb(febvimTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(febvimTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_vim_feb.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_vim_feb.append(mean(subj_day)) #Taking the average scores per day
  day_feb.append(i)


#Plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day_feb,polarity_vim_feb, '-.r')
ax.plot(day_feb,subjectivity_vim_feb, '-.g')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Scores')
plt.legend(['Polarity','Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/Special Analysis/PolaritySubjectivity_FebVim_daywise.png')
plt.show()


#Polarity~Subjectivity change in March: Vim
polarity_vim_mar=[]
subjectivity_vim_mar=[]
marVim = vim_df[vim_df['month']=='Mar']
day=[]

#iterating over 31 days
for i in range(1,32):

  marvimTemp=marVim[marVim['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(marvimTemp)):

    pol_day.append(tb(marvimTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(marvimTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_vim_mar.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_vim_mar.append(mean(subj_day)) #Taking the average scores per day
  day.append(i)


#Plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day,polarity_vim_mar, '-.r')
ax.plot(day,subjectivity_vim_mar, '-.g')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Scores')
plt.legend(['Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/Special Analysis/Subjectivity_MarVim_daywise.png')
plt.show()


####r/emacs####


emacs_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/emacs_fd_refined.csv')
emacs_df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1,inplace=True)
emacs_df


#r/emacs: Removing Special Characters

print(emacs_df['title'])
print('------Remove____SpecialChars------')
emacs_df['t1'] = emacs_df['title'].apply(lambda x: ' '.join([tweet_cleaner(word) for word in x.split()]))
print(emacs_df['t1'])


#r/emacs: Scrubbing

print(emacs_df['t1'])
print('------Remove____SpecialChars------')
emacs_df['t2'] = emacs_df['t1'].apply(lambda x: ' '.join([scrub_words(word) for word in x.split()]))
emacs_df.drop(['t1'],axis=1,inplace=True)
print(emacs_df['t2'])


#r/emacs: Converting to lower-case

print(emacs_df['t2'])
print('------Lower-Case------')
emacs_df['t3'] = emacs_df['t2'].apply(lambda x: ' '.join([word.lower() for word in x.split()]))
emacs_df.drop(['t2'],axis=1,inplace=True)
print(emacs_df['t3'])


#r/emacs: Removing stopwords

stop = stopwords.words("english")
print(emacs_df['t3'])
print('------Remove____Stopwords------')
emacs_df['t4'] = emacs_df['t3'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
emacs_df.drop(['t3'],axis=1,inplace=True)
print(emacs_df['t4'])


#r/emacs: Converting to upper-case
print(emacs_df['t4'])
print('------Upper-Case------')
emacs_df['t5'] = emacs_df['t4'].apply(lambda x: ' '.join([word.upper() for word in x.split()]))
emacs_df.drop(['t4'],axis=1,inplace=True)
print(emacs_df['t5'])


#r/vim: Using the full form of abbreviations
print(emacs_df['t5'])
print('------Removing Abbreviations------')
emacs_df['t6']=emacs_df['t5'].apply(lambda x: translator(x))
emacs_df.drop(['t5'],axis=1,inplace=True)
print(emacs_df['t6'])


#r/emacs: Counting word Frequency
words_in_tweet = [tweet.lower().split() for tweet in emacs_df['t6']]
# List of all words across tweets
all_words_no_urls = list(itertools.chain(*words_in_tweet))
# Create counter
counts_no_urls = collections.Counter(all_words_no_urls)
#r/emacs: Keyword Frequeny (Top 5)
clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),columns=['words', 'count'])
print(clean_tweets_no_urls.head())


#Lemmatizing

lmtzr=WordNetLemmatizer()
print(emacs_df['t6'])
print('------Lemmatization------')
emacs_df['t7'] = emacs_df['t6'].apply(lambda x: ' '.join([lmtzr.lemmatize(word,'v') for word in x.split()]))
emacs_df.drop(['t6'],axis=1,inplace=True)
print(emacs_df['t7'])


#Converting to upper-case
print(emacs_df['t7'])
print('------Upper-Case------')
emacs_df['t8'] = emacs_df['t7'].apply(lambda x: ' '.join([word.upper() for word in x.split()]))
emacs_df.drop(['t7'],axis=1,inplace=True)
print(emacs_df['t8'])


#Polarity~Subjectivity change in January: Emacs
polarity_emacs_jan=[]
subjectivity_emacs_jan=[]
janEmacs = emacs_df[emacs_df['month']=='Jan']
day=[]

#iterating over 31 days
for i in range(1,32):

  janemacsTemp=janEmacs[janEmacs['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(janemacsTemp)):

    pol_day.append(tb(janemacsTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(janemacsTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_emacs_jan.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_emacs_jan.append(mean(subj_day)) #Taking the average scores per day
  day.append(i)


#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day,polarity_emacs_jan, '-.r')
ax.plot(day,subjectivity_emacs_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Scores')
plt.legend(['Polarity','Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/Special Analysis/PolaritySubjectivity_JanEmacs_daywise.png')
plt.show()


#Polarity~Subjectivity change in February: Emacs
polarity_emacs_feb=[]
subjectivity_emacs_feb=[]
febEmacs = emacs_df[emacs_df['month']=='Feb']
day_feb=[]

#iterating over 29 days
for i in range(1,30):

  febemacsTemp=febEmacs[febEmacs['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(febemacsTemp)):

    pol_day.append(tb(febemacsTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(febemacsTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_emacs_feb.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_emacs_feb.append(mean(subj_day)) #Taking the average scores per day
  day_feb.append(i)


#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day_feb,polarity_emacs_feb, '-.r')
ax.plot(day_feb,subjectivity_emacs_feb, '-.g')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Scores')
plt.legend(['Polarity','Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/Special Analysis/PolaritySubjectivity_FebEmacs_daywise.png')
plt.show()


#Polarity~Subjectivity change in March: Emacs
polarity_emacs_mar=[]
subjectivity_emacs_mar=[]
marEmacs = emacs_df[emacs_df['month']=='Mar']
day=[]

#iterating over 31 days
for i in range(1,32):

  maremacsTemp=marEmacs[marEmacs['day']==i]
  pol_day=[]
  subj_day=[]

  for j in range(len(maremacsTemp)):

    pol_day.append(tb(maremacsTemp.iloc[j,-1]).sentiment.polarity)
    subj_day.append(tb(maremacsTemp.iloc[j,-1]).sentiment.subjectivity)

  polarity_emacs_mar.append(mean(pol_day)) #Taking the average scores per day
  subjectivity_emacs_mar.append(mean(subj_day)) #Taking the average scores per day
  day.append(i)


#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day,polarity_emacs_mar, '-.r')
ax.plot(day,subjectivity_emacs_mar, '-.g')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Scores')
plt.legend(['Polarity','Subjectivity'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/Special Analysis/PolaritySubjectivity_MarEmacs_daywise.png')
plt.show()


#Polarity: r/vim and r/emacs (January)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,polarity_vim_jan, '-b')
ax.plot(day,polarity_emacs_jan, '-r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Polarity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/PolarityF_Jan_emacsVim.png')
plt.show()


#Polarity: r/vim and r/emacs (February)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,polarity_vim_feb, '-b')
ax.plot(day_feb,polarity_emacs_feb, '-r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Polarity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/PolarityF_Feb_emacsVim.png')
plt.show()


#Polarity: r/vim and r/emacs (March)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,polarity_vim_mar, '-b')
ax.plot(day,polarity_emacs_mar, '-r')
ax.set_xlabel('Day in March')
ax.set_ylabel('Polarity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/PolarityF_Mar_emacsVim.png')
plt.show()




#Subjectivity: r/vim and r/emacs (January)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,subjectivity_vim_jan, '-b')
ax.plot(day,subjectivity_emacs_jan, '-r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Subjectivity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/SubjectivityF_Jan_emacsVim.png')
plt.show()


#Subjectivity: r/vim and r/emacs (February)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,subjectivity_vim_feb, '-b')
ax.plot(day_feb,subjectivity_emacs_feb, '-r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Subjectivity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/SubjectivityF_Jan_emacsVim.png')
plt.show()


#Subjectivity: r/vim and r/emacs (March)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,subjectivity_vim_mar, '-b')
ax.plot(day,subjectivity_emacs_mar, '-r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Subjectivity Scores')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/Special Analysis/SubjectivityF_Jan_emacsVim.png')
plt.show()
