#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
cmd = ['wc', '-l', 'hightemp.txt']
try:
    res = subprocess.check_call(cmd)
except:
    print "Error."
