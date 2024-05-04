import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code():
    data = entry.get()  # Get data from the entry widget
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Ask user to select the file location to save the QR code image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img.save(file_path)

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")

# Create label and entry widgets
label = tk.Label(root, text="Enter data to generate QR code:")
label.pack()
entry = tk.Entry(root, width=40)
entry.pack()

# Create generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Run the application
root.mainloop()
