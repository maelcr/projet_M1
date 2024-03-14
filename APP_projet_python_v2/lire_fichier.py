import os

#lire le fichié spécifiée
def lire_fichier_txt (file_name):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    with open(abs_file_path, 'r') as file:
        content = file.read()
    return content