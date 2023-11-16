def generate_uploadBackevent_js(directory_path):
    js_code = f'''function uploadBackevent(event) {{
    event.preventDefault(); // Prevent the form from being submitted normally

    // Check if the button is already disabled
    let createEventButton = document.getElementById('create-backevent-button');
    if (createEventButton.disabled) {{
        return; // Do nothing if the button is already disabled
    }}

    // Disable the button to prevent multiple clicks
    createEventButton.disabled = true;

    let form = document.getElementById('backevent-form');
    let titleInput = document.getElementById('title');
    let placeInput = document.getElementById('place');
    let textInput = document.getElementById('text');
    let errorMessage = document.getElementById('error-message');

    if (titleInput.value.length > 255 || placeInput.value.length > 255 || textInput.value.length > 65535) {{
        errorMessage.textContent = "Input values are too long. Please keep them within specified limits.";
        errorMessage.style.display = 'block'; // Display the error message
        createEventButton.disabled = false; // Enable the button
        return;
    }}

    // Check the number of files
    let maxFiles = 3;
    let imageFiles = document.getElementById('images').files;

    if (imageFiles.length !== maxFiles) {{
        errorMessage.textContent = `Please select exactly ${{maxFiles}} images.`;
        errorMessage.style.display = 'block';
        createEventButton.disabled = false; // Enable the button
        return;
    }}

    // Check the file size
    let maxFileSize = 100 * 1024; // 100KB in bytes
    for (let i = 0; i < imageFiles.length; i++) {{
        if (imageFiles[i].size > maxFileSize) {{
            errorMessage.textContent = "Image size exceeds the maximum allowed size (100KB).";
            errorMessage.style.display = 'block'; // Display the error message
            createEventButton.disabled = false; // Enable the button
            return;
        }}
    }}

    // Reset error message if no errors
    errorMessage.style.display = 'none';

    // AJAX request
    let formData = new FormData(form);

    // Append each file to the FormData object
    for (let i = 0; i < imageFiles.length; i++) {{
        formData.append('images[]', imageFiles[i]);
    }}

    // Create an XMLHttpRequest object
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {{
        if (xhr.readyState === 4) {{
            createEventButton.disabled = false; // Enable the button
            if (xhr.status === 200) {{
                // Event created successfully
                document.getElementById('status-message').textContent = 'Événement créé avec succès !';
                form.reset(); // Clear the form
            }} else {{
                // Event creation failed
                document.getElementById('status-message').textContent = "Impossible de créer l'événement. Réessayez.";
            }}
        }}
    }};

    // Open a POST request to the server
    xhr.open('POST', 'backevent-editor.php', true);

    // Send the form data as the request body
    xhr.send(formData);
}}
'''

    with open(f"{directory_path}/backevent/js/uploadBackevent.js", "w") as js_file:
        js_file.write(js_code)
        print("uploadBackevent.js generated !")
