from google.colab import drive # This is used to connect with the google drive to save the generated datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
drive.mount('/gdrive/')


vim_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/vim_finalDF.csv')
vim_df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1,inplace=True)
emacs_df=pd.read_csv('/gdrive/My Drive/DrAdams_Task3_Files/CSV/emacs_finalDF.csv')
emacs_df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1,inplace=True)

months = ['Jan', 'Feb', 'Mar']

#r/vim: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_jan=[]
day=[]
janVim_upvote = vim_df[vim_df['month']=='Jan']

for i in range(1,32):
  janvimTemp=janVim_upvote[janVim_upvote['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janvimTemp)):
    upvt_day.append(janvimTemp['upvote count'][j])
  upvtAvg_vim_jan.append(mean(upvt_day))
  day.append(i)

ax.plot(day,upvtAvg_vim_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_jan.png')
plt.show()


#r/emacs: UpVote Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_jan=[]
day=[]
janEmacs_upvote = emacs_df[emacs_df['month']=='Jan']

for i in range(1,32):
  janemacsTemp=janEmacs_upvote[janEmacs_upvote['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(janemacsTemp)):
    upvt_day.append(janemacsTemp['upvote count'][j])
  upvtAvg_emacs_jan.append(mean(upvt_day))
  day.append(i)

ax.plot(day,upvtAvg_emacs_jan, '-.r')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Frequency')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_jan.png')
plt.show()


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

for i in range(1,30):
  febvimTemp=febVim_upvote[febVim_upvote['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febvimTemp)):
    upvt_day.append(febvimTemp['upvote count'][j])
  upvtAvg_vim_feb.append(mean(upvt_day))
  day_feb.append(i)

ax.plot(day_feb,upvtAvg_vim_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_feb.png')
plt.show()


#r/vim: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_feb=[]
day_feb=[]
febVim_upvote = vim_df[vim_df['month']=='Feb']

for i in range(1,30):
  febvimTemp=febVim_upvote[febVim_upvote['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febvimTemp)):
    upvt_day.append(febvimTemp['upvote count'][j])
  upvtAvg_vim_feb.append(mean(upvt_day))
  day_feb.append(i)

ax.plot(day_feb,upvtAvg_vim_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_feb.png')
plt.show()


#r/emacs: UpVote Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvote = emacs_df[emacs_df['month']=='Feb']

for i in range(1,30):
  febemacsTemp=febEmacs_upvote[febEmacs_upvote['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(febemacsTemp)):
    upvt_day.append(febemacsTemp['upvote count'][j])
  upvtAvg_emacs_feb.append(mean(upvt_day))
  day_feb.append(i)

ax.plot(day_feb,upvtAvg_emacs_feb, '-.r')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_feb.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,upvtAvg_vim_feb, '-r')
ax.plot(day_feb,upvtAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Frequency')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteFreq_feb_emacsVim.png')
plt.show()


#r/vim: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_vim_mar=[]
day=[]
marVim_upvote = vim_df[vim_df['month']=='Mar']

for i in range(1,32):
  marvimTemp=marVim_upvote[marVim_upvote['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(marvimTemp)):
    upvt_day.append(marvimTemp['upvote count'][j])
  upvtAvg_vim_mar.append(mean(upvt_day))
  day.append(i)

ax.plot(day,upvtAvg_vim_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteFreq_daywise_mar.png')
plt.show()


#r/emacs: UpVote Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtAvg_emacs_mar=[]
day=[]
marEmacs_upvote = emacs_df[emacs_df['month']=='Mar']

for i in range(1,32):
  maremacsTemp=marEmacs_upvote[marEmacs_upvote['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvt_day=[]
  for j in range(len(maremacsTemp)):
    upvt_day.append(maremacsTemp['upvote count'][j])
  upvtAvg_emacs_mar.append(mean(upvt_day))
  day.append(i)

ax.plot(day,upvtAvg_emacs_mar, '-.r')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteFreq_daywise_mar.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtAvg_vim_mar, '-r')
ax.plot(day,upvtAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Frequency')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteFreq_Mar_emacsVim.png')
plt.show()


#r/vim: UpVote ratio change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_jan=[]
day=[]
janVim_upvoteR = vim_df[vim_df['month']=='Jan']

for i in range(1,32):
  janvimTemp=janVim_upvoteR[janVim_upvoteR['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janvimTemp)):
    upvtR_day.append(janvimTemp['upvote ratio'][j])
  upvtRAvg_vim_jan.append(mean(upvtR_day))
  day.append(i)

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

for i in range(1,32):
  janemacsTemp=janEmacs_upvoteR[janEmacs_upvoteR['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(janemacsTemp)):
    upvtR_day.append(janemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_jan.append(mean(upvtR_day))
  day.append(i)

ax.plot(day,upvtRAvg_emacs_jan, '-.b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_jan.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtRAvg_vim_jan, '-r')
ax.plot(day,upvtRAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_Jan_emacsVim.png')
plt.show()


#r/vim: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_feb=[]
day_feb=[]
febVim_upvoteR = vim_df[vim_df['month']=='Feb']

for i in range(1,30):
  febvimTemp=febVim_upvoteR[febVim_upvoteR['day']==i]
  febvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febvimTemp)):
    upvtR_day.append(febvimTemp['upvote ratio'][j])
  upvtRAvg_vim_feb.append(mean(upvtR_day))
  day_feb.append(i)

ax.plot(day_feb,upvtRAvg_vim_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/UpvoteRatio_daywise_feb.png')
plt.show()


#r/emacs: UpVote ratio change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_emacs_feb=[]
day_feb=[]
febEmacs_upvoteR = emacs_df[emacs_df['month']=='Feb']

for i in range(1,30):
  febemacsTemp=febEmacs_upvoteR[febEmacs_upvoteR['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(febemacsTemp)):
    upvtR_day.append(febemacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_feb.append(mean(upvtR_day))
  day_feb.append(i)

ax.plot(day_feb,upvtRAvg_emacs_feb, '-.b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_feb.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day_feb,upvtRAvg_vim_feb, '-r')
ax.plot(day_feb,upvtRAvg_emacs_feb, '-b')
ax.set_xlabel('Day in Feb')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_feb_emacsVim.png')
plt.show()


#r/vim: UpVote ratio change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
upvtRAvg_vim_mar=[]
day=[]
marVim_upvoteR = vim_df[vim_df['month']=='Mar']

for i in range(1,32):
  marvimTemp=marVim_upvoteR[marVim_upvoteR['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(marvimTemp)):
    upvtR_day.append(marvimTemp['upvote ratio'][j])
  upvtRAvg_vim_mar.append(mean(upvtR_day))
  day.append(i)

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

for i in range(1,32):
  maremacsTemp=marEmacs_upvoteR[marEmacs_upvoteR['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  upvtR_day=[]
  for j in range(len(maremacsTemp)):
    upvtR_day.append(maremacsTemp['upvote ratio'][j])
  upvtRAvg_emacs_mar.append(mean(upvtR_day))
  day.append(i)

ax.plot(day,upvtRAvg_emacs_mar, '-.b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/UpvoteRatio_daywise_mar.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,upvtRAvg_vim_mar, '-r')
ax.plot(day,upvtRAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Upvote Ratio')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/UpvoteRatio_mar_emacsVim.png')
plt.show()


#r/vim: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_jan=[]
day=[]
janVim_comment = vim_df[vim_df['month']=='Jan']

for i in range(1,32):
  janvimTemp=janVim_comment[janVim_comment['day']==i]
  janvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janvimTemp)):
    cmmt_day.append(janvimTemp['comments count'][j])
  cmmtAvg_vim_jan.append(mean(cmmt_day))
  day.append(i)

ax.plot(day,cmmtAvg_vim_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_jan.png')
plt.show()


#r/emacs: Comments Frequency change in January
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_jan=[]
day=[]
janEmacs_comment = emacs_df[emacs_df['month']=='Jan']

for i in range(1,32):
  janemacsTemp=janEmacs_comment[janEmacs_comment['day']==i]
  janemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(janemacsTemp)):
    cmmt_day.append(janemacsTemp['comments count'][j])
  cmmtAvg_emacs_jan.append(mean(cmmt_day))
  day.append(i)

ax.plot(day,cmmtAvg_emacs_jan, '-.g')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments')
plt.legend(['January'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_jan.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,cmmtAvg_vim_jan, '-r')
ax.plot(day,cmmtAvg_emacs_jan, '-b')
ax.set_xlabel('Day in Jan')
ax.set_ylabel('Comments Count')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/CommentsF_jan_emacsVim.png')
plt.show()


#r/vim: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_vim_feb=[]
day_feb=[]
febVim_comment = vim_df[vim_df['month']=='Feb']

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
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_feb.png')
plt.show()


#r/emacs: Comments Frequency change in February
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_feb=[]
day_feb=[]
febEmacs_comment = emacs_df[emacs_df['month']=='Feb']

for i in range(1,30):
  febemacsTemp=febEmacs_comment[febEmacs_comment['day']==i]
  febemacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(febemacsTemp)):
    cmmt_day.append(febemacsTemp['comments count'][j])
  cmmtAvg_emacs_feb.append(mean(cmmt_day))
  day_feb.append(i)

ax.plot(day_feb,cmmtAvg_emacs_feb, '-.g')
ax.set_xlabel('Day in February')
ax.set_ylabel('Comments')
plt.legend(['February'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_feb.png')
plt.show()


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

for i in range(1,32):
  marvimTemp=marVim_comment[marVim_comment['day']==i]
  marvimTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(marvimTemp)):
    cmmt_day.append(marvimTemp['comments count'][j])
  cmmtAvg_vim_mar.append(mean(cmmt_day))
  day.append(i)

ax.plot(day,cmmtAvg_vim_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_vim/commentFreq_mar.png')
plt.show()


#r/emacs: Comments Frequency change in March
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cmmtAvg_emacs_mar=[]
day=[]
marEmacs_comment = emacs_df[emacs_df['month']=='Mar']

for i in range(1,32):
  maremacsTemp=marEmacs_comment[marEmacs_comment['day']==i]
  maremacsTemp.reset_index(drop=True,inplace=True)
  cmmt_day=[]
  for j in range(len(maremacsTemp)):
    cmmt_day.append(maremacsTemp['comments count'][j])
  cmmtAvg_emacs_mar.append(mean(cmmt_day))
  day.append(i)

ax.plot(day,cmmtAvg_emacs_mar, '-.g')
ax.set_xlabel('Day in March')
ax.set_ylabel('Comments')
plt.legend(['March'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/r_emacs/commentFreq_mar.png')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(day,cmmtAvg_vim_mar, '-r')
ax.plot(day,cmmtAvg_emacs_mar, '-b')
ax.set_xlabel('Day in Mar')
ax.set_ylabel('Comments Count')
plt.legend(['vim','emacs'])
plt.savefig('/gdrive/My Drive/DrAdams_Task3_Files/PNG/Both/CommentsF_mar_emacsVim.png')
plt.show()






