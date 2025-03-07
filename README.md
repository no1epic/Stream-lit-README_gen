README.gen

Table of Contents

Overview

Installation

Usage

Examples

License

Overview

README.gen is a robust Streamlit-powered application that simplifies the creation of professional README.md files. By utilizing AI, it analyzes your code snippets and automatically generates well-structured documentation, significantly reducing the effort and time needed for project documentation.

Installation

To set up and install the necessary dependencies, follow these steps:

Clone the Repository

git clone https://github.com/mananrg/Streamlit-README.gen
cd readmegen

Create a Virtual Environment (Optional but Recommended)

python -m venv streamlit
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies

pip install -r requirements.txt

Configure OpenAI API Key

Create a secrets.toml file inside the .streamlit directory and add your OpenAI API key:

OPENAI_API_KEY = "your_openai_api_key_here"

Usage

Launch the Application

streamlit run app.py

Upload Code Files

Click on the "Upload your code files" button to add one or more code files that require documentation.

Generate the README

Click the "Generate README" button. If no files have been uploaded, you will be prompted to do so.

Once generated, the left column will display the README’s Markdown content, while the right column will show a preview.

Download the README

Click on the "Download README.md" button to save the generated README.md file.

Examples

Below is an example demonstrating how README.gen generates documentation for a simple code snippet:

Example Code Snippet

# A simple Python script
def hello_world():
    print("Hello, World!")

Generated README Output

Hello World Example

Description:
This project features a basic Python script that prints "Hello, World!" to the console.

Usage:
Run the script using the following command:

python hello_world.py

Example Output:
