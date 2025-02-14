# ORYX - AI-Powered Crypto Assistant

<div align="center">[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.1-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.6.0-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![React](https://img.shields.io/badge/React-17.0.2-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)

ORYX is a state-of-the-art AI-powered cryptocurrency assistant that provides real-time insights, analysis, and market intelligence for crypto traders and enthusiasts. Leveraging advanced machine learning algorithms and real-time data from multiple sources, ORYX helps you make informed decisions in the crypto market.

  <img src="https://raw.githubusercontent.com/oryxai/Oryx/32ec6e7a950304e142770e27cc9057e53f53bd26/assets/longlogo.svg" alt="ORYX Logo" width="200"/>
</div>

## Features

**Real-time Analysis**
- Live cryptocurrency market data
- Instant price updates and alerts
- Real-time trend detection

**AI-Powered Insights**
- Advanced price predictions
- Market sentiment analysis
- Smart trading signals
- Risk assessment

**Market Intelligence**
- Technical indicators
- Volume analysis
- Market correlation tracking
- Liquidity monitoring

**API Integrations**
- Solscan
- CoinGecko
- Binance

## Tech Stack

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)

</div>

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 14+
- PostgreSQL
- Redis

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/oryxai/Oryx.git
cd oryx
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

4. **Start the application**
```bash
python src/main.py
```

## API Documentation

Our API is fully documented using OpenAPI (Swagger) specification. Once the application is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Security

ORYX implements industry-standard security practices:

- JWT authentication
- Rate limiting
- CORS protection
- Environment variable configuration
- Secure API key handling

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find ORYX helpful, please consider giving it a star.

## Contact

- Website: [useoryx.com](https://useoryx.com)
- Twitter: [@useoryx](https://x.com/useoryx.com)
- Repository: [github.com/oryxai/Oryx](https://github.com/oryxai/Oryx)

## Disclaimer

This project is for educational and informational purposes only. Cryptocurrency trading involves substantial risk, and past performance does not guarantee future results. ORYX's predictions and analyses should not be considered as financial advice. 
