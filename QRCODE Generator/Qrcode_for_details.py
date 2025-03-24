import qrcode
qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter your name:")
age=int(input("Enter your age:"))
email=input("Enter your email:")
mobile=int(input("Enter your mobile number:"))
l={"name":name,"age":age,"email":email,"mobile number":mobile}
qr.add_data(l)
qr.make(fit=True)
i=qr.make_image()
i.save("Details.png")
i.show()
