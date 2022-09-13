from exif_filter import EXIFFilter
from app_ui import UI

class Controller:
    def __init__(self, filter, ui):
        self.filter = filter
        self.ui = ui

    def update_meta_data():
        pass

    def update_ui():
        pass

def test_filter():
    # Create Filter
    filter = EXIFFilter("squid - Copy.jpg")
    # Load photo
    filter.read_exif_data()
    # List Data
    filter.display_data()
    # delete Data
    response = None
    response = input("select a tag to delete: ")
    while (response != 'save'):
        if (response in filter.exif_data.keys()):
            filter.remove_exif_data(response)
        else:
            print(f'{response} is not a valid tag name')
        response = input("select a tag to delete: ")

    filter.display_data()
    # Save Data
    filter.save_file("squid_temp.jpg")

def test_app_ui():
    ui = UI()
    ui.run_gui()

def main():
    #test_filter()
    test_app_ui()

if __name__ == '__main__':
    main()