import os
import webbrowser
from keyboard import press_and_release
from config import ALERT_HTML_PATH


class WindowsController:
    def handle(self):
        """opens the alert window
        """
        self._minimize_all()
        self._open_web_window(ALERT_HTML_PATH)

    def _open_web_window(self, filename):
        """Opens a file in the default browser

        Args:
            filename (string): the path of the file 
        """
        webbrowser.open('file://' + os.path.realpath(filename))

    def _minimize_all(self):
        """Minimizes all of the other windows open on the PC
        """
        press_and_release('windows+d')
