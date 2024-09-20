from Controller.data import DataBase



class ControllerConta:

    @staticmethod
    def cadastrarConta():
        conexao, cursor = DataBase.conectar()
        descricao = input("Descrição: ")
        dataVencimento = input("Data Vencimento: ")
        valor = float(input("Valor: "))
        status = False
        SQL_QUERY = ("INSERT INTO contas (descricao, datavencimento, valor, status) values (%s, %s, %s, %s)")
        cursor.execute(SQL_QUERY,(descricao,dataVencimento,valor,status))
        conexao.commit()
        cursor.close()
        conexao.close()
        return "Conta cadastrada com Sucesso!"

