def generate_display_chooser_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT id, title, date, place, display FROM {website}_backevent ORDER BY date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $eventId = $row['id'];
        $title = $row['title'];
        $date = $row['date'];
        $place = $row['place'];
        $display = $row['display'];
        
        echo "<div id='backevent-display-" . $eventId . "' style='display: flex; align-items: center;'>";

        // Text container (left-aligned)
        echo "<div>";
        echo "<h4 id='title-display-" . $eventId . "' style='font-family: Lato-Bold; margin-bottom: 0px;'>$title</h3>";
        echo "<p id='place-display-" . $eventId . "' style='margin-bottom: 0px;'>Location : $place</p>";

        // Convert the database date to the desired format
        $dateTime = new DateTime($date);
        $formattedDate = $dateTime->format('d/m/Y H:i');

        echo "<p id='date-display-" . $eventId . "'>Date : $formattedDate</p>";
        echo "</div>";

        // Checkbox container (right-aligned)
        echo "<div style='margin-left: 32px;'>";
        echo "<label for='checkbox-display-" . $eventId . "' style='margin-right: 6px; margin-bototm: 0px;'>Afficher sur l'accueil</label>";
        echo "<input type='checkbox' id='checkbox-display-" . $eventId . "' ";
        echo $display == 1 ? "checked" : "";
        echo " onchange='updateDisplayStatus($eventId, this.checked)'>";
        echo "</div>";

        echo "</div>";
    }}
}} else {{
    echo "Aucune image trouvée.";
}}

$conn->close();
?>
'''

    with open(f"{directory_path}/backevent/requires/display_chooser.php", "w") as php_file:
        php_file.write(php_code)
        print("display_chooser.php generated !")
