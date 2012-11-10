'''
Created on 10.11.2012

@author: jussikin '''

import ConfigParser
import os

CONFIG_FILE="workdays.list"

config=ConfigParser.RawConfigParser()
if(os.path.exists(CONFIG_FILE)):
    config.read(CONFIG_FILE)

def isWorkday(day):
    if(config.has_option("holyday","{day}.{month}".format(day=day.day,month=day.month))):
        return False
    if(config.has_option("holyday","{day}.{month}.{year}".format(day=day.day,month=day.month,year=day.year))):
        return False
    if day.isoweekday()>5 :
        return False
    return True
    
        