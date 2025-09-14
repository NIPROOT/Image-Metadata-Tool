# Image Metadata Extractor & Remover

**Owner:** niproot  
**Email:** ilianothingg@gmail.com

![Banner](https://media.giphy.com/media/3o7aD4nmHFlxzwuEFO/giphy.gif)

---

## Project Overview

The **Image Metadata Extractor & Remover** is a **Python CLI tool** for analyzing, extracting, and removing metadata from images. It provides full EXIF extraction, camera information, GPS coordinates, and complete metadata removal for privacy protection.

This tool is perfect for photographers, developers, security analysts, and privacy-conscious users.

### Features

1. **Full Metadata Extraction**
   - Extract all EXIF tags
   - Camera make, model, lens info
   - Exposure, ISO, date/time, software info
   - Orientation and image details

2. **Camera Information Extraction**
   - Detect camera make and model
   - Detect lens model
   - Track photography equipment metadata

3. **GPS Location Extraction**
   - Convert DMS to Decimal Degrees
   - Handles N/S/E/W references
   - Reverse geocode to human-readable addresses using Nominatim

4. **Remove Metadata**
   - Remove all EXIF metadata safely
   - Preserve image quality
   - Protect privacy when sharing images online

5. **Interactive CLI**
   - Menu-driven command-line interface
   - Colorful outputs using `colorama`
   - Commands accessible continuously until exit

![CLI GIF](https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif)

---

## Installation

1. **Clone Repository**
```bash
git clone https://github.com/niproot/ImageMetadataTool.git
cd ImageMetadataTool
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Tool**
```bash
python main.py
```

---

## File Structure

```
main.py            # Main execution script with CLI
requirements.txt   # Python dependencies
```

### main.py Functions

- `get_image_metadata(path)` - Extract all EXIF tags
- `get_camera_info(path)` - Camera make, model, lens info
- `get_location_info(path)` - GPS coordinates and reverse geocoding
- `remove_meta_data(path)` - Remove all metadata from image

### requirements.txt
```
Pillow
piexif
colorama
geopy
```

---

## Usage

### Step 1: Launch CLI
```text
$ python main.py
```

### Step 2: Enter Image Path
```text
Image Path ---> /path/to/image.jpg
```

### Step 3: Use Commands

| Command | Action |
|---------|--------|
| 1       | Extract all metadata |
| 2       | Show camera info |
| 3       | Show GPS location info |
| 5       | Remove all metadata |
| help    | Show commands |
| exit    | Exit program |

![Usage GIF](https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif)

---

## Example Session

```text
$ python main.py
Image Path ---> example.jpg
COMMAND ---> 1
----0th----
271: b'Canon'
272: b'Canon EOS 80D'
---Exif---
33434: (1, 60)
36867: b'2025:09:14 16:00:00'
---GPS---
1: b'N'
2: ((37,1),(48,1),(30,1))
3: b'E'
4: ((122,1),(25,1),(0,1))
COMMAND ---> 5
All MetaData Removed!!!
```

![Session GIF](https://media.giphy.com/media/3o7TKM3zON8ioZjxO0/giphy.gif)

---

## GPS Handling

- Converts DMS to Decimal Degrees
- Considers GPSLatitudeRef and GPSLongitudeRef for N/S/E/W
- Reverse geocodes using `geopy.Nominatim`
- Displays human-readable location for extracted GPS

![GPS GIF](https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif)

---

## Privacy & Security

- Removes GPS, camera info, and EXIF metadata
- Protects privacy before uploading images online
- Ensures sensitive information is not leaked

---

## Screenshots & GIFs

![Metadata Screenshot](https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif)
![Remove Screenshot](https://media.giphy.com/media/xUOxf0rYFZ5fD4Hpuo/giphy.gif)

---

## Future Plans

- Add support for PNG, TIFF, and RAW formats
- GUI drag-and-drop interface
- Batch processing for multiple images
- Cloud integration for remote analysis
- Enhanced error handling and logging

![Future GIF](https://media.giphy.com/media/3o7aD6tMZ6bx0pEd7a/giphy.gif)

---

## Contributing

- Fork the repository
- Create feature/fix branch
- Submit pull request
- Report issues via GitHub

---

## License

This project is licensed under the **Apache License 2.0**.

You are free to:
- Use
- Modify
- Distribute
- Contribute

Refer to the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) for full details.

---

## Contact

**Owner:** niproot  
**Email:** ilianothingg@gmail.com  
**GitHub:** [https://github.com/niproot](https://github.com/niproot)

![Contact GIF](https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif)


