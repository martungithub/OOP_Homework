from datetime import datetime


class Cell:
    def __init__(self, value="", red=0, blue=0, green=0):
        self.value = value
        self.color = {'red': red, 'blue': blue, 'green': green}

    def set_value(self, value):
        self.value = value

    def set_color(self, red, blue, green):
        if red >= 0 and blue >= 0 and green >= 0 and isinstance(red, int) and isinstance(blue, int) and isinstance(
                green, int):
            self.color = {'red': red, 'blue': blue, 'green': green}
        else:
            raise Exception("Value error! (0 - 255)")

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

    def to_int(self):
        if isinstance(int(self.value), int):
            return int(self.value)
        return f"You can not convert {type(self.value)} to int!"

    def to_double(self):
        if isinstance(int(self.value), float):
            return int(self.value)
        return f"You can not convert {type(self.value)} to float!"

    def to_date(self):

        date_format = "%Y-%m-%d"

        try:
            date = datetime.strptime(self.value, date_format)
            return date

        except ValueError:
            print("The value cannot be converted to a date.")

    def reset(self):
        self.value = ""
        self.color = {'red': 0, 'blue': 0, 'green': 0}
