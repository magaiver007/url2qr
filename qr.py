import qrcode

# URL you want to convert into a QR code
url = 'enter_your_url_here'

# Generate QR code
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it somewhere, change the path as needed
img.save("my_qr_code.png")




