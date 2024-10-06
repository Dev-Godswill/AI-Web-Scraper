# <a name="webscraper"></a> AI-Powered Web Scraper: Automating Web Content Extraction and Parsing with OpenAI and Streamlit

## Table of Contents
- [Code Breakdown and Overview](#code-breakdown-and-overview)
- [Code Segments Breakdown](#code-segments-breakdown)
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
This is the main application file where the Streamlit interface is set up. It collects user input (URL and query) and displays the results of the scraping and parsing.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/27.png?raw=true">
* Imports necessary functions from the scrape.py and parse.py files.
* UI Elements: Uses Streamlit’s st.text_input() and st.button() to collect the website URL and the query for parsing.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/28.png?raw=true">
* Displays a simple UI title and input box for users to enter the URL of the website they want to scrape.
* Scrape the Website: When the "Scrape Website" button is clicked, the program scrapes the webpage and displays the DOM content.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/29.png?raw=true">
* Parse the Content: If content has been scraped, the user can input a description of what they want to extract from the content using OpenAI’s GPT model.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/30.png?raw=true">
This parses the content and displays the result using OpenAI based on the user’s description.

b. **parse.py**
This file contains the logic for **parsing web content** using the OpenAI API.

* **API Configuration:**

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/31.png?raw=true">
* **Prompt Template:** The template defines the structure of the input sent to OpenAI, ensuring only the desired information is extracted based on the user description.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/32.png?raw=true">

* **parse_with_openai function:** This function sends chunks of the scraped content to the OpenAI model and retrieves the parsed results.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/33.png?raw=true">

c. **scrape.py**

This file contains the logic for web scraping using Selenium and BeautifulSoup.

* **Selenium Setup:**

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/34.png?raw=true">

* **scrape_website function:** This function uses Selenium to access the target website and retrieve its HTML content.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/35.png?raw=true">

* **extract_body_content and clean_body_content functions:** These functions use BeautifulSoup to extract and clean the text content of the webpage.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/36.png?raw=true">

* **split_dom_content:** This function splits the DOM content into smaller chunks to handle large text inputs for processing by the OpenAI API.

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/37.png?raw=true">

## Technologies Used
* **Streamlit:** Used for building a simple and interactive user interface.
* **Selenium:** Automates the process of opening a browser, navigating to a webpage, and scraping its content.
* **BeautifulSoup:** Extracts and processes specific HTML elements from the webpage.
* **OpenAI API:** Leverages GPT models for processing and extracting information from the scraped content.
* **Python Dotenv:** Loads environment variables, such as the OpenAI API key, from a .env file.

## How To Run the Code
**Prerequisites:**
1. **Python Installation:** Make sure Python 3.x is installed on your system.
2. **Chromium WebDriver:** Install Chromium and configure it for Selenium scraping.
3. **OpenAI API Key:** Sign up for OpenAI and get your API key to use GPT models.

**Steps:**
1. **Install Required Libraries:**
     * Create a requirements.txt file with the necessary libraries (e.g., Selenium, BeautifulSoup, OpenAI, Streamlit).
     * Install dependencies using:

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/38.png?raw=true">

2. **Set Up Environment Variables:**
     * Create a .env file and add your OpenAI API key:

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/39.png?raw=true">

3. **Run the Streamlit Application:**
     * In the terminal, navigate to the project directory and run:

<img width="722" alt="webscraper" src="https://github.com/Dev-Godswill/picture-files/blob/main/40.png?raw=true">

4. **Access the Application:**
     * Open the provided local URL (usually http://localhost:8501) in your browser.
     * Input a website URL and describe the data you want to extract. The application will scrape the webpage and parse the content using OpenAI.

## Contributing
Contributions to this project is welcome! If you'd like to contribute, please follow these steps:
- Fork the project repository. 
- Create a new branch: git checkout -b feature/your-feature-name. 
- Make your changes and commit them: git commit -am 'Add your commit message'. 
- Push the changes to your branch: git push origin feature/your-feature-name. 
- Submit a pull request detailing your changes.

*Feel free to modify and adapt the project to your needs. If you have any questions or suggestions, please feel free to contact me: godswillodaudu@gmail.com*.
