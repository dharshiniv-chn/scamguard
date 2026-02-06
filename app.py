from fastapi import FastAPI, Request, HTTPException

app = FastAPI(title="ScamGuard Honeypot API")

API_KEY = "test123"

@app.api_route("/honeypot", methods=["GET", "POST"])
async def honeypot(request: Request):
    key = (
        request.headers.get("x-api-key")
        or request.headers.get("api-key")
        or request.headers.get("X-API-KEY")
    )

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "status": "ok",
        "service": "ScamGuard",
        "message": "Honeypot endpoint reachable"
    }
