from PIL import Image
import piexif
from colorama import Fore
import os
from geopy.geocoders import Nominatim



banner = Fore.CYAN+"""

           /$$                                             /$$              
          |__/                                            | $$              
 /$$$$$$$  /$$  /$$$$$$          /$$$$$$/$$$$   /$$$$$$  /$$$$$$    /$$$$$$ 
| $$__  $$| $$ /$$__  $$ /$$$$$$| $$_  $$_  $$ /$$__  $$|_  $$_/   |____  $$
| $$  \ $$| $$| $$  \ $$|______/| $$ \ $$ \ $$| $$$$$$$$  | $$      /$$$$$$$
| $$  | $$| $$| $$  | $$        | $$ | $$ | $$| $$_____/  | $$ /$$ /$$__  $$
| $$  | $$| $$| $$$$$$$/        | $$ | $$ | $$|  $$$$$$$  |  $$$$/|  $$$$$$$
|__/  |__/|__/| $$____/         |__/ |__/ |__/ \_______/   \___/   \_______/
              | $$                                                          
              | $$                                                          
              |__/                    
              
  _ 
 / |
 | | --- FOR EXTRACKT METADATA
 |_|
 
 
  ___ 
 |_  )
  / / --- FOR EXTRACKT CAMERA DATA
 /___|
      


  ____
 |__ /
  |_ \ --- FOR EXTRACKT LOCATION DATA
 |___/
      
  _ _  
 | | | 
 |_  _| --- FOR REMOVE METADATA
   |_| 
       
                                   
"""
def get_location_info(path):
    try:
        image = Image.open(path)
        exif_bytes = image.info.get("exif") 
        if not exif_bytes:
            print("No EXIF data found")
            return
        exif_dict = piexif.load(exif_bytes)
        gps_data = exif_dict.get("GPS", {})
        if gps_data:
            lat = gps_data.get(piexif.GPSIFD.GPSLatitude)
            lon = gps_data.get(piexif.GPSIFD.GPSLongitude)
    
            def dms_to_dd(dms):
                return dms[0][0]/dms[0][1] + dms[1][0]/dms[1][1]/60 + dms[2][0]/dms[2][1]/3600
            latitude = dms_to_dd(lat)
            longitude = dms_to_dd(lon)

            geolocator = Nominatim(user_agent="geoapi")
            location = geolocator.reverse((latitude, longitude))
            print(location.address)
    except Exception as Ex:
        print(Fore.RED+f"ERROR: {Ex}")

def get_camera_info(path):
    try:
        image = Image.open(path)
        exif_bytes = image.info.get("exif") 
        if not exif_bytes:
            print("No EXIF data found")
            return
        exif_dict = piexif.load(exif_bytes)
        camera_make = exif_dict["0th"].get(piexif.ImageIFD.Make)
        camera_model = exif_dict["0th"].get(piexif.ImageIFD.Model)
        lens_model = exif_dict["Exif"].get(piexif.ExifIFD.LensModel)

        print("Camera Make:", camera_make.decode() if camera_make else None)
        print("Camera Model:", camera_model.decode() if camera_model else None)
        print("Lens Model:", lens_model.decode() if lens_model else None)
    except Exception as Ex:
        print(Fore.RED+f"ERROR: {Ex}")

def get_image_metadata(path):
    try:
        image = Image.open(path)
        exif_bytes = image.info.get("exif") 
        if not exif_bytes:
            print("No EXIF data found")
            return
        exif_dict = piexif.load(exif_bytes)
        for idf in exif_dict:
            print(Fore.RED+f"----{idf}----")
            for tag in exif_dict[idf]:
                print(Fore.RED+f"{tag}: {exif_dict[idf][tag]}")
            print("EXIF loaded successfully")
    except Exception as Ex:
        print(Fore.RED+f"ERROR: {Ex}")

def remove_meta_data(path):
    try:
        image = Image.open(path)
        exif_bytes = image.info.get("exif") 
        if not exif_bytes:
            print("No EXIF data found")
            return
        
        piexif.remove(path)
        print("All MetaData Removed!!!")
    except Exception as Ex:
        print(Fore.RED+f"ERROR: {Ex}")


    
def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        get_image_path = input(Fore.GREEN+"Image Path ---> ")
        if os.path.exists(get_image_path):
            os.system('cls' if os.name == 'nt' else 'clear')
            image = Image.open(get_image_path)
            if "exif" in image.info:
                print(banner)
                while True:
                    cli = input(Fore.RED+"COMMAND ---> ")
                    if cli == "":
                        continue
                    elif cli == "1":
                        get_image_metadata(get_image_path)
                    elif cli == "2":
                        get_camera_info(get_image_path)
                    elif cli == "3":
                        get_location_info(get_image_path)
                    elif cli == "4":
                        remove_meta_data(get_image_path)
                    else:
                        print(Fore.CYAN+"Please Input at 1 - 5")
                        continue
            else:
                print("No EXIF data found in this image")
                exif_dict = None
        else:
            print(Fore.LIGHTBLUE_EX+"File Path is wrong Try Again")
    except Exception as Ex:
        print(Fore.RED+f"ERROR: {Ex}")
    
if __name__ == "__main__":
    main()