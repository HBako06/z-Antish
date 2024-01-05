import pyodbc

class BaseDeDatos:
    def __init__(self):
        self.server = 'tcp:sqlcamote.database.windows.net'
        self.database = 'sqlcamote'
        self.username = 'camote'
        self.password = 'PedroCastillo159'

        self.connection_string = (
            f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};"
            f"UID={self.username};PWD={self.password};"
        )

    def ejecutar_query(self, query):
        with pyodbc.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

    def obtener_valor(self, query):
        with pyodbc.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result is not None else None

    def aumentar_veces_iniciado(self, bot_name):
        query_select = f"SELECT vecesIniciado FROM JK_HabilitarBots WHERE name_bot = '{bot_name}'"
        veces_iniciado = self.obtener_valor(query_select)

        if veces_iniciado is not None:
            veces_iniciado += 1

            query_update = f"UPDATE JK_HabilitarBots SET vecesIniciado = {veces_iniciado} WHERE name_bot = '{bot_name}'"
            self.ejecutar_query(query_update)

    def verificar_estado_bot(self, bot_name):
        query_select = f"SELECT status FROM JK_HabilitarBots WHERE name_bot = '{bot_name}'"
        estado_bot = self.obtener_valor(query_select)

        return True if estado_bot else False
