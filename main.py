
import requests
import yadisk
#import json
import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorisation': 'OAuth2 {}'.format(self.token)
        }

    def get_files_list(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        #json_formatted_str = json.dumps(response.json(), indent=2)
        #print(json_formatted_str)
        return response.json()

    def _get_upload_link(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    def upload_via_yadisk(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        y = yadisk.YaDisk(token=token)
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        y.check_token()
        y.get_disk_info()
        headers = self.get_headers()
        buffer_list = path_to_file.split("\\")
        save_as = buffer_list[-1]
        with open(path_to_file, "r") as f:
            y.upload(f, save_as, overwrite=True, headers=headers)
        # Тут ваша логика
        # Функция может ничего не возвращать

    def upload_aka_webinar(self, file_path):
        buffer_list = path_to_file.split("\\")
        filename = buffer_list[-1]
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        upload_link = self._get_upload_link(file_path=file_path)
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "True"}
        response = requests.get(url, headers=headers, params=params)
        # Какого лешего он мне выдает ошибку авторизации?
        response_data = response.json()
        return(response_data)
        upload_url = response_data["href"]
        response = requests.put(upload_url, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success!")



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    pp = pprint.PrettyPrinter(indent = 4)
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите токен: ")
    yup = YaUploader(token)
    yup.upload_via_yadisk(path_to_file)
    pp.pprint(yup.get_files_list())
    """yup.upload_aka_webinar(path_to_file)
    pp.pprint(yup.upload_aka_webinar(path_to_file))
    pp.pprint(yup.get_files_list())"""
    # У меня возникает ошибка авторизации/401 при попытке получить request через мой токен
    # Поэтому я переделал всю работу через библиотеку yadisk, т.к. при ее использовании проблем с аутентификацией не возникает
    # И чисто технически файл он загружает

