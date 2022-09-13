from exif import Image
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames

class EXIFFilter:
    def __init__(self, fil):
        self.exif_data = {}
        self.photo_file = fil
        self.img = None
    def open_file(self):
        '''opens a photo file and returns an Image object'''
        with open(self.photo_file, 'rb') as photo_src:
            img = Image(photo_src)
            self.img = img
            
        return img

    def read_exif_data(self):
        '''Reads the exit data from an Image object'''
        img = self.open_file()
        if img.has_exif:
            for data in img.get_all().items():
                self.exif_data[data[0]] = data[1]

    def display_data(self):
        for item in self.exif_data:
            print(item)

    def remove_exif_data(self, tag):
        if (tag in self.img.get_all().keys() and tag in self.exif_data.keys()):
            self.img.delete(tag)
            self.exif_data.pop(tag)

    def save_file(self, location):
        with open(location, 'wb') as image_src:
            image_src.write(self.img.get_file())
        

