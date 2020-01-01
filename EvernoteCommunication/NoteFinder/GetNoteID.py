# Logger
from Logger.Logger import logger

# Evernote
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
import evernote.edam.type.ttypes as Types

# Utils
import EvernoteCommunication.NoteFinder.utils as util
from utils.apiRef import token


def filternotes(notebook_id, notestore):
    """
    Returns ID of note
    :param notebook_id:
    :param notestore:
    """
    # Build Notefilter Obj
    update_filter = NoteFilter(order=Types.NoteSortOrder.UPDATED, notebookGuid=notebook_id)
    result_spec = NotesMetadataResultSpec(includeTitle=True, includeCreated=True, includeAttributes=True)
    result_list = notestore.findNotesMetadata(token, update_filter, util.offset, util.max_notes, result_spec)

    return result_list
