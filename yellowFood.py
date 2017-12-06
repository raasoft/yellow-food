from trello import TrelloApi
import json

TRELLO_APP_KEY='b730b6c72f876470a8c4cbf5ebe41dc0'

trello=TrelloApi(TRELLO_APP_KEY)

print trello.get_token_url('YellowFood', expires='90days', write_access=True) 

user_token='3632e23297d6255b31eca3bfaf3629c37f2f01c8e6e1f08d3c40d2672448af72'

trello.set_token(user_token)

data = json.loads(trello.boards.get('5a0068aabd9f13a3c7e28b7e'))

