from PIL import Image
import os

def encryptImage(input_path, output_path, key):
    image = Image.open(input_path)
    encrypted_image = Image.new("RGB", image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))

            r_encrypted = r ^ key
            g_encrypted = g ^ key
            b_encrypted = b ^ key
            encrypted_image.putpixel((x, y), (r_encrypted, g_encrypted, b_encrypted))

    encrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

def decryptImage(input_path, output_path, key):
    encryptImage(input_path, output_path, key)

# User Interface 

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

input_path = r"C:\Users\Mohin\OneDrive\Desktop\Mitali's Internship\image.jpg"
output_path = r"C:\Users\Mohin\OneDrive\Desktop\Mitali's Internship\imagedst.jpg"

try:
    key = int(input("Enter key (0-255): "))
    if 0 <= key <= 255:
        if choice == 'E':
            encryptImage(input_path, output_path, key)
        elif choice == 'D':
            decryptImage(input_path, output_path, key)
        else:
            print("Invalid choice. Enter E for encryption or D for decryption.")
    else:
        print("Invalid key! Please enter a value between 0 and 255.")
except ValueError:
    print("Please enter a valid numeric key.")
