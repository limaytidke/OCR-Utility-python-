import subprocess
import os
import pytesseract
from PIL import Image

image_path = "/home/limay/Projects/OCR-Utility/save.png"

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
        text = pytesseract.image_to_string(img)
        print(f"Extracted Text: {text.strip()}")

if __name__ == "__main__":
    main()
