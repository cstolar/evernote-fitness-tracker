# Import Evernote
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.constants as UserStoreConstants

def versionchecker(user_store):
    """
    Checks version of python and evernote api.
    :param user_store:
    """
    version_ok = user_store.checkVersion(
        "Testing",
        UserStoreConstants.EDAM_VERSION_MAJOR,
        UserStoreConstants.EDAM_VERSION_MINOR
    )
    print("Is my Evernote API version up to date? ", str(version_ok))
    print("")
    if not version_ok:
        exit(1)