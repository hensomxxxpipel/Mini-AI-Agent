# Mini AI Agent

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/hensomxxxpipel/Mini-AI-Agent.git
   cd Mini-AI-Agent
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

### Start FastAPI Backend
Run the FastAPI server:
```sh
uvicorn api.main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Start Streamlit Frontend
Run the Streamlit application:
```sh
streamlit run frontend/app.py
```
The frontend will be available at [http://localhost:8501](http://localhost:8501).

## API Endpoint

### POST `/chat`
Accepts user input and returns a response from the LLM model.

## Usage
1. Open the Streamlit UI.
2. Enter a question in the text box.
3. Click the "Send" button.
4. The chatbot will generate a response using LangChain.
