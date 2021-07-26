import requests


def buscar_avatar(usuario):
    """
    busca avatar de usuario no github
    :param usuario: string com o nome do usuario
    :return: string com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('heitor-oss'))
