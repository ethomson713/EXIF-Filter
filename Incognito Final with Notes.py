#This is an EXIF-deleting program built by the Project Incognito team for the Global Legal Hackathon 2022
#This is for DEMONSTRATION PURPOSES ONLY
#Attributions: thanks to Eric Thomson for his Python support and Sarah Emery for her GUI design support
#Attributions: the GUI was converted from Figma to Tkinter using Tkinter Designer by Parth Jadhav (https://github.com/ParthJadhav/Tkinter-Designer)

#Prerequisite libraries: exif and tkinter

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from exif import Image
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames, asksaveasfilename

class EXIFFilter:
    def __init__(self):
        self.exif_data = {}
        self.photo_file = None
        self.img = None
        self.end_file = None
    def ask_for_file(self):
        self.photo_file = askopenfilenames()[0];
    def ask_for_save_loc(self):
        return asksaveasfilename();
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

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

filter = EXIFFilter()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_1.place(
    x=176.0,
    y=392.0,
    width=148.0,
    height=51.0
)

canvas.create_text(
    250,
    350.0,
    justify="center",
    text="Protect yourself and your community with metadata-free images",
    fill="#000000",
    font=("Arsenal Italic", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    249.0,
    222.0,
    image=image_image_1
)

canvas.create_text(
    250.0,
    75.0,
    justify="center",
    text="PROJECT INCOGNITO",
    fill="#000000",
    font=("Arsenal Regular", 48 * -1)
)
window.resizable(False, False)
window.mainloop()







#PAGE TWO
window = Tk()

window.geometry("500x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_2.1.png"))
image_1 = canvas.create_image(
    249.0,
    452.0,
    image=image_image_1
)

canvas.create_text(
    135.0,
    290.0,
    anchor="nw",
    text="Accepted File Types: JPG, JPEG, PNG",
    fill="#000000",
    font=("Arsenal Regular", 16 * -1)
)

def get_the_file():
    filter.ask_for_file()
    filter.open_file()
    window.destroy()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_2.1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_the_file,
    relief="flat",
)
button_1.place(
    x=158.0,
    y=224.0,
    width=184.0,
    height=51.0
)

canvas.create_text(
    50.0,
    135.0,
    anchor="nw",
    text="Browse and select the image you want to clean: ",
    fill="#000000",
    font=("Arsenal Bold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.2.png"))
image_2 = canvas.create_image(
    249.0,
    30.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()





#Page Three
window = Tk()

window.geometry("500x500")
window.configure(bg = "#FFFFFF")

device_data = True
location_data = True
time_data = True
def click_yes_device_data():
    device_data = True
def click_no_device_data():
    device_data = False
def click_yes_location_data():
    device_data = True
def click_no_location_data():
    device_data = False
def click_yes_time_data():
    device_data = True
def click_no_time_data():
    device_data = False

def delete_the_data():
    if device_data==True:
        if "make" in filter.exif_data.keys():
            filter.remove_exif_data("make")
        if "model" in filter.exif_data.keys():
            filter.remove_exif_data("model")
        if "orientation" in filter.exif_data.keys():
            filter.remove_exif_data("orientation")
        if "software" in filter.exif_data.keys():
            filter.remove_exif_data("software")
        if "datetime" in filter.exif_data.keys():
            filter.remove_exif_data("datetime")
        if "x_resolution" in filter.exif_data.keys():
            filter.remove_exif_data("x_resolution")
        if "y_resolution" in filter.exif_data.keys():
            filter.remove_exif_data("y_resolution")
        if "y_and_c_positioning" in filter.exif_data.keys():
            filter.remove_exif_data("y_and_c_positioning")
        if "_exif_ifd_pointer" in filter.exif_data.keys():
            filter.remove_exif_data("_exif_ifd_pointer")
        if "_gps_ifd_pointer" in filter.exif_data.keys():
            filter.remove_exif_data("_gps_ifd_pointer")
        if "exposure_time" in filter.exif_data.keys():
            filter.remove_exif_data("exposure_time")
        if "f_number" in filter.exif_data.keys():
            filter.remove_exif_data("f_number")
        if "exposure_program" in filter.exif_data.keys():
            filter.remove_exif_data("exposure_program")
        if "photographic_sensitivity" in filter.exif_data.keys():
            filter.remove_exif_data("photographic_sensitivity")
        if "exif_version" in filter.exif_data.keys():
            filter.remove_exif_data("exif_version")
        if "offset_time" in filter.exif_data.keys():
            filter.remove_exif_data("offset_time")
        if "offset_time_original" in filter.exif_data.keys():
            filter.remove_exif_data("offset_time_original")
        if "shutter_speed_value" in filter.exif_data.keys():
            filter.remove_exif_data("shutter_speed_value")
        if "aperture_value" in filter.exif_data.keys():
            filter.remove_exif_data("aperture_value")
        if "exposure_bias_value" in filter.exif_data.keys():
            filter.remove_exif_data("exposure_bias_value")
        if "metering_mode" in filter.exif_data.keys():
            filter.remove_exif_data("metering_mode")
        if "flash" in filter.exif_data.keys():
            filter.remove_exif_data("flash")
        if "focal_length" in filter.exif_data.keys():
            filter.remove_exif_data("focal_length")
        if "color_space" in filter.exif_data.keys():
            filter.remove_exif_data("color_space")
        if "pixel_x_dimension" in filter.exif_data.keys():
            filter.remove_exif_data("pixel_x_dimension")
        if "pixel_y_dimension" in filter.exif_data.keys():
            filter.remove_exif_data("pixel_y_dimension")
        if "exposure_mode" in filter.exif_data.keys():
            filter.remove_exif_data("exposure_mode")
        if "white_balance" in filter.exif_data.keys():
            filter.remove_exif_data("white_balance")
        if "digital_zoom_ratio" in filter.exif_data.keys():
            filter.remove_exif_data("digital_zoom_ratio")
        if "focal_length_in_35mm_film" in filter.exif_data.keys():
            filter.remove_exif_data("focal_length_in_35mm_film")
        if "scene_capture_type" in filter.exif_data.keys():
            filter.remove_exif_data("scene_capture_type")
    if location_data == True:
        if "gps_latitude_ref" in filter.exif_data.keys():
            filter.remove_exif_data("gps_latitude_ref")
        if "gps_latitude" in filter.exif_data.keys():
            filter.remove_exif_data("gps_latitude")
        if "gps_longitude_ref" in filter.exif_data.keys():
            filter.remove_exif_data("gps_longitude_ref")
        if "gps_longitude" in filter.exif_data.keys():
            filter.remove_exif_data("gps_longitude")
    if time_data == True:
        if "datetime_original" in filter.exif_data.keys():
            filter.remove_exif_data("datetime_original")
        if "datetime_digitized" in filter.exif_data.keys():
            filter.remove_exif_data("datetime_digitized")
    window.destroy()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_3.1.png"))
image_1 = canvas.create_image(
    249.0,
    452.0,
    image=image_image_1
)
# generate Image
button_image_1 = PhotoImage(
    file=relative_to_assets("button_3.1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=delete_the_data,
    relief="flat"
)
button_1.place(
    x=158.0,
    y=330.0,
    width=184.0,
    height=51.0
)
# no button for delete time data
button_image_2 = PhotoImage(
    file=relative_to_assets("button_3.2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=click_no_time_data,
    relief="flat"
)
button_2.place(
    x=342.0,
    y=272.0,
    width=76.0,
    height=31.0
)
# yes button for delete time data
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=click_yes_time_data,
    relief="flat"
)
button_3.place(
    x=259.0,
    y=272.0,
    width=76.0,
    height=31.0
)

canvas.create_text(
    61.0,
    276.0,
    anchor="nw",
    text="Delete Time Data?",
    fill="#000000",
    font=("Arsenal Regular", 18 * -1)
)
# no button for delete location data
button_image_4 = PhotoImage(
    file=relative_to_assets("button_3.4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=click_no_location_data,
    relief="flat"
)
button_4.place(
    x=342.0,
    y=218.0,
    width=76.0,
    height=31.0
)

# yes button for delete location data
button_image_5 = PhotoImage(
    file=relative_to_assets("button_3.5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=click_yes_location_data,
    relief="flat"
)
button_5.place(
    x=259.0,
    y=218.0,
    width=76.0,
    height=31.0
)

canvas.create_text(
    49.0,
    218.0,
    anchor="nw",
    text="Delete Location Data?",
    fill="#000000",
    font=("Arsenal Regular", 18 * -1)
)

# no button for delete device data
button_image_6 = PhotoImage(
    file=relative_to_assets("button_3.6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=click_no_device_data,
    relief="flat"
)
button_6.place(
    x=342.0,
    y=159.0,
    width=76.0,
    height=31.0
)

# button 7 is the yes button for device data
button_image_7 = PhotoImage(
    file=relative_to_assets("button_3.7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=click_yes_device_data,
    relief="flat"
)
button_7.place(
    x=259.0,
    y=159.0,
    width=76.0,
    height=31.0
)



canvas.create_text(
    56.0,
    163.0,
    anchor="nw",
    text="Delete Device Data?",
    fill="#000000",
    font=("Arsenal Regular", 18 * -1)
)

canvas.create_text(
    129.0,
    98.0,
    anchor="nw",
    text="Choose metadata to remove:",
    fill="#000000",
    font=("Arsenal Bold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_3.2.png"))
image_2 = canvas.create_image(
    249.0,
    30.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()





#Page 4
window = Tk()

window.geometry("500x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def save_new_photo():
    location = filter.ask_for_save_loc();
    filter.save_file(location)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_4.1.png"))
image_1 = canvas.create_image(
    249.0,
    452.0,
    image=image_image_1
)

canvas.create_text(
    89.0,
    344.0,
    anchor="nw",
    text="Thank you for using Project Incognito!",
    fill="#000000",
    font=("Arsenal Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=148.0,
    y=265.0,
    width=198.0,
    height=51.0
)

canvas.create_text(
    104.0,
    215.0,
    anchor="nw",
    text="Upload cleaned image to Incognito Repository\n(internet connection required):",
    fill="#000000",
    font=("Arsenal Regular", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_4.2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=save_new_photo,
    relief="flat"
)
button_2.place(
    x=158.0,
    y=141.0,
    width=184.0,
    height=51.0
)

canvas.create_text(
    70.0,
    111.0,
    anchor="nw",
    text="Save cleaned image to your local device as a PNG or JPG:",
    fill="#000000",
    font=("Arsenal Regular", 16 * -1)
)

canvas.create_text(
    125.0,
    76.0,
    anchor="nw",
    text="Your image has been cleaned!",
    fill="#000000",
    font=("Arsenal Bold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_4.2.png"))
image_2 = canvas.create_image(
    246.0,
    30.0,
    image=image_image_2
)

canvas.create_text(
    189.0,
    375.0,
    anchor="nw",
    text="Return to Homepage",
    fill="#0057B7",
    font=("Arsenal Bold", 14 * -1)
)
window.resizable(False, False)
window.mainloop()



