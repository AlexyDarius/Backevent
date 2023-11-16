def generate_upload_backevent_php(directory_path, website):
    php_code = f'''<?php

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['images'])) {{
    $upload_dir = "images/"; // Directory where you want to store uploaded images
    $title = $_POST['title'];
    $place = $_POST['place'];
    $date = $_POST['date'];
    $text = $_POST['text'];
    $link = $_POST['link'];
    $max_file_size = 100000; // 100kb

    // Iterate through each uploaded file
    for ($i = 0; $i < count($_FILES['images']['name']); $i++) {{
        $uploaded_file = $upload_dir . basename($_FILES['images']['name'][$i]);

        // Check the file size
        if ($_FILES['images']['size'][$i] > $max_file_size) {{
            header("HTTP/1.1 400 Bad Request");
            error_log("File size exceeds the maximum allowed size (100KB).");
            echo "File size exceeds the maximum allowed size (100KB).";
            exit;
        }}

        // Move the uploaded file to the destination
        if (!move_uploaded_file($_FILES['images']['tmp_name'][$i], $uploaded_file)) {{
            header("HTTP/1.1 500 Internal Server Error 1");
            error_log("Failed to move the uploaded file.");
            echo "Failed to move the uploaded file.";
            exit;
        }}
    }}

    // Connect to the MySQL database
    $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
    if ($conn->connect_error) {{
        header("HTTP/1.1 500 Internal Server Error 2");
        error_log("Connection failed: " . $conn->connect_error);
        echo "Connection failed: " . $conn->connect_error;
        exit;
    }}

    // Insert image information and details into the database
    $sql = "INSERT INTO {website}_backevent (title, date, place, img_filename1, img_filename2, img_filename3, uploaded_by, text, link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssssssss", $title, $date, $place, $_FILES['images']['name'][0], $_FILES['images']['name'][1], $_FILES['images']['name'][2], $_SESSION['username'], $text, $link);

    if ($stmt->execute()) {{
        echo "Images uploaded and information stored in the database!";
    }} else {{
        header("HTTP/1.1 500 Internal Server Error 3");
        $error_message = "Failed to store information in the database. Error: " . $stmt->error;
        error_log($error_message);
        echo $error_message;
    }}

    $stmt->close();
    $conn->close();
}}
?>
'''

    with open(f"{directory_path}/backevent/requires/upload_backevent.php", "w") as php_file:
        php_file.write(php_code)
        print("upload_backevent.php generated !")
