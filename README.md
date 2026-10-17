
# Lkhibra AI Chatbot

A simple AI chatbot built with Python, Streamlit,
and Groq API.

The chatbot answers questions using information
stored in a JSON file and remembers the conversation
during the current session.

## Features

- AI-powered responses using Groq
- Knowledge stored in JSON
- Conversation memory using Streamlit
- Chat interface
- Clear conversation button
- API error handling
- No database required

## Project Structure

lkhibra-chatbot/
├── app.py
├── knowledge.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## 1. Create a Virtual Environment

Open a terminal in the project folder.

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Groq API

Visit:

https://console.groq.com/keys

Create an API key.

Open the `.env` file and replace the placeholder:

```env
GROQ_API_KEY=your_actual_api_key
```

Never commit your real API key to GitHub.

## 4. Customize the Knowledge

Open `knowledge.json`.

You can modify:

- Chatbot personality
- System instructions
- Academy information
- Training details
- Pricing
- Contact information

## 5. Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your browser.

Default URL:

http://localhost:8501

## How It Works

1. The application loads information from knowledge.json.
2. The user sends a message.
3. Streamlit stores the message in session_state.
4. The application sends the instructions, knowledge,
   and conversation history to Groq.
5. Groq generates a response.
6. The response appears in the chat interface.
7. Streamlit saves the response in conversation history.

## AI Model

The application uses:

openai/gpt-oss-20b

Model availability and free-tier limits depend on Groq.

## Limitations

- Conversation history is not permanently saved.
- Restarting or resetting the session can erase messages.
- The chatbot does not use a database.
- The chatbot does not search the internet.
- JSON knowledge is passed as context, not retrieved
  through a dedicated search system.
- AI responses may contain inaccuracies.
