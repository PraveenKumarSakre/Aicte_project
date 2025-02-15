 Image Steganography using OpenCV:
This project demonstrates image steganography using Python and OpenCV, where a secret message is hidden inside an image and later extracted using a passcode.

 Features:
Encrypts a secret message inside an image by modifying pixel values.
Requires a passcode to decrypt the hidden message.
Extracts only alphabetic characters from the encrypted image.
Stops reading when a termination character (~) is found.

Installation:
Install Python (if not installed) from python.org.
Install required dependencies:
pip install opencv-python

🔐 Encryption (Hiding the Message):
Run the encrypt.py script to embed a secret message into an image.
python encrypt.py

How It Works:
Reads an input image (pic.jpg).
Takes a secret message and a passcode as input.
Encodes the message into pixel values.
Saves the modified image as encryptedImage.png.
Stores the passcode in password.txt for decryption
.
🔓 Decryption (Retrieving the Message):
Run decrypt.py to extract the secret message.
python decrypt.py

How It Works:
Reads the encrypted image (encryptedImage.png).
Asks for a passcode (must match the stored passcode).
Extracts and prints the hidden message.
Filters only alphabets (A-Z, a-z).
Stops reading at the termination character (~).






