import logging

def setup_logger(log_file_name = 'OT_process.log'):
    """Function enables logging"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    log_format = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

    file_handler = logging.FileHandler(log_file_name)

    file_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    logger.info('Running {}'.format(__name__))