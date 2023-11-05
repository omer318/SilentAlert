import time
from datetime import datetime

import requests
from config import PROBE_PERIOD, TIME_BETWEEN_LOGS
from handlers.windows_controller import WindowsController


class AlertsController:
    def __init__(self, areas_of_interest) -> None:
        requests.packages.urllib3.disable_warnings()
        self.areas_of_interest = areas_of_interest
        self.windows_controller = WindowsController()
        self.counter = 0

    def handle(self):
        """A wrapper for listening to alerts

        Args:
            areas (list): the Areas to be alerted about
        """
        print(f"Listening for alerts in {self.areas_of_interest}")
        self._alerts_listener()

    def _handle_incoming_alert(self, list_alerts):
        """Handles an alert being activated

        Args:
            list_alerts (List): a list of the incoming alerts
        """
        self.windows_controller.handle()
        for alert in list_alerts:
            message = "New Alert: " + alert["name_en"] + ". Zone: " + alert["zone_en"]
            print(message)

    def _alerts_listener(self):
        while True:
            response = requests.get(
                "http://api.tzevaadom.co.il/notifications", verify=False
            )
            red_cases = response.json()

            if red_cases:
                print(red_cases)
                if self._check_if_area_of_interest(red_cases):
                    self._handle_incoming_alert(red_cases)
            self._handle_cycle()

    def _handle_cycle(self):
        if self.counter == TIME_BETWEEN_LOGS:
            print(f"No Alerts found {datetime.now()}")
        time.sleep(PROBE_PERIOD)  # important for not crashing
        self.counter = self.counter % TIME_BETWEEN_LOGS + PROBE_PERIOD

    def _check_if_area_of_interest(self, alerts_dict):
        for alert in alerts_dict:
            if not set(self.areas_of_interest).isdisjoint(alert["cities"]):
                print(alert["cities"])
                return True
        return False
