def generate_venv(directory_path, website, username, password):
    php_code = f'''# In .htaccess or virtual host configuration
SetEnv DB_{website}_USERNAME {username}
SetEnv DB_{website}_PASSWORD {password}
setEnv DB_{website}_DB {website}_db
'''

    with open(f"{directory_path}/.htaccess", "w") as php_file:
        php_file.write(php_code)
        print(".htaccess generated !")
