# RAG-ai-teaching-assistant
A RAG-based AI teaching assistant for finding relevant content in a large playlist.


## How It Works

This project implements a Retrieval-Augmented Generation (RAG) pipeline for an AI teaching assistant that helps students find relevant concepts in recorded machine learning lectures.

### 1. Video-to-Audio Conversion
Educational videos are converted into MP3 audio files using FFmpeg.

### 2. Speech Transcription
Audio files are transcribed using Whisper, producing JSON data containing lecture text and associated metadata.

### 3. Text Chunking
Transcripts are divided into smaller chunks while preserving relevant information, including lecture titles, video numbers, timestamps, and text.

### 4. Embedding Generation
Ollama's BGE-M3 embedding model converts each text chunk into a vector representation. The vectors and chunk metadata are stored in `embeddings.joblib`.

### 5. Semantic Retrieval
When a user submits a question, the system generates an embedding for that question. It calculates cosine similarity between the question vector and the stored chunk embeddings, then retrieves the five most similar chunks.

### 6. Answer Generation
The retrieved chunks, along with their lecture titles and timestamps, are added to a prompt and passed to the Llama 3.2 model through Ollama.

### 7. Lecture Navigation
The assistant generates a natural-language answer identifying relevant lectures and timestamps so students can locate the corresponding content.

## Technology Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Embeddings:** BGE-M3 through Ollama
- **Language Model:** Llama 3.2 through Ollama
- **Speech Recognition:** Whisper
- **Media Processing:** FFmpeg
- **Data Storage:** JSON and Joblib

## Running the Assistant

1. Start Ollama and ensure the required models are available.
2. Generate the lecture transcripts and chunks.
3. Generate and save the embeddings to `embeddings.joblib`.
4. Run the inference script.
5. Enter a question about the course when prompted.

The assistant retrieves relevant lecture segments and generates an answer with video titles and timestamps.
