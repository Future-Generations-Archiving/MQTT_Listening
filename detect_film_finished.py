import time
import pygetwindow as gw
from typing import List

def notify_complete():
    pass

def photos_open() -> bool:
    titles: List[str] = gw.getAllTitles()
    exists: bool = False
    for title in titles:
        if ".jpg" in title and "Photos" in title:
            exists = True
            break
    return exists

waiting_for_finish: bool = True

while True:
    if waiting_for_finish:
        if photos_open():
            notify_complete()
            waiting_for_finish = False
    else:
        if not photos_open():
            waiting_for_finish = True
    time.sleep(5)


        



