
import config
import base64
import requests
import json

API = base64.b64decode(config.API.encode()).decode()

def soovi_generaator():
    response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": f"Bearer {API}",
        "Content-Type": "application/json",
      },
      data=json.dumps({
        "model": "mistralai/devstral-2512:free",
        "messages": [
            {
              "role": "user",
              "content": "«Сгенерируй одно короткое и тёплое рождественское поздравление на эстонском языке. Текст должен быть простым, дружелюбным и подходить для открытки. Добавь 1–2 уместных рождественских эмодзи. Без пояснений.»"
            }
          ]
      })
    )

    response = response.json()
    print(response)
    response = response['choices'][0]['message']['content']
    return response
soovi = soovi_generaator()
print(soovi)