import logging



def setup_logging(level=logging.ERROR, arquivo=None):
    handlers = [logging.StreamHandler()]

    if arquivo:
        handlers.append(logging.FileHandler(arquivo, encoding="utf-8"))

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=handlers,
    )