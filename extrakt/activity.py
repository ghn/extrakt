from tcx2gpx.tcx2gpx import TCX2GPX


def open_activity(file_path):
    validate_input_file(file_path)
    gpx_file = open(file_path, "r")
    return gpxpy.parse(gpx_file)


def convert_tcx(file_path):
    gps_object = TCX2GPX(tcx_path=file_path)
    gps_object.convert()


def validate_input_file(file_path):
    VALID_EXTENSIONS = ("gpx", "gpx.gz", "tcs", "tcx.gz")

    if file_path.endswith(VALID_EXTENSIONS):
        return True
    else:
        raise ValueError(f"The format of '{file_path}' is not accepted")
