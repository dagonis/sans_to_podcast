import logging 
import magic
import os

import eyed3
from eyed3.id3.apple import PCST, PCST_FID, WFED, WFED_FID, TDES, TDES_FID

logging.getLogger(__name__)

def update_file(file_to_update, prefix):
    logging.debug(f"Working on {file_to_update}")
    f = eyed3.load(file_to_update)
    file_name =  file_to_update.split('/')[-1]
    chunk1, chunk2, chunk3 = file_name.split('_')
    new_title = "Day {} Part {}".format(chunk2[0], int(chunk2[1], 16) - 9)
    if PCST_FID not in f.tag.frame_set:
        f.tag.frame_set[PCST_FID] = PCST()
    if WFED_FID not in f.tag.frame_set:
        f.tag.frame_set[WFED_FID] = WFED(u"http://2spooky.space")
    f.tag.title = new_title
    f.tag.album = prefix
    f.tag.save()
    logging.debug(f"Finished work on {file_to_update}")
    return True

