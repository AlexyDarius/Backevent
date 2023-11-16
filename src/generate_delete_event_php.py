def generate_delete_event_php(directory_path, website):
    php_code = f'''<?php

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['event_id'])) {{
    // Retrieve the image ID from the POST request
    $eventId = $_POST['event_id'];

    // Connect to the MySQL database
    $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
    if ($conn->connect_error) {{
        die("Connection failed: " . $conn->connect_error);
    }}

    // Retrieve the image filename from the database
    $sql = "SELECT img_filename FROM {website}_event WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $eventId);
    $stmt->execute();
    $stmt->bind_result($imageFilename);
    $stmt->fetch();
    $stmt->close();

    if (!empty($imageFilename)) {{
        // Delete the image file from the server
        $imagePath = "../images/" . $imageFilename;
        if (file_exists($imagePath)) {{
            unlink($imagePath);
        }}

        // Delete the database entry
        $sql = "DELETE FROM dariusdev_event WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $eventId);
        $stmt->execute();
        $stmt->close();

        echo "Événement supprimée !";
    }} else {{
        echo "Événement impossible à trouver.";
    }}

    $conn->close();
}}

?>
'''

    with open(f"{directory_path}/event/requires/delete_event.php", "w") as php_file:
        php_file.write(php_code)
        print("delete_event.php generated !")
