from trello import TrelloApi
import json

TRELLO_APP_KEY='b730b6c72f876470a8c4cbf5ebe41dc0'

trello=TrelloApi(TRELLO_APP_KEY)

print trello.get_token_url('YellowFood', expires='90days', write_access=True) 

user_token='cbecb81059cebb2d026afa70977c99834a51b4c53343f4cbc280a0ad69549943'

trello.set_token(user_token)

boards = trello.boards.get('5a0068aabd9f13a3c7e28b7e')

print boards['name']
print boards['labelNames']

lists = trello.boards.get_list('5a0068aabd9f13a3c7e28b7e')
cards = trello.boards.get_card('5a0068aabd9f13a3c7e28b7e')


for l in lists:
    print l['name']


for c in cards:
    print c['name']
    print c['due']

print cards[0]

print cards[0]['due']

