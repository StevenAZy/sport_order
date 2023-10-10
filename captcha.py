import requests

from config import API_KEY, SECRET_KEY


def captcha_extract(img_base64):
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + get_access_token()
    
    payload={
        'image': img_base64,
        'detect_direction': False,
        'paragraph': False,
        'probability': False
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # print(response.text)
    return response.json()
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

# if __name__ == '__main__':
#     img_base64 = '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'
#     captcha_text(img_base64)