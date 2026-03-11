from pathlib import Path


def percorrer(target_path, level=0):
    def printar(folder, level):
        print('\t' * level + folder)

    printar(target_path.name, level)
    for file in target_path.iterdir():
        if file.is_dir():
            percorrer(file, level+1)
        else:
            printar(file.name, level+1)


result = Path('.')
percorrer(result)
