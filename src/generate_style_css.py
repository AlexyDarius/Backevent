def generate_style_css(directory_path, bg_color, color):
    css_code = f'''/* Add styles for the login container */
#login-container {{
    text-align: center;
    margin: 20px;
}}

.image-box {{
    max-width: 500px;
    margin: 10px;
    background-color: #fff;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    padding: 10px;
    text-align: center;
}}

.image-box img {{
    max-width: 100%;
    height: auto;
}}

form {{
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
}}

label, input {{
    display: block;
    margin: 10px 0;
}}

input[type="text"], input[type="password"] {{
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}}

button {{
    background-color: {bg_color};
    color: {color};
    padding: 10px 20px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}}

.edit-container input[type="text"] {{
    max-width: 100%; /* Adjust this value as needed */
    box-sizing: border-box; /* Keeps the input within its container */
}}


'''

    with open(f"{directory_path}/backevent/css/style.css", "w") as js_file:
        js_file.write(css_code)
        print("style.css generated !")
