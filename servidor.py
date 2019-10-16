import Pyro4

@Pyro4.expose

class Media:
    def passar(self, nota, nota2):

            a = ((nota*2)+(nota2*3))/5

            if a>=60:
                return 'passou'
            else:
                return 'se fudeo'
           
daemon = Pyro4.Daemon()

uri = daemon.register(Media)
numeroServidor = Pyro4.locateNS()
numeroServidor.register('objeto', uri)
print(uri)

daemon.requestLoop()
