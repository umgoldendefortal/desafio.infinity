from faker import Faker

fake = faker()

lista_de_pessoas =  []

for _ in range(3):
    pessoa = {
        'nome' : fake.name(),
        'idade' : fake.random_int(min=18, max=90),
        endereco : {
            'rua' : fake.street_address(),
            'city' : fake.city(),
            'state' : fake.state(),
            'pais' : fake.country(),   
        }
        lista_endereco.append(pessoa)
    }