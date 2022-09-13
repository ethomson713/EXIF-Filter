from tkinter import *
import tkinter as tk
from tkinter import Image
from PIL import *
from PIL import ImageTk, Image
import PIL as pil
from tkinter.filedialog import FileDialog, askdirectory, askopenfilenames, asksaveasfilename
import tkinter.messagebox
from exif_filter import EXIFFilter
class UI():
    def __init__(self):
        ################################################################################
        #
        #
        # HEY WILL! ADD YOUR CODE HERE :)
        #
        #
        #
        #
        #
        #
        #
        #
        ##############################################################################

        self.file = askopenfilenames()
        self.file = self.file[0]
 
        self.filter = EXIFFilter(self.file)
        self.root = tk.Tk(self.file)
        self.root.geometry("400x400")
        self.root.title("EXIF Filter")


        # configure the self.root window
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=4)

        # create a button frame
        self.btn_frame = tk.Frame(self.root)
        self.data_frame = tk.Frame(self.root)
        self.save_photo = tk.Button(self.btn_frame, text="Save Image", command = self.save_new_photo)
        self.save_photo.config(width=20)
        self.save_photo.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.del_camera_info = tk.Button(self.btn_frame, text="Delete Camera Data", command=self.delete_camera_data)
        self.del_gps_info    = tk.Button(self.btn_frame, text="Delete GPS Data", command=self.delete_gps_data)
        self.del_image_info   = tk.Button(self.btn_frame, text="Delete Time Data", command=self.delete_image_data)
        self.del_camera_info.config(width=20)
        self.del_gps_info.config(width=20)
        self.del_image_info.config(width=20)

        self.data_frame.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5, columnspan=5)

        # create a photo frame
        self.photo_frame = tk.Frame(self.root)

        #add frames to the self.root window
        self.btn_frame.grid(row=0, column=0, sticky=tk.NS, padx=5, pady=5)
        self.load_image()
        
        

    def add_deletion_boxes(self):
        self.del_camera_info.grid(row=2, column=0, sticky=tk.W, padx=5 ,pady=5)
        self.del_gps_info.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.del_image_info.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        
    
    def load_image(self):
        img = PhotoImage(fr"{self.file}")
        lbl = Label(self.photo_frame, image=img)
        lbl.grid(row = 5, column=0, sticky=tk.N, padx=5, pady=5)
        self.photo_frame.grid(row=5, column=1, sticky=tk.EW, padx=5, pady=5, columnspan=5)
        self.add_deletion_boxes()
        self.filter.read_exif_data()


    def delete_camera_data(self):
        if "make" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("make")
        if "model" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("model")
        if "orientation" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("orientation")
        if "software" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("software")
        if "datetime" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("datetime")
        if "x_resolution" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("x_resolution")
        if "y_resolution" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("y_resolution")
        if "y_and_c_positioning" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("y_and_c_positioning")
        if "_exif_ifd_pointer" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("_exif_ifd_pointer")
        if "_gps_ifd_pointer" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("_gps_ifd_pointer")
        if "exposure_time" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("exposure_time")
        if "f_number" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("f_number")
        if "exposure_program" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("exposure_program")
        if "photographic_sensitivity" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("photographic_sensitivity")
        if "exif_version" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("exif_version")
        if "offset_time" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("offset_time")
        if "offset_time_original" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("offset_time_original")
        if "shutter_speed_value" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("shutter_speed_value")
        if "aperture_value" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("aperture_value")
        if "exposure_bias_value" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("exposure_bias_value")
        if "metering_mode" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("metering_mode")
        if "flash" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("flash")
        if "focal_length" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("focal_length")
        if "color_space" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("color_space")
        if "pixel_x_dimension" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("pixel_x_dimension")
        if "pixel_y_dimension" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("pixel_y_dimension")
        if "exposure_mode" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("exposure_mode")
        if "white_balance" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("white_balance")
        if "digital_zoom_ratio" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("digital_zoom_ratio")
        if "focal_length_in_35mm_film" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("focal_length_in_35mm_film")
        if "scene_capture_type" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("scene_capture_type")
        tk.messagebox.showinfo(message="Removed Camera Data")
    
    def delete_gps_data(self):
        if "gps_latitude_ref" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("gps_latitude_ref")
        if "gps_latitude" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("gps_latitude")
        if "gps_longitude_ref" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("gps_longitude_ref")
        if "gps_longitude" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("gps_longitude")
        tk.messagebox.showinfo(message="Removed GPS Data")

    def delete_image_data(self):
        if "datetime_original" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("datetime_original")
        if "datetime_digitized" in self.filter.exif_data.keys():
            self.filter.remove_exif_data("datetime_digitized")
        tk.messagebox.showinfo(message="Removed Time Data")

    def save_new_photo(self):
        location = asksaveasfilename()
        self.filter.save_file(location)
        tk.messagebox.showinfo(message="Saved!")

    def run_gui(self):
        self.root.mainloop()
    