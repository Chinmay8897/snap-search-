import tkinter as tk
from PIL import Image, ImageTk


class ImageViewerGUI:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

        # Create a frame to hold the image and other GUI elements
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Load the image
        self.image = Image.open(self.image_path)

        # Resize the image to fit the window
        self.image = self.image.resize((500, 500))

        # Convert the image to a PhotoImage object
        self.photo_image = ImageTk.PhotoImage(self.image)

        # Create a canvas to display the image
        self.image_canvas = tk.Canvas(self.main_frame, width=500, height=500)
        self.image_canvas.pack()

        # Display the image on the canvas
        self.image_canvas.create_image(0, 0, image=self.photo_image, anchor="nw")

        # Create a button to close the window
        self.close_button = tk.Button(self.main_frame, text="Close", command=self.close)
        self.close_button.pack()

    def close(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Viewer")

    image_viewer_gui = ImageViewerGUI(root, "C:\doutnut\mainqns.jpg")
    image_viewer_gui.start()
