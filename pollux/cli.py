import os, sys
import typer
from pollux.inputer import *
from pollux.license import license_setup, license_text

app = typer.Typer()
types = ['pip', 'tex', 'github']


@app.command()
def pip(act: str, name: str):
    _act = act.lower()
    if _act == 'init':
        # init directory
        pwd = sys.path[0]
        if not os.listdir(pwd):
            res = input("Current dir is not empty! Continue? [y/N]").lower()
            if res == 'y':
                # clean all file and continue
                pass
            else:
                pass


def _general():
    """
    Added README.md and .gitignore file
    :return:
    """
