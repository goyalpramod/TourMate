from fastapi import FastAPI
import uvicorn
from chatbot import generate_message

app = FastAPI()

@app.get("/")
def read_root():
    return {"Greetings": "Welcome to TourMate!"}

@app.post("/get_itinerary")
def make_ititinerary(location: str, duration: str):
    output = generate_message(location,duration)
    return output

if __name__ == "__main__":
    uvicorn.run("api:app", port=8080, reload=True)