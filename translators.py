import requests
import hashlib
import random

def translate_text_google(text, target_language):
    endpoint = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': 'auto',
        'tl': target_language,
        'dt': 't',
        'q': text
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    result = response.json()
    return result[0][0][0]

def translate_text_microsoft(text, target_language):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {
        'api-version': '3.0',
        'to': target_language
    }
    headers = {
        'Ocp-Apim-Subscription-Key': "YOUR_SUBSCRIPTION_KEY",
        'Content-Type': 'application/json',
        'Content-Length': str(len(text)),
    }
    response = requests.post(endpoint, headers=headers, params=params, json=[{'Text': text}])
    response.raise_for_status()
    result = response.json()
    return result[0]['translations'][0]['text']

def translate_text_ibm(text, target_language):
    endpoint = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v3/translate"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer YOUR_API_KEY",
    }
    data = {
        'text': text,
        'model_id': 'en-' + target_language
    }
    response = requests.post(endpoint, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result['translations'][0]['translation']

def translate_text_baidu(text, target_language):
    appid = "YOUR_APP_ID"
    secret_key = "YOUR_SECRET_KEY"
    endpoint = "https://api.fanyi.baidu.com/api/trans/vip/translate"
    salt = str(random.randint(32768, 65536))
    sign = appid + text + salt + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    params = {
        'appid': appid,
        'q': text,
        'from': 'auto',
        'to': target_language,
        'salt': salt,
        'sign': sign
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    result = response.json()
    return result['trans_result'][0]['dst']

