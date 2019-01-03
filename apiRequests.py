#coding=utf-8

import requests
import re
import urllib3

def login(username,password):
    session = requests.Session()
    urllib3.disable_warnings()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'prodqa.tealeaf.ibmcloud.com',
        'Origin': 'https://prodqa.tealeaf.ibmcloud.com',
        'Referer': 'https://prodqa.tealeaf.ibmcloud.com/webapp/login',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
    }
    res= session.get('https://prodqa.tealeaf.ibmcloud.com/webapp/login',verify=False,headers=headers)
    reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
    pattern = re.compile(reg)
    result = pattern.findall(str(res.content))
    token = result[0]
    print(token)

    '''
    post_data = {
        'j_username': 'guch@cn.ibm.com',
        'j_password': 'Luck@2019'
    }

    session.post('https://prodqa.tealeaf.ibmcloud.com/webapp/j_spring_security_check',verify=False,data=post_data,headers=headers)
    #res = session.get('https://prodqa.tealeaf.ibmcloud.com/webapp/home')
    res = session.get('https://prodqa.tealeaf.ibmcloud.com/webapp/api/audit/download?startTime=2018-01-01&endTime=2018-11-13&orgCode= tealeaf-com')
    print(res.content)

    payload = {'k': codeKey[0], 't': timeKey}
    yzm_url='http://210.41.224.117/Login/xLogin/yzmDvCode.asp'
    yzmdata = session.get(yzm_url, params=payload, headers=headers)  #刷新验证码，上文要点2
    post_data = {
        'WinW': '1366',
        'WinH': '728',
        'txtId': username,
        'txtMM': password,
        'verifycode': yzm,
        'codeKey': codeKey[0],
        'Login': 'Check',
        'IbtnEnter.x': 10,
        'IbtnEnter.y': 10
    }
    post_url='http://210.41.224.117/Login/xLogin/Login.asp'
    step3 = session.post(post_url, data=post_data, headers=headers)   #post登陆数据
    '''
    return session

cuitJWC=login('username','password')
#con=cuitJWC.get('http://jxgl.cuit.edu.cn/JXGL/xs/MainMenu.asp')
#print(con.text)