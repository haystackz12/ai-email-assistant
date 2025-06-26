import streamlit as st
import requests
import json
import base64

# --- Configuration ---
# Your API Key will be automatically provided by the Canvas environment at runtime.
# DO NOT add your API key directly here.
API_KEY = ""
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# --- Utility Function for Copy to Clipboard (for Streamlit on some platforms) ---
# This function is a workaround for copy-to-clipboard in some Streamlit deployment
# environments where navigator.clipboard might be restricted.
def copy_to_clipboard_js():
    js_code = """
    function copyTextToClipboard(text) {
        var textArea = document.createElement("textarea");
        textArea.value = text;
        textArea.style.position = "fixed";  // Avoid scrolling to bottom
        textArea.style.left = "-9999px";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            // console.log('Copying text command was ' + msg);
        } catch (err) {
            // console.error('Oops, unable to copy', err);
        }
        document.body.removeChild(textArea);
    }
    """
    st.components.v1.html(f"<script>{js_code}</script>", height=0)


# --- AI Email Generation Function ---
def generate_email_with_gemini(prompt_text):
    """
    Calls the Gemini API to generate email content based on a prompt.
    """
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt_text}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,  # Controls randomness. Lower for more focused.
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 800,
        }
    }

    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        result = response.json()

        if result and result.get("candidates"):
            first_candidate = result["candidates"][0]
            if first_candidate.get("content") and first_candidate["content"].get("parts"):
                return first_candidate["content"]["parts"][0]["text"]
        
        st.error("AI did not return a valid response. Please try again.")
        st.json(result) # Display full result for debugging
        return None

    except requests.exceptions.RequestException as e:
        st.error(f"Error calling Gemini API: {e}. Please check your internet connection or try again.")
        return None
    except json.JSONDecodeError:
        st.error("Failed to parse JSON response from API.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

# --- Streamlit Application Layout ---

st.set_page_config(layout="wide", page_title="AI Email Assistant")

# Apply custom CSS for styling (Tailwind-like approach via Streamlit's markdown)
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    .stTextArea>div>div>textarea {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    .stSelectbox>div>div {
        border-radius: 8px;
        padding: 5px;
        border: 1px solid #ccc;
    }
    .stMarkdown h1 {
        color: #2c3e50;
        font-family: 'Inter', sans-serif;
        text-align: center;
        margin-bottom: 1rem;
    }
    .stMarkdown h2 {
        color: #34495e;
        font-family: 'Inter', sans-serif;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .stMarkdown p {
        font-family: 'Inter', sans-serif;
        color: #555;
    }
    .email-output-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
        min-height: 200px;
        white-space: pre-wrap; /* Preserve whitespace and wrap text */
        font-family: 'Courier New', monospace; /* Monospace for code-like output */
        font-size: 14px;
        color: #333;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

st.title("📧 AI Email Assistant")
st.write("Generate professional, friendly, or urgent email drafts instantly using AI.")

# Input Fields
with st.container():
    st.markdown("---")
    st.subheader("Email Details")

    col1, col2 = st.columns(2)
    with col1:
        recipient = st.text_input("Recipient (e.g., info@example.com)", "recipient@example.com")
    with col2:
        subject = st.text_input("Subject Line", "Meeting Follow-up")

    st.markdown("---")
    st.subheader("Email Content & Tone")

    keywords_context = st.text_area(
        "Keywords or Context (e.g., 'follow up on last meeting, discussed project proposal, next steps')",
        "Follow up on our last meeting. Discuss project proposal. Outline next steps for implementation. Emphasize collaboration.",
        height=150
    )

    tone_options = [
        "Professional", "Friendly", "Urgent", "Empathetic", "Persuasive", "Concise", "Casual", "Formal"
    ]
    selected_tone = st.selectbox("Desired Tone", tone_options)

    # Generate Button
    if st.button("Generate Email Draft"):
        if not keywords_context:
            st.warning("Please provide some keywords or context to generate the email.")
        else:
            prompt = (
                f"Draft an email for a recipient with the subject '{subject}'.\n"
                f"Context/Keywords: {keywords_context}\n"
                f"Desired Tone: {selected_tone}\n"
                f"Please provide the complete email, starting with a salutation and ending with a closing."
            )
            
            with st.spinner("Generating email draft..."):
                generated_email_content = generate_email_with_gemini(prompt)
            
            if generated_email_content:
                st.session_state['generated_email'] = generated_email_content
                st.session_state['recipient'] = recipient
                st.session_state['subject'] = subject

# Display Generated Email
if 'generated_email' in st.session_state and st.session_state['generated_email']:
    st.markdown("---")
    st.subheader("Generated Email Draft")

    full_email_display = (
        f"**To:** {st.session_state['recipient']}\n"
        f"**Subject:** {st.session_state['subject']}\n\n"
        f"{st.session_state['generated_email']}"
    )
    
    st.markdown(
        f'<div class="email-output-box">{full_email_display}</div>',
        unsafe_allow_html=True
    )

    copy_to_clipboard_js()
    if st.button("Copy Email to Clipboard"):
        # The JavaScript function will be called on button click
        st.components.v1.html(
            f"""
            <script>
                copyTextToClipboard({json.dumps(st.session_state['generated_email'])});
            </script>
            """,
            height=0
        )
        st.success("Email copied to clipboard!")

st.markdown("---")
st.write("Powered by Google Gemini.")
