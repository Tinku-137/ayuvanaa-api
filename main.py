from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/webhook")
async def gupshup_webhook(request: Request):
    data = await request.json()
    try:
        message = data.get("payload", {}).get("payload", {}).get("text", "")
        phone = data.get("payload", {}).get("sender", {}).get("phone", "")
        name = data.get("payload", {}).get("sender", {}).get("name", "")

        if message.lower() == "hi":
            return JSONResponse(content={
                "message": f"👋 Hello {name}, welcome to Ayuvanaa Personal Assistant!\nPlease fill this form: https://ayuvanaa.com/register/"
            })
        elif message.lower() in ["i am quit", "quit", "stop"]:
            return JSONResponse(content={
                "message": f"🛑 You’ve been unsubscribed, {name}. Thank you!"
            })
        else:
            return JSONResponse(content={"message": "✅ Message received. Thank you!"})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

