import git

def obtener_historial_commits(ruta_repositorio):
    # Abre el repositorio en la ruta especificada
    repo = git.Repo(ruta_repositorio)
    
    # Obtiene todos los commits
    commits = list(repo.iter_commits())
    
    # Imprime el historial de commits
    for commit in commits:
        print(f"ID: {commit.hexsha}")
        print(f"Autor: {commit.author.name}")
        print(f"Fecha: {commit.committed_datetime}")
        print(f"Mensaje: {commit.message}")
        print("-" * 40)

if __name__ == "__main__":
    # Ruta del repositorio local en Codespaces
    ruta = "/workspaces/store_branches" 
    
    # Llamamos a la función para obtener el historial
    obtener_historial_commits(ruta)
