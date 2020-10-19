import praw #importing Python Reddit API Wrapper
from psaw import PushshiftAPI #from Pushshift.io API Wrapper importing the API to extract the posts to search public reddit comments and submissions
import datetime as dt # This is used to extract the time stamp
import pandas as pd # this is used to create the dataframe
from google.colab import drive # This is used to connect with the google drive to save the generated datasets
drive.mount('/gdrive/') #Mounting Google Drive


#A Reddit instance is created and provided it with parameters like client_id , client_secret, password and a user_agent. These values are otained while creating an application on reddit
reddit = praw.Reddit(client_id='TVDysQd1QD54cA',client_secret='wuvzimFI4uFtt4cIljzbSq8lmJw',username='kush_1999',password='Mithai-1234',user_agent='DrAdams_Task3_vim')
api = PushshiftAPI(reddit)


subreddit = 'vim' # The name of the subreddit used




#r/vim: Extraction

#declaring the data i will be extracting
title=[]
url=[]
upvote_count=[]
downvote_count=[]
comments_count=[] 
upvote_ratio=[]
overall_vote=[]
subreddit_name=[]
month=[]
day=[]
id=[]
total_awards_received=[]



#starting from January (Month: j = 1)

#A loop iteration technique has been implied because I found that the number of post extraction in a single run is limited by the APIs (MAX 1000 posts in one go).
#I have assumed that there can not be more than 1000 posts in a single day by any subreddit. So the loop iteration technique iterates daywise.
j=1

#The loop will iterate up to March: J=3:
while j <= 3:

  #JANUARY 2020
  if j == 1:
    print('Working on January')
    
    #THIS LOOP WILL ITERATE THE DAYS AND WILL COLLECT DATA FROM 1ST JAN 2020 TO 30TH JAN 2020
    for i in range(2,32):
      st_i =i-1 #START DATE: st_i stands for start day index
      start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/01
      end_epoch=int(dt.datetime(2020, j, i).timestamp())

      #NOW EXTRACTING THE SUBMISSION CLUSTERS
      submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
      
      #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA
      for k in submission_cluster:

        #APPENDING DATA INTO THE LISTS

        id.append(k.id) #EXTRACTING THE IDENTIFIER
        title.append(k.title) #TAKING THE TITLE
        url.append(k.url) #URL FOR REFERENCE
        upvote_count.append(k.ups) #UPVOTE COUNT
        downvote_count.append(k.downs) #DOWNVOTE COUNT
        overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
        upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
        comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
        subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
        total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
        month.append('Jan') # MONTH
        day.append(st_i) #DAY

    #EXTRACTING THE DATA OF 31ST JAN 2020 (LAST DAY)    
    print('Last Day Jan...')
    st_i =st_i+1 # 31ST JAN: st_i stands for start day index 
    i=1 # 1ST FEB
    start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/01/31
    end_epoch=int(dt.datetime(2020, j+1, i).timestamp()) # j= 2, i=1 (1ST FEB): GETTING THE TIME-STAMP OF THE END DATE 2020/02/01

    #NOW EXTRACTING THE SUBMISSION CLUSTERS AGAIN
    submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
    
    #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA AGAIN
    for k in submission_cluster:

      #APPENDING DATA INTO THE LISTS FOR THE LAST DAY IN JAN

      id.append(k.id) #EXTRACTING THE IDENTIFIER
      title.append(k.title) #TAKING THE TITLE
      url.append(k.url) #URL FOR REFERENCE
      upvote_count.append(k.ups) #UPVOTE COUNT
      downvote_count.append(k.downs) #DOWNVOTE COUNT
      overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
      upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
      comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
      subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
      total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
      month.append('Jan') #MONTH
      day.append(st_i) #LAST DAY

    j+=1 #INCREMENTING THE MONTH

  #FEBRUARY 2020
  if j==2:
    print('Working on February')

    #THIS LOOP WILL ITERATE THE DAYS AND WILL COLLECT DATA FROM 1ST FEB 2020 TO 28TH FEB 2020  
    for i in range(2,30):


      st_i =i-1 #START DATE: st_i stands for start day index
      start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/02
      end_epoch=int(dt.datetime(2020, j, i).timestamp())
      
      #NOW EXTRACTING THE SUBMISSION CLUSTERS
      submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
      
      #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA
      for k in submission_cluster:

        #APPENDING DATA INTO THE LISTS

        id.append(k.id) #EXTRACTING THE IDENTIFIER
        title.append(k.title) #TAKING THE TITLE
        url.append(k.url) #URL FOR REFERENCE
        upvote_count.append(k.ups) #UPVOTE COUNT
        downvote_count.append(k.downs) #DOWNVOTE COUNT
        overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
        upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
        comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
        subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
        total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
        month.append('Feb') #MONTH
        day.append(st_i) #DAY

    #EXTRACTING THE DATA OF 31ST JAN 2020 (LAST DAY)   
    print('Last Day Feb...')
    st_i =st_i+1 # 29Th FEB: st_i stands for start day index 
    i=1 # 1ST MAR


    start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/02/29
    end_epoch=int(dt.datetime(2020, j+1, i).timestamp()) #GETTING THE TIME-STAMP OF THE END DATE 2020/03/01
    
    #NOW EXTRACTING THE SUBMISSION CLUSTERS AGAIN
    submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
    
    #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA AGAIN
    for k in submission_cluster:

      #APPENDING DATA INTO THE LISTS FOR THE LAST DAY IN FEB

      id.append(k.id) #EXTRACTING THE IDENTIFIER
      title.append(k.title) #TAKING THE TITLE
      url.append(k.url) #URL FOR REFERENCE
      upvote_count.append(k.ups) #UPVOTE COUNT
      downvote_count.append(k.downs) #DOWNVOTE COUNT
      overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
      upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
      comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
      subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
      total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
      month.append('Feb') #MONTH
      day.append(st_i) #LAST DAY

    
    j+=1 #INCREMENTING THE MONTH

  #MARCH 2020
  if j==3:
    print('Working on March')

    #THIS LOOP WILL ITERATE THE DAYS AND WILL COLLECT DATA FROM 1ST MAR 2020 TO 30TH MAR 2020  
    for i in range(6,32):


      st_i =i-1 #START DATE: st_i stands for start day index
      start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/03
      end_epoch=int(dt.datetime(2020, j, i).timestamp())

      #NOW EXTRACTING THE SUBMISSION CLUSTERS
      submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
      
      #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA
      for k in submission_cluster:
      
        #APPENDING DATA INTO THE LISTS

        id.append(k.id) #EXTRACTING THE IDENTIFIER
        title.append(k.title) #TAKING THE TITLE
        url.append(k.url) #URL FOR REFERENCE
        upvote_count.append(k.ups) #UPVOTE COUNT
        downvote_count.append(k.downs) #DOWNVOTE COUNT
        overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
        upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
        comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
        subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
        total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
        month.append('Mar') #MONTH
        day.append(st_i) #DAY

    #EXTRACTING THE DATA OF 31ST MAR 2020 (LAST DAY)  
    print('Last Day Mar...')


    st_i =st_i+1 # 31ST MAR: st_i stands for start day index 
    i=1 # 1ST APR


    start_epoch=int(dt.datetime(2020, 1, st_i).timestamp()) #GETTING THE TIME-STAMP OF THE START DATE 2020/03/31
    end_epoch=int(dt.datetime(2020, j+1, i).timestamp()) #GETTING THE TIME-STAMP OF THE END DATE 2020/04/01
    
    #NOW EXTRACTING THE SUBMISSION CLUSTERS AGAIN
    submission_cluster=list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit=subreddit,filter=['url','author', 'title', 'subreddit'],limit=None))
    
    #ITERATING OVER THE EXTRACTED CLUSTERS TO EXTRACT INDIVIDUAL DATA AGAIN
    for k in submission_cluster:

      #APPENDING DATA INTO THE LISTS FOR THE LAST DAY IN MAR

      id.append(k.id) #EXTRACTING THE IDENTIFIER
      title.append(k.title) #TAKING THE TITLE
      url.append(k.url) #URL FOR REFERENCE
      upvote_count.append(k.ups) #UPVOTE COUNT
      downvote_count.append(k.downs) #DOWNVOTE COUNT
      overall_vote.append(k.ups-k.downs) #DIFFERENCE BETWEEN UPVOTE AND DOWNVOTE COUNTS
      upvote_ratio.append(k.upvote_ratio) #UPVOTE RATIO
      comments_count.append(len(k.comments)) #NUMBER OF COMMENTS
      subreddit_name.append(k.subreddit) #NAME OF THE SUBREDDIT: vim
      total_awards_received.append(k.total_awards_received) #NUMBER OF AWARDS RECEIVED
      month.append('Mar') #MONTH
      day.append(st_i) #LAST DAY


    j+=1 #INCREMENTING THE MONTH
    
    

    
#CONVERTING THE LISTS INTO INDIVIDUAL SINGLE-COLUMNED DATAFRAMES

id_df=pd.DataFrame(id,columns=['identifier'])
title_df=pd.DataFrame(title,columns=['title'])
url_df=pd.DataFrame(url,columns=['url'])
upvote_count_df=pd.DataFrame(upvote_count,columns=['upvote count'])
downvote_count_df=pd.DataFrame(downvote_count,columns=['downvote count'])
comments_count_df=pd.DataFrame(comments_count,columns=['comments count'])
upvote_ratio_df=pd.DataFrame(upvote_ratio,columns=['upvote ratio'])
overall_vote_df=pd.DataFrame(overall_vote,columns=['overall vote'])
subreddit_name_df=pd.DataFrame(subreddit_name,columns=['subreddit'])
total_awards_received_df=pd.DataFrame(total_awards_received,columns=['total awards'])
month_df=pd.DataFrame(month,columns=['month'])
day_df=pd.DataFrame(day,columns=['day'])


#CONCATING THE INDIVIDUAL DATAFRAMES BY SETTING THE AXIS AS 1 TO BUILD ONE SINGLE DATAFRAME WITH MULTIPLE FEATURES 

vim_df=pd.concat([id_df,title_df,url_df,upvote_count_df,downvote_count_df,comments_count_df,upvote_ratio_df,overall_vote_df,subreddit_name_df,total_awards_received_df,month_df,day_df],axis=1)
vim_df.to_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/vim_finalDF.csv')
