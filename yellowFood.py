import sys
import webbrowser
from rtmapi import Rtm

import arrow

from trello import TrelloApi
import json

from datetime import datetime

import datetime

TRELLO_APP_KEY='b730b6c72f876470a8c4cbf5ebe41dc0'

trello=TrelloApi(TRELLO_APP_KEY)

#print trello.get_token_url('YellowFood', expires='90days', write_access=True) 
 
user_token='cbecb81059cebb2d026afa70977c99834a51b4c53343f4cbc280a0ad69549943'

trello.set_token(user_token)

boards = trello.boards.get('5a0068aabd9f13a3c7e28b7e')

print boards['name']
print boards['labelNames']

lists = trello.boards.get_list('5a0068aabd9f13a3c7e28b7e')
cards = trello.boards.get_card('5a0068aabd9f13a3c7e28b7e')


for l in lists:
    print l['name']


date = datetime.date.today()
start_week = date - datetime.timedelta(date.weekday())
end_week = start_week + datetime.timedelta(7)

for c in cards:
    date = c['due']
    if date != None:
    	ndate = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        if ndate < end_week and ndate > start_week:
        	print ndate
        	print c['name']

#print cards[0]

print cards[0]['due']


# call the program as `listtasks.py api_key shared_secret [optional: token]`
# get those parameters from http://www.rememberthemilk.com/services/api/keys.rtm
api_key = 'b19b027b96334359aec524dc86c2dae7'
shared_secret = '5ae70fe5149cbafc'

#####token = sys.argv[3] if len(sys.argv) >= 4 else None

token = '8d72f9b0316ac225faf1309833c5e5b0068f86e4'
api = Rtm(api_key, shared_secret, "delete", token)
    
# authenication block, see http://www.rememberthemilk.com/services/api/authentication.rtm
# check for valid token
if not api.token_valid():
    # use desktop-type authentication
    url, frob = api.authenticate_desktop()
    # open webbrowser, wait until user authorized application
    webbrowser.open(url)
    raw_input("Continue?")
    # get the token for the frob
    api.retrieve_token(frob)
    # print out new token, should be used to initialize the Rtm object next time
    # (a real application should store the token somewhere)
    print "New token: %s" % api.token

# get all open tasks, see http://www.rememberthemilk.com/services/api/methods/rtm.tasks.getList.rtm
result = api.rtm.tasks.getList(filter="status:incomplete")
for tasklist in result.tasks:
    for taskseries in tasklist:
        print taskseries.task.due, taskseries.name

