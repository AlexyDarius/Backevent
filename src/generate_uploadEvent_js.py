def generate_uploadEvent_js(directory_path):
    js_code = f'''function uploadEvent(event) {{
    event.preventDefault(); // Prevent the form from being submitted normally

    // Check if the button is already disabled
    let createEventButton = document.getElementById('create-event-button');
    if (createEventButton.disabled) {{
        return; // Do nothing if the button is already disabled
    }}

    // Disable the button to prevent multiple clicks
    createEventButton.disabled = true;

    let form = document.getElementById('event-form');
    let titleInput = document.getElementById('title');
    let placeInput = document.getElementById('place');
    let textInput = document.getElementById('text');
    let errorMessage = document.getElementById('error-message');

    if (titleInput.value.length > 255) {{
        errorMessage.textContent = "Title is too long. Please keep it under 255 characters.";
        errorMessage.style.display = 'block'; // Display the error message
        return;
    }}

    if (placeInput.value.length > 255) {{
        errorMessage.textContent = "Place is too long. Please keep it under 255 characters.";
        errorMessage.style.display = 'block'; // Display the error message
        return;
    }}

    if (textInput.value.length > 65535) {{
        errorMessage.textContent = "Text is too long. Please keep it under 65 535 characters.";
        errorMessage.style.display = 'block'; // Display the error message
        return;
    }}

    // Check the file size
    let maxFileSize = 100 * 1024; // 100KB in bytes
    if (document.getElementById('image').files[0].size > maxFileSize) {{
        errorMessage.textContent = "Image size exceeds the maximum allowed size (100KB).";
        errorMessage.style.display = 'block'; // Display the error message
        return;
    }}

    // Reset error message if no errors
    errorMessage.style.display = 'none';

    //AJAX request
    let formData = new FormData(form);

    // Create an XMLHttpRequest object
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {{
        if (xhr.readyState === 4) {{
            createEventButton.disabled = false; // Enable the button
            if (xhr.status === 200) {{
                // Image uploaded successfully
                document.getElementById('status-message').textContent = 'Événement créé avec succès !';
                form.reset(); // Clear the form
            }} else {{
                // Image upload failed
                document.getElementById('status-message').textContent = "Impossible de créer l'événement. Réessayez.";
            }}
        }}
    }};

    // Open a POST request to the server
    xhr.open('POST', 'event-editor.php', true);

    // Send the form data as the request body
    xhr.send(formData);
}}
'''

    with open(f"{directory_path}/event/js/uploadEvent.js", "w") as js_file:
        js_file.write(js_code)
        print("uploadEvent.js generated !")
