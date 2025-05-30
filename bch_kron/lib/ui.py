#!/usr/bin/env python3

import os

from bch_kron.lib.constants import ENV

import bch_kron.lib.util as UU
import bch_kron.lib.tools.poison as PP
import bch_kron.lib.scripting as SS
import bch_kron.lib.service as SERVICE


def do_matches(target): print(SERVICE.matches(target))
def do_serve():         SERVICE.serve()
def do_at(time, cmd):   SS.do_at(time,cmd)
def do_answer(code):    SS.script4answer(code).touch()
def do_clearscripts():  [s.unlink() for s in SS.scripts]

def do_alarm(msg='deedoo'):
    now = UU.now()
    if ENV.f_ANSWERED.exists():
        ENV.f_ANSWERED.unlink()
    code = UU.code4dt(now)
    for ii in UU.msloop(sec=3):
        PP.poisonpill()
        if ii % 3000 == 0:
            print()
            UU.announce( UU.phones4dt(now), msg)
            print(code)
        if code in SS.answers():
            break
        #if SS.matching_answers(code):
        #    break
    UU.say('answered'); ENV.f_ANSWERED.touch()

def do_codes():
    for h in range(24):
        h%4==0 and print()
        acc = []
        for m in range(0,60,5):
            if m%15 == 0:
                acc.append([])
            acc[-1].append( UU.code4hhmm(UU.hhmm4h4m(h,m)))
        acc = [ UU.PIPE.join(x) for x in acc]
        acc = '  '.join(acc)
        print(f"{UU.hhmm4h4m(h,0)}\t{acc}")

