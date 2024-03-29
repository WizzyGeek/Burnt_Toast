from matplotlib.pyplot import bar, savefig, show
from math import log1p

def reader(fn: str, sep: str = " ") -> tuple[list[int], list[int]]:
    y = [0, 2]
    x = [0, 1]

    with open(fn, "r") as df:
        while True:
            data_ = df.readline()
            if not data_:
                break
            data = data_.split(sep)
            x.append(int(data[0]))
            y.append(int(data[1]))

    return x, y

def log1p_reader(fn: str, sep: str = " ") -> tuple[list[int], list[float]]:
    y = [0, 2]
    x = [0, log1p(1)]

    with open(fn, "r") as df:
        while True:
            data_ = df.readline()
            if not data_:
                break
            data = data_.split(sep)
            x.append(int(data[0]))
            y.append(log1p(int(data[1])))

    return x, y

def delta_reader(fn: str, sep: str = " ") -> tuple[list[int], list[float]]:
    y = [0, 2]
    x = [0, 1]
    last = 2

    with open(fn, "r") as df:
        while True:
            data_ = df.readline()
            if not data_:
                break
            data = data_.split(sep)
            x.append(int(data[0]))
            temp = int(data[1])
            y.append(temp - last)
            last = temp

    return x, y

def greater_reader(fn: str, sep: str = " ") -> tuple[list[int], list[float]]:
    y = [0, 2]
    x = [0, 1]
    last = -1

    with open(fn, "r") as df:
        while True:
            data_ = df.readline()
            if not data_:
                break
            data = data_.split(sep)
            temp = int(data[1])
            if temp >= last:
                x.append(int(data[0]))
                y.append(temp)
                last = temp

    return x, y

if __name__ == "__main__":
    data = reader("ret.txt")
    bar(data[0], data[1], width=1, align="edge")
    savefig("plot.png")
    show()