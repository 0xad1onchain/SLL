from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def server():
    if request.method == "GET":
        return render_template('index.html', msg="YOLO")
    if request.method == "POST":
        date = request.form['dob']
        print(date)
        a=[]
        date = date.split('/')
        for i in date:
            a.append(int(i))
        print (a)
        try:
            datetime.datetime(a[2], a[1], a[0])
        except ValueError:
            return render_template('index.html', msg="Date not correct")
        return render_template('index.html', msg="Submit Successful")




if __name__ == "__main__":
    app.run(debug=True)