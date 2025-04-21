import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def summarize_text(content: str, mode: str = "brief") -> str:
    if mode == "bullet":
        style = "Give a concise bullet-point summary."
    elif mode == "detailed":
        style = "Provide a detailed and structured summary."
    else:
        style = "Summarize this briefly in 3-4 sentences."

    prompt = f"{style}\n\n{content}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )

    return response["choices"][0]["message"]["content"].strip()
