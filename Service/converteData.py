from datetime import datetime


class servico:

    @staticmethod
    def converteData(data):
        return datetime.strptime(data, "%d/%m/%Y").date()
    
    