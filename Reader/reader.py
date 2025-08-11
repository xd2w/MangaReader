"""
A lightweight manga reader using Flask.

This file must be ran in the directory with folder with volumes.

"""

import os
import glob

from flask import Flask, send_file, render_template, send_from_directory

dir_path = "Books"

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

    text_files = glob.glob(os.path.join(dir_path, series, "*.txt"))
    if text_files:
        vol_list.extend([os.path.basename(f) for f in text_files])

    # print(vol_list)
    # exit()

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
        # return send_file(f"{dir_path}/{series}/{vol}/{path}")
        return send_from_directory(f"{dir_path}/{series}/{vol}", path)
    except FileNotFoundError:
        return "File not found", 404


@app.route("/reader/txt/<series>/<vol>")
def viewer_txt(series, vol):
    # return render_template(
    #     "viewer_txt.html", series=series, vol=vol, disp_style="horizontal-scroll"
    # )
    with open(f"{dir_path}/{series}/{vol}.txt", "r", encoding="cp932") as file:
        content = file.read()
    return render_template(
        "viewer_txt.html",
        content=content,
        series=series,
        disp_style="horizontal-scroll",
    )


@app.route("/reader/txt/<series>/contents/<vol>.txt")
def get_txt_file(series, vol):
    try:
        # return send_file(f"{dir_path}/{series}/{vol}.txt")
        return send_from_directory(f"{dir_path}/{series}", f"{vol}.txt")
    except FileNotFoundError:
        return "File not found", 404


@app.route("/reader/epub/<series>/<vol>")
def viewer_htmlz(series, vol):
    return render_template(
        "viewer_htmlz.html", series=series, vol=vol, disp_style="horizontal-scroll"
    )
    return send_from_directory(
        f"{dir_path}/{series}/{vol}", "index.html", mimetype="text/html"
    )


@app.route("/reader/epub/<series>/<vol>/<path:path>")
def get_html_files(series, vol, path):
    try:
        # return send_file(f"{dir_path}/{series}/{vol}/{path}")
        return send_from_directory(f"{dir_path}/{series}/{vol}", path)
    except FileNotFoundError:
        return "File not found", 404


if __name__ == "__main__":
    # webbrowser.open("http://localhost:5000/")
    app.run(host="127.0.0.1", port=5000, debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=False)
