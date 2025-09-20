import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.0-flash")
def ai(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

