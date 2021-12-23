import logging

logging.basicConfig(filename='../exam-ignacio-alvarez/logs/app.log', filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
