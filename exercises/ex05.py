class People:
    def __init__(self, name='', age=0, profession=''):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return f'{self.name}, {self.age} ages, {self.profession}'
    
    @property
    def greetings(self):
        if self.profession:
            return f'Hello, I am {self.name}! I work with {self.profession}.'
        else:
            return f'Hello, I am {self.name}!'
        
    def niver(self):
        self.age += 1

   # Criando 3 instâncias da classe Pessoa
person1 = People(name='Alice', age=25, profession='Engenheira')
person2 = People(name='Luiza', age=30, profession='Desenvolvedor')
person3 = People(name='Jaque', age=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(person1)
print(person2)
print(person3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
person1.niver()
person3.niver()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(person1)
print(person3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(person1.greetings)
print(person2.greetings)
print(person3.greetings)

    
