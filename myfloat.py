# -*- coding: utf-8 -*-
import os
import sys
import fcntl
import logging

# logfile and format
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/var/log/float.log',
                filemode='a+')

# usage info
USAGE = "Usage: # python myfloat.py /path/to/float.file"

# return the count and sum of floats in one line
def count_and_sum_line(line):
    lcnt = 0
    lsum = 0.0
    try:
        strings = line.split()
        for string in strings:
            try:
                num = float(string)
                logging.debug("Float: {0}".format(num))
                lcnt += 1
                lsum += num
            except(ValueError):
                logging.exception("String {0} is NOT float".format(string))
    except:
        logging.exception("Any Line Error")

    return (lcnt, lsum)

# return the count and sum of floats in one readable file 
def count_and_sum(file_path):
    try:
        with open(file_path) as file_obj:
            fcnt = 0
            fsum = 0.0

            fcntl.flock(file_obj, fcntl.LOCK_EX) # lock first
            for line in file_obj:
                lcnt, lsum = count_and_sum_line(line)
                logging.debug("{0} floats whose sum = {1} in Line: {2}"
                        .format(lcnt, lsum, line))
                fcnt += lcnt
                fsum += lsum

            fcntl.flock(file_obj, fcntl.LOCK_UN) # unlock

            logging.info("{0} floats in File {1}, whose sum is {2}"
                    .format(fcnt, file_path, fsum))
            return (fcnt, fsum)

    except:
        logging.exception("Any File Error")
        return (0, 0.0)

def main(args):

    if len(args) < 2:
        # at least one parameter
        print USAGE
        return None

    file_path = args[1]
    logging.debug("Input file path: {0}".format(file_path))

    # check if file_path is a readable file
    if not os.path.isfile(file_path):
        logging.error("file {0} is NOT a readable file".format(file_path))
        print ("file {0} is NOT a readable file".format(file_path))
        return None

    (fcnt, fsum) = count_and_sum(file_path)
    print ("{0} floats in File {1}, whose sum is {2}".format(fcnt, file_path, fsum))
    return

if __name__ == '__main__':
    main(sys.argv)
