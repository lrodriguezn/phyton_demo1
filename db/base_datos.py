import pyodbc

conexion_db = {"host": "localhost\\sql2019",
               "database": "Nomina_2101_AnclayViento",
               "user": "sanomina",
               "password": "ZEUSTEC*"
            }


class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = pyodbc.connect("DRIVER={{SQL Server}};SERVER={0}; database={1};trusted_connection=yes;UID={2};PWD={3}".format(kwargs["host"],kwargs["database"],kwargs["user"],kwargs["password"]))
        self.cursor = self.conector.cursor()
    
    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def mostrar_db(self):
        try:
            self.cursor.execute("SELECT name FROM master.dbo.sysdatabases")
            for reg in self.cursor:
                print(reg)
        except:
            print("error consultado bases de datos")

        
