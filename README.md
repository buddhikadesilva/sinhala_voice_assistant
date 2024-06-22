# Sinhala Voice Assistant

This project aims to create a Sinhala voice assistant using Python. The assistant leverages existing English language models and performs intermediate translation to and from Sinhala. The primary libraries used in this project are `translate`, `ollama`, and `gTTS`.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Sinhala Voice Assistant is designed to provide a seamless interaction experience in Sinhala by utilizing English language models for natural language processing. The process involves translating user inputs in Sinhala to English, processing the input using the language model, and then translating the output back to Sinhala.

## Features

- Voice input and output in Sinhala
- Intermediate translation between Sinhala and English
- Utilizes existing English language models for robust NLP
- Text-to-speech conversion using Google Text-to-Speech (gTTS)

## Installation

To get started with the Sinhala Voice Assistant, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/buddhikadesilva/sinhala_voice_assistant.git
   cd sinhala_voice_assistant
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Sinhala Voice Assistant, use the following command:

```bash
python main.py
```

### Example Code

Here is a basic example of how the assistant works:

```python
from translate import Translator
import ollama
from gtts import gTTS
import os

# Initialize translators
translator_to_english = Translator(to_lang="en", from_lang="si")
translator_to_sinhala = Translator(to_lang="si", from_lang="en")

# Input in Sinhala
input_text_sinhala = "ඔබ කෙසේද?"

# Translate to English
input_text_english = translator_to_english.translate(input_text_sinhala)

# Process using English language model (placeholder for actual model usage)
response_english = ollama.query(input_text_english)

# Translate response back to Sinhala
response_sinhala = translator_to_sinhala.translate(response_english)

# Convert text to speech
tts = gTTS(text=response_sinhala, lang='si')
tts.save("response.mp3")
os.system("mpg321 response.mp3")
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Description of the feature or fix"
   ```
4. Push to the branch.
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
