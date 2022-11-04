from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "static/"

@app.route("/upload-resume")
def upload():
   return render_template("upload.html")

@app.route("/resume-details", methods = ['POST', 'GET'])
def details():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)
        return redirect('static/'+filename)
   

if __name__ == "__main__":
   app.run(debug=True)
