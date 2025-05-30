#!/usr/bin/env python3

from codes import codes
import datetime
from util import COMMA
from constants import ENV



def dd4int(x): return str(x+100)[-2:]
def int4dd(dd): return int(f"1{dd}")-100
def now(): return datetime.datetime.now()
def hhmm4dt(dt): return dt.strftime('%H:%M')
def hhmmss4dt(dt): return dt.strftime('%H:%M:%S')
def code4hhmm(hhmm):
    try:
        return codes[hhmm]
    except KeyError:
        return 'xxx'
def code4dt(dt): return code4hhmm(hhmm4dt(dt))
def phones4dt(dt):
    hhmm=hhmm4dt(dt)
    hh, mm = hhmm.split(':')
    return f"{hh} {mm} {COMMA}"


