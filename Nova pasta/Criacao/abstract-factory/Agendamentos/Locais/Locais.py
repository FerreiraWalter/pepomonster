from Agendamentos import Agendamentos

class Barbearia(Agendamentos):
    """
    Agendar horario na barbearia
    """
    def mostrar_agendamento(self):
        print("Cleiton está disponível.")
        print("Agendado com sucesso.")


class SalaodeBeleza(Agendamentos):
    """
    Alugar horario no salao
    """
    def mostrar_agendamento(self):
        print("Suzane está disponível.")
        print("Agendado com sucesso.")


class Restaurante(Agendamentos):
    """
    Alugar lugar no restaurante
    """
    def mostrar_agendamento(self):
        print("Mesa 13 está disponível.")
        print("Agendado com sucesso.")

