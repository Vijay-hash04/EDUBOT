import google.generativeai as genai
import os
from dotenv import load_dotenv
from pypdf import PdfReader

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------
# LOAD DATA ONLY ONCE
# -----------------------------
def load_college_data():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    context = ""

    print("\nLoading college data from:", DATA_FOLDER)

    if not os.path.exists(DATA_FOLDER):
        print("Data folder not found!")
        return "No college data found."

    for file in os.listdir(DATA_FOLDER):

        file_path = os.path.join(DATA_FOLDER, file)

        # TXT files
        if file.endswith(".txt"):
            print("Loaded TXT:", file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    context += f.read() + "\n"
            except:
                print("Error reading TXT:", file)

        # PDF files
        elif file.endswith(".pdf"):
            print("Loaded PDF:", file)

            try:
                reader = PdfReader(file_path)

                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        context += text + "\n"

            except:
                print("Error reading PDF:", file)

    print("Data loading completed\n")

    return context

# Load data ONCE when server starts
COLLEGE_CONTEXT = load_college_data()


# -----------------------------
# CHATBOT RESPONSE FUNCTION
# -----------------------------
def get_bot_response(question):

    prompt = f"""
You are an AI Admission Assistant for Government College of Engineering, Bodinayakanur.

Use the following college information to answer questions.

College Information:
{COLLEGE_CONTEXT}

Instructions:
- Use bullet points when listing items or breakdown of items
- Use short and clear sentences
- Keep answers concise
- Add spacing between sections
- If the answer is not in the data, say politely you don't know.

Question:
{question}

Answer:
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception:
        return "⚠️ AI service temporarily unavailable. Please try again later."