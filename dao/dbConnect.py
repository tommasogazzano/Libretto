import pathlib

import mysql.connector


class DBConnect:

 #   @classmethod
 #   def getConnection(cls):
#        try:
#            cnx = mysql.connector.connect(
 #               user = "root",
  #              password = "Tommaso2003!",
   #             host = "127.0.0.1",
  #              database = "libretto")
   #         return cnx
  #      except mysql.connector.Error as err:
  #          print("Non riesco a collegarmi al database")
  #          print(err)
  #          return None
    def __init__(self):
        RuntimeError("Non creare un'istanza di questa classe, per favore")

    _myPool = None

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            #creo una connesione, e restituisco il metodo get_connection
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connection.cfg",
                    pool_size=3,
                    pool_name = "myPool"
                )
                return cls._myPool.get_connection()
            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al database")
                print(err)
                return None
        else:
            # se il pool esiste, resituisco direttamente la connessione
            return cls._myPool.get_connection()

