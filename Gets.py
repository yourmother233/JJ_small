import requests
import json
def get_translate_date(word=None):
    From_data={
    'i': word,
    'from': 'AUTO',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15813378850276',
    'sign': '63058b31bfe17fae9a526290d9ac2799',
    'ts': '1581337885027',
    'bv': '5575008ba9785f184b106838a72d6536',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'}
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    response = requests.post(url,data=From_data)
    content = json.loads(response.text)
    print(content['translateResult'][0][0]['tgt'])
if __name__=='__main__':
    str = input("Please input anything about small dick in any language")
    get_translate_date(str)