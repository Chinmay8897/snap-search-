
import pytesseract as tess 
tess.pytesseract.tesseract_cmd = r'C:\Users\kbmsb\Downloads\tesseract.exe'
from PIL import Image ,ImageTk

import tkinter as tk
import sys
class ImageViewerGUI:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
         


        
        self.image = Image.open(self.image_path)
        image_w = self.image.width
        image_h = self.image.height


        self.photo_image = ImageTk.PhotoImage(self.image)

  
        self.image_canvas = tk.Canvas(self.main_frame, width=image_w, height=image_h)
        self.image_canvas.pack()

        self.image_canvas.create_image(0, 0, image=self.photo_image, anchor="nw")

        
        self.close_button = tk.Button(self.main_frame, text="Close", command=self.close)
        self.close_button.pack()

    def close(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()


user_input = ""

class InputGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Place Your Image ")
        
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.text_box = tk.Text(self.root, height=20, width=40)
        self.text_box.pack()

        self.button = tk.Button(self.root, text="Search", command=self.store_input_and_terminate_window)
        self.button.pack()

        self.root.mainloop()

    def store_input_and_terminate_window(self):
        
        global user_input
        user_input = self.text_box.get("1.0", "end-1c")

        image = Image.open("interface.jpg")
        
        

        print(user_input)

        self.root.destroy()

if __name__ == "__main__":
    input_gui = InputGUI()



def image_scanner():
    print("kkj")
    img = Image.open(user_input)
    text = tess.image_to_string(img)
    print(text)

    img = Image.open('0012.jpg')
    data = tess.image_to_string(img)
    img = Image.open('mainqns.jpg')
    okok = tess.image_to_string(img)
    img = Image.open('outqns.jpg')
    lala = tess.image_to_string(img)
    if(text==data):
     root = tk.Tk()
     root.title("Image Viewer")

     image_viewer_gui = ImageViewerGUI(root, "C:/doutnut/09444.jpg")
     image_viewer_gui.start()
    elif(text==lala):
      root = tk.Tk()
      root.title("Image Viewer")

      image_viewer_gui = ImageViewerGUI(root, "C:/doutnut/outans.jpg")
      image_viewer_gui.start()
            
    elif(text==okok):
      root = tk.Tk()
      root.title("Image Viewer")

      image_viewer_gui = ImageViewerGUI(root, "C:\doutnut\mainans.jpg")
      image_viewer_gui.start()
    else:
        root = tk.Tk()
        root.title("Image Viewer")

        image_viewer_gui = ImageViewerGUI(root, "C:/doutnut/retans.jpg")
        image_viewer_gui.start()
image_scanner()
