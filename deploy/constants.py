from enums.deploy_units import DEPLOY_UNIT
from deploy.classes.DeployUnit import DeployUnit

# pypy is option as well. NOTE: it can be 2x-3x faster
PYTHON_INTERPETATOR = "python"
COMMON_CFG = "common.cfg"

FULL_COMMAND = PYTHON_INTERPETATOR + " -m services.arbitrage_between_pair"

BALANCE_SCREEN_NAME = "Balance_Retrieval"
BALANCE_WINDOW_NAME = "balance_update"
BALANCE_UPDATE_COMMAND = PYTHON_INTERPETATOR + " -m services.balance_monitoring --cfg " + COMMON_CFG 
BALANCE_UPDATE_DEPLOY_UNIT = DeployUnit(BALANCE_SCREEN_NAME, BALANCE_WINDOW_NAME, BALANCE_UPDATE_COMMAND)

COMMON_SCREEN_NAME = "crypto"

ARBITRAGE_NOTIFIER_SCREEN_NAME = COMMON_SCREEN_NAME
ARBITRAGE_NOTIFIER_WINDOW_NAME = "arbitrage_notifier"
ARBITRAGE_NOTIFIER_COMMAND = PYTHON_INTERPETATOR + " -m services.arbitrage_monitoring --cfg " + COMMON_CFG
ARBITRAGE_NOTIFIER_DEPLOY_UNIT = DeployUnit(ARBITRAGE_NOTIFIER_SCREEN_NAME, ARBITRAGE_NOTIFIER_WINDOW_NAME,
                                            ARBITRAGE_NOTIFIER_COMMAND)

ORDER_BOOK_RETRIEVAL_SCREEN_NAME = COMMON_SCREEN_NAME
ORDER_BOOK_RETRIEVAL_WINDOW_NAME = "order_book_retrieval"
ORDER_BOOK_RETRIEVAL_COMMAND = PYTHON_INTERPETATOR + " -m services.order_book_retrieval --cfg " + COMMON_CFG
ORDER_BOOK_RETRIEVAL_DEPLOY_UNIT = DeployUnit(ORDER_BOOK_RETRIEVAL_SCREEN_NAME, ORDER_BOOK_RETRIEVAL_WINDOW_NAME,
                                              ORDER_BOOK_RETRIEVAL_COMMAND)

HISTORY_RETRIEVAL_SCREEN_NAME = COMMON_SCREEN_NAME
HISTORY_RETRIEVAL_WINDOW_NAME = "history_retrieval"
HISTORY_RETRIEVAL_COMMAND = PYTHON_INTERPETATOR + " -m services.history_retrieval --cfg " + COMMON_CFG
HISTORY_RETRIEVAL_DEPLOY_UNIT = DeployUnit(HISTORY_RETRIEVAL_SCREEN_NAME, HISTORY_RETRIEVAL_WINDOW_NAME,
                                           HISTORY_RETRIEVAL_COMMAND)

TELEGRAM_NOTIFIER_SCREEN_NAME = COMMON_SCREEN_NAME
TELEGRAM_NOTIFIER_WINDOW_NAME = "telegram_notifier"
TELEGRAM_NOTIFIER_COMMAND = PYTHON_INTERPETATOR + " -m services.telegram_notifier --cfg " + COMMON_CFG
TELEGRAM_NOTIFIER_DEPLOY_UNIT = DeployUnit(TELEGRAM_NOTIFIER_SCREEN_NAME, TELEGRAM_NOTIFIER_WINDOW_NAME,
                                           TELEGRAM_NOTIFIER_COMMAND)

TRADE_SAVING_SCREEN_NAME = COMMON_SCREEN_NAME
TRADE_SAVING_WINDOW_NAME = "trade_saving"
TRADE_SAVING_COMMAND = PYTHON_INTERPETATOR + " -m services.trade_storing --cfg " + COMMON_CFG
TRADE_SAVING_DEPLOY_UNIT = DeployUnit(TRADE_SAVING_SCREEN_NAME, TRADE_SAVING_WINDOW_NAME, TRADE_SAVING_COMMAND)

EXPIRED_ORDER_PROCESSING_SCREEN_NAME = COMMON_SCREEN_NAME
EXPIRED_ORDER_PROCESSING_WINDOW_NAME = "expired_order_processing"
EXPIRED_ORDER_PROCESSING_COMMAND = PYTHON_INTERPETATOR + " -m services.expired_order_processing --cfg " + COMMON_CFG
EXPIRED_ORDER_PROCESSING_DEPLOY_UNIT = DeployUnit(EXPIRED_ORDER_PROCESSING_SCREEN_NAME,
                                                  EXPIRED_ORDER_PROCESSING_WINDOW_NAME,
                                                  EXPIRED_ORDER_PROCESSING_COMMAND)

FAILED_ORDER_PROCESSING_SCREEN_NAME = COMMON_SCREEN_NAME
FAILED_ORDER_PROCESSING_WINDOW_NAME = "failed_order_processing"
FAILED_ORDER_PROCESSING_COMMAND = PYTHON_INTERPETATOR + " -m services.failed_order_processing --cfg " + COMMON_CFG
FAILED_ORDER_PROCESSING_DEPLOY_UNIT = DeployUnit(FAILED_ORDER_PROCESSING_SCREEN_NAME,
                                                 FAILED_ORDER_PROCESSING_WINDOW_NAME,
                                                 FAILED_ORDER_PROCESSING_COMMAND)


DATA_RETRIEVAL_SERVICES = {
    DEPLOY_UNIT.ARBITRAGE_NOTIFIER: ARBITRAGE_NOTIFIER_DEPLOY_UNIT,
    DEPLOY_UNIT.ORDER_HISTORY: HISTORY_RETRIEVAL_DEPLOY_UNIT,
}
