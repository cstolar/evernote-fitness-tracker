#
# A simple Evernote API demo script that lists all notebooks in the user's
# account and creates a simple test note in the default notebook.
#
# Before running this sample, you must fill in your Evernote developer token.
#
# To run (Unix):
#   export PYTHONPATH=../../lib; python EDAMTest.py
#
import evernote.edam.userstore.constants as UserStoreConstants
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient
import pymysql
from bs4 import BeautifulSoup


db = pymysql.connect("localhost", "py", "test", "fitnesstracker")
cursor = db.cursor()


auth_token = "S=s1:U=95a02:E=176a40703a6:C=16f4c55d478:P=1cd:A=en-devtoken:V=2:H=4d9eb91a60f74da30b14a8d9b678ff4a"

sandbox = True
china = False

client = EvernoteClient(token=auth_token, sandbox=sandbox, china=china)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print("Is my Evernote API version up to date? ", str(version_ok))
print("")
if not version_ok:
    exit(1)

note_store = client.get_note_store()

# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()

print("Found ", len(notebooks), " notebooks:")
for notebook in notebooks:
    print("  * ", notebook.name)
    nGuid = notebook.guid

# Filter Configuration
updated_filter = NoteFilter(order=Types.NoteSortOrder.UPDATED, notebookGuid=nGuid)
offset = 0
max_notes = 10
result_spec = NotesMetadataResultSpec(includeTitle=True, includeCreated=True, includeAttributes=True)
result_list = note_store.findNotesMetadata(auth_token, updated_filter, offset, max_notes, result_spec)
#print(updated_filter)

# Find Training note
for note in result_list.notes:
    #print(note.title, " - ", note.guid, " - ", note.created)
    if note.title == "Training Diary":
        training_guid = note.guid
        break

# Get Training Note content
note_content = note_store.getNoteContent(auth_token, training_guid)

soup = BeautifulSoup(note_content, 'html.parser')
finder = soup.find_all('td')

train_data = {}



for element in finder:
    if element.text == "Date":
        train_data.update({element.text: finder[4].text})
    elif element.text == "Exercise":
        train_data.update({element.text: finder[5].text})
    elif element.text == "Weight":
        train_data.update({element.text: finder[6].text})
    elif element.text == "Reps":
        train_data.update({element.text: finder[7].text})
    else:
        pass

print(train_data.get("Date"))

print("initializing sql push")
sql = "INSERT INTO training_data(idtraining_data, training_date, training_type, training_reps, training_weight) VALUES ('%i', '%s', '%s', '%s', '%s' )" % (3, train_data.get("Date"), train_data.get("Exercise"), train_data.get("Reps"), train_data.get("Weight"))
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print("Pushed to DB")
except:
   # Rollback in case there is any error
   db.rollback()
db.close()


