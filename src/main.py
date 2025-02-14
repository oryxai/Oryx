from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uvicorn
from datetime import datetime

from services.crypto_service import CryptoService
from services.ai_service import AIService
from services.market_service import MarketService

# Load environment variables
load_dotenv()

app = FastAPI(
    title="ORYX AI Crypto Assistant",
    description="Advanced AI-powered cryptocurrency analysis and insights",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
crypto_service = CryptoService()
ai_service = AIService()
market_service = MarketService()

@app.get("/")
async def root():
    return {
        "name": "ORYX AI Crypto Assistant",
        "version": "1.0.0",
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/v1/market/analysis/{coin_id}")
async def get_market_analysis(coin_id: str):
    try:
        market_data = await market_service.get_market_data(coin_id)
        ai_analysis = await ai_service.analyze_market_data(market_data)
        return {
            "coin_id": coin_id,
            "market_data": market_data,
            "analysis": ai_analysis,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/v1/predictions/{coin_id}")
async def get_price_predictions(coin_id: str):
    try:
        predictions = await ai_service.get_price_predictions(coin_id)
        return {
            "coin_id": coin_id,
            "predictions": predictions,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 