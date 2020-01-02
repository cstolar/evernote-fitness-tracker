# Logging
from Logger.Logger import logger

# Import Evernote
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.constants as UserStoreConstants

def versionchecker(client):
    """
    Checks version of python and evernote api.
    :param client:
    """
    user_store = client.get_user_store()
    version_ok = user_store.checkVersion(
        "Testing",
        UserStoreConstants.EDAM_VERSION_MAJOR,
        UserStoreConstants.EDAM_VERSION_MINOR
    )
    if not version_ok:
        logger.critical("Version requirements not satisfied")
        exit(1)
