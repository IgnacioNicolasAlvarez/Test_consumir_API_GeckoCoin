import logging

logging.basicConfig(filename='../test_data_dev_per/logs/app.log', filemode='a',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
