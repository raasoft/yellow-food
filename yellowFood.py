# b730b6c72f876470a8c4cbf5ebe41dc0

from trello import TrelloApi

TRELLO_APP_KEY='b730b6c72f876470a8c4cbf5ebe41dc0'

trello=TrelloApi(TRELLO_APP_KEY)

user_token=trello.get_token_url('YellowFood', expires='30days', write_access=True) 
#   'https://trello.com/1/authorize?key='+TRELLO_APP_KEY+'&name=My+App&expiration=30days&response_type=token&scope=read,write'

trello.set_token(user_token)

trello.boards.list(TRELLO_APP_KEY, )
trello.boards.get('Yellow Meal Planning Board')
