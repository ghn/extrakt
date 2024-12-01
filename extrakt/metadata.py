import os
import yaml


def create_metadata_file(gpx, output_dir):
    output_file = os.path.join(output_dir, "trace.yml")
    with open(output_file, "w") as file:
        data = extract_data(gpx)
        yaml.dump(data, file, default_flow_style=False)

    return output_file


def extract_data(gpx):
    moving_data = gpx.get_moving_data()
    uphill, downhill = gpx.get_uphill_downhill()
    start_time, end_time = gpx.get_time_bounds()

    return {
        "distance": round(gpx.length_3d()),
        "moving_time": moving_data.moving_time,
        "stopped_time": moving_data.stopped_time,
        "uphill": round(uphill),
        "downhill": round(downhill),
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
    }
