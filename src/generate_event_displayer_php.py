def generate_event_displayer_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT title, date, place, img_filename, text, link FROM {website}_event ORDER BY date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $imagePath = "modules/event/images/" . $row['img_filename'];
        $title = $row['title'];
        $date = $row['date'];
        $place = $row['place'];
        $text = $row['text'];
        $link = $row['link'];
        
        echo "<section style='margin: 32px;'>";
        echo "<div class='container'>";
        echo "<div class='row d-flex justify-content-center'>";
        echo " <div class='col-md-12'>";
        echo "<div>";
        echo "<h3 style='text-align: center;font-family: Lato-Bold; margin-bottom:12px'>$title</h3>";
        echo "<p class='text-center' style='margin-bottom:0px'>Lieu : $place</p>";

        // Convert the database date to the desired format
        $dateTime = new DateTime($date);
        $formattedDate = $dateTime->format('d/m/Y H:i');

        echo "<p class='text-center'>Date : $formattedDate";
        echo "</div>";
        echo "</div>";
        echo "</div>";
        echo "<div class='row'>";
        echo "<div class='col d-flex justify-content-center'>";
        echo "<div class='d-flex image-box'>";
        echo "<a href='$imagePath'><img class='img-fluid' width='500px' height='430px' src='$imagePath'></a>";
        echo "</a></div>";
        echo "</div>";
        echo "</div>";
        echo "<div style='margin:32px' class='row'>";
        echo "<div class='col d-flex justify-content-center'>";
        echo "<div class='text-center'>";
        echo "<h4 style='font-family: Lato-Bold' class='text-center'>$title</h4>";
        echo "<p style='text-align: justify;width: 90%;max-width: 768px;'>$text</p>";
        echo "<a class='btn' role='button' data-bss-hover-animate='pulse' href='$link' style='background: var(--bs-secondary);color: var(--bs-body-bg);text-shadow: 0px 0px 8px var(--bs-black); font-size: 20px; margin-top: 12px'>Réserver votre place</a>";
        echo "</div>";
        echo "</div>";
        echo "</div>";
        echo "<hr>";
        echo "</div>";
        echo "</section>";
    }}
}} else {{
    echo "Aucun événement trouvée.";
}}

$conn->close();
?>
'''

    with open(f"{directory_path}/event/requires/event_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("event_displayer.php generated !")
