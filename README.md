### Project Pixelprint
Now, you can print anything on https://pixelbattles.ru/ using "main.py" from this repo.

## Using
 1. Clone the repo.
 2. Create a new virtual environment - `python3 -m venv venv`
 3. Activate the virtual environment:
    - On macOS: `source venv/bin/activate`
    - On Linux: Same
    - On Windows: `venv\Scripts\activate`
 4. Copy your image next to "convert.py"
 5. Edit line 39: replace 'slipe.png' with your image filename. You can also edit the output XML filename.
 6. If you change the output XML filename, edit line 74 to match your XML filename.
 7. Add your headers:
    - Open https://pixelbattles.ru/
    - Authorize on the site
    - Press F12 (on Mac - fn+Volume Up)
    - Go to the "Network" tab in the inspector
    - Paint any pixel
    - Open the PUT request named "pix"
    - Scroll to "Request Headers"
    - Check the "Raw" checkbox
    - Copy your headers and paste them into the `headers` dictionary in "main.py", keeping the syntax.
 8. Run the printer using `python3 main.py`

**Note:** If you want to print your image from specific coordinates, list them on line 74 in the "main.py" file.
