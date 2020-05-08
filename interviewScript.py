import requests
import json
from bs4 import BeautifulSoup

url_dict = {'Ben Shapiro' : 'https://scrapsfromtheloft.com/2019/06/01/ben-shapiro-the-entitlement-generation/',
'Dustin Hoffman':'https://scrapsfromtheloft.com/2019/04/29/dustin-hoffman-interview-empire-2006/',
'Bill Burr':'https://scrapsfromtheloft.com/2018/10/06/bill-burr-on-cucks-white-privilege-sjws-feminism-transcript/',
'Jordan Peterson':'https://scrapsfromtheloft.com/2018/08/23/jordan-petersons-channel-4-interview-cathy-newman-transcript/',
'Barack Obama':'https://scrapsfromtheloft.com/2018/08/15/president-obama-interview-real-time-with-bill-maher/',
'Bertrand Russell':'https://scrapsfromtheloft.com/2019/02/02/a-conversation-with-bertrand-russell-1952/',
'John Huston':'https://scrapsfromtheloft.com/2018/03/28/how-i-make-films-interview-john-huston-gideon-bachmann/',
'Richard Dawkins':'https://scrapsfromtheloft.com/2018/01/02/richard-dawkins-playboy-interview-chip-rowe/',
'James B. Harris':'https://scrapsfromtheloft.com/2018/02/16/james-b-harris-interview-2002/',
}