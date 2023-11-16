def generate_upload_event_php(directory_path, website):
    php_code = f'''<?php 
// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {{
    $upload_dir = "images/"; // Directory where you want to store uploaded images
    $uploaded_file = $upload_dir . basename($_FILES['image']['name']);
    $title = $_POST['title'];
    $place = $_POST['place'];
    $date = $_POST['date'];
    $text = $_POST['text'];
    $link = $_POST['link'];
    $max_file_size = 100000; // 100kb

    // Check the file size
   if ($_FILES['image']['size'] > $max_file_size) {{
    header("HTTP/1.1 400 Bad Request");
    echo "File size exceeds the maximum allowed size (100KB).";
    }}else{{

        if (move_uploaded_file($_FILES['image']['tmp_name'], $uploaded_file)) {{
            // Image uploaded successfully
            $imageFilename = basename($_FILES['image']['name']);
            $uploadedBy = $_SESSION['username'];

            // Connect to the MySQL database
            $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
            if ($conn->connect_error) {{
                die("Connection failed: " . $conn->connect_error);
            }}

            // Insert image information and legend into the database
            $sql = "INSERT INTO {website}_event (title, date, place,  img_filename, uploaded_by, text, link) VALUES (?, ?, ?, ?, ?, ?, ?)";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("sssssss", $title, $date, $place, $imageFilename, $uploadedBy, $text, $link);

            if ($stmt->execute()) {{
                echo "Image téléchargée et information stockées !";
            }} else {{
                header("HTTP/1.1 500 Internal Server Error");
                echo "Événement créé mais il est impossible de stocker les informations. Réessayez.";
            }}

            $stmt->close();
            $conn->close();
        }} else {{
            header("HTTP/1.1 500 Internal Server Error");
            echo "Impossible de créer l'événement. Réessayez.";
        }}
    }}
}}
?>
'''

    with open(f"{directory_path}/event/requires/upload_event.php", "w") as php_file:
        php_file.write(php_code)
        print("upload_event.php generated !")
