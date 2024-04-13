import subprocess

def setup():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("All required libraries have been successfully installed.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing the required libraries:", e)

if __name__ == "__main__":
    setup()
