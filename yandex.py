# import pytest
import requests


class Yandex:

    def __init__(self, token, url='https://cloud-api.yandex.net/v1/disk/resources/'):
        self.token = token
        self.url = url

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_name):
        response = requests.get(url=f'{self.url}?path={folder_name + r"/"}', headers=self.get_headers())
        if response.status_code != 200:
            create = requests.put(url=f'{self.url}?path={folder_name}', headers=self.get_headers())
            # print(create)
            return create.status_code
        else:
            return response.status_code


if __name__ == '__main__':
    with open('Yandex.txt', 'r', encoding='utf-8') as file_token_ya:
        token_yandex = file_token_ya.read()
    connect = Yandex(token=token_yandex)
    new_folder = connect.create_folder(folder_name='Test')
    print(new_folder)
