def generate_backevent_php(directory_path, main_domain, full_body_tag, backevent_title):
    php_code = f'''<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>{backevent_title}</title>
    <link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/backevent/css/style.css">
</head>
{full_body_tag}
<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <header>
        <h1 style="color: var(--bs-secondary);font-family: Lato-Black;font-size: 48px; text-align : center; margin : 32px">Nos événements passés</h1>
    </header>

    <h2 style="text-align : center; font-family: Lato-Bold;color: var(--bs-primary);font-size: 24px;">Retrouvez nos précédents événements ici</h2>

    <hr style='margin-top:32px'>

    <div id="backevent-container">

<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/backevent/requires/backevent_displayer.php';
require $_SERVER['DOCUMENT_ROOT']. '/modules/backevent/requires/selective_displayer.php';
?>

    </div>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/backevent.php", "w") as php_file:
        php_file.write(php_code)
        print("backevent.php generated !")
