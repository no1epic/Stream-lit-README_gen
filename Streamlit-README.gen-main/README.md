# README.gen

![favicon](favicon.ico)

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Description

**README.gen** is a powerful Streamlit application designed to streamline the process of creating professional README.md files. By leveraging the power of AI, README.gen analyzes your code snippets and automatically generates comprehensive and well-structured documentation, minimizing the effort and time required for project documentation.

## Installation

Follow these steps to install the necessary dependencies and set up the application:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mananrg/Streamlit-README.gen
    cd readmegen
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv streamlit
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add your OpenAI API key to Streamlit secrets**:
    Create a file named `secrets.toml` in the `.streamlit` directory of the project and add your OpenAI API key:
    ```toml
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

## Usage

1. **Run the application**:
    ```bash
    streamlit run app.py
    ```

2. **Upload your code files**:
    - Click on the "Upload your code files" button to upload one or more code files that need to be documented.

3. **Generate the README**:
    - Click on the "Generate README" button. If you haven't uploaded any files, you will be prompted to do so.
    - Upon generating, the application will display the Markdown content of the README on the left column and a preview on the right column.

4. **Download the generated README**:
    - Click on the "Download README.md" button to download the generated README file.

## Examples

Here's an example walkthrough of the generated README.md file by README.gen:

### Example Code Snippet

Consider the following code snippet:
```python
# A simple Python example
def hello_world():
    print("Hello, World!")
```

This code would result in a generated README content similar to:

# Hello World Example

## Description
This project contains a simple Python script to print "Hello, World!" to the console.

## Usage
Run the following command to execute the script:
```bash
python hello_world.py
```

## Examples
The script will output:
```
Hello, World!
```

## License

This project is licensed under the terms of the MIT license. 
---

<div class="footer">
    <p>Developed with ❤ by [Manan R. Gandhi | Sahil Gawande]</p>
</div>
