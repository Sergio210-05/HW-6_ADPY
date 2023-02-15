import pytest
from yandex import Yandex


def test_create_folder():
    with open('Yandex.txt', 'r', encoding='utf-8') as file_token_ya:
        token_yandex = file_token_ya.read()
    connect = Yandex(token=token_yandex)
    new_folder = connect.create_folder(folder_name='Test')
    assert new_folder != 401, "Unauthorized"
    assert new_folder != 403, "Forbidden request"
    assert new_folder != 400, "Bad Request"
    assert new_folder in [200, 201]


if __name__ == '__main__':
    test_create_folder()
