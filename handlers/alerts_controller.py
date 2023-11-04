import tzevaadom # kudos to https://github.com/itaiguli/python-pikudHaoref-api

from handlers.windows_controller import WindowsController 


class AlertsController:
    def __init__(self, areas_of_interest) -> None:
        self.areas_of_interest = areas_of_interest
        self.windows_controller = WindowsController()

    def handle(self):
        """A wrapper for listening to alerts

        Args:
            areas (list): the Areas to be alerted about
        """
        tzevaadom.alerts_listener(self._handle_incoming_alert, self.areas_of_interest)
        


    def _handle_incoming_alert(self, list_alerts):
        """Handles an alert being activated

        Args:
            list_alerts (List): a list of the incoming alerts
        """
        self.windows_controller.handle()
        for alert in list_alerts:
            message = "New Alarm: " + \
                alert["name_en"] + ". Zone: " + alert["zone_en"]
            print(message)
