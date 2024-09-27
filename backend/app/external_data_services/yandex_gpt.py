import requests

import copy

YANDEX_GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
YANDEX_GPT_FOLDER_ID = "your_yandex_gpt_folder_id"
YANDEX_GPT_IAM_TOKEN = "your_yandex_gpt_iam_token"

def request_yandex_gpt(data: dict):
    r_data = {}
    # Указываем тип модели
    r_data["modelUri"] = f"gpt://{YANDEX_GPT_FOLDER_ID}/yandexgpt"
    # Настраиваем опции
    r_data["completionOptions"] = {"temperature": 0.3, "maxTokens": 1000}
    # Указываем контекст для модели
    r_data["messages"] = [
        {"role": "system", "text": "Исправь ошибки в тексте."},
        {"role": "user", "text": f"{data['data']}"},
    ]
    #response = requests.post(
    #    YANDEX_GPT_URL,
    #    headers={
    #        "Accept": "application/json",
    #        "Authorization": f"Bearer {YANDEX_GPT_IAM_TOKEN}"
    #    },
    #    json=data,
    #)
    #return response.json()
    return_data = copy.deepcopy(data)
    return_data["data"] = {'result': {'alternatives': [{'message': {'role': 'assistant', 'text': 'Ошибки сами себя не исправят.'}, 'status': 'ALTERNATIVE_STATUS_FINAL'}], 'usage': {'inputTextTokens': '29', 'completionTokens': '9', 'totalTokens': '38'}, 'modelVersion': '07.03.2024'}}
    return return_data