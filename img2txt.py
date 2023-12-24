import base64
import urllib
import requests
import json

API_KEY = "gCXEiMYKCd1zwzGusIOEy1Nl"
SECRET_KEY = "53WuNLAoLXLYYarWOVUKSgBa6wC4WY9f"


def get_text(path):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=" + get_access_token()
    image=get_file_content_as_base64(path, True)

    # image 可以通过 get_file_content_as_base64("C:\fakepath\1.jpg",True) 方法获取
    payload = 'image='+image
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_data = json.loads(response.text)

    words_result = response_data["words_result"]
    words_value = words_result[0]
    result = words_value["words"]

    print(result)
    return result



def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))




#get_text('tempfile/技能截图_20231019_160733.png')
