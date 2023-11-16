def generate_update_display_status_php(directory_path, website):
    php_code = f'''<?php

// Get the data from the AJAX request
$data = json_decode(file_get_contents("php://input"));

$eventId = $data->eventId;
$isChecked = $data->isChecked;

// Connect to the database
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);

if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Update the display status in the database
$sql = "UPDATE {website}_backevent SET display = " . ($isChecked ? 1 : 0) . " WHERE id = " . $eventId;

if ($conn->query($sql) === TRUE) {{
    echo json_encode(['success' => true]);
}} else {{
    echo json_encode(['success' => false, 'error' => $conn->error]);
}}

$conn->close();
?>

'''

    with open(f"{directory_path}/event/requires/update_display_status.php", "w") as php_file:
        php_file.write(php_code)
        print("update_display_status.php generated !")
