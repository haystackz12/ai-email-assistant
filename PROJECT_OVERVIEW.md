# 📧 AI Email Assistant: Supercharged with AI

This project showcases a sophisticated AI-powered email assistant built using Python and Streamlit, leveraging the power of the Google Gemini API. It's designed to significantly streamline your email drafting process, offering extensive customization and intelligent features for both new emails and replies.

---

## ✨ Live Application

Experience the AI Email Assistant live! Click here:
👉 [**Launch the AI Email Assistant on Streamlit Cloud**](https://ai-email-assistant-axv2ad79p8meh66awec9zc.streamlit.app/) 👈
*(Remember to replace `YOUR_STREAMLIT_APP_URL_HERE` with your actual deployed app link on Streamlit Community Cloud after deployment.)*

---

## 🌟 Key Features & Improvements

This application has evolved to include a wide array of functionalities, making it a powerful tool for various email needs:

### **Core Email Generation**

* **Contextual Email Generation:** Provide keywords or a brief context, and the AI will generate a full, coherent email draft.

* **Scenario/Template Selector:** Choose from 50+ pre-defined email scenarios (e.g., Meeting Request, Job Application Follow-up, Sales Pitch, Apology Email) across professional, casual, marketing, internal, support, recruitment, event, announcement, educational, and personal categories. Selecting a scenario pre-populates the subject and context for a quick start.

* **Language Selection:** Generate emails in multiple languages (English, Spanish, French, German, Japanese, Mandarin, Arabic, Portuguese, Italian, Korean, Russian).

### **Customization & Control**

* **Expanded Tone Selection:** Choose from a wide range of predefined tones (Professional, Friendly, Urgent, Empathetic, Persuasive, Concise, Casual, Formal, Humorous, Sarcastic, Direct) or define a completely custom tone.

* **Email Length Control:** Specify the desired length for the generated email (Short, Medium, or Long) to control verbosity.

* **Key Phrases/Keywords to Include:** Add specific words, phrases, or names that *must* be incorporated into the generated email.

* **Customizable Call-to-Action (CTA):** Define a specific call-to-action that the AI should clearly include in the email (e.g., "Please schedule a call," "Review the attached document by Friday").

* **Attachment Mention:** Instruct the AI to mention planned attachments by name, ensuring phrases like "Please find attached..." are naturally integrated.

* **Sender Information:** Include optional fields for your name and title/company to personalize the email's closing signature.

### **Reply & Analysis Features**

* **"Reply to an Existing Email" Mode:** Toggle a mode where you can paste the content of an original email. The AI will then generate a contextual reply based on your instructions.

* **Content Summarization (for Reply Mode):** With a click, summarize the pasted original email to quickly grasp its key points and action items.

* **Sentiment Analysis (for Reply Mode):** Automatically analyze and display the sentiment (Positive, Neutral, Negative, Mixed) of the original email, helping you tailor your reply's tone.

### **Usability & Workflow Enhancements**

* **Generated Email History:** Stores the last 5 generated email drafts within the current session, allowing you to review and compare previous outputs.

* **Clear All Inputs Button:** Conveniently placed at both the top and bottom of the input form to reset all fields and start fresh.

* **Scroll to Generated Email:** The page automatically scrolls down to the generated email section once a draft is produced, improving user flow.

* **Generated Word Count Display:** Provides an instant word count for the generated email, helping you meet length requirements.

* **Iterative Prompt Refinement:** After an email is generated, you can provide additional instructions to refine it further, making the iteration process seamless.

### **Advanced AI Control**

* **Custom AI Parameters:** Fine-tune the AI's behavior with sliders for "Creativity (Temperature)" and a number input for "Max Output Tokens," giving power users more control over the generated content's style and length.

* **Dynamic Placeholders:** The AI is instructed to use generic placeholders (e.g., `[Recipient's Name]`, `[Meeting Date]`) when specific details are not provided, making the drafts easily customizable.

## 🛠️ How It Was Built

* **Frontend & Backend (Python Web App):** [Streamlit](https://streamlit.io/)

* **AI Model:** [Google Gemini API](https://ai.google.dev/gemini-api) (`gemini-2.0-flash` model)

* **HTTP Requests:** `requests` Python library

* **Styling:** Custom CSS (leveraging some Tailwind-like principles for a clean, modern look).

## 🚀 How to Run Locally

To get this AI Email Assistant running on your local machine:

1.  **Clone the repository:**
    If you haven't already, clone this GitHub repository to your local machine:

    ```bash
    git clone [https://github.com/haystackz12/ai-email-assistant.git](https://github.com/haystackz12/ai-email-assistant.git)
    cd ai-email-assistant
    ```

2.  **Create a virtual environment (recommended):**
    This isolates your project dependencies.

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

    (Ensure `requirements.txt` contains `streamlit` and `requests`).

4.  **Set up your Google Gemini API Key:**

    * Obtain your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

    * In your project's root directory (`ai-email-assistant`), create a folder named `.streamlit` (if it doesn't exist):

        ```bash
        mkdir .streamlit
        ```

    * Inside the `.streamlit` folder, create a file named `secrets.toml`:

        ```bash
        touch .streamlit/secrets.toml
        ```

    * Open `secrets.toml` with a text editor and add your API key in the following format:

        ```toml
        GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
        ```

        **Important:** Replace `"YOUR_ACTUAL_GEMINI_API_KEY_HERE"` with your actual key, keeping the quotation marks.
        **Security Note:** It's crucial **NOT** to commit `secrets.toml` to your public GitHub repository. Ensure `.streamlit/secrets.toml` is listed in your `.gitignore` file.

5.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    Your web browser should automatically open the application, usually at `http://localhost:8501`.

## 💡 Understanding the Output

The generated email drafts will adapt based on all the inputs you provide (context, tone, length, key phrases, CTA, attachments, language, and sender info).

* **Structure:** Emails typically follow a standard format: Salutation, Body, Closing, and Signature.

* **Placeholders:** If your context doesn't provide specific details for things like names, dates, or project names, the AI is designed to use clear placeholders (e.g., `[Recipient's Name]`, `[Meeting Date]`) that you can easily fill in manually.

* **Copying:** Use the "Copy Email Content to Clipboard" button to quickly transfer the AI-generated email body (excluding the To/Subject lines you entered) to your clipboard for pasting into your email client.

## 🚀 Future Enhancements (Conceptual)

While already powerful, here are some ideas for how this assistant could evolve:

* **Direct Calendar Integration:** Implement a "Schedule Meeting" button that uses no-code automation platforms (like Zapier or Make) to create calendar events in Google Calendar, Outlook Calendar, etc., based on the email content.

* **Draft Sending (via API):** Integrate with email service APIs (e.g., SendGrid, Mailgun) to allow sending drafted emails directly from the app (requires more complex authentication and scope).

* **Email Template Saving:** Allow users to save their own custom scenarios or preferred configurations as reusable templates.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
