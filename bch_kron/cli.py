#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
# ]
# ///

import sys
from pathlib import Path
from typing import List
from typing_extensions import Annotated

import typer

import bch_kron.lib.ui as UI

app = typer.Typer()

@app.command()
def at( time, cmd: List[str] ):
    UI.do_at( time, ' '.join(cmd) )

@app.command()
def serve():
    UI.do_serve()

@app.command()
def clear():
    UI.do_clearscripts()

@app.command()
def alarm():
    UI.do_alarm()

@app.command()
def codes():
    UI.do_codes()

@app.command()
def answer(code):
    UI.do_answer(code)

@app.command()
def matches(target):
    UI.do_matches(target)

cli=app
if __name__ == '__main__':
    app()
