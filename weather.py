#!/usr/bin/python3
from sense_hat import SenseHat
import sys
import getopt
import json

mmHg = 0.750061673
dF = 33.8
if __name__ == '__main__':

    try :
        opts, args = getopt.getopt(sys.argv[1:], 'p:t:h:')
    except getopt.GetoptError as err :
        print (err)
        sys.exit (1)

    sense = SenseHat()

    if not opts:
        data = json.dumps({"Temperature": "{0:.3f}[C]".format(sense.temp),
         "Humidity": "{0:.3f}[%%]".format(sense.humidity),
          "Pressure": "{0:.3f}[hPa]".format(sense.pressure)})
        print(data)
    else:
        for opt, arg in opts :
            if '-p' in opt:
                if arg == 'hPa':
                    print(json.dumps({"Pressure": "{0:.3f}[hPa]".format(sense.pressure)}))
                elif arg == 'mmHg':
                    print(json.dumps({"Pressure": "{0:.3f}[mmHg]".format(sense.pressure*mmHg)}))
            elif '-t' in opt:
                if arg == 'C':
                    print(json.dumps({"Temperature": "{0:.3f}[C]".format(sense.temp)}))
                elif arg == 'F':
                    print(json.dumps({"Temperature": "{0:.3f}[F]".format(sense.temp*dF)}))
            elif '-h' in opt:
                print(json.dumps({"Humidity": "{0:.3f}[%%]".format(sense.humidity)}))
