# 🏎️ F1 Vector QA (FAISS + Ollama)

A local, privacy-respecting Question Answering system built with FAISS, Sentence Transformers, and the Ollama LLM. Ask anything about Formula 1 and get accurate answers from your custom dataset!

## 🔧 Features

- 🧠 Uses local LLMs via [Ollama](https://ollama.com/) (e.g. LLaMA2)
- 🧷 Fast semantic search with FAISS
- ✨ Clean embedding generation with `all-MiniLM-L6-v2`
- 📄 Works on any `.txt` knowledge base
- 🌐 CLI-based interaction

## 🗂️ Project Structure

<pre> ```text f1-vector-qa/ ├── data/ │ └── f1_knowledge.txt # Your Formula 1 knowledge base ├── app.py # Main Python script ├── requirements.txt # Required dependencies └── README.md # Project documentation ``` </pre>


## 🚀 Getting Started

### 1. Clone the repo

```bash

git clone https://github.com/your-username/f1-vector-qa.git
cd f1-vector-qa

```
### 2. Set up virtual environment

```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Start Ollama and load a model

```bash
ollama run llama2

```

### 5. Run the app

```bash
python app.py

```

#### Example Interaction

```bash
Ask anything about F1 ➤ Who won the 2023 World Championship?
🧠 Answer:
Max Verstappen dominated the 2023 F1 season and secured the championship title with Red Bull Racing.

```
