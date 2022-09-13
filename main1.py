import pandas as pd
import time
import praw 
import csv
import datetime 

reddit = praw.Reddit(
    client_id = "your id,
    client_secret = "your secret",
    username = "your un",
    password = "your pw",
    user_agent = "test-instance"
)


def writeheaders():
    f.writerow(["Number","Keyword","Title","Score","Comments","URL","Domain","Permalink","ID","Subreddit","CreatedDate"])

def writefields():
    f.writerow([startNum, search.strip(), submission.title,
                submission.score, submission.num_comments,
                submission.url, submission.domain, "https://www.reddit.com/"+ submission.permalink, submission.id,
                submission.subreddit, datetime.datetime.utcfromtimestamp(submission.created).strftime('%m-%d-%Y')])





print("Authenticating... " + str(reddit.user.me()) + " ... Verified!\r\n")

outfilename = input("Enter a CSV filename to output the data to (e.g., soar_example.csv):\r\n")
search = input("Enter a search key. (If multiple, please use commas to separate keywords or terms):\r\n")
sortsub = input("Please enter sort criteria -- relevance, hot, top, new, or comments.\r\n")
filtersub = input("Do you want to restrict to a certain subreddit? Enter 'Yes' or 'No'.\r\n")

search_list = search.split(',')

if(filtersub.lower()=="yes"):
    subreddit = input("Please enter subreddit name. If multiple, use comma separators:\r\n")
    subreddit_list = subreddit.split(',')
    file = open(outfilename, "w+", newline="\n", encoding="utf-8")
    f = csv.writer(file)
    writeheaders()
    for subs in subreddit_list:
        for search in search_list:
            startNum = 0
            for submission in reddit.subreddit(subs.strip()).search(search, sort=sortsub):
                startNum += 1
                writefields()
            print("Outputting the results '" + search.strip() + "' in 'r/" + subs.strip() + "'\r\n")
        file.close
else:
    file = open(outfilename, "w+", newline="\n", encoding="utf-8")
    f = csv.writer(file)
    writeheaders()
    for search in search_list:
        startNum = 0
        for submission in reddit.subreddit('all').search(search.lower(), sort=sortsub):
            startNum += 1
            writefields()
        print("Outputting the results '" + search.strip() + "' in 'r/all'\r\n")
    file.close
#end