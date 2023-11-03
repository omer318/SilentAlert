import webbrowser
import os
import tzevaadom  # kudos to https://github.com/itaiguli/python-pikudHaoref-api


def alerts_handler(list_alerts):
    for alert in list_alerts:

        message = "New Alarm: " + \
            alert["name_en"] + ". Zone: " + alert["zone_en"]
        print(message)
        open_web_window('./index.html')


def open_web_window(filename):
    webbrowser.open('file://' + os.path.realpath(filename))


def listen_on_alerts(areas):
    tzevaadom.alerts_listener(alerts_handler,areas)


def main():
    listen_on_alerts([])


if __name__ == "__main__":
    main()
