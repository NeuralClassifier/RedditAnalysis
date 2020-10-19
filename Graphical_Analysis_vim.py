from google.colab import drive # This is used to connect with the google drive to save the generated datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
drive.mount('/gdrive/')


#Importing the datasets
vim_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/vim_finalDF.csv')


#Calculating the correlation using Heatmap
corr_vim = vim_df.corr()
plot_t=sns.heatmap(corr_vim)
figure = plot_t.get_figure()
figure.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/Heatmap_vim.png') #saving the image


#Declaring the months
months = ['Jan', 'Feb', 'Mar']

#r/vim: Monthwise upvote Bar plot

fig = plt.figure()
ax = fig.add_axes([1,1,1,1])
vim_UpvoteMonthWise=[]

#iterating over 3 months
for i in months:
  month_temporary = vim_df[vim_df['month']==i]
  vim_UpvoteMonthWise.append(month_temporary['upvote count'].sum()) #total upvote
ax.bar(months,vim_UpvoteMonthWise)
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteF_monthwiseBar.png') #saving the image
plt.show()



#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_jan=[]
day=[]
janVim_upvote = vim_df[vim_df['month']=='Jan']

#iterating over the days in January
for i in range(1,32):
  janvimTemp=janVim_upvote[janVim_upvote['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janvimTemp)):
    upvt_day.append(janvimTemp['upvote count'][j])
  upvtAvg_vim_jan.append(mean(upvt_day)) #average upvote daily
  day.append(i)

ax.plot(day,upvtAvg_vim_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_jan.png') #saving the image
plt.show()


#r/vim: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_feb=[]
day_feb=[]
febVim_upvote = vim_df[vim_df['month']=='Feb']

#iterating over the days in February
for i in range(1,30):
  febvimTemp=febVim_upvote[febVim_upvote['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febvimTemp)):
    upvt_day.append(febvimTemp['upvote count'][j])
  upvtAvg_vim_feb.append(mean(upvt_day)) #average upvote daily
  day_feb.append(i)

ax.plot(day_feb,upvtAvg_vim_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_feb.png') #saving the image
plt.show()


#r/vim: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_mar=[]
day=[]
marVim_upvote = vim_df[vim_df['month']=='Mar']

#iterating over the days in March
for i in range(1,32):
  marvimTemp=marVim_upvote[marVim_upvote['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(marvimTemp)):
    upvt_day.append(marvimTemp['upvote count'][j])
  upvtAvg_vim_mar.append(mean(upvt_day)) #average upvote daily
  day.append(i)

ax.plot(day,upvtAvg_vim_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_mar.png') #saving the image
plt.show()


#r/vim: UpVote Frequency change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(day,upvtAvg_vim_jan, '-.r')
ax.plot(day_feb,upvtAvg_vim_feb, '-.g')
ax.plot(day,upvtAvg_vim_mar, '-.b')
ax.set_xlabel('Day')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January','February','March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_3months.png') #saving the image
plt.show()



#r/vim: UpVote ratio change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_jan=[]
day=[]
janVim_upvoteR = vim_df[vim_df['month']=='Jan']

#iterating over the days in January
for i in range(1,32):
  janvimTemp=janVim_upvoteR[janVim_upvoteR['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janvimTemp)):
    upvtR_day.append(janvimTemp['upvote ratio'][j])
  upvtRAvg_vim_jan.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

ax.plot(day,upvtRAvg_vim_jan, '-.b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_jan.png') #saving the image
plt.show()


#r/vim: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_feb=[]
day_feb=[]
febVim_upvoteR = vim_df[vim_df['month']=='Feb']

#iterating over the days in February
for i in range(1,30):
  febvimTemp=febVim_upvoteR[febVim_upvoteR['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febvimTemp)):
    upvtR_day.append(febvimTemp['upvote ratio'][j])
  upvtRAvg_vim_feb.append(mean(upvtR_day)) #average upvote ratio daily
  day_feb.append(i)

ax.plot(day_feb,upvtRAvg_vim_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_feb.png') #saving the image
plt.show()


#r/vim: UpVote ratio change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_mar=[]
day=[]
marVim_upvoteR = vim_df[vim_df['month']=='Mar']

#iterating over the days in March
for i in range(1,32):
  marvimTemp=marVim_upvoteR[marVim_upvoteR['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(marvimTemp)):
    upvtR_day.append(marvimTemp['upvote ratio'][j])
  upvtRAvg_vim_mar.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

ax.plot(day,upvtRAvg_vim_mar, '-.b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_mar.png') #saving the image
plt.show()


#r/vim: UpVote ratio change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


ax.plot(day,upvtRAvg_vim_jan, '-.r')
ax.plot(day_feb,upvtRAvg_vim_feb, '-.g')
ax.plot(day,upvtRAvg_vim_mar, '-.b')


ax.set_xlabel('Day')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January','February','March'])
 
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatioChange_daywise_3months.png') #saving the image

plt.show()


#r/vim: Comments Frequency monthwise

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
vim_commentMonthWise=[]

#iterating of the months
for i in months:
  month_temporary = vim_df[vim_df['month']==i]
  vim_commentMonthWise.append(month_temporary['comments count'].sum())
ax.bar(months,vim_commentMonthWise, color='b')
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_monthwiseBar.png') #saving the image
plt.show()


#r/vim: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_jan=[]
day=[]
janVim_comment = vim_df[vim_df['month']=='Jan']

#iterating over the days in January
for i in range(1,32):
  janvimTemp=janVim_comment[janVim_comment['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janvimTemp)):
    cmmt_day.append(janvimTemp['comments count'][j])
  cmmtAvg_vim_jan.append(mean(cmmt_day)) #Average comments per day
  day.append(i)

ax.plot(day,cmmtAvg_vim_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_jan.png') #saving the image
plt.show()


#r/vim: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_feb=[]
day_feb=[]
febVim_comment = vim_df[vim_df['month']=='Feb']

#iterating over the days in February
for i in range(1,30):
  febvimTemp=febVim_comment[febVim_comment['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(febvimTemp)):
    cmmt_day.append(febvimTemp['comments count'][j])
  cmmtAvg_vim_feb.append(mean(cmmt_day))
  day_feb.append(i)

ax.plot(day_feb,cmmtAvg_vim_feb, '-.g')
ax.set_xlabel('Day in February')
ax.set_ylabel('Comments')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_feb.png') #saving the image
plt.show()


#r/vim: Comments Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_mar=[]
day=[]
marVim_comment = vim_df[vim_df['month']=='Mar']

#iterating over the days in March
for i in range(1,32):
  marvimTemp=marVim_comment[marVim_comment['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(marvimTemp)):
    cmmt_day.append(marvimTemp['comments count'][j])
  cmmtAvg_vim_mar.append(mean(cmmt_day)) #average comments per day
  day.append(i)

ax.plot(day,cmmtAvg_vim_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_mar.png') #saving the image
plt.show()


#r/vim: Comments Frequency change of all months together
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


ax.plot(day,cmmtAvg_vim_jan, '-.r')
ax.plot(day_feb,cmmtAvg_vim_feb, '-.g')
ax.plot(day,cmmtAvg_vim_mar, '-.b')
ax.set_xlabel('Day')
ax.set_ylabel('Comments')
plt.legend(["March","February","January"])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_daywise_3months.png') #saving the image
plt.show()


#r/vim: Comments and upvote Frequency analysis in Jan
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


ax.plot(day,upvtAvg_vim_jan, '-.r')
ax.plot(day,cmmtAvg_vim_jan, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentUpvote_daywise_Jan.png') #saving the image
plt.show()


#r/vim: Comments and upvote Frequency analysis in Feb
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


ax.plot(day_feb,upvtAvg_vim_feb, '-.r')
ax.plot(day_feb,cmmtAvg_vim_feb, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentUpvote_daywise_Feb.png') #saving the image
plt.show()


#r/vim: Comments and upvote Frequency analysis in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


ax.plot(day,upvtAvg_vim_mar, '-.r')
ax.plot(day,cmmtAvg_vim_mar, '-.g')
ax.set_xlabel('Day')
ax.set_ylabel('Count')
plt.legend(['Upvote','Comments'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentUpvote_daywise_Mar.png') #saving the image
plt.show()


#r/vim: Number of Posts monthwise
plot_t = sns.countplot(x='month', data=vim_df)
figure = plot_t.get_figure()
figure.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/PostFreq_monthwise.png') #saving the image




