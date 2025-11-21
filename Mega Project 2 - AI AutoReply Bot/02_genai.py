import google.generativeai as genai
from dotenv import load_env()

load_env()

# Configure Gemini API
genai.configure(api_key="os.getenv("Gemini_api_key")")

command = """[11:42 am, 21/11/2025] F Siddharth Vvp: Shu message delete Kari nakhe che
[11:43 am, 21/11/2025] RD UBHADIYA: Are chat bot banavto to pan taro reply na aayo to delete kari didhi😂
[11:43 am, 21/11/2025] F Siddharth Vvp: Ohho
[11:43 am, 21/11/2025] F Siddharth Vvp: Reply didho to khara
[11:44 am, 21/11/2025] F Siddharth Vvp: Shu kye Kai baju
[11:44 am, 21/11/2025] RD UBHADIYA: Atayre bija ne gotyo
[11:45 am, 21/11/2025] RD UBHADIYA: Aava msg kare 6e
[11:46 am, 21/11/2025] RD UBHADIYA: Kham tara ma karu
[11:46 am, 21/11/2025] F Siddharth Vvp: Ha
"""

prompt = f"""
You are a person named Rohit.
You speak Gujarati + English.
You are from India and you are a coder.
Analyze chat history and respond exactly like Rohit would.

Chat History:
{command}
"""

# Create Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(prompt)

print(response.text)

