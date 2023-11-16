def generate_updateDisplayStatus_js(directory_path):
    js_code = f'''function updateDisplayStatus(eventId, isChecked) {{
    fetch('requires/update_display_status.php', {{
        method: 'POST',
        headers: {{
            'Content-Type': 'application/json',
        }},
        body: JSON.stringify({{
            eventId: eventId,
            isChecked: isChecked,
        }}),
    }})
    .then(response => response.json())
    .then(data => {{
        // Handle the response if needed
        console.log(data);
    }})
    .catch((error) => {{
        console.error('Error:', error);
    }});
}}
'''

    with open(f"{directory_path}/backevent/js/updateDisplayStatus.js", "w") as js_file:
        js_file.write(js_code)
        print("updateDisplayStatus.js generated !")
