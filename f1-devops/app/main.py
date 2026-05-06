from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Welcome to the F1 API"}

@app.get("/standings")
def get_standings():
    return [{"position": 1, "driver" : "Max Verstappen", "team": "Red Bull", "points":77},
            {"position": 2, "driver": "Lando Norris", "team": "McLaren", "points": 62},
            {"position":3, "driver": "Carlos Sainz", "team": "Williams", "points": 24}] 

@app.get("/race-results")
def race_results():
    return[{"position": 1, "driver" : "Max Verstappen", "time": "1:32:07.456", "fastest lap": True},
           {"position": 2, "driver" : "Lando Norris", "time": "1:33:07.456", "fastest lap": False},
           {"position": 3, "driver" : "Carlos Sainz", "time": "1:40:07.456", "fastest lap": False}]