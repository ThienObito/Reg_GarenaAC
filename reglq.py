import requests
import random
import string
import time
def random_string(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))
def run():
    email = random_string(6)
    user = random_string(13)
    cookies = {
        '_ga': 'GA1.1.1387551280.1675945855',
        '_ga_1M7M9L6VPX': 'GS1.1.1679023440.5.0.1679023440.0.0.0',
        'datadome': '7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.1387551280.1675945855; _ga_1M7M9L6VPX=GS1.1.1679023440.5.0.1679023440.0.0.0; datadome=7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
        'Origin': 'https://sso.garena.com',
        'Referer': 'https://sso.garena.com/ui/register?locale=vi',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/111.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'x-datadome-clientid': '7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
    }

    data = {
        'username': user,
        'email': f'{email}@gmail.com',
        'password': '37b0842cacde5e00f31bda0acce6e4a82e62ef97dba46b38d5ec41abab71526e9ea41d1a2b0b41db0f20b8aa4b9d5df19cd0dc50e0a09a0060c0e00e39306c1c5fcd0394e8e66ab0e06211d665f501b17e6ac38df2399cc548a8fb078bb70ec6c36fa8cbecb9e9680b22e15fe6a608fc0b4b4fef6f0c178c8989650d4ac604d1',
        'location': 'VI',
        'redirect_uri': '',
        'locale': 'vi',
        'mobile_no': '',
        'otp': '',
        'format': 'json',
        'id': '1679023495865',
    }

    response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
    #print(response)
    check = response['username']
    if check == user: #cai nay de check user
        print(user+" | @Tobi19")
        with open("garena.txt", "a+", encoding="utf-8") as f:
            f.write(user+" | @Tobi19"+"\n")
while True:
    try:
        run()
    except:
        print("Lỗi xảy ra, đang thử lại...")
        time.sleep(5)
        continue
    time.sleep(20)
