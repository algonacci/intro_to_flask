from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structures/")
def render_data_structures():
    
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "Inferno"
    ]
    
    car = {
        "brand": "Tesla",
        "model": "X model",
        "year":"2021",
    }
    
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    
    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons
    }
    
    return render_template("data_structures.html", **kwargs)

@app.route("/conditionals-basics/")
def render_conditionals():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)

@app.route("/for-loop/")
def render_loops_for():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/conditionals/")
def render_for_loop_conditional():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows",
    }
    
    return render_template("loops_and_conditionals.html", user_os=user_os)