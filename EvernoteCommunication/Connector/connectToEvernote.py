# Logging
from Logger.Logger import logger

# Import token
from utils.apiRef import token, china, sandbox

# Import Evernote Libraries
from evernote.api.client import EvernoteClient


# Connect to Evernote & get User Store
def connecttoevernote():
    """
    Connects client to Evernote and returns client session
    :return: client
    """
    client = EvernoteClient(token=token, sandbox=sandbox, china=china)
    logger.info("Connected to Evernote")
    return client
