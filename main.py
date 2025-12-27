from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow React frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Hello! This is NullAxis backend."}

@app.post("/query")
def query_handler(q: Query):
    msg = q.message.lower()
    
    if "error" in msg or "issue" in msg:
        return {"response": "Thanks for reaching out! Regarding your issue, here's some information: Try restarting the app and clearing cache. Does this resolve your issue?"}
    elif "feature" in msg or "add" in msg:
        return {"response": "Thank you for your suggestion! We've logged your feature request for our product team to review."}
    elif "buy" in msg or "pricing" in msg:
        return {"response": "Thanks for your interest! Our sales team will be in touch soon. In the meantime, could you tell us more about your needs? How many team members do you have?"}
    else:
        return {"response": "Thanks for your query. I couldn't find an immediate answer, but I've routed your request to our support team. They'll get back to you shortly."}
