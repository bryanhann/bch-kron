#!/usr/bin/env python3

import sys
import os
import time
import datetime

from bch_kron.lib.constants import ENV
from bch_kron.lib.codes import codes

BACKSPACES = '\b' * 50
SPACE = ' '
COMMA = '.'
PIPE = '|'

def lfilter(*a,**b):    return list(filter(*a,*b))
def code4hhmm(hhmm):    return codes.get(hhmm, 'xxx')

def err(msg):       sys.stderr.write(msg); sys.stderr.flush()
def backerr(msg):   err( BACKSPACES + msg )
def announce(*a):   print(a); say(*a)
def say(*args):     os.system( f'say {SPACE.join(args)}' )
def now():          return datetime.datetime.now()
def dd4int(n):      return str(100+n)[-2:]
def hhmm4h4m(h,m):  return f"{dd4int(h)}:{dd4int(m)}"
def dd4int(x):      return str(x+100)[-2:]
def int4dd(dd):     return int(f"1{dd}")-100
def hhmm4dt(dt):    return dt.strftime('%H:%M')
def hhmmss4dt(dt):  return dt.strftime('%H:%M:%S')
def code4dt(dt):    return code4hhmm(hhmm4dt(dt))

def phones4dt(dt):
    hh, mm = hhmm4dt(dt).split(':')
    return f"{hh} {mm} {COMMA}"

def msloop(sec=1):
    factor = 1000
    while True:
        for ii in range(int(sec*factor)):
            yield ii
            time.sleep(1/factor)

#def file_remove(file): file.exists() and file.unlink()
