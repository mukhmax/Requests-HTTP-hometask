import requests


TOKEN = ''
url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def uploads(self, file_path: str):
        headers = {'Content_type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        url_upload = requests.get(url, headers=headers, params=params).json().get('href', '')
        res = requests.put(url_upload, data=open('test.txt', 'rb'))
        print(res.status_code)


if __name__ == '__main__':
    path_to_file = 'Netology/test.txt'
    uploader = YaUploader(token=TOKEN)
    uploader.uploads(path_to_file)
