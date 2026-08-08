# 🎬 CineStage — Movie Information Extractor

🚀 **My First Generative AI Project**

CineStage is a Generative AI-powered Movie Information Extractor built using **LangChain, Mistral AI, Pydantic, and Streamlit**.

The application takes an unstructured paragraph containing movie information and extracts important details such as the **movie title, release year, genre, director, cast, rating, and summary** into a structured format.

## 💡 The Problem & Solution

Movie information is often hidden inside unstructured paragraphs, making it difficult to extract specific details using traditional programming logic.

CineStage uses an **LLM-powered extraction workflow** to understand the paragraph and identify the required movie information according to a predefined **Pydantic schema**.

The schema provides clear format instructions to the Mistral AI model, helping produce consistent and structured output.

## 🛠️ Key Features

* 🎯 **Structured Data Extraction**
  Extracts movie information according to a predefined Pydantic schema.

* 🤖 **Mistral AI Integration**
  Uses `mistral-small-2506` through LangChain for intelligent information extraction.

* 📝 **Prompt Engineering**
  Uses carefully designed prompts and Pydantic format instructions to guide the model's output.

* 💻 **Interactive Streamlit UI**
  Provides a simple and user-friendly interface where users can enter a paragraph and extract movie information.

* 🔐 **Environment Security**
  API credentials are stored securely using `.env` configuration instead of hardcoding them in the source code.

## 🧩 Technologies Used

* **Python**
* **LangChain**
* **Mistral AI**
* **Pydantic**
* **Streamlit**
* **python-dotenv**

## ⚙️ How It Works

The application follows a simple workflow:

```text
User enters a paragraph
        ↓
Streamlit Interface
        ↓
LangChain Prompt
        ↓
Mistral AI
        ↓
Pydantic Format Instructions
        ↓
Structured Movie Information
```

## 📋 Extracted Information

The application extracts the following movie information:

| Field          | Description                 |
| -------------- | --------------------------- |
| `title`        | Movie title                 |
| `release_year` | Year the movie was released |
| `genre`        | Movie genre(s)              |
| `director`     | Movie director              |
| `cast`         | Main cast members           |
| `rating`       | Movie rating                |
| `summary`      | Movie summary               |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [YOUR_GITHUB_REPOSITORY_URL]
```

### 2. Navigate to the Project

```bash
cd CineStage
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

### 5. Run the Application

```bash
streamlit run UIcore.py
```

The application will open in your browser.

## 🎥 Project Demo

Check out the short screen recording below to see CineStage in action.

## 📚 What I Learned

This project helped me gain practical experience with:

* Generative AI and LLMs
* LangChain
* Mistral AI
* Prompt engineering
* Structured information extraction
* Pydantic schemas
* Streamlit application development
* Environment variable management

This is just the beginning of my Generative AI journey. 🚀

I'm excited to continue learning and building more advanced **LLM and Agentic AI applications**.

## 🔗 Connect With Me

If you're interested in **Generative AI, LLM applications, LangChain, or AI engineering**, feel free to connect and share your thoughts.

---

⭐ If you find this project interesting, consider giving the repository a star!
