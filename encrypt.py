import cv2

# Load the image
img = cv2.imread("download.png")  #give path of img

if img is None:
    print("Error: Image not found!")
    exit()

# Input message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save password
with open("password.txt", "w") as file:
    file.write(password)

# Append termination character "~"
msg += "~"

# Store message into pixels
index = 0
height, width, _ = img.shape

for i in range(height):
    for j in range(width):
        for k in range(3):  # Loop through RGB channels
            if index < len(msg):
                img[i, j, k] = ord(msg[index])  # Store ASCII value
                index += 1
            else:
                break

# Save encrypted image
cv2.imwrite("encryptedImage.png", img)
print("Encryption complete. Encrypted image saved as 'encryptedImage.jpg'.")
