from django.shortcuts import render
from decouple import config
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

# 네이버 파파구 번역
def papagu(request):
    return render(request, 'utilities/papagu.html')

def translated(request):
    #1. 사용자가 입력한 번역하고자 하는 한국어 텍스트
    word = request.GET.get('word')

    #2. 네이버에 번역 요청을 위해 필요한 준비
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    #3. 요청을 보낼 url
    papagu_url = 'https://openapi.naver.com/v1/papago/n2mt'

    #4. 헤더 정보 구성
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    #5. 요청 데이터 준비
    data = {
        'source': 'ko',
        'target': 'en',
        'text': word,
    }

    #6. 네이버 요청을 보내자!
    papagu_response = requests.post(papagu_url, headers=headers, data=data).json()

    #7. 번역된 텍스트 뽑기
    english = papagu_response.get('message').get('result').get('translatedText')

    context = {
        'korea': word,
        'english': english,
    }
    return render(request, 'utilities/translated.html',context)