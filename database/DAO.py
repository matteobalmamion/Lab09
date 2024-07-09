from database.DB_connect import DBConnect
from model.aereoporto import Aereoporto
from model.volo import Volo


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()
        result={}
        cursor=conn.cursor(dictionary=True)
        query = "SELECT * FROM flights"
        cursor.execute(query)
        for row in cursor:
            flight=Volo(row["ID"], row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["DISTANCE"])
            if (flight.start, flight.arrive) in result:
                result[(flight.start, flight.arrive)].append(flight)
            else:
                result[(flight.start, flight.arrive)] = [flight]
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)
        for row in cursor:
            result[row["ID"]]=Aereoporto(row["ID"], row["AIRPORT"], row["CITY"], row["COUNTRY"])
        cursor.close()
        conn.close()
        return result