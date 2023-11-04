from handlers.alerts_controller import AlertsController
from config import AREAS

def main():
    alerts_controller = AlertsController(AREAS)
    alerts_controller.handle()


if __name__ == "__main__":
    main()
