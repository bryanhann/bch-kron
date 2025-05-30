#!/usr/bin/env python3

import os
from pathlib import Path

from bch_kron.lib.constants import ENV

CROND = ENV.d_CROND
NEWLINE = '\n'

def scripts4dt(dt):  return [x for x in scripts() if dt.strftime('%H:%M:%S').startswith(x.name)]
def matching_dt(dt): return [x for x in scripts() if dt.strftime('%H:%M:%S').startswith(x.name)]
def scripts():       return sorted(list(CROND.glob('*')))
def text4script(s):  return s.exists() and s.read_text() or ''
#def do_answer(code): script4answer(code).touch()
def answers():       return filter( None,  map( answer4script, scripts() ))
#def matching_answers(target): return target in answers()
def script4answer(a): return CROND/f'answer.{a}'
def answer4script(s): return s.name.startswith('answer.') and s.name.split('.')[1]
def append4script4txt(s, txt): s.write_text(text4script(s)+txt)
def do_at(time,cmd): append4script4txt( CROND/time, cmd + NEWLINE )
