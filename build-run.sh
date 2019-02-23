#!/bin/sh

gcc -shared -o test.so test.c
./test.py

