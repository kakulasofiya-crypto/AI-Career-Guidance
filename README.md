# 🎯 AI Career Guidance Platform

An AI-powered career guidance application that recommends suitable career paths based on a user's education, skills, interests, experience level, and career goals. It combines rule-based career matching with Google Gemini AI to generate personalized learning roadmaps and career preparation guidance.

## 📌 Problem Statement

Students and job seekers often struggle to identify suitable career paths and understand which skills they need to develop. This project aims to simplify career planning by analyzing user profiles and providing personalized career recommendations, learning roadmaps, project ideas, and interview preparation.

## ✨ Features

- **Personalized Career Guidance:** Generates career advice based on the user's profile.
- **Career Matching Dashboard:** Compares five career paths using selected skills and interests.
- **Match Score Visualization:** Displays career match scores in an interactive bar chart.
- **Skill Gap Analysis:** Highlights skills that users may need to develop for different careers.
- **Six-Month Learning Roadmap:** Provides a structured plan for learning and career preparation.
- **Project Recommendations:** Suggests practical projects to build technical skills and a portfolio.
- **Interview Preparation:** Generates interview questions with sample answers.
- **Seven-Day Action Plan:** Recommends actionable steps to get started.
- **Downloadable Career Plan:** Allows users to download their personalized AI-generated report.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- Pandas
- Plotly
- python-dotenv

## ⚙️ How It Works

1. The user enters their education, branch, skills, interests, career goal, and experience level.
2. The career-matching module calculates rule-based scores for available career paths.
3. The application visualizes the matching results and highlights potential skill gaps.
4. Google Gemini AI generates a personalized career guidance report.
5. The user reviews the recommendations and downloads the report.

## 💻 Installation and Setup

### Prerequisites

- Python installed on your system
- A Google Gemini API key
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/kakulasofiya-crypto/AI-Career-Guidance.git
cd AI-Career-Guidance
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a file named `.env` in the project root and add:

```text
GEMINI_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your own Gemini API key.

**Security:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
AI-Career-Guidance/
├── app.py
├── career_matcher.py
├── requirements.txt
├── .gitignore
├── .env                  # Local secret; not committed
└── README.md
```

## 🎯 Career Paths

The career-matching module currently compares these career paths:

- AI Engineer
- Data Scientist
- Software Developer
- Cybersecurity Analyst
- Data Analyst

Match scores are rule-based estimates derived from the selected skills and interests. They are guidance indicators, not predictions of employment or hiring probability.

## 🔮 Future Enhancements

- User accounts and saved career profiles
- Learning progress tracking
- Personalized course recommendations
- Resume analysis and improvement suggestions
- Expanded career paths and skill frameworks
- Online deployment for public access

## 👩‍💻 Author

**Sofiya Kakula**

GitHub: [kakulasofiya-crypto](https://github.com/kakulasofiya-crypto)

## 📄 License

This project is developed for educational and career-development purposes. A formal open-source license can be added if the project is released under one.