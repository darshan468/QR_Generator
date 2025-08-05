import qrcode

image_url = "https://1drv.ms/i/c/c0d20c910e4cb06f/EY6WaxhBZBdPpe8zvaiJGYABz7UmwC_rd8MYz6aJVntzkw?e=Ctzbqh"       #I take this image from downloaded on system
qr = qrcode.make(image_url)
qr.save("qr_code.png")

print("QR code saved")