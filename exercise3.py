##"C:/Users/jfafi/PycharmProjects/python_ex3/precip_data.txt"

import numpy

def filereader(path):
    precip = []
    f = open(path, "r")
    for line in f:
        precip.append(line[26:30])
    return precip

my = numpy.array(xi[1:]).astype(numpy.float)