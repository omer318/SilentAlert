import os
import webbrowser

from config import ALERT_HTML_PATH
from keyboard import press_and_release


class WindowsController:
    def handle(self):
        """opens the alert window
        """
        self._minimize_all()
        self._open_web_window(ALERT_HTML_PATH)

    @staticmethod
    def _open_web_window(filename):
        """Opens a file in the default browser

        Args:
            filename (string): the path of the file 
        """

        print("opens web window")
        webbrowser.open('file://' + os.path.realpath(filename))

    @staticmethod
    def _minimize_all():
        """Minimizes all the other windows open on the PC
        """
        print("minimizing all windows")
        press_and_release('windows+d')
