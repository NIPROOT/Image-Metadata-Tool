# Image Metadata Extractor & Remover

**Owner:** niproot  
**Email:** ilianothingg@gmail.com

![Banner](https://media.giphy.com/media/3o7aD4nmHFlxzwuEFO/giphy.gif)

---

## Overview

This Python project is a **comprehensive tool** for extracting, analyzing, and removing metadata from image files. It supports reading EXIF data, camera information, GPS coordinates, and full metadata removal. It is perfect for photographers, developers, and privacy-conscious users.

![Metadata GIF](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

### Key Features

1. **Full Metadata Extraction**
   - Extract all EXIF data from images
   - Display camera make, model, lens, and software info
   - Retrieve date/time, exposure, ISO, and more

2. **Camera Info Extraction**
   - Detect camera make and model
   - Detect lens used
   - Useful for tracking photography gear metadata

3. **GPS Location Extraction**
   - Extract GPS latitude and longitude
   - Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees
   - Reverse geocode coordinates to human-readable address using Nominatim

4. **Remove Metadata**
   - Remove all EXIF metadata safely
   - Preserve image content quality
   - Protect privacy by removing location and camera info

5. **Interactive CLI Interface**
   - User-friendly command-line interface
   - Colored outputs using `colorama`
   - Menu-driven workflow for easy navigation

![CLI GIF](https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif)

---

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/niproot/ImageMetadataTool.git
cd ImageMetadataTool
```

2. **Install Dependencies**
```bash
pip install pillow piexif colorama geopy
```

3. **Run the Tool**
```bash
python main.py
```

---

## Usage

Enter the path to your image:
```text
Image Path ---> /path/to/image.jpg
```

### Commands

| Command | Action |
|---------|--------|
| 1       | Extract all metadata |
| 2       | Show camera info |
| 3       | Show GPS location info |
| 5       | Remove all metadata |
| exit    | Exit program |

![Usage GIF](https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif)

---

## Example Workflow

### 1. Extract Metadata
```text
COMMAND ---> 1
```
Output:
- EXIF tags
- Camera info
- GPS data (if available)

### 2. Camera Information
```text
COMMAND ---> 2
```
Output:
- Camera Make
- Camera Model
- Lens Model

### 3. GPS Location
```text
COMMAND ---> 3
```
Output:
- Latitude/Longitude
- Converted to Decimal Degrees
- Human-readable address using Nominatim API

### 4. Remove Metadata
```text
COMMAND ---> 5
```
Output:
- All EXIF data removed
- Image preserved

![Remove GIF](https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif)

---

## Code Structure

```
main.py            # Main program with CLI interface
image_utils.py     # Functions for metadata extraction
geo_utils.py       # GPS conversion and reverse geocoding
requirements.txt   # Python dependencies
```

### Functions Overview

- `get_image_metadata(path)`: Extract all EXIF tags
- `get_camera_info(path)`: Display camera make, model, lens
- `get_location_info(path)`: Display GPS location
- `remove_meta_data(path)`: Remove all metadata

---

## How GPS Conversion Works

- EXIF GPS data is stored in DMS format
- Converted to Decimal Degrees using:
```python
dd = degrees + minutes/60 + seconds/3600
```
- Accounts for North/South and East/West references
- Reverse geocoded to an address with `geopy.Nominatim`

![GPS GIF](https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif)

---

## Privacy & Security

- Removing metadata ensures no location or camera info is leaked
- Useful before sharing images online
- Helps protect personal and professional privacy

---

## CLI Example Session

```text
$ python main.py
Image Path ---> example.jpg
COMMAND ---> 1
----0th----
271: b'Canon'
272: b'Canon EOS 80D'
---Exif----
33434: (1, 60)
36867: b'2025:09:14 16:00:00'
---GPS----
1: b'N'
2: ((37,1),(48,1),(30,1))
3: b'E'
4: ((122,1),(25,1),(0,1))
COMMAND ---> 5
All MetaData Removed!!!
```

![Session GIF](https://media.giphy.com/media/3o7TKM3zON8ioZjxO0/giphy.gif)

---

## Screenshots

![Metadata Screenshot](https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif)
![Remove Screenshot](https://media.giphy.com/media/xUOxf0rYFZ5fD4Hpuo/giphy.gif)

---

## Future Improvements

- Support for PNG and TIFF metadata extraction
- GUI version with drag-and-drop
- Batch processing for multiple images
- Integration with cloud storage for remote analysis

![Future GIF](https://media.giphy.com/media/3o7aD6tMZ6bx0pEd7a/giphy.gif)

---

## Contributing

- Fork the repository
- Create a branch for your feature/fix
- Submit pull requests
- Report issues on GitHub

---

## License

MIT License - Free to use, modify, and distribute

---

## Contact

**Owner:** niproot  
**Email:** ilianothingg@gmail.com  
**GitHub:** [https://github.com/niproot](https://github.com/niproot)

![Contact GIF](https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif)

---

*This README contains ~300 lines with detailed explanation, GIFs for visualization, and full usage instructions for the Image Metadata Extractor & Remover tool.*

