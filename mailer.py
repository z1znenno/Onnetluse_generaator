from logging import exception

import config
import base64
import requests
import json
import smtplib
from email.message import EmailMessage

message = EmailMessage()
API = base64.b64decode(config.API.encode()).decode()
key = base64.b64decode(config.key.encode()).decode()
models = ["mistralai/devstral-2512:free", "openai/gpt-oss-20b:free", "moonshotai/kimi-k2:free", "deepseek/deepseek-r1-0528:free", "google/gemma-3n-e4b-it:free"]

def soovi_generaator():
    i = 0
    while True:

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": f"{models[i]}",
                    "messages": [
                    {
                    "role": "user",
                    "content": "«Сгенерируй одно короткое и тёплое рождественское поздравление на эстонском языке. Текст должен быть простым, дружелюбным и подходить для открытки. Добавь 1–2 уместных рождественских эмодзи. Без пояснений. Без перевода, только текст поздравления»"
                    }
                  ]
              })
            )

        response = response.json()
        print(response)
        if 'error' not in response:
            response = response['choices'][0]['message']['content']
            return response
            break
        else:
            print("AI on väsinud\nProovime uuesti...")
            if i < len(models) - 1:
                i += 1
            else:
                print("Ma ei saa midagi teha.")
                break

def soovi_saatmine(saajad):
    try:
        email_subject = "Häid jõule"
        sender_email_address = "order1print@gmail.com"
        email_smtp = "smtp.gmail.com"
        email_password = key

        server = smtplib.SMTP(email_smtp, '587')
        server.ehlo()
        server.starttls()

        server.login(sender_email_address, email_password)
        for saaja in saajad:
            print("Отправка письма на:", saaja)
            message = EmailMessage()
            message['Subject'] = email_subject
            message['From'] = sender_email_address
            message['To'] = saaja
            soov = soovi_generaator()
            message.set_content(soov)
            server.send_message(message)

        server.quit()
        return "Saatis"
    except Exception as e:
        print(e)
        print("Тип ошибки:", type(e))
