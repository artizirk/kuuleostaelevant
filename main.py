#!/usr/bin/env python3
###########################################################################
#                          Kuule osta elevant ära                         #
#                                                                         #
#                                                                         #
#Author:  Arti Zirk <arti.zirk@gmail.com                                  #
#License: Do What the Fuck You Want to Public License                     #
#                                                                         #
###########################################################################

print("> Kuule osta elevant ära!")
while True:
    try:
        vastus = input("< ").lower()
        print("> Seda räägivad kõik, et " + vastus + " aga osta elevant ära!")
    except (EOFError, KeyboardInterrupt) as e:
        print("\033[4D> Mis sul viga on, et elevanti ei taha ??")
        exit()
    except:
        print("Error, mingine kala ujus sisse")
        exit()
