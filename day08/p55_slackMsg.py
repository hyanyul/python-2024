#file: p55_slackMsg.py
#desc: 슬랙으로 스마트폰 메시지 보내기

'''
순서
1. http://api.slack.com/ 에서 Your app > Create your first app
2. From Scratch 클릭(앱 이름은 영어로만(한글로 불가))
3. 워크스페이스 선택
4. Incomming Webhook > On > Add New Webhook to workspace 클릭 > 채널 선택 > 허용
'''

import requests
import json

slack_url = 'http://hooks.slack.com/sercives/'  #슬랙앱 링크
headers = {'Content-type' : 'application/json'}
data = {'text' : 'Python에서 보내는 메시지'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('메시지 전송 성공')
else:
    print('메시지 전송 실패')