import unittest
import requests

def new_folder_in_disk(name_folder):
        get_headers= {'Content-Type': 'application/json', 'Authorization': 'key'}
        href = 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F'
        response = requests.put(href+name_folder, headers=get_headers)
        return response.status_code

class TestTest(unittest.TestCase):
    # Проверка response.status_code
    # 201 - ок
    def test_response_status_code_201(self):
        response_status_test_201 = new_folder_in_disk('new_folder')
        print(response_status_test_201)
        self.assertEqual(response_status_test_201, 201)

    # 404 - не удалось найти запрошенный ресурс
    def test_response_status_code_404(self):
        response_status_test_404 = new_folder_in_disk('new_folder'*45)
        print(response_status_test_404)
        self.assertEqual(response_status_test_404, 404)

    # 409 - папка уже создана
    def test_response_status_code_409(self):
        response_status_test_409 = new_folder_in_disk('new_folder')
        print(response_status_test_409)
        self.assertEqual(response_status_test_409, 409)

if __name__ == '__main__':
    unittest.main()
