import os
import re
import sys

import dask.dataframe as dd
import pandas as pd


def get_data(participant_number, cores=12, digits=2, logging=True):
    # setup output for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, "w")

    print("(1/6) Construct Paths", file=output, flush=True)
    # setup paths for loading
    participant_folder = "./rawData/Participant" + str(participant_number).zfill(digits) + "/"
    eye_tracking_path = participant_folder + "Eyedata_S1_P" + str(participant_number) + ".csv"
    psychopy_csv_path = participant_folder

    # get path for psychopy log and csv data
    for (dirpath, dirnames, filenames) in os.walk(psychopy_csv_path):
        for file in filenames:
            file, ext = os.path.splitext(file)
            if ext == ".csv" and "Eye" not in file:
                psychopy_csv_path += file + ext

    print("(2/6) Read Eye Tracker Data", file=output, flush=True)
    # read tracker data
    df_eye_tracking = pd.read_csv(eye_tracking_path, header=None, sep=";")

    # setup regex for number eextraction
    three_extractor_compiled = re.compile("\((.*), (.*), (.*)\)")
    two_extractor_compiled = re.compile("\((.*), (.*)\)")

    # function to extract numbers from a (x,x,x) format
    def three_extractor(value):
        pattern = three_extractor_compiled.match(value)
        return float(pattern.group(1)), float(pattern.group(2)), float(pattern.group(3))

    # function to extract numbers from a (x,x) format
    def two_extractor(value):
        pattern = two_extractor_compiled.match(value)
        return float(pattern.group(1)), float(pattern.group(2))

    # get type for parallel processing
    meta_type = dd.utils.make_meta(0.0)

    # partition dataframe for parallel work
    ddf_eye_tracking = dd.from_pandas(df_eye_tracking, npartitions=cores)

    print("(3/6) Transform Eye Tracker Data", file=output, flush=True)
    # extract the data from the eye-tracking csv to numbers and rename the columns
    df_0 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[0]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=[
            "l_gaze_point_in_user_coordinate_system_x",
            "l_gaze_point_in_user_coordinate_system_y",
            "l_gaze_point_in_user_coordinate_system_z",
        ],
    )
    df_1 = pd.DataFrame(ddf_eye_tracking[1].compute().transpose().tolist(), columns=["l_valid"])
    df_2 = pd.DataFrame(ddf_eye_tracking[2].compute().transpose().tolist(), columns=["r_valid"])
    df_3 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[3]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=[
            "r_gaze_point_in_user_coordinate_system_x",
            "r_gaze_point_in_user_coordinate_system_y",
            "r_gaze_point_in_user_coordinate_system_z",
        ],
    )
    df_4 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[4]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=[
            "l_gaze_origin_in_user_coordinate_system_x",
            "l_gaze_origin_in_user_coordinate_system_y",
            "l_gaze_origin_in_user_coordinate_system_z",
        ],
    )
    df_5 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[5]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=[
            "r_gaze_origin_in_user_coordinate_system_x",
            "r_gaze_origin_in_user_coordinate_system_y",
            "r_gaze_origin_in_user_coordinate_system_z",
        ],
    )
    df_6 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[6]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["l_display_x", "l_display_y"],
    )
    df_7 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[7]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["r_display_x", "r_display_y"],
    )
    df_8 = pd.DataFrame(ddf_eye_tracking[8].compute().transpose().tolist(), columns=["time"])
    df_9 = pd.DataFrame(ddf_eye_tracking[9].compute().transpose().tolist(), columns=["l_pupil_diameter"])
    df_10 = pd.DataFrame(ddf_eye_tracking[10].compute().transpose().tolist(), columns=["r_pupil_diameter"])

    # remove ddf_eye_tracking to save a bit of ram
    del ddf_eye_tracking

    # concat the dataframes to one eyetracking dataframe
    df_eye_tracking = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10], axis=1)

    print("(4/6) Normalize Eye Tracker Time", file=output, flush=True)
    # normalize the time to seconds
    t_0 = df_eye_tracking["time"][0]
    df_eye_tracking["time"] = (df_eye_tracking["time"].astype(float) - t_0) / 1000000.0

    df_eye_tracking = df_eye_tracking.drop(
        [
            "l_gaze_point_in_user_coordinate_system_x",
            "l_gaze_point_in_user_coordinate_system_y",
            "l_gaze_point_in_user_coordinate_system_z",
        ],
        axis=1,
    )
    df_eye_tracking = df_eye_tracking.drop(
        [
            "r_gaze_point_in_user_coordinate_system_x",
            "r_gaze_point_in_user_coordinate_system_y",
            "r_gaze_point_in_user_coordinate_system_z",
        ],
        axis=1,
    )
    df_eye_tracking = df_eye_tracking.drop(
        [
            "l_gaze_origin_in_user_coordinate_system_x",
            "l_gaze_origin_in_user_coordinate_system_y",
            "l_gaze_origin_in_user_coordinate_system_z",
        ],
        axis=1,
    )

    df_eye_tracking = df_eye_tracking.drop(
        [
            "r_gaze_origin_in_user_coordinate_system_x",
            "r_gaze_origin_in_user_coordinate_system_y",
            "r_gaze_origin_in_user_coordinate_system_z",
        ],
        axis=1,
    )

    print("(5/6) Read PsychoPy Data", file=output, flush=True)

    def get_name(data):
        data = data.split("\\")[-1]
        data = data.split(".")[0]
        return data

    # read the data from the psychopy csv file
    df_psydata = pd.read_csv(psychopy_csv_path)

    print("(6/6) Transform PsychoPy Data", file=output, flush=True)
    df_text = ["Eyetracking", df_psydata["image.started"][2], df_psydata["image_2.started"][2]]

    df_s1 = [get_name(df_psydata["ImagePath"][2]), df_psydata["image_2.started"][2], df_psydata["image_2.started"][3]]
    df_s2 = [get_name(df_psydata["ImagePath"][3]), df_psydata["image_2.started"][3], df_psydata["image_2.started"][4]]
    df_s3 = [get_name(df_psydata["ImagePath"][4]), df_psydata["image_2.started"][4], df_psydata["image_2.started"][5]]
    df_s4 = [get_name(df_psydata["ImagePath"][5]), df_psydata["image_2.started"][5], df_psydata["image_3.started"][6]]

    df_bro = ["BrocantinyErklaerung", df_psydata["image_4.started"][7], df_psydata["image_5.started"][8]]
    df_b1 = [get_name(df_psydata["ImagePath"][8]), df_psydata["image_5.started"][8], df_psydata["image_5.started"][9]]
    df_b2 = [get_name(df_psydata["ImagePath"][9]), df_psydata["image_5.started"][9], df_psydata["image_5.started"][10]]
    df_b3 = [get_name(df_psydata["ImagePath"][10]), df_psydata["image_5.started"][10],
             df_psydata["image_10.started"][11]]

    df_pro = ["programmErklaerung", df_psydata["image_10.started"][11], df_psydata["image_14.started"][12]]
    df_p1 = [get_name(df_psydata["ImagePath"][12]), df_psydata["image_14.started"][12],
             df_psydata["image_14.started"][13]]
    df_p2 = [get_name(df_psydata["ImagePath"][13]), df_psydata["image_14.started"][13],
             df_psydata["image_14.started"][14]]
    df_p3 = [get_name(df_psydata["ImagePath"][14]), df_psydata["image_14.started"][14],
             df_psydata["text_3.started"][15]]

    columns = ["Snippet", "Start", "Stop"]
    df_snippets = pd.DataFrame([], columns=columns)
    df_snippets = df_snippets.append(pd.DataFrame([df_text], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_s1], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_s2], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_s3], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_s4], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_bro], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_b1], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_b2], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_b3], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_pro], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_p1], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_p2], columns=columns))
    df_snippets = df_snippets.append(pd.DataFrame([df_p3], columns=columns))

    return df_snippets, df_eye_tracking
