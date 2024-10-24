import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.youtube.com/@chandu_yt4775/featured"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("channel.svg", scale=8)
