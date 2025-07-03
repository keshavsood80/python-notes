from logger import logging

def add(a,b):
    logging.debug('The addition operation is taking place')
    return a+b

logging.debug('The addition function is called')
add(10,15)

# go to terminal
# type cd 12. Logging
# type cd logs
# type python test.py

# It will not display
# go to app.log file , you can see log is created and you can see add operation is taking place.