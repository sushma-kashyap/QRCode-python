import qrcode as qr

img=qr.make('some data here')
img.save("some.png")