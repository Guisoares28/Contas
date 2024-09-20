<<<<<<< HEAD
from Model.data import DataBase
from Service.converteData import servico
import psycopg2
=======
from Controller.data import DataBase

>>>>>>> 7a0dbb2426ccdc2718067961a4d2c289221f7150


class ControllerConta:

    @staticmethod
    def cadastrarConta():
        conexao, cursor = DataBase.conectar()
        descricao = input("Descrição: ")
<<<<<<< HEAD
        while(True):
            try:
                dataVencimento_string = input("Data Vencimento: ")
                data = servico.converteData(dataVencimento_string)
                break
            except ValueError:
                print("\nDigite a data no formato correto (Dia/Mês/Ano)")
        while(True):
            try:
                valor = float(input("Valor: "))
                break
            except ValueError:
                print("\nTipo de dado incorreto!")
        status = False
        try:
            SQL_QUERY = ("INSERT INTO contas (descricao, datavencimento, valor, status) values (%s, %s, %s, %s)")
            cursor.execute(SQL_QUERY,(descricao,data,valor,status))
            conexao.commit()
            return "\nConta cadastrada com Sucesso!!!"   
        except psycopg2.Error:
            return "\nNão foi possível cadastrar a conta, Tente novamente"
        finally:
            cursor.close()
            conexao.close()
            
        
=======
        dataVencimento = input("Data Vencimento: ")
        valor = float(input("Valor: "))
        status = False
        SQL_QUERY = ("INSERT INTO contas (descricao, datavencimento, valor, status) values (%s, %s, %s, %s)")
        cursor.execute(SQL_QUERY,(descricao,dataVencimento,valor,status))
        conexao.commit()
        cursor.close()
        conexao.close()
        return "Conta cadastrada com Sucesso!"
>>>>>>> 7a0dbb2426ccdc2718067961a4d2c289221f7150

