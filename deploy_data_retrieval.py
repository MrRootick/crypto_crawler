from deploy.constants import DATA_RETRIEVAL_SERVICES, TELEGRAM_NOTIFIER_DEPLOY_UNIT

from debug_utils import print_to_console, LOG_ALL_ERRORS
from utils.time_utils import sleep_for

from deploy.service_utils import deploy_telegram_notifier, deploy_process_in_screen


if __name__ == "__main__":
    screen_name = TELEGRAM_NOTIFIER_DEPLOY_UNIT.screen_name

    deploy_telegram_notifier(screen_name, should_create_screen=True)
    sleep_for(3)

    print_to_console("2 stage - init data retrieval services...", LOG_ALL_ERRORS)
    for deploy_unit in DATA_RETRIEVAL_SERVICES.values():
        deploy_process_in_screen(screen_name, deploy_unit)