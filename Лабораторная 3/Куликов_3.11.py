import zipfile

with zipfile.ZipFile('desktop.zip') as z:
    for info in z.infolist():
        parts = info.filename.rstrip('/').split('/')
        depth = len(parts) - 1
        indent = '  ' * depth
        name = parts[-1]
        if info.is_dir():
            print(f'{indent}{name}')
        else:
            print(f'{indent}{name} {info.file_size}')