# Configure Logging
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w', # means write in this app.log file.
    level= logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )