import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github
    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'http://api.github.com/users/{usuario}'
    res = requests.get(url)
    return res.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('bruno-ba'))
