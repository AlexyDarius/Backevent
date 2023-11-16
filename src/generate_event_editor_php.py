def generate_event_editor_php(directory_path, main_domain, full_body_tag):
    php_code = f'''<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>Votre interface de gestion d'événement</title>
    <link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/event/css/style.css">
</head>
{full_body_tag}<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/event/requires/upload_event.php';
?>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <header>
        <h1 style="margin: 32px; font-weight: bold; text-align: center">Bienvenue sur votre espace gestionnaire d'événement</h1>
    </header>

    <!-- Form for uploading images -->
    <div id="upload-container">
        <form id="event-form" method="post" enctype="multipart/form-data" onsubmit="uploadEvent(event);">
            <label for="title">Titre (255 caractères max):</label>
            <input type="text" name="title" id="title" required maxlength="255">
            <label for="title">Lieu (255 caractères max):</label>
            <input type="text" name="place" id="place" required maxlength="255">
            <label for="date">Date et heure</label>
            <input type="datetime-local" name="date" id="date">
            <label for="image">Sélectionnez une image de couverture à télécharger (200ko max, utiliser <a href="https://cloudconvert.com/webp-converter">compression webp si possible</a>, taille max conseillée 512x512px):</label>
            <input type="file" name="image" id="image" accept="image/*" required>
            <input type="hidden" name="MAX_FILE_SIZE" value="100000"> <!-- 100ko -->
            <label for="date">Texte à afficher</label>
            <textarea id="text" name="text" rows="6" cols="60"></textarea>
            <label for="date">Lien vers la réservation</label>
            <input type="link" name="link" id="link">
            <button type="submit" id="create-event-button">Créer l'événement</button>
            <label for="warning">! Ne pas cliquer plusieurs fois sur le bouton de création !</label>
            <div id="error-message" style="color: red; display: none;"></div>
        </form>
        <div id="status-message"></div>
    </div>

    <div id="display-container" style="margin: 32px">
        <form id="event-display-form">
            <h2 style="margin: 32px; text-align: center; text-decoration: underline;">Sélection des événements à afficher sur l'accueil</h2>
            <?php
            require $_SERVER['DOCUMENT_ROOT']. '/modules/event/requires/display_chooser.php'
            ?>
        </form>
    <hr>
    </div>

    <div id="image-container" style="margin-top:32px">

<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/event/requires/back_office_display.php';
?>

</div>
    <p style="text-align: center; font-size: 24px"><a href="https://{main_domain}/">Revenir à l'accueil</a></p>
</div>

    <script src="js/script.js"></script>
    <script src="js/uploadEvent.js"></script>
    <script src="js/updateDisplayStatus.js></script>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/event/event-editor.php", "w") as php_file:
        php_file.write(php_code)
        print("event-editor.php generated !")
