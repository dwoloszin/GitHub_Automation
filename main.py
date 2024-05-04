import logging
import logging.handlers
import pandas as pd
import os
import sys
import time
import zipfile
import time

import AnatelFiles
import ImportDF
import Csv_zip
import CleanData
import distCalc
import distanceT
import GOOGLE_CREATOR
import timeit
inicioTotal = timeit.default_timer()

#timeexport = time.strftime("%Y%m%d_")
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')
csv_path = os.path.join(script_dir, 'export/'+'AnatelBase'+'.csv')
zip_path = os.path.join(script_dir, 'export/'+'AnatelBase'+'.zip')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

'''
try:
    SOME_SECRET = os.environ["ANATEL_Mosiac"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise
'''

'''
if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Berlin: {temperature}')
'''
if __name__ == "__main__":
    print('OK')
    logger.info('OK')
    #AnatelFiles.download('SP',['GSM', 'WCDMA', 'LTE', 'NR'])
    AnatelFiles.download('SP',['GSM'])


 
        