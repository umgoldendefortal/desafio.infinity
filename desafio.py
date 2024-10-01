from faker import Faker
import random

fake = Faker()

def gerar_pessoa():
    genero = random.choice(['Masculino', 'Feminino'])
    
    if genero == 'Masculino':
        nome = fake.first_name_male()
    else:
        nome = fake.first_name_female()
    
    idade = random.randint(18, 80)
    
    endereco = {
        'rua': fake.street_address(),
        'cidade': fake.city(),
        'estado': fake.state(),
        'pais': fake.country()
    }
    
    return {
        'nome': nome,
        'genero': genero,
        'idade': idade,
        'endereco': endereco
    }

quantidade_de_pessoas = 5  
lista_de_pessoas = [gerar_pessoa() for _ in range(quantidade_de_pessoas)]

for pessoa in lista_de_pessoas:
    print(f"Nome: {pessoa['nome']}, Gênero: {pessoa['genero']}, Idade: {pessoa['idade']}, Endereço: {pessoa['endereco']['rua']}, {pessoa['endereco']['cidade']} - {pessoa['endereco']['estado']}, {pessoa['endereco']['pais']}")

vencedor = random.choice(lista_de_pessoas)

print("\nO vencedor do sorteio foi:")
print(f"Nome: {vencedor['nome']}, Gênero: {vencedor['genero']}, Idade: {vencedor['idade']}, Endereço: {vencedor['endereco']['rua']}, {vencedor['endereco']['cidade']} - {vencedor['endereco']['estado']}, {vencedor['endereco']['pais']}")
