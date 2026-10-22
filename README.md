
# AI Approval-Based Agent

An AI-powered approval workflow built with Python, Streamlit,
and Groq. The application generates a personalized letter,
allows a human to review and edit it, and requires an explicit
decision before making the approved letter available.

## Features

- AI-generated letters using a Groq-hosted language model
- Human review and editing before approval
- Approve or reject workflow
- Download approved letters
- Input validation
- Automated unit tests

## Tech Stack

- Python
- Streamlit
- Groq API
- OpenAI Python SDK (Groq-compatible API)
- python-dotenv
- unittest

## Project Structure

```text
approval-based-agent/
├── app.py
├── main.py
├── test_main.py
├── test_ai.py
├── requirements.txt
├── README.md
└── .gitignore
```

The local `.env` file stores the API key and must not be
committed to GitHub.

## Run Locally

1. Install Python.
2. Clone or download this repository.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory:

   ```text
   GROQ_API_KEY=your_groq_api_key
   ```

5. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal.

## Run Tests

```bash
python -m unittest test_main.py -v
```

## How It Works

1. The user submits a writing request.
2. The AI generates a draft.
3. The user reviews and edits the draft.
4. The user approves or rejects it.
5. An approved letter becomes available for download.

## Safety and Limitations

- The human must review the generated content before approval.
- The AI may still produce inaccurate information.
- Approval currently prepares a downloadable letter; it does not
  send an email or submit a leave request to an HR system.
- Approval decisions are not yet stored in a persistent audit log.
- API access and usage are subject to Groq's limits and terms.

## Future Improvements

- Persistent approval history
- More document types
- Stronger validation of generated content
- Integration with authorized external services

## Author

Created as a learning project to understand AI agents,
human approval workflows, and application deployment.
