# 경제전문가입니다.
# 2027년 주식시세가 어떻게 될지알려주는 프로그램을 구현하시오.
# 반도체주, 전력시설주, 우주항공주
# 500자 이내로 짧게 알려줘

import os
from pathlib import Path  #디장고
from dotenv import load_dotenv
import openai
from openai import OpenAI


#--------------------------------------------------------------------------------------------------
# 1. key 가져오기
BASE_DIR =Path(__file__).resolve().parent.parent
envFile = BASE_DIR/'.env'
print(BASE_DIR)
print(envFile)

load_dotenv(envFile)
api_key = os.getenv('open_ai_key')
# print(api_key)

#--------------------------------------------------------------------------------------------------
# 2. 검색어 입력부분 - chat gpt 연결해서 진행
while True:
    txt_input = input('경재전문가입니다>>>')
    if txt_input: break
    print('.')
    print('.')
    print()

print('완료')

#--------------------------------------------------------------------------------------------------
# 3. OpenAI client 연결부분 - 글자생성, 이미지생성, 음성생성, 동영상생성
client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model ='gpt-5.6',
        instructions= (
            "경제전문가입니다."
            "2027년 주식시세가 어떻게 될지 알려주는 프로그램을 구현시오."
            "[반도체주,전력시설주,우주항공주]으로 알려주세요."
            "500자 이내로 짧게 알려줘."
        ),
        input = f'{txt_input}를 가지고 [경제전문가입니다] - 2027년 주식시세가 어떻게 될지알려주는 프로그램,반도체주, 전력시설주, 우주항공주,500자 이내로 짧게 알려줘.',
        max_output_tokens=1000,              #토큰사용량 제한 가능
    )
except openai.APIConnectionError as error:
    print(f"인터넷연결,방화벽 문제 등 확인요망 :{error}")
except openai.RateLimitError as error:
    print(f"요쳥량 또는 프로젝트 사용한도 확인 : {error}")
except openai.APIError as error:
    print(f"인증,권한 등 api 오류 확인 :  {error}")