import os
from time import time
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import * 
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv('TESTING') == 'true':
    print('Running in test mode')
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared',uri=True)
else: 
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
        user = os.getenv("MYSQL_USER"), 
        password = os.getenv("MYSQL_PASSWORD"), 
        host = os.getenv("MYSQL_HOST"), 
        port = 3306
        )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta: 
        database = mydb 

mydb.connect()
mydb.create_tables([TimelinePost])
#project
class Proj:
    def __init__(self, name, descrip, git) -> None:
        self.name = name
        self.descrip = descrip
        self.git = git
       # self.demo = demo


class Polaroid:
    def __init__(self, caption, pic):
        self.caption = caption
        self.pic = pic


class Exp:
    def __init__(self, name, descrip) -> None:
        self.name = name
        self.descrip = descrip


pols = [
    Polaroid("Swimming", "https://i.pinimg.com/736x/54/2d/e8/542de8a80f8a4c58cf42e37ee88f8ee9.jpg"),
    Polaroid("Hiking", ".\static\img\R.jpg"),
    Polaroid("Tennis",
             "https://i.pinimg.com/564x/e3/84/fb/e384fbdab133e1237f5e6d8af6ad5df2--spring-style-sporty.jpg")
]


@app.route('/')
def index():

    projs = [
        Proj("Google Maps", "A project that resembles and adds onto features of Google Maps.","https://www.google.ca/"),
        Proj("Designing a Processor", "Design of a processor written in verilog, which supports I/O devices and instructions.","https://www.google.ca/"),
        Proj("Assembly Language Programs", "Collection of projects that is written in ARM. which works on DE1-Soc Board." ,"https://www.google.ca/"),
        Proj("Bean Counter", "Game where player dodges obstacles to load a truck.","https://www.google.ca/"),
        Proj("Mario's Pizzeria", "Game where player needs to make a pizza according to customer's orders.","https://www.google.ca/"), 
        Proj("Personal Portfolio", "Showcases my interests, education, experience etc.","https://www.google.ca/"), 
        Proj("WeGrowth", "Children's app that teaches them about the environment and resembles flappy bird","https://www.google.ca/")
    ]

    exps = [
        Exp("UofT Robotics Association 🤖",  ["Team Member", " Present"]),
        Exp("Meta x MLH Fellowship 🖥️ ", ["Fellow", "Present"]),
        Exp("UofT West Wall Project ", ["Engineering Team", "Jan 2020 - June 2020"]),
        Exp("Experience 4", ["Click here to download"]),
        Exp("Experience 5", ["point 1", "point 2"]),
        Exp("Experience 6", ["point 1", "point 2"])
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=pols, experiences=exps)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), polaroids=pols)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post(): 
    name = request.form.get('name',None)
    if name == None:
        return "Invalid name", 400
    
    email = request.form['email']
    if not '@' in email:
        return "Invalid email",400
        
    content = request.form['content']
    if content == "":
        return "Invalid content", 400
    
    timeline_post=TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods =['GET'])
def get_time_line_post(): 
    return{
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods =['DELETE'])
def delete_time_line_post(): 
    id = request.form['id']
    TimelinePost.delete_by_id(id)
    return{
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline(): 
    return render_template('timeline.html', title="Timeline", TimelinePost=TimelinePost)

   