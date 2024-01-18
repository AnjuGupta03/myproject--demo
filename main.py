import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number the code image and complicated picture
    box_size = 10,#size of the box where qr code will be dispalyed
    border = 5 #it is the white part of image -- border in all 4 sides with white colour
)
data ="https://www.w3schools.com/sql/sql_distinct.asp"
 # in data i have given the path name

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill ="pink",back_color ="white")
img.save("text.png")
