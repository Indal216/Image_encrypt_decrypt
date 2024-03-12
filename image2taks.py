from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size

        
        img = img.convert("RGB")

        
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                r ^= key
                g ^= key
                b ^= key
                img.putpixel((x, y), (r, g, b))

      
        encrypted_path = image_path.split('.')[0] + '_encrypted.png'
        img.save(encrypted_path)
        print("Encryption Done. Encrypted image saved as", encrypted_path)

    except Exception as e:
        print('Error:', e)

def decrypt_image(encrypted_image_path, key):
    try:
        
        img = Image.open(encrypted_image_path)
        width, height = img.size

        img = img.convert("RGB")

        
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                r ^= key
                g ^= key
                b ^= key
                img.putpixel((x, y), (r, g, b))

        decrypted_path = encrypted_image_path.split('_encrypted.png')[0] + '_decrypted.png'
        img.save(decrypted_path)
        print("Decryption Done. Decrypted image saved as", decrypted_path)

    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    try:
        image_path = input('Enter path of the image: ')
        key = int(input('Enter Key for encryption and decryption of the image: '))
        encrypt_image(image_path, key)
        decrypt_image(image_path.split('.')[0] + '_encrypted.png', key)
    except Exception as e:
        print('Error caught:', e)
