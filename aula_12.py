from faker import Faker

fake = Faker()
lista_endereco = []

# Gerar endereços falsos
for _ in range(10):  # Por exemplo, gerar 10 endereços
    endereco = {
        'rua': fake.street_address(),
        'cidade': fake.city(),
        'estado': fake.state(),
        'pais': fake.country()
    }
    lista_endereco.append(endereco)

# Exibir os endereços gerados
for endereco in lista_endereco:
    print(f"{endereco['rua']}, {endereco['cidade']} - {endereco['estado']}, {endereco['pais']}")

