#!/usr/bin/env python2.7
# coding:utf-8
""""""

import os
import pyinotify

class WatchHandler(pyinotify.ProcessEvent):
    
    def process_IN_access(self, event):
        print 'ACCESS event', self.pathjoin(event)
        
    def process_IN_CLOSE_NOWRITE(self, event):
        print 'CLOSE NOWRITE event', self.pathjoin(event)
        
    def process_IN_CLOSE_WRITE(self, event):
        print 'CLOSE WRITE', self.pathjoin(event)
    
    def process_IN_MODIFY(self, event):
        print 'MODIFY', self.pathjoin(event)        
        
    def process_IN_OPEN(self, event):
        print 'OPEN', self.pathjoin(event)
        
    def pathjoin(self, event):
        return os.path.join(event.path, event.name)

def main(rootdir):
    wm = pyinotify.WatchManager()
    # mask = pyinotify.ALL_EVENTS
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY
    wm.add_watch(rootdir, pyinotify.ALL_EVENTS, rec=True)
    eh = WatchHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1])