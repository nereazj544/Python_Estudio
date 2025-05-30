import logging

def Setup_servidor():
    logging.basicConfig(filename="Python/Sockets_2_asincrono/log/info_servidor.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_cliente():
    logging.basicConfig(filename="Python/Sockets_2_asincrono/log/info_cliente.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def server_log(message):
    Setup_servidor()
    logging.info(f"[SERVER]: {message}")

def client_log(message):
    setup_cliente()
    logging.info(f"[CLIENT]: {message}")


def server_error(message):
    Setup_servidor()
    logging.error(f"[SERVER]: {message}")

def client_error(message):
    setup_cliente()
    logging.error(f"[CLIENT]: {message}")

def server_warning(message):
    Setup_servidor()
    logging.warning(f"[SERVER]: {message}")

def client_warning(message):
    setup_cliente()
    logging.warning(f"[CLIENT]: {message}")


def server_debug(message):
    Setup_servidor()
    logging.debug(f"[SERVER]: {message}")

def client_debug(message):
    setup_cliente()
    logging.debug(f"[CLIENT]: {message}")

def server_critical(message):
    Setup_servidor()
    logging.critical(f"[SERVER]: {message}")

def client_critical(message):
    setup_cliente()
    logging.critical(f"[CLIENT]: {message}")