from database.DB_connect import DBConnect
from model.state import State


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
    def getAllNodes(provider):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct Location 
            from nyc_wifi_hotspot_locations nwhl 
            where Provider = %s
        """
        cursor.execute(query, (provider, ))
        result = []
        for row in cursor:
            result.append(row["Location"])
        cursor.close()
        conn.close()
        return result
