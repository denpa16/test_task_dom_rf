import copy

import requests


DADATA_TOKEN = "your_dadata_api_token_here"
DADATA_URL = "https://cleaner.dadata.ru/api/v1/clean"
DADATA_SECRET_KEY = "your_dadata_secret_key_here"
YANDEX_GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
YANDEX_GPT_FOLDER_ID = "your_yandex_gpt_folder_id"
YANDEX_GPT_IAM_TOKEN = "your_yandex_gpt_iam_token"

def request_dadata(data):
    headers = {
        "Authorization": f"Token {DADATA_TOKEN}",
        "X-Secret": f"{DADATA_SECRET_KEY}"
    }
    #response = requests.post(f"{DADATA_URL}/{data['task_type']}", headers=headers, json={"query": data["data"]})
    #return response.json()
    return_data = copy.deepcopy(data)
    return_data["data"] = [
        {
            "source": "раб 846)231.60.14 *139",
            "type": "Стационарный",
            "phone": "+7 846 231-60-14 доб. 139",
            "country_code": "7",
            "city_code": "846",
            "number": "2316014",
            "extension": "139",
            "provider": "ООО \"СИПАУТНЭТ\"",
            "country": "Россия",
            "region": "Самарская область",
            "city": "Самара",
            "timezone": "UTC+4",
            "qc_conflict": 0,
            "qc": 0
        }
    ]
    return return_data
