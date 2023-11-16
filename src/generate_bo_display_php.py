def generate_bo_display_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT id, title, date, place, img_filename, text, link FROM {website}_event ORDER BY date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $eventId = $row['id'];
        $imagePath = "images/" . $row['img_filename'];
        $title = $row['title'];
        $date = $row['date'];
        $place = $row['place'];
        $text = $row['text'];
        $link = $row['link'];
        
        echo "<section id='event-box-" . $eventId . "' style='margin: 32px;'>";
        echo "<div class='container'>";
        echo "<div class='row d-flex justify-content-center'>";
        echo " <div class='col-md-12'>";
        echo "<div>";
        echo "<h3 id='title-" . $eventId . "' style='text-align: center;font-family: Lato-Bold; margin-bottom:12px'>$title</h3>";
        echo "<p id='place-" . $eventId . "' class='text-center' style='margin-bottom:0px'>Location : $place</p>";

        $dateTime = new DateTime($date);
        $formattedDate = $dateTime->format('d/m/Y H:i');

        echo "<p id='date-" . $eventId . "' class='text-center'>Date : $formattedDate";
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
        echo "<p id='text-" . $eventId . "' style='text-align: justify;width: 90%;max-width: 768px;'>$text</p>";
        echo "<a id='link-" . $eventId . "' class='btn' role='button' data-bss-hover-animate='pulse' href='$link' style='background: var(--bs-secondary);color: var(--bs-body-bg);text-shadow: 0px 0px 8px var(--bs-black); font-size: 20px; margin-top: 12px''>Réserver votre place</a>";
        echo "</div>";
        echo "</div>";
        echo "</div>";
        echo "<button style='margin-right:8px; margin-bottom:24px' class='delete-button' data-event-id='$eventId'>Supprimer</button>";
        echo "<button class='edit-button' data-event-id='$eventId'>Éditer</button>";
        echo "<div class='edit-container' id='edit-container-$eventId' style='display: none;'>";
        echo "<label for='edited-title-$eventId'>Titre (255 caractères max) :</label>";
        echo "<input type='text' id='edited-title-$eventId' placeholder='Éditer le titre'>";
        echo "<label for='edited-place-$eventId'>Lieu (255 caractères max) :</label>";
        echo "<input type='text' id='edited-place-$eventId' placeholder='Éditer le lieu'>";
        echo "<label for='edited-date-$eventId'>Date et heure:</label>";
        echo "<input type='datetime-local' id='edited-date-$eventId' placeholder='Éditer la date'>";
        echo "<label for='edited-text-$eventId'>Éditer le texte :</label>";
        echo "<textarea id='edited-text-$eventId' name='text' rows='6' cols='60'></textarea>";
        echo "<label for='edited-link-$eventId'>Lieu (255 caractères max) :</label>";
        echo "<input type='link' id='edited-link-$eventId' placeholder='Éditer le lien'>";
        echo "<button class='save-button' style='margin-right:6px; margin-top:24px' id='save-button-$eventId' data-event-id='$eventId'>Sauvegarder</button>";
        echo "<button class='cancel-button' id='cancel-button-$eventId' data-event-id='$eventId'>Annuler</button>";
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

    with open(f"{directory_path}/event/requires/back_office_display.php", "w") as php_file:
        php_file.write(php_code)
        print("back_office_display.php generated !")
