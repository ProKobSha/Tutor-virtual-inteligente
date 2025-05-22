import openai

def generar_respuesta(pregunta, api_key):
    openai.api_key = api_key
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pregunta}]
    )
    return respuesta['choices'][0]['message']['content']
