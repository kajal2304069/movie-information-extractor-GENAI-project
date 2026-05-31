# 🎬 Movie Information Extractor

An AI-powered Streamlit application that extracts structured movie information from unstructured movie descriptions using LangChain, Mistral AI, and Pydantic.

## 🚀 Live Demo

🔗 **Try the App:** https://movie-information-extractor-genai-project-mhdj4evxapvgcvnv2f8b.streamlit.app

No installation required—simply open the link, paste a movie description, and get structured movie details instantly.

---

## 📖 Overview

Movie descriptions often contain a lot of information in plain text. This application leverages Large Language Models (LLMs) to automatically extract and organize important movie details into a structured format.

The app converts unstructured movie descriptions into clean JSON data, making it useful for content management, recommendation systems, data analysis, and AI-powered applications.

---

## ✨ Features

* 🎬 Extract Movie Title
* 📅 Identify Release Year
* 🎭 Detect Movie Genres
* 🎥 Extract Director Information
* 👥 Identify Cast Members
* ⭐ Extract Ratings
* 📖 Generate Structured Summary
* 📦 View Raw JSON Output
* 🌐 Interactive Web Interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* Pydantic
* Python Dotenv

---

## 🧠 How It Works

1. User enters a movie description.
2. LangChain creates a structured prompt.
3. Mistral AI analyzes the text.
4. Pydantic validates the response schema.
5. Structured movie information is displayed in the Streamlit interface.

---

## 📸 Example

### Input

3 Idiots is a 2009 Indian comedy-drama film directed by Rajkumar Hirani. The film stars Aamir Khan, R. Madhavan, and Sharman Joshi...

### Output

* Title: 3 Idiots
* Release Year: 2009
* Genre: Comedy, Drama
* Director: Rajkumar Hirani
* Cast: Aamir Khan, R. Madhavan, Sharman Joshi
* Summary: Extracted automatically by the AI model

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

pip install -r requirements.txt

streamlit run Cinesage/uicore.py
```

## 🔐 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
```

## 👩‍💻 Author

**Kajal Kumari Singh**

B.Tech Student | Full Stack Development & Generative AI Enthusiast
