import psycopg2

class DataBase:
    
    @staticmethod
    def conectar():
        conexao = psycopg2.connect(
            database = "contasDatabase",
            host = "localhost",
            user = "postgres",
            password = "senha",
            port = "5432"
        )
        cursor = conexao.cursor()
        return conexao, cursor