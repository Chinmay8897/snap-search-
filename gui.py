
import pytesseract as tess 
tess.pytesseract.tesseract_cmd = r'C:\Users\kbmsb\Downloads\tesseract.exe'
from PIL import Image 
def image_scanner():
   
    img = Image.open('mainqns.jpg')
    text = tess.image_to_string(img)
    print(text)

    img = Image.open('0012.jpg')
    data = tess.image_to_string(img)
    if(text==data):
          print("answerimggui")
    else:
            img = Image.open('mainqns.jpg')
            data = tess.image_to_string(img)
            print("ddd")
image_scanner()             
     
