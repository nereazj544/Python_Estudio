import logging

def setup_servidor():
    logging.basicConfig(filename="Python/Sockets_2_asincrono/log/info_servidor.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.debug("[DEBUG]: ")
    logging.info("[INFO]: ")
    logging.warning("[WARNING]: ")
    logging.error("[ERROR]: ")
    logging.critical("[CRITICAL]: ")
    logging.info("Logging setup complete.")

def setup_cliente():
    logging.basicConfig(filename="Python/Sockets_2_asincrono/log/info_cliente.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.debug("[DEBUG]: ")
    logging.info("[INFO]: ")
    logging.warning("[WARNING]: ")
    logging.error("[ERROR]: ")
    logging.critical("[CRITICAL]: ")
    logging.info("Logging setup complete.")
