import os
import tempfile
import time

from jinja2 import Environment, FileSystemLoader

IMAGE_DIMENSION = {"width": 1088, "height": 436}  # Strava image size


def create_image(gpx, output_dir, webdriver):
    """
    Generate an image of the gpx trace with the map
    """
    html_config = build_map_config(gpx)

    webpage_path = generate_webpage(html_config)

    webdriver.get(webpage_path)

    time.sleep(1)

    output_file = os.path.join(output_dir, "trace.png")
    webdriver.save_screenshot(output_file)
    # webdriver.quit()

    return output_file


def build_map_config(gpx):
    coordinates = [
        [f"{a.latitude:.6f}", f"{a.longitude:.6f}"]
        for a in gpx.tracks[0].segments[0].points
    ]
    return {"coordinates": coordinates, **IMAGE_DIMENSION}


def generate_webpage(config):
    """
    Create a webpage with the map+trace and returns the file path
    """
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__)))
    )
    template = env.get_template("template.html")
    output_html = template.render(config)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        tmp_file.write(output_html.encode("utf-8"))
        tmp_file_path = tmp_file.name

    return f"file://{tmp_file_path}"
