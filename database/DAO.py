from database.DB_connect import DBConnect
from model.location import Location


class DAO():
    @staticmethod
    def getAllProviders():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct Provider  
            from nyc_wifi_hotspot_locations nwhl 
            order by Provider asc 
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["Provider"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllLocation(provider):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select Location, avg(Latitude) as Latitude , avg(Longitude) as Longitude 
            from nyc_wifi_hotspot_locations nwhl 
            where Provider = %s
            group by Location
        """
        cursor.execute(query, (provider, ))
        result = []
        for row in cursor:
            result.append(Location(**row))
        cursor.close()
        conn.close()
        return result
