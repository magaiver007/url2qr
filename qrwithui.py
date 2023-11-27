import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = url_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,  # Adjust box size here
        border=3,     # Adjust border size here
    )
    qr.add_data(url)
    qr.make(fit=True)
    global qr_img
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize((250, 250))  # Resize QR code to 250x250 pixels
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    img_label.config(image=qr_img_tk)
    img_label.image = qr_img_tk

def save_qr():
    if qr_img:
        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_img.save(file_path)

app = tk.Tk()
app.title('QR Code Generator')
app.geometry('600x500')  # Set window size to 400x500 pixels

tk.Label(app, text="Enter URL:").pack(padx=10, pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(padx=10, pady=10)    

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr)
generate_button.pack(padx=10, pady=10)

img_label = tk.Label(app)
img_label.pack(padx=10, pady=10)

save_button = tk.Button(app, text="Save QR Code", command=save_qr)
save_button.pack(padx=10, pady=10)

app.mainloop()
