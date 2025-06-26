# 📧 AI Email Assistant (Streamlit)

This is an AI-powered email assistant built with Streamlit and the Google Gemini API. It allows users to quickly generate email drafts based on a provided context and desired tone, streamlining the email writing process.

## ✨ Live Application

Experience the AI Email Assistant live! Click here:
👉 **[Launch the AI Email Assistant on Streamlit Cloud](https://ai-email-assistant-axv2ad79p8meh66awec9zc.streamlit.app/)** 👈

## ✨ Features

* **Contextual Email Generation:** Input keywords or context to get a full email draft.
* **Tone Selection:** Choose from various tones (Professional, Friendly, Urgent, Empathetic, Persuasive, Concise, Casual, Formal, Humorous, Sarcastic, Direct, Custom).
* **Email Length Control:** Specify short, medium, or long email drafts.
* **Key Phrases/Keywords to Include:** Ensure specific words or phrases are incorporated.
* **Sender Information Fields:** Include your name and title/company for a personalized closing.
* **Pre-defined Scenario/Template Selector:** Choose from 50+ common email scenarios.
* **"Reply to an Existing Email" Mode:** Generate replies based on pasted original email content.
* **Generated Email History (Session-based):** View previous drafts within the current session.
* **Clear All Inputs Button:** Easily reset all input fields.
* **Generated Word Count Display:** See the length of your generated email.
* **Iterative Prompt Refinement:** Quickly refine the last generated email with new instructions.
* **Content Summarization (for Reply Mode):** Summarize original emails.
* **Sentiment Analysis of Original Email (for Reply Mode):** Get quick sentiment feedback on original emails.
* **Attachment Mention / Placeholder:** Instruct the AI to mention attachments by name.
* **Language Selection for Output:** Generate emails in multiple languages.
* **Custom AI Parameters:** Adjust creativity (temperature) and max output tokens.
* **Customizable Call-to-Action (CTA) Prompts:** Ensure specific calls to action are included.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/haystackz12/ai-email-assistant.git](https://github.com/haystackz12/ai-email-assistant.git)
    cd ai-email-assistant
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
4.  **Set up your Google Gemini API Key:**
    * Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey).
    * Create a folder named `.streamlit` in your project's root directory: `mkdir .streamlit`
    * Inside `.streamlit`, create a file named `secrets.toml`: `touch .streamlit/secrets.toml`
    * Open `secrets.toml` and add your API key:
        ```toml
        GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
        ```
        (Replace `YOUR_ACTUAL_GEMINI_API_KEY_HERE` with your actual key, keeping the quotes.)
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The app will open in your web browser, usually at `http://localhost:8501`.

## ⚙️ API Key

This application uses the Google Gemini API. When deployed on platforms like Streamlit Community Cloud, the API key is typically handled securely as a secret. For local development, it's read from `.streamlit/secrets.toml`. **Do NOT commit your `secrets.toml` file to GitHub.** Add `.streamlit/secrets.toml` to your `.gitignore` file if you haven't already.

## License

This project is open source and available under the [MIT License](LICENSE).