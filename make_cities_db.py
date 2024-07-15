import numpy as np
import pandas as pd
import sqlite3

colnames = ["geonameid", "name", "asciiname",
            "alternatenames", "latitude", "longitude",
            "featureclass", "featurecode", "countrycode",
            "cc2", "admin1", "admin2", "admin3", "admin4",
            "population", "elevation", "dem", "timezone",
            "modification_date"]

cities_frame = pd.read_csv("cities15000.txt",names=colnames, dtype=str, sep='\t')

con = sqlite3.connect('cities.db')

cities_frame.to_sql("cities", con)

con.commit()
con.close()
