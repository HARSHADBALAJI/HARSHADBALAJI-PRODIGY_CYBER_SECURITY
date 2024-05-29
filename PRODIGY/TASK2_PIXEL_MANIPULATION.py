from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Encrypting the image
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)
    
    # Creating a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    
    # Saving the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size
    
    # Decrypting the image
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)
    
    # Creating a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    
    # Saving the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    while True:
        choice = input("Enter 'e' to encrypt image or 'd' to decrypt image: ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' or 'd'.")
            continue
        #image_path = input("Enter the path to the image: ")
        image_path = r"C:\Users\SRISHABRISURIYA\OneDrive\Desktop\PRODIGY\New folder\Butterfly_macro.jpeg"
        key = int(input("Enter the encryption/decryption key: "))
        
        if choice == 'e':
            encrypt_image(image_path, key)
        else:
            decrypt_image(image_path, key)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()