import qrcode

image_url = "https://maps.app.goo.gl/qqcxRQRjf8nUX4q97"
qr = qrcode.make(image_url)
qr.save("qr_code.png")

print("QR code saved!")