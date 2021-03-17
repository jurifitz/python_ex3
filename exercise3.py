import numpy
import filereader

precipi = filereader.file() ##insert file path
mydata = numpy.array(precipi[1:]).astype(numpy.float)
print(f"Minimal precipitation: {mydata.min()}")
print(f"Maximal precipitation: {mydata.max()}")
print(f"Mean precipitation: {mydata.mean()}")
