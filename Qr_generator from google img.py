import qrcode

image_url = "https://tse4.mm.bing.net/th/id/OIP.VuTDEE_u6F7iTcGnzd9s_gHaJ3?pid=Api&P=0&h=180"       #i take this image from google
qr = qrcode.make(image_url)
qr.save("qr_code.png")

print("QR code saved!")