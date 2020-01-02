# Logger
from Logger.Logger import logger

from evernote.api.client import EvernoteClient


def notestore(client):
    return client.get_note_store()


def getnotebookid(notestore):
    """
    Takes the client session and returns the GUID of the notebook containing sportsdata
    :param notestore:
    :return: notebook ID
    """
    # TODO Change how the notebooks are being filtered. Someday: get sports notebooks
    notebook_id = notestore.listNotebooks()[0].guid
    logger.info("Found Notebook: %s, Name: %s" % (notebook_id, notestore.listNotebooks()[0].name))
    return notebook_id
