from google.colab import drive # This is used to connect with the google drive to save the generated datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
drive.mount('/gdrive/') #mounting google drive


#Importing the datasets
vim_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/vim_finalDF.csv')
emacs_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/emacs_finalDF.csv')

months = ['Jan', 'Feb', 'Mar']


#r/vim: Total Awards Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_vim_jan=[]
day=[]
janVim_totalawards = vim_df[vim_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janvimTemp=janVim_totalawards[janVim_totalawards['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(janvimTemp)):
    totalAwa_day.append(janvimTemp['total awards'][j])
  totalAwarddsAvg_vim_jan.append(mean(totalAwa_day)) #Average awards daily
  day.append(i)

#plotting
ax.plot(day,totalAwarddsAvg_vim_jan, '-.c')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Total Awards')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/TotalAwaFreq_daywise_jan.png') #saving the image
plt.show()

#r/emacs: Total Awards Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_emacs_jan=[]
day=[]
janEmacs_totalawards = emacs_df[emacs_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janemacsTemp=janEmacs_totalawards[janEmacs_totalawards['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(janemacsTemp)):
    totalAwa_day.append(janemacsTemp['total awards'][j])
  totalAwarddsAvg_emacs_jan.append(mean(totalAwa_day)) #Average awards daily
  day.append(i)

#plotting
ax.plot(day,totalAwarddsAvg_emacs_jan, '-.c')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Total Awards')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/TotalAwaFreq_daywise_jan.png') #saving the plot
plt.show()

#r/emacs & r/vim Total Awards comparison: January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,totalAwarddsAvg_vim_jan, '-r')
ax.plot(day,totalAwarddsAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Total Awards')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/TotalAwaFreq_jan_emacsVim.png') #saving the plot
plt.show()

#r/vim: Total Awards Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_vim_feb=[]
day_feb=[]
febVim_totalawards = vim_df[vim_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febvimTemp=febVim_totalawards[febVim_totalawards['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(febvimTemp)):
    totalAwa_day.append(febvimTemp['total awards'][j])
  totalAwarddsAvg_vim_feb.append(mean(totalAwa_day)) #Average Awards Daily
  day_feb.append(i)

#plotting
ax.plot(day_feb,totalAwarddsAvg_vim_feb, '-.c')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Total Awards')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/TotalAwaFreq_daywise_feb.png') #saving the image
plt.show()


#r/emacs: Total Awards Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_emacs_feb=[]
day_feb=[]
febEmacs_totalawards = emacs_df[emacs_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febemacsTemp=febEmacs_totalawards[febEmacs_totalawards['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(febemacsTemp)):
    totalAwa_day.append(febemacsTemp['total awards'][j])
  totalAwarddsAvg_emacs_feb.append(mean(totalAwa_day)) #Average awards daily
  day_feb.append(i)

#Plotting
ax.plot(day_feb,totalAwarddsAvg_emacs_feb, '-.c')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Total Awards')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/TotalAwaFreq_daywise_feb.png') #saving the image
plt.show()

#r/emacs & r/vim Total Awards comparison: February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,totalAwarddsAvg_vim_feb, '-r')
ax.plot(day_feb,totalAwarddsAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Total Awards')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/TotalAwaFreq_feb_emacsVim.png') #saving the image
plt.show()


#r/vim: Total Awards Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_vim_mar=[]
day=[]
marVim_totalawards = vim_df[vim_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  marvimTemp=marVim_totalawards[marVim_totalawards['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(marvimTemp)):
    totalAwa_day.append(marvimTemp['total awards'][j])
  totalAwarddsAvg_vim_mar.append(mean(totalAwa_day)) #Average awards daily
  day.append(i)

#plotting
ax.plot(day,totalAwarddsAvg_vim_mar, '-.c')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Total Awards')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/TotalAwaFreq_daywise_mar.png') #saving the image
plt.show()


#r/emacs: Total Awards Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
totalAwarddsAvg_emacs_mar=[]
day=[]
marEmacs_totalawards = emacs_df[emacs_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,30):
  maremacsTemp=marEmacs_totalawards[marEmacs_totalawards['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  totalAwa_day=[]
  for j in range(len(maremacsTemp)):
    totalAwa_day.append(maremacsTemp['total awards'][j])
  totalAwarddsAvg_emacs_mar.append(mean(totalAwa_day)) #Average Awards Daily
  day.append(i)

#plotting
ax.plot(day_feb,totalAwarddsAvg_emacs_mar, '-.c')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Total Awards')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/TotalAwaFreq_daywise_mar.png') #saving the image
plt.show()


#r/emacs & r/vim Total Awards comparison: March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,totalAwarddsAvg_vim_mar, '-r')
ax.plot(day_feb,totalAwarddsAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Total Awards')
plt.legend(['r/vim','r/emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/TotalAwaFreq_mar_emacsVim.png') #saving the image
plt.show()


#BarPlot of Total Awards comparison between r/vim and r/emacs
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
sub_reddits = ['r/vim','r/emacs']
total_awards_count=[vim_df['total awards'].sum(),emacs_df['total awards'].sum()]
ax.bar(sub_reddits,total_awards_count, color='orange')
ax.set_xlabel('SubReddits')
ax.set_ylabel('Total Awards in 3 months')
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/TotalAwaFreq_barPlot_emacsVim.png') #saving the image
plt.show()


#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_jan=[]
day=[]
janVim_upvote = vim_df[vim_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janvimTemp=janVim_upvote[janVim_upvote['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janvimTemp)):
    upvt_day.append(janvimTemp['upvote count'][j])
  upvtAvg_vim_jan.append(mean(upvt_day)) #average upvote daily
  day.append(i)

#plotting
ax.plot(day,upvtAvg_vim_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_jan.png') #saving the image
plt.show()


#r/emacs: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_jan=[]
day=[]
janEmacs_upvote = emacs_df[emacs_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janemacsTemp=janEmacs_upvote[janEmacs_upvote['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janemacsTemp)):
    upvt_day.append(janemacsTemp['upvote count'][j])
  upvtAvg_emacs_jan.append(mean(upvt_day)) #average upvote daily
  day.append(i)

#plotting
ax.plot(day,upvtAvg_emacs_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_jan.png') #saving the image
plt.show()


#r/emacs & r/vim Upvote Frequency comparison: January

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtAvg_vim_jan, '-r')
ax.plot(day,upvtAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteFreq_jan_emacsVim.png')
plt.show()


#r/vim: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_feb=[]
day_feb=[]
febVim_upvote = vim_df[vim_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febvimTemp=febVim_upvote[febVim_upvote['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febvimTemp)):
    upvt_day.append(febvimTemp['upvote count'][j])
  upvtAvg_vim_feb.append(mean(upvt_day)) #average upvote daily
  day_feb.append(i)

#plotting
ax.plot(day_feb,upvtAvg_vim_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_feb.png') #saving the image
plt.show()


#r/emacs: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvote = emacs_df[emacs_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febemacsTemp=febEmacs_upvote[febEmacs_upvote['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febemacsTemp)):
    upvt_day.append(febemacsTemp['upvote count'][j])
  upvtAvg_emacs_feb.append(mean(upvt_day)) #average upvote daily
  day_feb.append(i)

#plotting
ax.plot(day_feb,upvtAvg_emacs_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_feb.png') #saving the image
plt.show()


#r/emacs & r/vim Upvote Frequency comparison: February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,upvtAvg_vim_feb, '-r')
ax.plot(day_feb,upvtAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteFreq_feb_emacsVim.png') #saving the image
plt.show()


#r/vim: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_mar=[]
day=[]
marVim_upvote = vim_df[vim_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  marvimTemp=marVim_upvote[marVim_upvote['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(marvimTemp)):
    upvt_day.append(marvimTemp['upvote count'][j])
  upvtAvg_vim_mar.append(mean(upvt_day)) #average upvote daily
  day.append(i)

#plotting
ax.plot(day,upvtAvg_vim_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_mar.png') #saving the image
plt.show()


#r/emacs: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_mar=[]
day=[]
marEmacs_upvote = emacs_df[emacs_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  maremacsTemp=marEmacs_upvote[marEmacs_upvote['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(maremacsTemp)):
    upvt_day.append(maremacsTemp['upvote count'][j])
  upvtAvg_emacs_mar.append(mean(upvt_day)) #average upvote daily
  day.append(i)

#plotting
ax.plot(day,upvtAvg_emacs_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_mar.png') #saving the image
plt.show()


#r/emacs & r/vim Upvote Frequency comparison: March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtAvg_vim_mar, '-r')
ax.plot(day,upvtAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteFreq_Mar_emacsVim.png') #saving the image
plt.show()


#r/vim: UpVote ratio change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_jan=[]
day=[]
janVim_upvoteR = vim_df[vim_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janvimTemp=janVim_upvoteR[janVim_upvoteR['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janvimTemp)):
    upvtR_day.append(janvimTemp['upvote ratio'][j])
  upvtRAvg_vim_jan.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

#plotting
ax.plot(day,upvtRAvg_vim_jan, '-.b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_jan.png')
plt.show()


#r/emacs: UpVote ratio change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_emacs_jan=[]
day=[]
janEmacs_upvoteR = emacs_df[emacs_df['month']=='Jan']

#iterating over the dates in March
for i in range(1,32):
  janemacsTemp=janEmacs_upvoteR[janEmacs_upvoteR['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janemacsTemp)):
    upvtR_day.append(janemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_jan.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

#plotting
ax.plot(day,upvtRAvg_emacs_jan, '-.b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_jan.png') #saving the image
plt.show()

#r/emacs & r/vim Upvote Ratio comparison: January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtRAvg_vim_jan, '-r')
ax.plot(day,upvtRAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_Jan_emacsVim.png') #saving the image
plt.show()


#r/vim: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_feb=[]
day_feb=[]
febVim_upvoteR = vim_df[vim_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febvimTemp=febVim_upvoteR[febVim_upvoteR['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febvimTemp)):
    upvtR_day.append(febvimTemp['upvote ratio'][j])
  upvtRAvg_vim_feb.append(mean(upvtR_day)) #avergae upvote ratio daily
  day_feb.append(i)

#Plotting
ax.plot(day_feb,upvtRAvg_vim_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_feb.png') #saving the image
plt.show()


#r/emacs: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvoteR = emacs_df[emacs_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febemacsTemp=febEmacs_upvoteR[febEmacs_upvoteR['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febemacsTemp)):
    upvtR_day.append(febemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_feb.append(mean(upvtR_day)) #average upvote ratio daily
  day_feb.append(i)

#plotting
ax.plot(day_feb,upvtRAvg_emacs_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_feb.png') #saving the image
plt.show()


#r/emacs & r/vim Upvote Ratio comparison: February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,upvtRAvg_vim_feb, '-r')
ax.plot(day_feb,upvtRAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_feb_emacsVim.png') #saving the image
plt.show()


#r/vim: UpVote ratio change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_mar=[]
day=[]
marVim_upvoteR = vim_df[vim_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  marvimTemp=marVim_upvoteR[marVim_upvoteR['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(marvimTemp)):
    upvtR_day.append(marvimTemp['upvote ratio'][j])
  upvtRAvg_vim_mar.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

#plotting
ax.plot(day,upvtRAvg_vim_mar, '-.b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_mar.png')
plt.show()



#r/emacs: UpVote ratio change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_emacs_mar=[]
day=[]
marEmacs_upvoteR = emacs_df[emacs_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  maremacsTemp=marEmacs_upvoteR[marEmacs_upvoteR['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(maremacsTemp)):
    upvtR_day.append(maremacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_mar.append(mean(upvtR_day)) #average upvote ratio daily
  day.append(i)

#plotting
ax.plot(day,upvtRAvg_emacs_mar, '-.b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_mar.png') #saving the image
plt.show()


#r/emacs & r/vim Total Upvote Ratio comparison: March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtRAvg_vim_mar, '-r')
ax.plot(day,upvtRAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_mar_emacsVim.png') #saving the image
plt.show()


#r/vim: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_jan=[]
day=[]
janVim_comment = vim_df[vim_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janvimTemp=janVim_comment[janVim_comment['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janvimTemp)):
    cmmt_day.append(janvimTemp['comments count'][j])
  cmmtAvg_vim_jan.append(mean(cmmt_day)) #average comments per day
  day.append(i)

#plotting
ax.plot(day,cmmtAvg_vim_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_jan.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_jan=[]
day=[]
janEmacs_comment = emacs_df[emacs_df['month']=='Jan']

#iterating over the dates in January
for i in range(1,32):
  janemacsTemp=janEmacs_comment[janEmacs_comment['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janemacsTemp)):
    cmmt_day.append(janemacsTemp['comments count'][j])
  cmmtAvg_emacs_jan.append(mean(cmmt_day)) #average comments per day
  day.append(i)

#plotting
ax.plot(day,cmmtAvg_emacs_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_jan.png') #saving the image
plt.show()


#r/emacs & r/vim Comments Frequency comparison: January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,cmmtAvg_vim_jan, '-r')
ax.plot(day,cmmtAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments Count')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/CommentsF_jan_emacsVim.png') #saving the image
plt.show()


#r/vim: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_feb=[]
day_feb=[]
febVim_comment = vim_df[vim_df['month']=='Feb']

#iterating over the dates in February
for i in range(1,30):
  febvimTemp=febVim_comment[febVim_comment['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(febvimTemp)):
    cmmt_day.append(febvimTemp['comments count'][j])
  cmmtAvg_vim_feb.append(mean(cmmt_day)) #average comments per day
  day_feb.append(i)

#plotting
ax.plot(day_feb,cmmtAvg_vim_feb, '-.g')
ax.set_xlabel('Day in February')
ax.set_ylabel('Comments')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_feb.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_feb=[]
day_feb=[]
febEmacs_comment = emacs_df[emacs_df['month']=='Feb']

##iterating over the dates in March
for i in range(1,30):
  febemacsTemp=febEmacs_comment[febEmacs_comment['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(febemacsTemp)):
    cmmt_day.append(febemacsTemp['comments count'][j])
  cmmtAvg_emacs_feb.append(mean(cmmt_day)) #average comments daily
  day_feb.append(i)

#plotting
ax.plot(day_feb,cmmtAvg_emacs_feb, '-.g')
ax.set_xlabel('Day in February')
ax.set_ylabel('Comments')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_feb.png')
plt.show()


#r/emacs & r/vim Comments comparison: February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,cmmtAvg_vim_feb, '-r')
ax.plot(day_feb,cmmtAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Comments Count')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/CommentsF_feb_emacsVim.png')
plt.show()


#r/vim: Comments Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_mar=[]
day=[]
marVim_comment = vim_df[vim_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  marvimTemp=marVim_comment[marVim_comment['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(marvimTemp)):
    cmmt_day.append(marvimTemp['comments count'][j])
  cmmtAvg_vim_mar.append(mean(cmmt_day)) #average comments per day
  day.append(i)

#plotting
ax.plot(day,cmmtAvg_vim_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_mar.png') #saving the image
plt.show()


#r/emacs: Comments Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_mar=[]
day=[]
marEmacs_comment = emacs_df[emacs_df['month']=='Mar']

#iterating over the dates in March
for i in range(1,32):
  maremacsTemp=marEmacs_comment[marEmacs_comment['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(maremacsTemp)):
    cmmt_day.append(maremacsTemp['comments count'][j])
  cmmtAvg_emacs_mar.append(mean(cmmt_day)) #average comments per day
  day.append(i)

#plotting
ax.plot(day,cmmtAvg_emacs_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_mar.png') #saving the image
plt.show()

#r/emacs & r/vim Comments Frequency comparison: March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,cmmtAvg_vim_mar, '-r')
ax.plot(day,cmmtAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Comments Count')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/CommentsF_mar_emacsVim.png') #saving the image
plt.show()

