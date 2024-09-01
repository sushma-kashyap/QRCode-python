import qrcode
import qrcode.constants 

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=4,
)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="yellow")
img.save("youtube.png")