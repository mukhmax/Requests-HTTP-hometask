import requests
# from pprint import pprint

url_sh = 'https://akabab.github.io/superhero-api/api/'


def input_superheroes():
    superheros_id = {}
    name = None
    total = requests.get(url_sh + 'all.json').json()
    while name != 'e':
        name = input('Введите имя супергероя или "e" для завершения ввода: ')
        if name == 'e':
            break
        else:
            counter = 0
            for superhero in total:
                if superhero['name'].lower() == name.lower():
                    superheros_id[str.title(name)] = superhero['id']
                    print('Принято!\n')
                else:
                    counter += 1
            if counter >= len(total):
                print('Нет такого героя')
    return superheros_id


def smartest():
    superheros_list = input_superheroes()
    superheros_intelligences = {}
    for superhero, ids in superheros_list.items():
        superheros_intelligences[superhero] = requests.get(url_sh + f'powerstats/{ids}.json').json()['intelligence']
    genius = max(superheros_intelligences, key=superheros_intelligences.get)
    return f'\n{genius} самый умный!'


if __name__ == '__main__':
    print(smartest())
