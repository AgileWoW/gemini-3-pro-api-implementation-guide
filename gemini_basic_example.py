from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

# For complex reasoning (HIGH thinking level)
response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Develop a multi-agent workflow for supply chain optimization.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.HIGH 
        )
    )
)

print(response.text)
