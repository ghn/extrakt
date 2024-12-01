# Extrakt 🦎

Extract metadata and generate the image map of a GPX trace file.

## Usage

```bash
python main.py -f path/to/trace.gpx -o /output/directory
```

Will produce `trace.yml` and `trace.jpg` in the desired location.

or use the package in your python project.

## Image Map Generation Process

The image map is generated from a screenshot of a webpage that displays an OpenStreetMap with a trace rendered using
Leaflet.js. The process follows these steps:

1. **Webpage Creation**: The webpage is first created and saved as a cache file.
2. **Rendering**: Selenium then renders the webpage using a headless Firefox browser.
3. **Screenshot Capture**: A screenshot is taken of the rendered page to produce the image map.

## Development

### Setup

Create virtualenv

OSX

```bash
brew install virtualenv
```

then

```bash
virtualenv venv venv
source venv/bin/activate
pip install .
pip install -r requirements-test.txt
```

### Run tests

```bash
black .
flake8 .
pytest
```

## Inspired by

* [Draw GPS track on openstreetmap](https://blog.aaronlenoir.com/2019/09/25/draw-gps-track-on-openstreetmap/)
