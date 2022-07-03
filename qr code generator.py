import pyqrcode

data = "www.shikharadhikari.tech" #data inside qr code
url = pyqrcode.create(data) #creating qr code
url.png('myqr.png', scale=6) #saving the qr code in png file