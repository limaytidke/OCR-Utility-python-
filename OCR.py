import subprocess
import os
import pytesseract
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = f"{BASE_DIR}+save.png"

print("Select area")

def main():
    subprocess.run(["xfce4-screenshooter","-r","-s",image_path],check=True)
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Could not open image")
    except subprocess.CalledProcessError:
        print("Error: Failed to take screenshot.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        text = pytesseract.image_to_string(img).strip()
        subprocess.run(["xclip", "-selection", "clipboard"], input=text, text=True, check=True)
if __name__ == "__main__":
    main()
