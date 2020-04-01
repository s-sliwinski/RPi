#!/usr/bin/python3
from sense_hat import SenseHat
import sys
import getopt
import json

if __name__ == '__main__':

    uflag = 0

    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:rpy")
    except getopt.GetoptError as err:
        print (err)
        sys.exit (1)

    for opt, arg in opts :
        if 'u' in opt:
            if 'D' in arg:
                dflag = 0
                break
            elif 'R' in arg:
                dflag = 1
                break
    else:
        print('specify unit by "-u D" or "-u R"')
        sys.exit(1)

    sense = SenseHat()
    sense.set_imu_config(True, True, True)
    for opt, arg in opts :
            if '-r' in opt:
                if dflag:
                    print('R')
                    orientation_rad = sense.get_orientation_radians()
                    print(json.dumps({"roll": "{0:.3f}".format(orientation_rad["roll"])}))
                else:
                    print('D')
                    orientation = sense.get_orientation_degrees()
                    print(json.dumps({"roll": "{0:.3f}".format(orientation["roll"])}))
            elif '-p' in opt:
                if dflag:
                    print('R')
                    orientation_rad = sense.get_orientation_radians()
                    print(json.dumps({"pitch": "{0:.3f}".format(orientation_rad["pitch"])}))
                else:
                    print('D')
                    orientation = sense.get_orientation_degrees()
                    print(json.dumps({"pitch": "{0:.3f}".format(orientation["pitch"])}))
            elif '-y' in opt:
                if dflag:
                    print('R')
                    orientation_rad = sense.get_orientation_radians()
                    print(json.dumps({"yaw": "{0:.3f}".format(orientation_rad["yaw"])}))
                else:
                    print('D')
                    orientation = sense.get_orientation_degrees()
                    print(json.dumps({"yaw": "{0:.3f}".format(orientation["yaw"])}))
