import webbrowser
import os


def open_alert_window(filename):
    webbrowser.open('file://' + os.path.realpath(filename))

def main():
    open_alert_window('./index.html')

if __name__ == "__main__":
    main()