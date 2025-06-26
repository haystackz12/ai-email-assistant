# 📧 AI Email Assistant (Streamlit)

This is an AI-powered email assistant built with Streamlit and the Google Gemini API. It allows users to quickly generate email drafts based on a provided context and desired tone, streamlining the email writing process.

## ✨ Features

* **Contextual Email Generation:** Input keywords or context to get a full email draft.
* **Tone Selection:** Choose from various tones (Professional, Friendly, Urgent, Empathetic, Persuasive, Concise, Casual, Formal).
* **Recipient & Subject Fields:** Easily specify email recipient and subject.
* **Copy to Clipboard:** A convenient button to copy the generated email.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-email-assistant-streamlit.git](https://github.com/YOUR_GITHUB_USERNAME/ai-email-assistant-streamlit.git)
    cd ai-email-assistant-streamlit
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The app will open in your web browser, usually at `http://localhost:8501`.

## ☁️ Deployment (e.g., Streamlit Community Cloud)

This application can be easily deployed to Streamlit Community Cloud:
1.  Push your code to a public GitHub repository.
2.  Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Connect your GitHub account and select this repository.
4.  Streamlit will automatically detect `app.py` and `requirements.txt` and deploy your app!

## ⚙️ API Key

This application uses the Google Gemini API. When deployed on platforms like Streamlit Community Cloud, the API key is typically handled securely as a secret. For local development, you might need to set it as an environment variable or manually insert it (though direct insertion in code for public repos is not recommended).

## License

This project is open source and available under the [MIT License](LICENSE).