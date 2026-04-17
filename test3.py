from flask import Flask, request, render_template
import csv
import io


app = Flask(__name__)
##f = open('test.csv')
##outFile = open('containers.csv', 'w')

##free = csv.reader(f)
##outFile.write("number" + '\n')
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

def write_file(data):
    with open('containers.txt', 'w') as f:
        f.write(str(data))


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['u']
    write_file(text)
    return render_template('form.html')

    

if __name__ == "__main__":
    app.run()