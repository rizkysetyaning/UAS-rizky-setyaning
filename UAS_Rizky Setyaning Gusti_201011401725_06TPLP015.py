import matplotlib.pyplot as plt


class BaseFuzzy:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self):
        pass

    def down(self):
        pass


class Pressure(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 50  # Change the maximum value as needed

        self.p1 = 5
        self.p2 = 8
        self.p3 = 15
        self.p4 = 20
        self.p5 = 28
        self.p6 = 30
        self.p7 = 37
        self.p8 = 40
        self.p9 = 47

    def very_low(self, pressure):
        if pressure <= self.p1:
            return 1
        elif pressure <= self.p3:
            return (self.p3 - pressure) / (self.p3 - self.p1)
        else:
            return 0

    def low(self, pressure):
        if pressure <= self.p2:
            return 0
        elif pressure <= self.p4:
            return (pressure - self.p2) / (self.p4 - self.p2)
        else:
            return 0

    def medium(self, pressure):
        if pressure <= self.p3 or pressure > self.p7:
            return 0
        elif pressure <= self.p5:
            return (pressure - self.p3) / (self.p5 - self.p3)
        elif pressure <= self.p6:
            return 1
        elif pressure <= self.p7:
            return (self.p7 - pressure) / (self.p7 - self.p6)
        else:
            return 0

    def high(self, pressure):
        if pressure <= self.p6 or pressure > self.p9:
            return 0
        elif pressure <= self.p8:
            return (pressure - self.p6) / (self.p8 - self.p6)
        elif pressure <= self.p9:
            return 1
        else:
            return 0

    def very_high(self, pressure):
        if pressure <= self.p8:
            return 0
        elif pressure <= self.p9:
            return (pressure - self.p8) / (self.p9 - self.p8)
        else:
            return 0

    def graph(self, ax):
        x = list(range(self.minimum, self.maximum + 1))
        y_low = [self.low(p) for p in x]
        y_medium = [self.medium(p) for p in x]
        y_high = [self.high(p) for p in x]

        ax.plot(x, y_low, label='Low')
        ax.plot(x, y_medium, label='Medium')
        ax.plot(x, y_high, label='High')

        ax.set_xlabel('Pressure')
        ax.set_ylabel('Membership')
        ax.set_title('Pressure Membership Functions')
        ax.legend()
        ax.grid(True)


class Suhu:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self, x):
        return
