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


db.create_all()


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        r = request.data
        r = r.decode("utf-8")
        data_files = 0
        data_files_list = []

        for x in os.scandir("./data/"):
            if "data" in x.name:
                data_files = data_files + 1
                data_files_list.append(x.name)
        if len(data_files_list) == 0:
            xx = 1
        elif data_files > 50:
            xx = 1
        else:
            data_files_num_list = [int(x.replace("data", "").replace(".txt", "")) for x in data_files_list]

            xx = data_files_num_list[-1] + 1
        i = Data(data=r, date=str(datetime.now()))
        db.session.add(i)
        db.session.commit()

    else:
        r = ""
    return render_template("index.html")



if __name__ == '__main__':
    app.listen(process.env.PORT or 3000)
    app.run(debug=True)