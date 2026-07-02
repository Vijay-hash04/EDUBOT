🎓** EDUBOT: Streamlining Higher Education Admissions with Conversational AI**

📌 **Project Overview**

This is a web application designed to assist students by providing instant and accurate information about college admissions. Instead of manually searching through multiple web pages, users can interact with an AI-powered chatbot to receive details about courses, eligibility, fees, admission deadlines, placement information, scholarships, hostel facilities, and other campus-related queries.
The application uses Google's Gemini AI API to understand natural language questions and generate intelligent responses. It provides a simple, user-friendly interface that improves the admission enquiry experience for students and reduces repetitive work for college staff.

✨ **Features**

* 🤖 AI-powered chatbot using Gemini API
* 📚 Course information
* 💰 Fee structure details
* ✅ Eligibility criteria
* 📅 Admission deadlines
* 🏫 Campus and hostel information
* 🎓 Scholarship details
* 💼 Placement information
* 📄 PDF document processing
* 🔍 Dynamic response generation
* 📱 Responsive user interface


🛠️ Technologies Used

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Django

**Database**

* MySQL

**APIs**

* Google Gemini API

**Python Libraries**

* Django
* google-generativeai
* python-dotenv
* requests
* beautifulsoup4
* markdown
* PyPDF
* mysqlclient / PyMySQL

⚙️ **Installation**

1. Clone the repository

```bash
git clone https://github.com/yourusername/admission-chatbot.git
cd admission-chatbot
```

2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

5. Configure the MySQL database

Update the database settings in Django's `settings.py`.

Run migrations:

python manage.py makemigrations
python manage.py migrate

6. Start the development server

python manage.py runserver

Open your browser and visit:
http://127.0.0.1:8000/

💬 **Example Questions**

* What courses are available?
* What is the fee structure for CSE?
* What is the eligibility for MCA?
* When is the last date for admission?
* Does the college provide hostel facilities?
* What are the placement statistics?
* Is any scholarship available?


🎯 **Objectives**

* Simplify the admission enquiry process.
* Provide accurate and instant information.
* Improve student engagement.
* Reduce manual workload for college staff.
* Deliver 24×7 assistance through AI.


🚀 **Future Enhancements**

* Voice-based interaction
* Multi-language support
* Student login and authentication
* Live admission status tracking
* Admin dashboard for content management
* WhatsApp and Telegram chatbot integration
* Analytics dashboard

---
👨‍💻 Author
**Vijayaganapathy M**
Python Full Stack Developer

**Skills**

* Python
* Django
* MySQL
* HTML
* CSS
* JavaScript
* REST APIs
* Google Gemini API

📜 **License**

This project is developed for educational and learning purposes. You are free to modify and extend it according to your requirements.
