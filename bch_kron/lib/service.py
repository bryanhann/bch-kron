#!/usr/bin/env python3

import time
import os

from bch_kron.lib.constants import ENV
import bch_kron.lib.scripting as SS
import bch_kron.lib.util as UU
import bch_kron.lib.tools.poison as PP


def serve():
    while PP.poisonpill():
        ENV.f_SERVING.touch()
        poll4dt(UU.now())


def pending4script(script):
    pending = script.parent/f'pending.{script.name}'
    pending.write_text( script.read_text() )
    os.chmod( str(pending), 0o777 )
    script.unlink()
    return pending

def poll4dt(dt):
    UU.backerr('bch.cron time_serve(): ' + dt.strftime('%H:%M:%S'))
    for pending in map(pending4script, SS.scripts4dt(dt)):
        pending_enter(pending)
        os.system( f'{pending}' )
        pending_exit(pending)
        time.sleep(3)

def pending_enter(script): UU.err( f"""
=========={script}
{script.read_text()}
======================================================
""")

def pending_exit(script): UU.err( f"""
======================================================
""")

