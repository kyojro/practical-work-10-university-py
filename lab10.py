from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://pulsito:Writ8rUA@db4free.net/python_lab9' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    type = db.Column(db.String(120), unique=True)
    time= db.Column(db.Time, unique=True)

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(120), unique=True)

class Servers_Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    type = db.Column(db.String(120), unique=True)
    server_id = db.Column(db.Integer)


@app.route('/')
def add_example():
    id = int(1) 
    email = "email_for_notification@email.com"
    notify_type = "notification_type_example"
    time =  datetime.time(datetime.now()).strftime("%Y-%m-%d-%H:%M:%S") 

    server_name = "server_name_example"
    server_location = "server_location_example"

    group_name = "group_name_example"
    group_type = "group_type_example"

    servers_group = "servers_group_example"
    notification = Notification(id = id, email = email, type = notify_type, time = time)
    server = Server(id = id, name = server_name, location = server_location)
    servers_group = Servers_Group(id=id, name= group_name, type = group_type ,server_id=id )
    try:
        db.session.add(notification)
        db.session.add(server)
        db.session.add(servers_group)
        db.session.commit()
        return "Succesfully"
    except Exception as ex:
        return f"{ex} "

if(__name__) == "__main__":
    app.run()