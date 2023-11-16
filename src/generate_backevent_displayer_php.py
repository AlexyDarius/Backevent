def generate_backevent_displayer_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT id, title, date, place, img_filename1, img_filename2, img_filename3, text, link FROM {website}_backevent WHERE display = 1 ORDER BY date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $eventId = $row['id'];
        $title = $row['title'];
        $date = $row['date'];
        $place = $row['place'];
        $text = $row['text'];
        $link = $row['link'];

        echo "<section style='margin: 32px;>";
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

        // Display the images in a carousel
        echo "<div class='carousel slide' data-bs-ride='false' id='carousel-$eventId' style='height: 512px; width: 910px'>";
        echo "<div class='carousel-inner'>";

        for ($i = 1; $i <= 3; $i++) {{
            $imagePath = "modules/backevent/images/" . $row["img_filename$i"];
            echo "<div class='carousel-item" . ($i == 1 ? " active" : "") . "'>";
            echo "<img class='img-fluid w-100 d-block' src='$imagePath' alt='Slide Image' style='max-width: 910px; max-height: 512px; object-fit: contain;'>";
            echo "</div>";
        }}

        echo "</div>";
        echo "<a class='carousel-control-prev' href='#carousel-$eventId' role='button' data-bs-slide='prev'>";
        echo "<span class='carousel-control-prev-icon' aria-hidden='true'></span>";
        echo "<span class='visually-hidden'>Previous</span>";
        echo "</a>";
        echo "<a class='carousel-control-next' href='#carousel-$eventId' role='button' data-bs-slide='next'>";
        echo "<span class='carousel-control-next-icon' aria-hidden='true'></span>";
        echo "<span class='visually-hidden'>Next</span>";
        echo "</a>";
        echo "</div>";

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
    echo "No events found.";
}}

$conn->close();
?>
'''

    with open(f"{directory_path}/backevent/requires/backevent_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("backevent_displayer.php generated !")
