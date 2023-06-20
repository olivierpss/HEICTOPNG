# Script de Olivier Durieux

import os
import shutil
import subprocess


def convert_heic_to_png(input_path, output_path):
    # Vérifier si le fichier d'entrée existe
    if not os.path.isfile(input_path):
        print(f"Le fichier '{input_path}' n'existe pas.")
        return

    # Vérifier si l'outil 'heif-convert' est disponible
    if not shutil.which('heif-convert'):
        print("L'outil 'heif-convert' n'est pas installé. Veuillez l'installer.")
        return

    # Copier le fichier HEIC dans le répertoire de sortie
    shutil.copy2(input_path, output_path)

    # Exécuter la commande shell pour convertir l'image HEIC en PNG
    subprocess.run(['heif-convert', output_path])


def batch_convert_heic_to_png(input_directory):
    # Vérifier si le répertoire d'entrée existe
    if not os.path.exists(input_directory):
        print(f"Le répertoire '{input_directory}' n'existe pas.")
        return

    # Vérifier si le répertoire de sortie existe, sinon le créer
    output_directory = os.path.join(input_directory, "output")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Obtenir la liste des fichiers HEIC à convertir
    heic_files = [filename for filename in os.listdir(input_directory)
                  if filename.endswith(".HEIC") or filename.endswith(".heic")]

    total_files = len(heic_files)
    current_file = 0

    # Parcourir tous les fichiers du répertoire d'entrée
    for filename in heic_files:
        current_file += 1

        # Afficher le progrès
        print(f"Conversion en cours ({current_file}/{total_files})")

        # Construire les chemins d'entrée et de sortie
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, os.path.splitext(filename)[0])

        # Vérifier si l'image existe déjà dans le dossier de sortie
        if os.path.isfile(output_path + ".JPG") or os.path.isfile(output_path + ".jpg"):
            print(f"L'image '{filename}' existe déjà dans le dossier de sortie. La conversion est ignorée.")
            continue

        # Convertir l'image HEIC en PNG
        convert_heic_to_png(input_path, output_path)

    # Supprimer tous les fichiers sans extension dans le répertoire de sortie
    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        if os.path.isfile(file_path) and os.path.splitext(filename)[1] == "":
            os.remove(file_path)

    print("Conversion terminée.")


# Saisie du chemin du répertoire d'entrée par l'utilisateur
input_directory = input("Veuillez saisir le chemin du répertoire contenant les images HEIC : ")
batch_convert_heic_to_png(input_directory)
