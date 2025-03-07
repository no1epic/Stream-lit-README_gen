README.gen
favicon

Table of Contents
Description
Installation
Usage
Examples
License
Description
README.gen is a powerful Streamlit application designed to streamline the process of creating professional README.md files. By leveraging the power of AI, README.gen analyzes your code snippets and automatically generates comprehensive and well-structured documentation, minimizing the effort and time required for project documentation.

Installation
Follow these steps to install the necessary dependencies and set up the application:

Clone the repository:

git clone https://github.com/mananrg/Streamlit-README.gen
cd readmegen
Create a virtual environment (optional but recommended):

python -m venv streamlit
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

pip install -r requirements.txt
Add your OpenAI API key to Streamlit secrets: Create a file named secrets.toml in the .streamlit directory of the project and add your OpenAI API key:

OPENAI_API_KEY = "your_openai_api_key_here"
Usage
Run the application:

streamlit run app.py
Upload your code files:

Click on the "Upload your code files" button to upload one or more code files that need to be documented.
Generate the README:

Click on the "Generate README" button. If you haven't uploaded any files, you will be prompted to do so.
Upon generating, the application will display the Markdown content of the README on the left column and a preview on the right column.
Download the generated README:

Click on the "Download README.md" button to download the generated README file.
Examples
Here's an example walkthrough of the generated README.md file by README.gen:

Example Code Snippet
Consider the following code snippet:

# A simple Python example
def hello_world():
    print("Hello, World!")
This code would result in a generated README content similar to:

Hello World Example
Description
This project contains a simple Python script to print "Hello, World!" to the console.

Usage
Run the following command to execute the script:

python hello_world.py
Examples
The script will output:

Hello, World!
