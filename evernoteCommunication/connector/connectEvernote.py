# Import token
from utils.apiRef import token, china, sandbox

# Import Evernote Libraries
from evernote.api.client import EvernoteClient


# Connect to Evernote & get User Store
def connecttoevernote():
    """
    Connects client to Evernote
    :return: User_store
    """
    client = EvernoteClient(token=token, sandbox=sandbox, china=china)
    print("Successfully connected to Evernote")
    return client.get_user_store()
