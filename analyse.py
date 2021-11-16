import pandas as pd
from matplotlib.pyplot import show

df = pd.read_csv("data.txt", sep=" ", names=["offset", "val"], header=None)

if __name__ == "__main__":
    df.sort_values(by=["val"], inplace=True)

    # df.plot.bar(y="val", align="edge", width=1)
    df.plot.bar(y="offset", align="edge", width=1)
    show()