import webbrowser
import os
import tzevaadom  # kudos to https://github.com/itaiguli/python-pikudHaoref-api
import keyboard

# Areas to listen for alerts in
AREAS = ["ראשון לציון - מזרח", "תעשיון צריפין"]
ALERT_HTML_PATH = './index.html'  # Path to the alert html file


def alerts_handler(list_alerts):
    """Handles an alert being activated
        it minimizes the windows and opens the alert window

    Args:
        list_alerts (List): a list of the incoming alerts
    """
    minimize_all()
    open_alert_window()
    for alert in list_alerts:

        message = "New Alarm: " + \
            alert["name_en"] + ". Zone: " + alert["zone_en"]
        print(message)


def open_web_window(filename):
    """Opens a file in the default browser

    Args:
        filename (string): the path of the file 
    """
    webbrowser.open('file://' + os.path.realpath(filename))


def open_alert_window():
    """opens the alert window
    """
    open_web_window(ALERT_HTML_PATH)


def minimize_all():
    """Minimizes all of the other windows open on the PC
    """
    keyboard.press_and_release('windows+d')


def listen_on_alerts(areas):
    """A wrapper for listening to alerts

    Args:
        areas (list): the Areas to be alerted about
    """
    tzevaadom.alerts_listener(alerts_handler, areas)


def main():
    listen_on_alerts(AREAS)


if __name__ == "__main__":
    main()
