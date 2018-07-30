import logging
import logging.handlers

formatter = logging.Formatter("%(asctime)s | PID:%(process)d -> %(funcName)s at %(filename)s:%(lineno)d | %(levelname)s: %(message)s")

handler_to_terminal = logging.StreamHandler()
handler_to_terminal.setLevel(logging.INFO)
handler_to_terminal.setFormatter(formatter)


handler_to_file = logging.handlers.TimedRotatingFileHandler("./logs/lily.log", when="D", backupCount=7)
handler_to_file.setLevel(logging.INFO)
handler_to_file.setFormatter(formatter)


logger = logging.getLogger()
logger.addHandler(handler_to_terminal)
logger.addHandler(handler_to_file)

logger.setLevel(logging.INFO)