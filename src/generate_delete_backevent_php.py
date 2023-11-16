def generate_delete_backevent_php(directory_path, website):
    php_code = f'''<?php

require $_SERVER['DOCUMENT_ROOT'] . '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['backevent_id'])) {{
    // Retrieve the event ID from the POST request
    $eventId = $_POST['backevent_id'];

    // Connect to the MySQL database
    $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
    if ($conn->connect_error) {{
        die("Connection failed: " . $conn->connect_error);
    }}

    // Retrieve the image filenames from the database
    $sql = "SELECT img_filename1, img_filename2, img_filename3 FROM {website}_backevent WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $eventId);
    $stmt->execute();
    $stmt->bind_result($imageFilename1, $imageFilename2, $imageFilename3);
    $stmt->fetch();
    $stmt->close();

    // Delete the image files from the server
    deleteImage($imageFilename1);
    deleteImage($imageFilename2);
    deleteImage($imageFilename3);

    // Delete the database entry
    $sql = "DELETE FROM {website}_backevent WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $eventId);
    $stmt->execute();
    $stmt->close();

    echo "Événement supprimée !";

    $conn->close();
}}

function deleteImage($imageFilename)
{{
    if (!empty($imageFilename)) {{
        $imagePath = "../images/" . $imageFilename;
        if (file_exists($imagePath)) {{
            unlink($imagePath);
        }}
    }}
}}

?>
'''

    with open(f"{directory_path}/backevent/requires/delete_backevent.php", "w") as php_file:
        php_file.write(php_code)
        print("delete_backevent.php generated !")
