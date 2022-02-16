class Agendar(Agendamentos):
    """
    Agendar geral
    """

    BARBEARIA = 0
    SALAO_DE_BELEZA = 1
    RESTAURANTE = 2

    def agendar(self, local):
        if local == 0:
            Barbearia.mostrar_agendamento()
        elif local == 1:
            SalaodeBeleza.mostrar_agendamento()
        elif local == 2:
            Restaurante.mostrar_agendamento()