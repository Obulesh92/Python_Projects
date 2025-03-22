import qrcode
v=qrcode.make("https://www.youtube.com/")
v.save("docpy.png")
v.show()