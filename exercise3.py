import numpy
import filereader

precipi = filereader.file("C:/Users/jfafi/Desktop/Uni/Master/1.Semester/Seminar in Geodatenanalyse und Modellierung/03/precip_data.txt") ##insert file path
mydata = numpy.array(precipi[1:]).astype(float)
print(f"Minimal precipitation: {mydata.min()}")
print(f"Maximal precipitation: {mydata.max()}")
print(f"Mean precipitation: {mydata.mean()}")
