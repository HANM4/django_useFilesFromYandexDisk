import os
import requests


# receiving list files from Yandex Disk by api
def get_public_files_yandex_disk(public_key, path='/'):
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}&path={path}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибка: {response.status_code}")
        return []