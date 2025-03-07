# Imports
import streamlit as st
import readme_generator as rg

# Page Setup
favicon = 'favicon.ico'
st.set_page_config(page_title='README.gen', page_icon=favicon, layout="wide")

# Styling
st.markdown("""
        <style>
        .stButton button {
            display: block;
            margin: 0 auto;
            background-color: #00BF63;
            color: white;
        }

        .download_button button {
            display: block;
            margin: 0 auto;
            background-color: #00BF63;
            color: white;
        }

        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            color: white;
            background-color: #00BF63; 
            padding-top: 10px;
            text-align: center;
        }

        a:link , a:visited {
            color: white;
            background-color: transparent;
            text-decoration: underline;
        }
        a {
            display: block; 
            text-align: center; 
            color: white
        }
        h1 {
            text-align: center; 
            color: #00BF63
        }
                
        h2 {
           text-align: center;     
        }
        a:hover,  a:active {
            color: white;
            background-color: transparent;
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <h1>README.gen</h1>
            <br>
    <h2>Streamline project documentation with AI-powered efficiency</h2>
    """, unsafe_allow_html=True)

# Files Uploader
uploaded_files = st.file_uploader("Upload your code files:", accept_multiple_files=True)

# Generate Readme Button
if st.button("Generate README"):
    if not uploaded_files:
        st.warning("Please upload your code files before generating the README.")
    else:        
        content = ""
        for uploaded_file in uploaded_files:
            try:
                content += uploaded_file.read().decode('utf-8') + "\n\n"
                print("Inside UTF-8 try")
            except UnicodeDecodeError:
                print("Inside Except")
                # try:
                #     content += uploaded_file.read().decode('latin-1') + "\n\n"
                #     print("INside UnicodeDecode Try")
                # except UnicodeDecodeError:
                print("Inside UnicodeDecode Error")
                st.error(f"Could not decode file {uploaded_file.name}. Please ensure the file is properly encoded.")
                print("Inside UnicodeDecode Error")
            
        if content:
            prompt = (
                "You are an AI trained to generate professional README.md files. "
                "Given the following code snippet(s), analyze their structure, purpose, and functionality. "
                "Then, create a detailed and well-formatted README.md file in Markdown format that includes sections such as "
                "`Title`, `Description`, `Installation Instructions`, `Usage`, `Examples`, and `License`. \n\n"
                "Here is the code:\n\n"
                f"{content}\n"
                "```\n"
                "Based on the analysis, generate the README.md file."
            )
            response = rg.ask(prompt)
            if response == "False":
                st.error("Server currently down")
            # Column Section
            else:
                st.markdown("""<h2>Your README.md is generated</h2>""", unsafe_allow_html=True)
                st.markdown("""----""")
                readme_col, preview_col = st.columns(2)
                st.column_config.Column(width="maximum")

                # README Column
                with readme_col:
                    st.subheader("Markdown")
                    st.code(response)
                
                # Preview Column
                with preview_col:
                    st.subheader("Preview")
                    st.markdown(response)
                
                # Download Button
                st.markdown("---")
                download_button = st.download_button(
                    label="Download README.md",
                    data=response.encode(),
                    file_name="README.md",
                    mime="text/markdown",
                    key="download_button"
                )

# Footer 
footer = """
<div class="footer">
    <p>Developed with ❤ by <a href="https://fluttersolutions.in" target="_blank">Manan R. Gandhi</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
