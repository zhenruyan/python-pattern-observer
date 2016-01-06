"""
Implementacao simples do padrao de projeto observer em Python.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):
    __name__ = None  # opcional

    def action(self):  # aciona o evento
        pass


class Observer(object):

    def __init__(self):
        self.events = {}  # dicionario para armazenar eventos

    def add(self, event):
        """Adiciona um evento"""

        event_name = event.__name__ or event.__class__.__name__

        # se nao existe uma lista de eventos com determinado nome ...
        if event_name not in self.events:
            self.events[event_name] = []

        self.events[event_name].append(event)

        if event_name not in dir(self):
            # cria metodo generico para acionar eventos de um determinado nome
            setattr(self, event_name, lambda: self.action(event_name))

    def action(self, name):
        """Metodo que aciona uma lista de eventos (por nome)"""
        for e in self.events[name]:
            e.action()


class Hello(Event):
    __name__ = 'hello'

    def __init__(self, msg=None):
        self.msg = msg or 'Ai dentro'

    def action(self):
        print(self.msg)

# criando dois eventos
hello = Hello()
hello2 = Hello('Papai noel')

# criando observer
obj = Observer()
obj.add(hello)
obj.add(hello2)

# aciona os eventos de nome hello
obj.hello()  # ou obj.action('hello')
# Ai dentro
# Papai Noel