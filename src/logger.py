# ..)Inn thousand lines of code , which a are witten in diffrent files such as data igestion ,transformation and in al files it is diffivult to finf exception and errrors in complet pipeile flow we will log the all exception in logger so w can easly check in which files the error is accuring .

# creatiing logging.
import os 
import sys
import logging

# .)To add info of dattime of error import dattime a and add in logg exception .
from datetime import datetime

# .0The blw .log is extension
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# .0The blw in currentdir logs folder will be created which will store log files .
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# .0The blw will mwek the log directory.
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)
logging.basicConfig(
  filename= LOG_FILE_PATH,
  format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)

# 1st way to create log .
# 2nd way is to call logging is in app.py.
# if __name__ == "__main__":
#   logging.info("Logging started")