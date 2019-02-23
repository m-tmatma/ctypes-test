#!/bin/sh

gcc -fPIC -shared -o test.so test.c
./test.py

