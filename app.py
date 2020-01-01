# Initialize Evernote
from evernoteCommunication.connector.connectEvernote import connecttoevernote
from evernoteCommunication.versionchecker.checkVersion import versionchecker

user_store = connecttoevernote()
versionchecker(user_store)