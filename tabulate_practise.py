from tabulate import tabulate
from operator import itemgetter
from secrets import choice


all_pokemon = []
for i in range(1, 6):
    pokemon = dict()
    pokemon['attributes'] = choice(['fire', 'water', 'grass'])
    if pokemon['attributes'] == 'fire':
        pokemon['name'] = choice([
            'Vulpik #037',
            'Quilava #156',
            'Torchic #255'
        ])
        pokemon['skill'] = choice(
            ['fire skill 1', 'fire skill 2', 'fire skill 3'])
        pokemon['on effective on: '] = choice(['water', 'ice'])

    elif pokemon['attributes'] == 'water':
        pokemon['name'] = choice([
            'Watortle #008',
            'Seaking #119',
            'Seel #086'
        ])
        pokemon['skill'] = choice(
            ['water skill 1', 'water skill 2', 'water skill 3'])
        pokemon['on effective on: '] = choice(['grass', 'electrical'])

    elif pokemon['attributes'] == 'grass':
        pokemon['name'] = choice([
            'Paras #046',
            'Oddish #043',
            'Bayleef #153'
        ])
        pokemon['skill'] = choice(
            ['grass skill 1', 'grass skill 2', 'grass skill 3'])
        pokemon['on effective on: '] = choice(['fire', 'flying'])

    all_pokemon.append(pokemon)

# for key, value in pokemon.items():
#     print(f'{key:>20} : {value}')

sorted_pokemon = sorted(all_pokemon, key=itemgetter(
    "name"))

print(tabulate(sorted_pokemon, headers="keys"))
