from hmac import compare_digest
from user import User

'''
users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]'''
'''username_mapping = { 'bob': {
        'id': 1,
    'username': 'bob',
    'password': 'asdf'
}   
                    } '''
'''userid_mapping = { 1: {
    'id': 1,
    'username': 'bob',
    'password': 'asdf'
} 
                  }'''


users = [
    User(1, 'bob', 'asdf')
]
                  
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    
    '''if user and user.password == password:'''
    
    if user and compare_digest(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)