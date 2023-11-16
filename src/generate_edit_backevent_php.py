def generate_edit_backevent_php(directory_path, website):
    php_code = f'''<?php

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {{
    // Get the image ID and edited legend from the POST data
    $eventId = $_POST['backevent_id'];
    $editedTitle = $_POST['title'];
    $editedPlace = $_POST['place']; 
    $editedDate = $_POST['date'];
    $editedText = $_POST['text'];
    $editedLink = $_POST['link'];

    // Update the database with the new legend (replace with your database update code)
    $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);

    // Ensure you use prepared statements to prevent SQL injection /
    $sql = "UPDATE {website}_backevent SET title = ?, place = ?, date = ?, text = ?, link = ? WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssssi", $editedTitle, $editedPlace, $editedDate, $editedText, $editedLink, $eventId);

    if ($stmt->execute()) {{
        // Database update successful
        echo "Événement mis à jour avec succès !";
    }} else {{
        // Handle database update failure
        header("HTTP/1.1 500 Internal Server Error");
        echo "Impossible de metter à jour l'événement. Réessayez.";
    }}

    $stmt->close();
    $conn->close();
}}
?>
'''

    with open(f"{directory_path}/backevent/requires/edit_backevent.php", "w") as php_file:
        php_file.write(php_code)
        print("edit_backevent.php generated !")
