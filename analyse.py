import pandas as pd
from matplotlib.pyplot import show, bar

class UserPrompter:
    def __init__(self):
        self.next_type = str
        self.repeat = False
        self.accept_falsy = True

    def expect(self, next_type: type, /, *, repeat: bool = None, accept_falsy: bool = None):
        self.next_type = next_type
        self.repeat = repeat or self.repeat
        self.accept_falsy = accept_falsy or self.accept_falsy

    def poll(self, prompt: str = ""):
        while True:
            inp = input(prompt)

            try:
                ret = self.next_type(inp)
            except (TypeError, ValueError):
                if self.repeat:
                    print("Invalid Input!")
                    continue
                else:
                    raise
            else:
                if not self.accept_falsy and not ret:
                    print("Falsy/Empty Input not accepted! Try another value")
                    continue

                return ret

def main():
    p = UserPrompter()
    df = pd.read_csv("ret.txt", sep=" ", names=["offset", "val"], header=None)
    df["val"] = df["val"] / df["offset"]

    p.expect(int, repeat=True)

    x = p.poll("Filtering constant")

    if x > 0:
        df = df.loc[df["val"] == (x * df["offset"])]

    df.sort_values(by=["val"], inplace=True)

    # df.plot.bar(y="val", align="edge", width=1)
    # df.plot.bar(y="offset", align="edge", width=1)
    bar(df["offset"], df["val"], width=1, align="edge")
    show()

if __name__ == "__main__":
    main()