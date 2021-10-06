from flask import Flask, render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"].replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer(), primary_key=True)
    data = db.Column(db.Text())
    date = db.Column(db.Text())



@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        r = request.data
        r = r.decode("utf-8")


        i = Data(data=r, date=str(datetime.now()))
        db.session.add(i)
        db.session.commit()


    return render_template("index.html")



if __name__ == '__main__':
    app.listen(process.env.PORT or 3000)
    app.run(debug=False)