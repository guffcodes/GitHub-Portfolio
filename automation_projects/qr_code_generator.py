# QR Code Generator - USER INPUT - encode data into QR, customize filenames, and save as image files
import qrcode

# image handling may require - pip install Pillow

# Define a function that generates the QR code
def generate_qr_code():
    # Tell user to input a URL to encode the data into QR
    data = input("Enter a URL to encode in the QR code: ")
    
    # Create a QRCode with custom settings
    qr = qrcode.QRCode(
        version=1,  # QR code size
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # size of boxes in QR grid
        border=4,  # border thickness
    )
    
    qr.add_data(data)  # add the user-provided data to the QR code
    qr.make(fit=True)  # optimize the QR code size to fit the data

    # generate the QR code image - can change colors
    img = qr.make_image(fill_color="black", back_color="white")
    
    # save the generated QR code image to an image file - user can specify name
    filename = input("Enter a filename for your QR code (e.g., my_qrcode.jpg): ")
    img.save(filename)  # Save the image with the specified filename
    
    # notify the user that the QR code has been created successfully
    print(f"QR code has been generated and saved as '{filename}'.")

# Run the function
generate_qr_code()
