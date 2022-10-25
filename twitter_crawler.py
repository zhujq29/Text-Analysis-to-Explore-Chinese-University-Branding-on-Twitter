import tweepy
import xlwt
import xlrd
import re,string

consumer_key = 'YSyZ51YWv3E0IczudhbE3QkTi'
consumer_secret = 'rRgWfkW3FcwSvPSe0MQ0jJblPzKP331IqkVfNZFwlaVS6dixqK'
access_token = '1180011922395021313-RmJBGqsHZag9NJYJZLrjqBABwmgIMK'
access_token_secret = 'Fbi7ilOcJPhfmiDcxy0slRIuDEpazgWb50jkWAkULPNaF'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

schoolname = input("Please input the school name: ")
search_result = api.search(q=schoolname, 
                           count = 500, 
                           result_type = 'recent', 
                           lang = 'en', 
                           tweet_mode="extended",
                           since = "2019-10-23",
                           until = "2019-10-24")
ulist = []
rlist = []
dlist = []
resultlist = []
def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text


def strip_all_entities(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())

def Remove_Emoji(text):
    emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)
    new_text = emoji_pattern.sub(r'',text)
    return new_text 


            

for tweet in search_result:
    if 'retweeted_status' in tweet._json:
        screen_name = tweet._json['user']['screen_name']
        content = tweet._json['retweeted_status']['full_text']
        date = tweet._json['created_at']
        content1 = strip_all_entities(strip_links(content))
    else:
        screen_name = tweet._json['user']['screen_name']
        content = tweet.full_text
        date = tweet._json['created_at']
        content1 = strip_all_entities(strip_links(Remove_Emoji(content)))
        
    
    rlist.append(content1)
    for i in rlist:
        if not i in resultlist:
            resultlist.append(i)
            dlist.append(date)
            ulist.append(screen_name)   

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("data",cell_overwrite_ok=True) 


for item in range(len(resultlist)):
    sheet1.write(item,0,resultlist[item])


for item1 in range(len(dlist)):
    sheet1.write(item1,1,dlist[item1])


for item2 in range(len(ulist)):
    sheet1.write(item2,2,ulist[item2])

print(rlist)
print(dlist)
book.save(schoolname+".xls")

print("Finished.")
   
