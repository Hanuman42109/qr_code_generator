# qr_generator.py
# QR Code Generator for any given URL
# Author: Hanuman Sai Chanukya Srinivas Chilamkuri
# Date: July 16, 2025
# Description: Takes a URL input and prints the QR code to the terminal.

import qrcode

def generate_qr_terminal():
    """
    Prompts the user for a URL and displays the corresponding QR code
    in the terminal using ASCII characters.
    """
    url = input("Enter a URL to generate QR Code: ")
    
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make()
    
    print("\nGenerated QR Code:\n")
    qr.print_ascii(invert=True)  # invert=True for dark-on-light display

if __name__ == "__main__":
    generate_qr_terminal()
