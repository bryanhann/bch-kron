#!/usr/bin/env python3

import time
import datetime
import hashlib

from constants import ENV
from codes import codes

import util as UU
import scripting as SC
import tools.poison as PP
import timing as TT


def __do_alarm(msg='deedoo'):
    now = UU.now()
    if ENV.f_ANSWERED.exists():
        ENV.f_ANSWERED.unlink()
    code = TT.code4dt(now)
    for ii in UU.msloop(sec=3):
        PP.poisonpill()
        if ii % 3000 == 0:
            print()
            UU.announce( TT.phones4dt(now), msg)
            print(code)
        if SC.matching_answers(code):
            break
    UU.say('answered'); ENV.f_ANSWERED.touch()

def _print_codes():
    for h in range(24):
        h%4==0 and print()
        acc = []
        for m in range(0,60,5):
            if m%15 == 0:
                acc.append([])
            acc[-1].append( TT.code4hhmm(UU.hhmm4h4m(h,m)))
        acc = [ UU.PIPE.join(x) for x in acc]
        acc = '  '.join(acc)
        print(f"{UU.hhmm4h4m(h,0)}\t{acc}")

