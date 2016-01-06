"""
Implementacao do padrao de projeto observer em Python.

Nessa versao, o acionamento de um evento Event#call permite passagem de
argumentos e o Observer armazena apenas um evento por nome.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):

    def __init__(self, name, call=None):
        self.name = name or self.__class__.__name__
        self.call = call or self.call

    def call(self):
        pass


class Observer(object):

    events = {}

    def add(self, event):
        """Adiciona um evento"""
        self.events[event.name] = event
        # metodo generico para acionar um evento
        setattr(self, event.name, self.call(event.name))

    def on(self, *args):
        if len(args) == 1:
            return self.call(args[0])
        elif len(args) == 2:
            name = args[0]
            handler = args[1]
            self.add(Event(name, handler))

    def call(self, name):
        """Metodo que aciona um evento por nome"""
        return self.events[name].call
