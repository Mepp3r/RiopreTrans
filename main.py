from flask import Flask, render_template, request, redirect, url_for
import csv, firefox

app = Flask(__name__, template_folder='templates')

def update():
    with open('cache.csv', newline='') as file_in:
        reader = csv.reader(file_in)
        table = 'Horarios'
        for row in reader:
           table += f"<p>{row}<p>"
        return table
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        idPoint = request.form["id"]
        firefox.firefox(int(idPoint))
        return redirect("/result")
    return render_template('home.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return update()

if __name__ == '__main__':
    app.run(debug=True)