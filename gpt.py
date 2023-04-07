import openai

with open("openai_key.txt") as f:
    openai.api_key = f.read().strip()

async def generate_response(queri):
    async with open("openai_key.txt") as f:
        openai.api_key = f.read().strip()
    response = await openai.Completion.create(
        model="text-davinci-003",
        prompt=queri,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    message = response.choices[0].text.strip()
    return message