#Guide for SMS in Twilow

# from twilio.rest import Client

# account_sid = 'AC58ce0fab20dfaf93cb9c50e13b068441'
# auth_token = '73e360b56e4f4cf54ee9f0ff17e380b0'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+12067016270',
#   body='hi',
#   to='+917908934723'
# )

# print(message.sid)

# Guide barcode genaration

# import EAN13 from barcode module

# import PIL
# from PIL import Image

# bar_class = barcode.get_barcode_class('code39')
# barcode = 'http//192.168.0.19.8000'

# writer=ImageWriter()
# code128 = bar_class(barcode, writer)


# code128.save('code128', options={"write_text": False, "module_width":0.35, "module_height":10, "font_size": 8, "text_distance": -3, "quiet_zone": 1}) # save the resized image
from datetime import datetime
from PIL import Image
import os
import qrcode

company = input("Enter Company name :")
quantyty = int(input("Enter quentity :"))

for x in range(quantyty):
  print(company)
  now = datetime.now()
  ur_no = now.strftime('%d%m%Y%H%M%S%f')[:-4]
  Uid = company.upper()+ur_no
  print ("Current date and time : ")
  # example data
  Qr_data = "http://192.168.1.4:80/code/"+company.upper()+ur_no
  print(Qr_data)
  # output file name
  filename = ur_no+".png"
  image_path = "D:\Personal Projects\Arijit Sir\IOCLDEVCRM\QrImage"
  # generate qr code
  img = qrcode.make(Qr_data)
  resized_im = img.resize((round(img.size[0]*0.2), round(img.size[1]*0.2)))
  path_qr = (f"{image_path}/"+filename)
  print(path_qr)
  # save img to a file
  resized_im.save(f"{image_path}/"+filename)
