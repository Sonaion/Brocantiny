import os
import mne
import re
import dask.dataframe as dd
import numpy as np
import pandas as pd
import json
import copy
import sys
from pathlib import Path

mne.set_log_level("WARNING")


def load_raw(participant_number, cores=4, digits=2):
    # setup paths for loading
    participant_folder = "./rawData/Participant" + str(participant_number).zfill(digits) + "/"
    eye_tracking_path = participant_folder + "Eyedata_P" + str(participant_number) + ".csv"
    psychopy_csv_path = participant_folder

    # get path for psychopy log and csv data
    for (dirpath, dirnames, filenames) in os.walk(psychopy_csv_path):
        for file in filenames:
            file, ext = os.path.splitext(file)
            if ext == ".csv" and "Study" in file:
                psychopy_csv_path += file + ext

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

    # extract the data from the eye-tracking csv to numbers and rename the columns

    df_0 = pd.DataFrame(ddf_eye_tracking[0].compute().transpose().tolist(), columns=["l_valid"])
    df_1 = pd.DataFrame(ddf_eye_tracking[1].compute().transpose().tolist(), columns=["r_valid"])
    df_2 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[2]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["l_display_x", "l_display_y"], )
    df_3 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[3]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["r_display_x", "r_display_y"], )
    df_4 = pd.DataFrame(ddf_eye_tracking[4].compute().transpose().tolist(), columns=["time"])

    # remove ddf_eye_tracking to save a bit of ram
    del ddf_eye_tracking

    # concat the dataframes to one eyetracking dataframe
    df_eye_tracking = pd.concat([df_0, df_1, df_2, df_3, df_4], axis=1)

    # normalize the time to seconds
    t_0 = df_eye_tracking["time"][0]
    df_eye_tracking["time"] = (df_eye_tracking["time"].astype(float) - t_0) / 1000000.0

    # save the event times in a dataframe for better handling
    columns = [
        "Snippet",
        "SnippetStart",
        "SnippetStop",
        "SnippetInput",
    ]

    # read the data from the psychopy csv file
    df_psydata = pd.read_csv(psychopy_csv_path)

    # create a dataframe which holds the times and answers given for each snippet


    df = pd.DataFrame([],columns=columns)

    df = df.append(pd.DataFrame([["BE", df_psydata["Brocantiny.started"][2], df_psydata["text_5.started"][3], df_psydata["key_resp_6.keys"][2]]], columns=columns))
    df = df.append(pd.DataFrame([["B1", df_psydata["BS1.started"][4], df_psydata["BS2.started"][5], df_psydata["BSI1.keys"][4]]], columns=columns))
    df = df.append(pd.DataFrame([["B2", df_psydata["BS2.started"][5], df_psydata["BS3.started"][6], df_psydata["BSI2.keys"][5]]], columns=columns))
    df = df.append(pd.DataFrame([["B3", df_psydata["BS3.started"][6], df_psydata["BS4.started"][7], df_psydata["BSI3.keys"][6]]], columns=columns))
    df = df.append(pd.DataFrame([["B4", df_psydata["BS4.started"][7], df_psydata["text_6.started"][8], df_psydata["BSI4.keys"][7]]], columns=columns))

    df = df.append(pd.DataFrame([["PE", df_psydata["Brocantiny_2.started"][9], df_psydata["text_5.started"][10], df_psydata["key_resp_7.keys"][9]]], columns=columns))
    df = df.append(pd.DataFrame([["P1", df_psydata["PS1.started"][11], df_psydata["PS2.started"][12], df_psydata["PSI1.keys"][11]]], columns=columns))
    df = df.append(pd.DataFrame([["P2", df_psydata["PS2.started"][12], df_psydata["PS3.started"][13], df_psydata["PSI2.keys"][12]]], columns=columns))
    df = df.append(pd.DataFrame([["P3", df_psydata["PS3.started"][13], df_psydata["PS4.started"][14], df_psydata["PSI3.keys"][13]]], columns=columns))
    df = df.append(pd.DataFrame([["P4", df_psydata["PS4.started"][14], df_psydata["text_2.started"][15], df_psydata["PSI4.keys"][14]]], columns=columns))

    df = df.append(pd.DataFrame([["S1", df_psydata["satz_1.started"][16], df_psydata["satz_2.started"][17], df_psydata["key_resp_2.keys"][16]]], columns=columns))
    df = df.append(pd.DataFrame([["S2", df_psydata["satz_2.started"][17], df_psydata["satz_3.started"][18], df_psydata["key_resp_4.keys"][17]]], columns=columns))
    df = df.append(pd.DataFrame([["S3", df_psydata["satz_3.started"][18], df_psydata["text_3.started"][19], df_psydata["key_resp_5.keys"][18]]], columns=columns))

    df = df.reset_index(drop=True)

    # normalize the time of all the snippets

    t0 = df_psydata["Brocantiny.started"][2]
    df["SnippetStart"] = df["SnippetStart"] - t0
    df["SnippetStop"] = df["SnippetStop"] - t0


    return df, df_eye_tracking

