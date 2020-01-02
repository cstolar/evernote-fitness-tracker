# Logger
from Logger.Logger import logger

# Utils
from utils.apiRef import token

# Evernote
from evernote.api.client import EvernoteClient


def getnoteid(result_list, searchTerm):
    """

    :type searchTerm: basestring
    """
    for note in result_list.notes:
        if note.title == searchTerm:
            logger.info("Found Note: %s" % note.guid)
            return note.guid


def getnotecontent(result_list, searchterm, notestore):
    """
    Returns the content of the Note
    :param result_list:
    :param searchterm:
    :param notestore:
    :return:
    """
    noteid = getnoteid(result_list, searchterm)
    logger.info("Got Note Content for Search Term: %s" % searchterm)
    return notestore.getNoteContent(token, noteid)
