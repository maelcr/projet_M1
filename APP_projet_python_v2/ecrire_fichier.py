import os

#écrire le fichier spécifié avec le message en str
def ecrire_fichier_txt (file_name,message):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    with open(abs_file_path, 'w') as file:
        content = file.write(message)
    return content
