import pygetwindow as gw
from typing import List



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
        

        



