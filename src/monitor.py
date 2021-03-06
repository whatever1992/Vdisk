#!/usr/bin/env python
#coding=utf-8
import os
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY

wm = WatchManager()
mask = IN_DELETE | IN_CREATE |IN_MODIFY   # watched events

import pynotify

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

 
class PFilePath(ProcessEvent):
    def process_IN_CREATE(self, event):
        print   "Create file: %s " %   os.path.join(event.path, event.name)
        sendmessage("Create file", os.path.join(event.path, event.name))
 
    def process_IN_DELETE(self, event):
        print   "Delete file: %s " %   os.path.join(event.path, event.name)
        sendmessage("Delete file", os.path.join(event.path, event.name))
     
    def process_IN_MODIFY(self, event):
        print   "Modify file: %s " %   os.path.join(event.path, event.name)
        sendmessage("Modify file", os.path.join(event.path, event.name))
     
if __name__ == "__main__":
     
    notifier = Notifier(wm, PFilePath())
    wdd = wm.add_watch('.', mask, rec=True)
 
    while True:
        try :
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break
