import os
from openai import OpenAI
from google.colab import userdata

# OpenAI API 키 설정
api_key = userdata.get('gpt')

with open("problem1.py", "r") as f:
    loaded_code = f.read()

client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오. 라는 문제에서 {loaded_code} 라는 답안을 작성했을때, 완벽하게 구동했을때를 100점으로 해서 해당코드가 몇점인지 채점해줘",
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)