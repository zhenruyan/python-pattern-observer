"""
Implementacao do padrao de projeto observer em Python.

Nessa versao, o acionamento de um evento Event#trigger permite passagem de
argumentos e o Observable armazena apenas um observer por evento, o que faz com
que a classe Observer posssa ser abstraida e seu handler (callback) ser
utilizado diretamente.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):
    """Event or topic"""

    def __init__(self, call=None):
        self.call = call or self.call

    def call(self):  # subscriber/listener/observer/reciver handler/callback
        pass

    def on(self, call):  # [re]binding
        self.call = call

    def trigger(self, *args, **kwargs):  # notify/emit observer to some action
        return self.call(*args, **kwargs)


class Observable(object):
    """Observable or subject or provider or event source/generator"""

    events = {}

    def on(self, event, handler):
        self.events[event] = Event(handler)
        setattr(self, event, self.events[event])  # self.event.trigger()

    def trigger(self, *args, **kargs):
        return self.events[args[0]].trigger(*args[1:], **kargs)
