from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Direktori untuk menyimpan file yang diunggah
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "Tidak ada file yang diunggah"

    file = request.files["file"]

    if file.filename == "":
        return "Pilih file sebelum mengunggah"

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        return redirect(f"http://localhost:8501?file={file.filename}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
