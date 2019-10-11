# importa o pyro
import  Pyro4



numeroServidor = Pyro4.locateNS()


#URI
#É isso que o Pyro usa para identificar todos os objetos. 
#(semelhante ao URL de uma página da web para apontar para os diferentes documentos na web). 
#Sua forma de string é assim: “PYRO:” + nome do objeto + “@” + nome do servidor + número da porta. 
#Existem algumas outras formas que também podem ser adotadas. 
#Você também pode escrever o protocolo em letras minúsculas, se desejar (“pyro:”), 
#mas ele será automaticamente convertido em letras maiúsculas internamente.
#A classe que implementa o Pyro uris é Pyro4.URI(atalho para Pyro4.core.URI)

uri = numeroServidor.lookup('objeto')



#Proxy
#Um proxy é um objeto substituto para "a coisa real".
#Ele intercepta as chamadas de método que você faria normalmente
#em um objeto como se fosse o objeto real. O Pyro, então, executa
#alguma mágica para transferir a chamada para o computador que contém o objeto real,
#onde a chamada de método real é feita, e os resultados são retornados ao chamador.
#Isso significa que o código de chamada não precisa saber se está lidando com um objeto 
#normal ou remoto, porque o código é idêntico. A classe que implementa proxies Pyro é 
#Pyro4.Proxy(atalho para Pyro4.core.Proxy)

objeto = Pyro4.Proxy(uri)

# imprime mensagem
print('Por favor, digite sua nota:')

# recebe a nota
nota = int(input())

# imprime mensagem
print('Por favor, digite sua nota:')

# recebe a nota
nota2 = int(input())


# passa o objeto chamando a função passar com o argumento nota
print(objeto.passar(nota, nota2))
