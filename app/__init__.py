import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


class Proj:
    def __init__(self, name, descrip, git, demo, img) -> None:
        self.name = name
        self.descrip = descrip
        self.git = git
        self.demo = demo
        self.img = img


class Polaroid:
    def __init__(self, caption, pic):
        self.caption = caption
        self.pic = pic


class Exp:
    def __init__(self, name, descrip) -> None:
        self.name = name
        self.descrip = descrip


pols = [
    Polaroid("Caption of polaroid 1", "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&poi=%5B1936%2C1296%5D&w=3872&h=1936&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F35%2F2019%2F08%2F05144705%2FGettyImages-96709750-1.jpg"),
    Polaroid("Caption of polaroid 2", ".\static\img\R.jpg"),
    Polaroid("Caption of polaroid 3",
             "https://www.success.com/wp-content/uploads/2016/09/therealreasontravelingmakesyouhappy.jpg")
]


@app.route('/')
def index():

    projs = [
        Proj("Google Maps", "A project that resemble features of Google Maps. This project was divided into 4 Milestones that allowed further development of the map. These 4 milestones included: Implementation of functions that assisted in further milestones, Implementing and bettering the GUI, Implementation of Path-Finding Algorithms and Travelling-Salesman Algorithms.",
             "https://google.com/", "https://github.com/", "https://www.google.com/images/branding/product/2x/maps_96in128dp.png"),
        Proj("Designing a Processor", "Design of a processor written in verilog, which supports LEDR and the push buttons. Processor is able to support instructions such as add, substract, move, move-top and branch. Quartus Prime software was used to implement this project in verilog. Processor was tested through test benches and ModelSim Simulations to ensure correctness.",
             "https://github.com/", "https://github.com/AbishaKugathasan/ECE243-Labs", "https://www.google.com/images/branding/product/2x/maps_96in128dp.png"),
        Proj("Assembly Language Programs", "Collection of projects that is written in ARM. These projects utilizes I/O devices such as the LEDR, 7-Segment Display, Push Buttons, Switches and the A9-Private Timer. These programs were tested on a DE1-Soc Board.",
             "https://github.com/", "https://github.com/AbishaKugathasan/ECE243-Labs", "https://www.google.com/images/branding/product/2x/maps_96in128dp.png"),
        Proj("Video Games", "Collection of video games that are created in teams. Video games created include video games that connect to the VGA display. These games use animations and input/output devices. Also, includes video games that are played on desktop or mobile",
             "https://github.com/", "https://github.com/", "https://www.google.com/images/branding/product/2x/maps_96in128dp.png")
    ]

    exps = [
        Exp("University of Toronto Robotics Association", ["point1", "point 2", "point 3"]),
        Exp("Experience 2", ["point 1", "point 2", "point 3"]),
        Exp("Experience 3", ["point 1", "point 2", "point 3"]),
        Exp("Experience 4", ["point 1", "point 2", "point 3"])
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=pols, experiences=exps)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), polaroids=pols)
