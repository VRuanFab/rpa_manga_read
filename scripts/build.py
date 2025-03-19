import subprocess


def build():
    print('iniciando build...')

    command = [
        "poetry", "run", "pyinstaller",
        "--onefile",
        # "--windowed",
        "--name=baixar_mangá",
        "--add-data=.env;.",
        "main.py"
    ]
    
    try:
        subprocess.run(command, check=True)
        print('build Success')
    except subprocess.CalledProcessError:
        print('Error')