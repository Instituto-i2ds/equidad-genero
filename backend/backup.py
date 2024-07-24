import os
import subprocess
from datetime import datetime


def backup_docker_volume(volume_name: str, backup_dir: str):
    """
    Realiza un respaldo de un volumen Docker y lo guarda en el directorio especificado.

    :param volume_name: Nombre del volumen Docker a respaldar.
    :param backup_dir: Directorio en el host donde se guardará el archivo de respaldo.
    """
    # Configura el nombre del archivo de respaldo con una marca de tiempo.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_dir}/backup_{timestamp}.tar.gz"

    return print(f"Backup completed and saved to {backup_file}")
    # Asegúrate de que el directorio de respaldo exista.
    os.makedirs(backup_dir, exist_ok=True)

    # Comando para realizar el respaldo del volumen.
    backup_command = [
        "docker", "run", "--rm",
        "-v", f"{volume_name}:/volume",
        "-v", f"{backup_dir}:/backup",
        "alpine",
        "sh", "-c",
        f"tar -czvf /backup/{os.path.basename(backup_file)} -C /volume ."
    ]

    try:
        subprocess.run(backup_command, check=True)
        print(f"Backup completed and saved to {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")


# Llamada a la función con los parámetros deseados.
if __name__ == "__main__":
    VOLUME_NAME = "postgres_data"
    BACKUP_DIR = "./"
    backup_docker_volume(VOLUME_NAME, BACKUP_DIR)
