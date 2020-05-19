#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt


# In[18]:


top_10_games = pd.read_csv('Twitch Top 10 Trending Games.csv')
#print(top_10_games)

games = list(top_10_games.Game)
viewers = list(top_10_games['No. of Viewers'])
games.reverse()
viewers.reverse()

plt.figure(figsize=[15,10])
ax=plt.subplot()
plt.barh(range(len(games)),viewers, color=['green' if i > 50000 else 'blue' for i in viewers])
plt.title('Number of Views for Top 10 Games (1 Jan 2015)')
ax.set_yticks(range(len(games)))
ax.set_yticklabels(games)
ax.set_xticks(range(0,200001,50000))

plt.savefig('Top 10 Games.png',bbox_inches='tight')
plt.show()
plt.close('all')


# In[19]:


top_10_countries = pd.read_csv('Twitch Top 10 Countries Viewing League of Legends.csv')
#print(top_10_countries)

labels = list(top_10_countries.Country)
countries = list(top_10_countries['No. of Viewers'])

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'violet', 'khaki', 'yellowgreen']
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)

plt.figure(figsize=(16,12))
plt.pie(countries,autopct='%1.0f%%',pctdistance=0.9,explode=explode,startangle=225.5,colors=colors)
plt.title('Twitch Top 10 Trending Games by Country (1 Jan 2015)')
plt.legend(labels,loc=1)

plt.savefig('Top 10 Countries - LOL.png',bbox_inches='tight')
plt.show()
plt.close('all')


# In[20]:


us_views_by_hour = pd.read_csv('Twitch League of Legends US Views by Hour.csv')
#print(us_views_by_hour)

hour = range(24)
hours = list(us_views_by_hour.hour_of_day)
viewers_hour = list(us_views_by_hour.views)
viewers_lo_b = [i * 0.85 for i in viewers_hour]
viewers_up_b = [i * 1.15 for i in viewers_hour]

plt.figure(figsize=[16,6])
ax=plt.subplot()
plt.plot(hour,viewers_hour, marker='o')
plt.title('Twitch Number of League of Legends Viewers by Hour in the US (1 Jan 2015)')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Viewers')
plt.axis([-0.1,23.1,0,24001])
plt.fill_between(hour,viewers_lo_b,viewers_up_b,color='sienna',alpha=0.3)
ax.set_xticks(range(24))
ax.set_xticklabels([str(i)+':00' for i in hours])
ax.set_yticks(range(0,24000,2000))

plt.savefig('Viewers by Hour - US.png',bbox_inches='tight')
plt.show()
plt.close('all')

