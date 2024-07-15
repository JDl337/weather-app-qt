from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
import re

from weatherUi import Ui_MainWindow

import api_helpers
from description_parse import DescriptionReader
from query_cities_db import CitiesDB

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.locationSubmit.clicked.connect(self.on_submit)
        self.setWindowTitle("Weather App")

    def on_submit(self):
        inp = self.ui.locationInput.text()
        try:
            # validating input, getting result from db to ensure the location exists
            self.validate_input(inp)
            res = self.query_db(inp.strip())
            self.validate_result(res)
        
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

        else:
            self.update_location(res)
            try:
                api_res = api_helpers.get_api_response(res[1], res[2], res[3])
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
                return
            
            self.update_current(api_helpers.get_current_weather(api_res),
                                api_helpers.get_units(api_res))
            self.update_daily(api_helpers.get_today_weather(api_res),
                              api_helpers.get_units(api_res, "daily"))

            self.update_description(api_helpers.get_weather_code(api_res),
                                    api_helpers.get_string_time_of_day(api_res))

    def validate_input(self, inp):
        validation_regex = re.compile(r'^[a-zA-Z\s]*$')
        if (inp.strip() == ""):
            raise Exception("Enter a name")
        
        if (not validation_regex.match(inp)):
            raise Exception("Only letters allowed in input")

    def validate_result(self, res):
        if (res == None):
            raise Exception("Location unknown")

    def query_db(self, city):
        with CitiesDB() as db:
            return db.query_with_tz(city)

    def update_location(self, details):
     
        locationLabel = self.ui.location
        latitudeLabel = self.ui.latitude
        longitudeLabel = self.ui.longitude

        locationLabel.setText(details[0])
        latitudeLabel.setText(details[1])
        longitudeLabel.setText(details[2])

    def update_current(self, details, units):
        self.ui.temp.setText("{} {}".format(details["temperature_2m"],
                                            units["temperature_2m"]))
        self.ui.humidity.setText("{} {}".format(details["relative_humidity_2m"],
                                                units["relative_humidity_2m"]))
        self.ui.feelslike.setText("{} {}".format(details["apparent_temperature"],
                                                 units["apparent_temperature"]))
        self.ui.precip.setText("{} {}".format(details["precipitation"],
                                              units["precipitation"]))
        self.ui.pressure.setText("{} {}".format(details["surface_pressure"],
                                                units["surface_pressure"]))
        self.ui.windspeed.setText("{} {}".format(details["wind_speed_10m"],
                                                units["wind_speed_10m"]))

    def update_daily(self, details, units):
        self.ui.sunrise.setText(self.trim_date(details['sunrise']))
        self.ui.sunset.setText(self.trim_date(details['sunset']))
        self.ui.mintemp.setText("{} {}".format(details["temperature_2m_min"],
                                               units["temperature_2m_min"]))
        self.ui.maxtemp.setText("{} {}".format(details["temperature_2m_max"],
                                               units["temperature_2m_max"]))
        self.ui.uvmax.setText("{}".format(details["uv_index_max"]))

    def trim_date(self, date):
        i = date.index('T')
        return date[i+1:]

    def update_description(self, code, time_of_day="day"):
        self.ui.dayornight.setText(time_of_day.title())
        dr = DescriptionReader()
        desc = dr.describe_code(code, time_of_day)
        if (not desc):
            return
        self.ui.description.setText(desc)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
