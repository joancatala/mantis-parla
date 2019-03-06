#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os

def ejecutaScript():
    os.system('/usr/local/bin/python3.6 ./mantis-parla.py')	
    print ("L'script mantis-parla.py refresca cada 60 segons...")
    time.sleep(60)

while True:
    ejecutaScript()
