#importa o pyro
import Pyro4

# é algo referente a segurança, o pyro antes mostrava tudo, hpje é preciso utilizar para indicar classes chamadas remotamente
@Pyro4.expose

#Objeto Pyro
#Este é um objeto Python normal, mas está registrado no Pyro para que você possa acessá-lo
#remotamente. Os objetos Pyro são escritos como qualquer outro objeto, mas o fato de o Pyro 
#saber algo sobre eles os torna especiais, da maneira que você pode chamar métodos sobre eles a 
#partir de outros programas. Uma classe também pode ser um objeto Pyro, mas você também precisará
#informar ao Pyro sobre como deve criar objetos reais a partir dessa classe ao lidar com chamadas
#remotas.
class Media:
    # função que é utilizada para dizer se o usuario passou ou nao
    def passar(self, nota, nota2):

            a = ((nota*2)+(nota2*3))/5

            if a>=60:
                return 'passou'
            else:
                return 'se fudeo'
            



#Daemon Pyro (servidor)
#Essa é a parte do Pyro que escuta chamadas de método remoto, as envia para os objetos reais 
#apropriados e retorna os resultados para o chamador. Todos os objetos Pyro são registrados em um
#ou mais daemons.
daemon = Pyro4.Daemon()


uri = daemon.register(Media)
numeroServidor = Pyro4.locateNS()
numeroServidor.register('objeto', uri)
print(uri)

daemon.requestLoop()