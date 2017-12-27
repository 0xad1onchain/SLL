from flask import Flask, render_template, request
import datetime
#constructor of the class Flask demands __name__ of the app
app = Flask(__name__)

# '/' root route, methods=[] allows both GET and POST methods for request
@app.route('/', methods=['GET', 'POST'])
def server():
    if request.method == "GET":
        #rendering template of index.html and sending msg to the template for interpreting it
        return render_template('index.html', msg="YOLO")
    if request.method == "POST":
        #request.form is an object that allows you to access arugments in the form according to their name in the form
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
            #error msg
            return render_template('index.html', msg="Date not correct")
        marks= []
        marks.append(int(request.form['mark1']))
        marks.append(int(request.form['mark2']))
        marks.append(int(request.form['mark3']))
        marks.append(int(request.form['mark4']))
        marks.append(int(request.form['mark5']))
        credit = []
        credit.append(int(request.form['credit1']))
        credit.append(int(request.form['credit2']))
        credit.append(int(request.form['credit3']))
        credit.append(int(request.form['credit4']))
        credit.append(int(request.form['credit5']))
        su=0
        t=0
        for i in range (0, len(marks)):
            su = su + marks[i]*credit[i]
            t = t+credit[i]
        gpa = su/t

        if(gpa > 90):
            gpa = "S"
        elif(gpa > 80):
            gpa = "A"
        elif(gpa > 70):
            gpa = "B"
        elif(gpa > 60):
            gpa = "C"
        elif(gpa > 50):
            gpa = "D"
        elif(gpa > 40):
            gpa = "E"
        else:
            gpa = "F"

        return render_template('index.html', msg="GPA: "+gpa+" Submit Successful")

#running the app in port 5000 by default with debug mode ON
if __name__ == "__main__":
    app.run(debug=True)