# Alan Arellano <root@solucioneslibres.com> 2015
# Some code and ideas used to build this script extracted from:
# http://doc.qt.io
# http://stackoverflow.com/a/29260064/2026769
# http://stackoverflow.com/a/3393759/2026769
# http://stackoverflow.com/a/769221/2026769
# http://stackoverflow.com/a/29260865/2026769

import sys, time, os, threading
from PyQt5.QtWidgets import QApplication


class Screenshot(threading.Thread):
    def __init__(self,iteration,tag,data_dir):
        threading.Thread.__init__(self)
        self.iteration = iteration
        self.tag = tag
        self.data_dir = data_dir

        self.directory = None
        self.app = QApplication(sys.argv)

    def run(self):
        if self.tag is not None:
            self.directory = os.path.join(os.path.expanduser(self.data_dir),self.tag)
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        else:
            self.directory = os.path.expanduser(self.data_dir)

        self.screenshot()

    def screenshot(self):
        threading.Timer(self.iteration, self.screenshot).start()
        currenttime = str(int(time.time()))

        self.app.primaryScreen().grabWindow(self.app.desktop().winId()).save(os.path.join(self.directory,currenttime+'.png'), 'png')
        print "Screenshot saved to "+ os.path.join(self.directory,currenttime+".png")