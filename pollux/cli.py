import os, sys
import typer
from pollux.inputer import *
from pollux.license import license_setup, license_text

app = typer.Typer()
types = ['pip', 'tex', 'github']


@app.command()
def init(t: str):
    """
    Init current path as a T type project
    T can be tex, dl
    dl for deep learning
    """


def _general():
    """
    Added README.md and .gitignore file
    :return:
    """
