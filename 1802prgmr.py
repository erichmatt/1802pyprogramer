import pyb
from pyb import *
import os

program = None

with open("out.bin", "rb") as f:
    program = f
