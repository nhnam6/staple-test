import logging

logger = logging.getLogger("root")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
