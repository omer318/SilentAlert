import webbrowser
import os
import tzevaadom  # kudos to https://github.com/itaiguli/python-pikudHaoref-api
import keyboard

AREAS = ["ראשון לציון - מזרח", "תעשיון צריפין"]
ALERT_HTML_PATH = './index.html'

def alerts_handler(list_alerts):
    for alert in list_alerts:

        message = "New Alarm: " + \
            alert["name_en"] + ". Zone: " + alert["zone_en"]
        print(message)


def open_web_window(filename):
    webbrowser.open('file://' + os.path.realpath(filename))

def open_alert_window():    
        open_web_window(ALERT_HTML_PATH)

def minimize_all():
    keyboard.press_and_release('windows+d')


def listen_on_alerts(areas):
    tzevaadom.alerts_listener(alerts_handler, areas)


def main():
    #listen_on_alerts(AREAS)
    minimize_all()
    open_alert_window()


if __name__ == "__main__":
    main()
