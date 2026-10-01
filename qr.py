import qrcode

url = input("Enter the URL to generate QR code: ")

file_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save(file_path)
print("QR code was generated!")
