#!/usr/bin/python3
from sense_hat import SenseHat
import sys
import getopt

if __name__ == '__main__':

    x = 0
    y = 0
    color = ()
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "x:y:c:")
    except getopt.GetoptError as err:
        print (err)
        sys.exit (1)

    if not opts:
        print('select -x (0-7) -y (0-7) -c R,G,B')
        sys.exit(1)
    else:
        for opt, arg in opts :
                if '-x' in opt:

                    if int(arg) in range(0,7):
                        x = int(arg)
                    else:
                        print("wrong argument")
                        sys.exit(1)
                elif '-y' in opt:

                    if int(arg) in range(0,7):
                        y = int(arg)
                    else:
                        print("wrong argument")
                        sys.exit(1)
                elif '-c' in opt:
                    if arg == 'R':
                        color = red
                    elif arg == 'G':
                        color = green
                    elif arg == 'B':
                        color = blue
                    else:
                        print("wrong argument color")
                        sys.exit(1)

        sense = SenseHat()
        sense.set_pixel(x,y,color)
