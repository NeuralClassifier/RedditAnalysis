from google.colab import drive # This is used to connect with the google drive to save the generated datasets
import pandas as pd #used for importing, creating, saving, and manipulating datasets
import seaborn as sns #used for ploting graphs
import matplotlib.pyplot as plt #used for plotting graphs
from statistics import mean #for calculating average
drive.mount('/gdrive/') #mounting google-drive


#importing dataset with the posts from r/emacs
emacs_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/emacs_finalDF.csv')
emacs_df

#Finding the correlation with an heatmap
cor_emacs = emacs_df.corr()
plot_t=sns.heatmap(cor_emacs)
figure = plot_t.get_figure()
figure.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/Heatmap_emacs.png')

#declaring the months
months = ['Jan', 'Feb', 'Mar']

#r/emacs: Monthwise upvote Bar plot

fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
emacs_UpvoteMonthWise=[]

#iterating over months
for i in months:
  month_temporary = emacs_df[emacs_df['month']==i]
  emacs_UpvoteMonthWise.append(month_temporary['upvote count'].sum()) #Calculating the sum of the upvote count for each month
ax.bar(months,emacs_UpvoteMonthWise,color='r')
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteF_monthwiseBar.png') #saving the plot
plt.show()


#r/emacs: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtAvg_emacs_jan=[]
day=[]
janEmacs_upvote = emacs_df[emacs_df['month']=='Jan']

#iterating  over days in Jan
for i in range(1,32):
  janemacsTemp=janEmacs_upvote[janEmacs_upvote['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janemacsTemp)):
    upvt_day.append(janemacsTemp['upvote count'][j])
  upvtAvg_emacs_jan.append(mean(upvt_day)) #Calculating the average frequency each day
  day.append(i)

ax.plot(day,upvtAvg_emacs_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_jan.png') #saving the image
plt.show()

#r/emacs: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvote = emacs_df[emacs_df['month']=='Feb']

#Iterating over the days in Feb
for i in range(1,30):
  febemacsTemp=febEmacs_upvote[febEmacs_upvote['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febemacsTemp)):
    upvt_day.append(febemacsTemp['upvote count'][j])
  upvtAvg_emacs_feb.append(mean(upvt_day)) #Calculating the average frequency each day
  day_feb.append(i)

#plotting
ax.plot(day_feb,upvtAvg_emacs_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_feb.png') #saving the image
plt.show()

#r/emacs: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtAvg_emacs_mar=[]
day=[]
marEmacs_upvote = emacs_df[emacs_df['month']=='Mar']

#iterating over the days in March
for i in range(1,32):
  maremacsTemp=marEmacs_upvote[marEmacs_upvote['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(maremacsTemp)):
    upvt_day.append(maremacsTemp['upvote count'][j])
  upvtAvg_emacs_mar.append(mean(upvt_day)) #Calculating the average frequency each day
  day.append(i)

#plotting
ax.plot(day,upvtAvg_emacs_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_mar.png') #saving the image
plt.show()


#r/emacs: UpVote Frequency change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes

ax.plot(day,upvtAvg_emacs_jan, '-.r')
ax.plot(day_feb,upvtAvg_emacs_feb, '-.g')
ax.plot(day,upvtAvg_emacs_mar, '-.b')
ax.set_xlabel('Day')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January','February','March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_3months.png') #saving the image
plt.show()


#r/emacs: UpVote ratio change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtRAvg_emacs_jan=[]
day=[]
janEmacs_upvoteR = emacs_df[emacs_df['month']=='Jan']

#iterating over the days in Jan
for i in range(1,32):
  janemacsTemp=janEmacs_upvoteR[janEmacs_upvoteR['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janemacsTemp)):
    upvtR_day.append(janemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_jan.append(mean(upvtR_day)) #calculating the mean upvote ratio
  day.append(i)

ax.plot(day,upvtRAvg_emacs_jan, '-.b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_jan.png') #saving the image
plt.show()

#r/emacs: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtRAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvoteR = emacs_df[emacs_df['month']=='Feb']

#iterating over the days in feb
for i in range(1,30):
  febemacsTemp=febEmacs_upvoteR[febEmacs_upvoteR['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febemacsTemp)):
    upvtR_day.append(febemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_feb.append(mean(upvtR_day)) #calculating the mean upvote ratio
  day_feb.append(i)

ax.plot(day_feb,upvtRAvg_emacs_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_feb.png') #saving the image
plt.show()


#r/emacs: UpVote ratio change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
upvtRAvg_emacs_mar=[]
day=[]
marEmacs_upvoteR = emacs_df[emacs_df['month']=='Mar']

#Iterating over the days in Mar
for i in range(1,32):
  maremacsTemp=marEmacs_upvoteR[marEmacs_upvoteR['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(maremacsTemp)):
    upvtR_day.append(maremacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_mar.append(mean(upvtR_day)) #calculating the mean upvote ratio
  day.append(i)

ax.plot(day,upvtRAvg_emacs_mar, '-.b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_mar.png')
plt.show()

#r/emacs: UpVote ratio change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
ax.plot(day,upvtRAvg_emacs_jan, '-.r')
ax.plot(day_feb,upvtRAvg_emacs_feb, '-.g')
ax.plot(day,upvtRAvg_emacs_mar, '-.b')

ax.set_xlabel('Day')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January','February','March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatioChange_daywise_3months.png') #saving the image
plt.show()


#r/emacs: Comments Frequency monthwise

fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
emacs_commentMonthWise=[]

#Iterating over the months
for i in months:
  month_temporary = emacs_df[emacs_df['month']==i]
  emacs_commentMonthWise.append(month_temporary['comments count'].sum())
ax.bar(months,emacs_commentMonthWise, color='b')
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_monthwiseBar.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
cmmtAvg_emacs_jan=[]
day=[]
janEmacs_comment = emacs_df[emacs_df['month']=='Jan']

#Iterating over the days in Jan
for i in range(1,32):
  janemacsTemp=janEmacs_comment[janEmacs_comment['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janemacsTemp)):
    cmmt_day.append(janemacsTemp['comments count'][j])
  cmmtAvg_emacs_jan.append(mean(cmmt_day)) #taking the average comment counts per day
  day.append(i)

ax.plot(day,cmmtAvg_emacs_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_jan.png') #saving the image
plt.show()



#r/emacs: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
cmmtAvg_emacs_feb=[]
day_feb=[]
febEmacs_comment = emacs_df[emacs_df['month']=='Feb']

#iterating over the days in feb
for i in range(1,30):
  febemacsTemp=febEmacs_comment[febEmacs_comment['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(febemacsTemp)):
    cmmt_day.append(febemacsTemp['comments count'][j])
  cmmtAvg_emacs_feb.append(mean(cmmt_day)) #taking the average comment counts each day
  day_feb.append(i)

ax.plot(day_feb,cmmtAvg_emacs_feb, '-.g')
ax.set_xlabel('Day in February')
ax.set_ylabel('Comments')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_feb.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes
cmmtAvg_emacs_mar=[]
day=[]
marEmacs_comment = emacs_df[emacs_df['month']=='Mar']

#iterating over the days in March
for i in range(1,32):
  maremacsTemp=marEmacs_comment[marEmacs_comment['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(maremacsTemp)):
    cmmt_day.append(maremacsTemp['comments count'][j])
  cmmtAvg_emacs_mar.append(mean(cmmt_day)) #taking the average comment counts each day
  day.append(i)

ax.plot(day,cmmtAvg_emacs_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_mar.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes


ax.plot(day,cmmtAvg_emacs_jan, '-.r')
ax.plot(day_feb,cmmtAvg_emacs_feb, '-.g')
ax.plot(day,cmmtAvg_emacs_mar, '-.b')
ax.set_xlabel('Day')
ax.set_ylabel('Comments')
plt.legend(["March","February","January"])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_daywise_3months.png') #saving the image
plt.show()



#r/emacs: Comments and upvote Frequency analysis together in Jan
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #aadding the axes


ax.plot(day,upvtAvg_emacs_jan, '-.r')
ax.plot(day,cmmtAvg_emacs_jan, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentUpvote_daywise_Jan.png') #saving the image
plt.show()


#r/emacs: Comments and upvote Frequency analysis together in Feb
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes


ax.plot(day_feb,upvtAvg_emacs_feb, '-.r')
ax.plot(day_feb,cmmtAvg_emacs_feb, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentUpvote_daywise_Feb.png') #saving the image
plt.show()


#r/emacs: Comments and upvote Frequency analysis together in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #adding the axes


ax.plot(day,upvtAvg_emacs_mar, '-.r')
ax.plot(day,cmmtAvg_emacs_mar, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentUpvote_daywise_Mar.png') #saving the image
plt.show()


#r/emacs: Number of Posts monthwise
plot_t = sns.countplot(x='month', data=emacs_df)
figure = plot_t.get_figure()
figure.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/PostFreq_monthwise.png') #saving the image
