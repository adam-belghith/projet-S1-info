import sqlite3
import time
import asyncio


class Sensor:
    async def do_something(self):
        """ Do something with the sensors, e.g., get data

        Args:
            input_data (str, optional): . Defaults to "".
        """
        i = 0
        while i < 20:
            await asyncio.sleep(5)
            print("sensor")
            self.write_data(str(i))
            i += 1
        return 0
        
    def write_data(self, input_data = ""):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO MyTable (some_data) VALUES (?)",(input_data,) )
        conn.commit()
        conn.close()
        
    def query_data(self):
        conn = sqlite3.connect('database.db')
        
        res = conn.execute ( "SELECT * FROM MyTable" )
        txt = res.fetchall()
        conn.close()
        return txt
