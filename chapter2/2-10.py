#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("hightemp.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()
