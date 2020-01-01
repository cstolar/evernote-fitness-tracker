# Initialize Evernote
from EvernoteCommunication.Connector.connectToEvernote import connecttoevernote
from EvernoteCommunication.VersionChecker.checkVersion import versionchecker
from EvernoteCommunication.NotebookFinder.GetNotebookID import getnotebookid, notestore
from EvernoteCommunication.NoteFinder.GetNoteID import filternotes
from EvernoteCommunication.NoteFinder.FindNote import getnotecontent


# Connect
client = connecttoevernote()

# Check Version
versionchecker(client)

# Get NotebooksID
notestore = notestore(client)
notebook_id = getnotebookid(notestore)

# GetNoteID
note_result_list = filternotes(notebook_id, notestore)

# Filter for needed Note
getnotecontent(note_result_list, "Training Diary", notestore)