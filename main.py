from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

# Configura tu bucket GCP
GCP_BUCKET_NAME = "bkt-sales-data-2611"

client = storage.Client(project='windy-lyceum-475920-n3')


def upload_to_gcp(file):
    """Sube el archivo recibido a GCP Storage."""

    bucket = client.bucket(GCP_BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)
    return f'File {file.filename} uploaded to {GCP_BUCKET_NAME}.'


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        if "file" not in request.files:
            return "No seleccionaste archivo"

        file = request.files["file"]

        if file.filename == "":
            return "Archivo inválido"

        if file:
            upload_to_gcp(file)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
