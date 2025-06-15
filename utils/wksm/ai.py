from google import genai

client = genai.Client(api_key=key)


response = client.models.generate_content(
    model='gemini-2.5-flash-preview-05-20'
    content=''
)