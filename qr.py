import qrcode

# URL you want to convert into a QR code
url = 'https://eur04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcareer2.successfactors.eu%2Fcareer%3Fcompany%3Dnational05&data=05%7C01%7Cxidis.eleftherios%40nbg.gr%7C8310004bdbd445a6fa2f08dbeccf86e3%7C2ea23c3d03fe4d7bb181ece5512d85c6%7C0%7C0%7C638364148296151264%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=oTBt8L%2BDR8ZVkHn%2FYWg5NSHpgsOqSsemlJGpHozdZ8s%3D&reserved=0'

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




