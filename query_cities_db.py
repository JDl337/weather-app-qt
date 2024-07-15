import sqlite3

class CitiesDB:
    def __init__(self, dbname="cities.db"):
        self.dbname = dbname
        self.con = None

    def query_cityname(self, cityname):
        cur = self.con.cursor()
        res = cur.execute("""SELECT name, latitude, longitude
                            FROM cities WHERE name=?""", (cityname,))

        return res.fetchone()

    def query_alternatenames(self, cityname):
        formatted_name = "%,{},%".format(cityname)
        cur = self.con.cursor()
        res = cur.execute("""SELECT name, latitude, longitude
                            FROM cities WHERE alternatenames LIKE ?""", (formatted_name,))
        
        return res.fetchone()

    def query(self, cityname):
        formatted_name = "%,{},%".format(cityname)
        cur = self.con.cursor()
        res = cur.execute("""SELECT name, latitude, longitude
                            FROM cities WHERE name=? OR alternatenames LIKE ?""", (cityname, formatted_name))
        
        return res.fetchone()
    
    def query_with_tz(self, cityname):
        formatted_name = "%,{},%".format(cityname)
        cur = self.con.cursor()
        res = cur.execute("""SELECT name, latitude, longitude, timezone
                            FROM cities WHERE name=? OR alternatenames LIKE ?""", (cityname, formatted_name))
        
        return res.fetchone()

    def __enter__(self):
        self.con = sqlite3.connect(self.dbname)

        # the return value of enter is assigned to the name given in the with stmnt
        # with constructor() as *name*
        return self

    # called at the end of with block or in case of an exception
    def __exit__(self, exc_type, exc_value, traceback):
        self.con.close()
        
        # exit method returns true if the exception was handled
        # if it returns false then the exception is rethrown by the with statement
        # default is false
        # return True

if __name__ == "__main__":        
    with CitiesDB("cities.db") as db:
        # below exception will be passed to __exit__
        # raise Exception("Error!")
        print(db.query_cityname("New York"))
        print(db.query("New York"))
