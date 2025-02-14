import os
import aiohttp
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class CryptoService:
    def __init__(self):
        self.solscan_api_key = os.getenv("SOLSCAN_API_KEY")
        self.coingecko_api_key = os.getenv("COINGECKO_API_KEY")
        self.binance_api_key = os.getenv("BINANCE_API_KEY")
        
        self.solscan_base_url = "https://api.solscan.io/v2"
        self.coingecko_base_url = "https://api.coingecko.com/api/v3"
        self.binance_base_url = "https://api.binance.com/api/v3"

    async def get_token_info(self, token_address: str) -> Dict[str, Any]:
        """Get detailed token information from Solscan"""
        try:
            async with aiohttp.ClientSession() as session:
                headers = {"Authorization": f"Bearer {self.solscan_api_key}"}
                url = f"{self.solscan_base_url}/token/{token_address}"
                
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to get token info: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching token info: {str(e)}")
            return None

    async def get_market_data(self, coin_id: str) -> Dict[str, Any]:
        """Get market data from CoinGecko"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.coingecko_base_url}/coins/{coin_id}/market_data"
                params = {"x_cg_api_key": self.coingecko_api_key}
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to get market data: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching market data: {str(e)}")
            return None

    async def get_price_history(self, symbol: str, interval: str = "1d") -> List[Dict[str, Any]]:
        """Get price history from Binance"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.binance_base_url}/klines"
                params = {
                    "symbol": symbol,
                    "interval": interval,
                    "limit": 100
                }
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to get price history: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching price history: {str(e)}")
            return None

    async def get_market_sentiment(self, coin_id: str) -> Dict[str, Any]:
        """Get market sentiment data from CoinGecko"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.coingecko_base_url}/coins/{coin_id}/sentiment"
                params = {"x_cg_api_key": self.coingecko_api_key}
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to get sentiment data: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching sentiment data: {str(e)}")
            return None 