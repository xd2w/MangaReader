"""
A lightweight manga reader using Flask.

This file must be ran in the directory with folder with volumes.

"""

import os
import sys
from tkinter import Tk
from tkinter.filedialog import askdirectory
import webbrowser
import zipfile
import glob

from flask import Flask, send_file, render_template

Tk().withdraw()
dir_path = askdirectory(initialdir="~/Documents/mannga", title="Select manga volume")
dir_list = sorted(
    [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]
)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", collection=dir_list)


@app.route("/reader/<series>")
def volumes(series):
    vol_list = [
        f
        for f in os.listdir(os.path.join(dir_path, series))
        if os.path.isdir(os.path.join(dir_path, series, f))
    ]

    if not vol_list:
        return "<h1>No volumes found for this series</h>", 404

    vol_list = sorted(vol_list)

    return render_template("volumes.html", volumes=vol_list, series=series)


@app.route("/reader/<series>/<vol>")
def viewer(series, vol):
    imgs = sorted(os.listdir(f"{dir_path}/{series}/{vol}"))
    # print(f"Volume: {vol}, Images: {imgs}")
    return render_template("viewer.html", series=series, vol=vol, imgs=imgs)


@app.route("/reader/<series>/<vol>/<path:path>")
def get_file(series, vol, path):
    try:
        return send_file(f"{dir_path}/{series}/{vol}/{path}")
    except FileNotFoundError:
        return "File not found", 404


if __name__ == "__main__":
    # webbrowser.open("http://localhost:5000/")
    app.run(host="127.0.0.1", port=5000, debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=False)
