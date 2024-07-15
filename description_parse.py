import json

class DescriptionReader():

    def __init__(self, jsonpath="weather_descriptions.json"):
        with open(jsonpath, "r") as descr:
            self.data = json.load(descr)
    
    def describe_code(self, wmo_code, time_of_day="day"):
        try:
            return self.data[str(wmo_code)][time_of_day]["description"]
        except KeyError:
            return None

    def get_image(self, wmo_code, time_of_day="day"):
        try:
            return self.data[str(wmo_code)][time_of_day]["image"]
        except KeyError:
            return None

if __name__ == "__main__":
    dsr = DescriptionReader()
    print(dsr.describe_code("1"))
    print(dsr.describe_code("1", "night"))
    print(dsr.describe_code("5"))
    print(dsr.get_image("3"))
    print(dsr.get_image("5"))
