#!/usr/bin/env python3
########################################################################
#                     Kuule osta elevant ära                           #
#                                                                      #
#                                                                      #
# Author:  Arti Zirk <arti.zirk@gmail.com>                              #
# License: Do What the Fuck You Want to Public License                  #
#                                                                      #
########################################################################

import sys

asi = " ".join(sys.argv[1:])
if not asi.strip():  # argumente pole, kasuta vaikimisi asja
    asi = "elevant"


abi = """Kuule osta elevant ära
Kasutus: main.py [asi | -h | --abi]"""
if asi in ("-h", "--abi",):
    print(abi)
    exit(0)

print("> Kuule osta " + asi + " ära!")
while True:
    try:
        vastus = input("< ").lower()
        print("> Seda räägivad kõik, et {} aga osta {} ära!".format(vastus,
                                                                        asi))
    except (EOFError, KeyboardInterrupt) as e:
        print("\033[4D> Mis sul viga on, et " + asi + " ei taha ??")
        exit()
    except:
        print("Error, mingine kala ujus sisse")
        exit()
