import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.png")  
if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read stored password
with open("password.txt", "r") as file:
    saved_password = file.read().strip()


pas = input("Enter passcode for Decryption: ")

if saved_password == pas:
    message = []
    height, width, _ = img.shape

    for i in range(height):
        for j in range(width):
            for k in range(3):  # Iterate over RGB channels
                pixel_value = img[i, j, k]
                char = chr(pixel_value)

                if char.isalpha():  # Store only alphabets
                    message.append(char)

                if char == "~":  # Stop at termination character
                    print("\nDecryption message (only alphabets):", "".join(message))
                    exit()

    print("\nDecryption message (only alphabets):", "".join(message))
else:
    print("YOU ARE NOT AUTHORIZED!")
