#!/usr/bin/env python

ip1 = input("gimme yur IP address, dude!!!")

ip1 = ip1.split(".")

print("{:<12} {:<12} {:<12} {:<12}".format(*ip1))
