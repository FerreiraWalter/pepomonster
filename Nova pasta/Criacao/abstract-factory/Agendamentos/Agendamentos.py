from abc import ABCMeta, abstractmethod

class Agendamentos(metaclass = ABCMeta):
  """
  Mostrar Informacao do agendamento
  """
  @abstractmethod
  def mostrar_agendamento(self):
    pass
