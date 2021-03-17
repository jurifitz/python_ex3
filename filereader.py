def file(path):
    precip = []
    f = open(path, "r")
    for line in f:
        precip.append(line[26:30])
    return precip