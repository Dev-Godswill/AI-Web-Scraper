# <a name="webscraper"></a> AI-Powered Web Scraper: Automating Web Content Extraction and Parsing with OpenAI and Streamlit

## Table of Contents
- [Code Breakdown and Overview](#code-breakdown-and-overview)
- [Code Segments Breakdown](#code-segments-breakdown)
- [Skills Acquired](#skills-acquired)
- [Technologies Used](#technologies-used)
- [How To Run the Code](#how-to-run-the-code)
- [Contributing](#contributing)

## <a name="detailed-breakdown"></a> Code Breakdown and Overview

The code provided creates an AI-powered web scraper application using Streamlit, Selenium, BeautifulSoup, and OpenAI. Its primary function is to scrape content from a website and then allow users to interact with the extracted data by asking questions about it. The AI, through OpenAI’s API, helps parse and extract specific information based on user queries.

This project involves several programming skills such as:

* **Web scraping** using Selenium and BeautifulSoup.
* **Natural Language Processing (NLP)** by integrating OpenAI's models to analyze and extract specific information from web data.
* **User interface design** with Streamlit for an interactive experience.
* **API integration** by connecting to the OpenAI API for content parsing.
* **Handling large datasets** by splitting content into chunks for efficient processing.

## Code Segments Breakdown:
a. **main.py**
      import streamlit as st
      from scrape import (
          scrape_website,
          extract_body_content,
          clean_body_content,
          split_dom_content,
      )
      from parse import parse_with_openai


* **API Integration:** Integrating Google’s Generative AI API for content generation.
* **Web Development with Streamlit:** Building interactive web apps with file uploads, user inputs, and downloadable results.
* **PDF Generation:** Utilizing FPDF to convert generated questions into a professional-looking PDF.
* **Error Handling:** Managing different file encodings and edge cases during text extraction.

## Technologies Used
* **Streamlit:** Used to create the web interface for uploading documents, interacting with users, and displaying MCQs.
* **pdfplumber:** A library for extracting text from PDF documents.
* **python-docx:** Extracts text from DOCX (Microsoft Word) files.
* **FPDF:** A lightweight library to generate PDF files.
* **Google Generative AI (Gemini Model):** This API is used to generate the actual MCQs from the text provided by the user.
* **OS Module:** Handles file paths and directory creation.

## How To Run the Code
To run the code on your local machine, follow these steps:

**Step 1: Clone the Repository and Install Requirements**

1. Clone the project repository or copy the code to your local machine.
2. Ensure you have Python installed.
3. Create a virtual environment (optional but recommended):

<img width="722" alt="MCQ-Generator" src="https://github.com/Dev-Godswill/picture-files/blob/main/23.png?raw=true">

    Then, activate the virtual environment:
      **Windows:** env\Scripts\activate
      **Mac/Linux:** source env/bin/activate
      
4. Install the required Python libraries. If you have a requirements.txt file (as you do), you can install the dependencies directly:

<img width="722" alt="MCQ-Generator" src="https://github.com/Dev-Godswill/picture-files/blob/main/24.png?raw=true">

**Step 2: Set up API Key**
The project requires an API key to access Google’s Generative AI model. You must set up your **Google API Key** and place it in your environment as follows:

1. Go to Google Cloud Console and generate an API key for the Gemini Model.
2. Update the code where the GOOGLE_API_KEY is required:

<img width="722" alt="MCQ-Generator" src="https://github.com/Dev-Godswill/picture-files/blob/main/25.png?raw=true">

**Step 3: Run the Streamlit Application**
Once the environment is set up and dependencies are installed, run the Streamlit web app using the following command:

<img width="722" alt="MCQ-Generator" src="https://github.com/Dev-Godswill/picture-files/blob/main/26.png?raw=true">

Replace your_script_name.py with the name of the script that contains the code above.

**Step 4: Access the Web Interface**
After running the Streamlit app, a URL will be provided in your terminal (usually http://localhost:8501). Open this in your web browser to start using the MCQ generator.

**Step 5: Upload Files and Generate MCQs**
* Upload a text document in PDF, DOCX, or TXT format.
* Specify the number of questions you want to generate.
* Download the MCQs as TXT or PDF files.

## Contributing
Contributions to this project is welcome! If you'd like to contribute, please follow these steps:
- Fork the project repository. 
- Create a new branch: git checkout -b feature/your-feature-name. 
- Make your changes and commit them: git commit -am 'Add your commit message'. 
- Push the changes to your branch: git push origin feature/your-feature-name. 
- Submit a pull request detailing your changes.

*Feel free to modify and adapt the project to your needs. If you have any questions or suggestions, please feel free to contact me: godswillodaudu@gmail.com*.
