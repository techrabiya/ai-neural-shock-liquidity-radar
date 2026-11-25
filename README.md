⚡ AI Neural Shock & Liquidity Radar 🧠📉

An interactive real-time stress-testing and liquidity-risk simulation platform built with Python and Streamlit. This application models how sudden market crashes, volatility spikes, and liquidity dry-ups affect a multi-asset trading book, calculating execution slippage and triggering automated risk guardrails before losses escalate. 💥📊

🧠 What This Application Does 🎯

Financial markets rarely fail from price movement alone—when volatility surges, liquidity often disappears at the exact moment positions need to be reduced. AI Neural Shock & Liquidity Radar bridges that gap by combining price-shock modeling with liquidity haircut simulation in a single interactive dashboard. ⚡🛡️

Users can adjust market shock severity, volatility regime multipliers, liquidity haircuts, and hard risk ceilings to observe how capital, PnL, slippage drag, and position-level risk alerts respond instantaneously. 🎛️📈

🚀 Key Capabilities ✨

1. Interactive Multi-Factor Stress Testing: Adjust market crash percentages (0% to -45%), volatility regime multipliers (1.0x to 4.5x), liquidity haircuts (0% to 65%), and hard risk ceilings in real time. 🎛️🔥
2. Liquidity Slippage & Execution Drag Modeling: Calculates hidden liquidation costs caused by thin order books during severe market stress. 💧📉
3. Automated AI Guardrail Engine: Evaluates each asset against risk thresholds and assigns clear operational statuses: 🤖🚨
4. ✅ NORMAL REGIME — Risk remains within standard operating parameters. 🟢✨
5. ⚠️ TRIM EXPOSURE — Volatility or drawdown pressure requires gradual position reduction. 🟡⚖️
6. 🚨 AI HARD BREAKER — Critical risk or liquidity limit breached; immediate de-risking required. 🔴🛑
7. Dynamic Scenario Trajectory Curve: Plots raw price-shock impact against liquidity-adjusted total stress across shock levels from 0% to -45%. 📈📊
8. Granular Asset-Level Risk Matrix: Breaks down allocated capital, shock PnL, effective haircut percentages, slippage losses, and net stress impact across every instrument and trading desk. 📋💎

⚙️ How It Works 🔄

1. Input Stress Parameters: Configure market shock, volatility multiplier, liquidity haircut, and portfolio risk limit from the control sidebar. 🎚️⚙️
2. Regime & Impact Computation: The engine scales shock severity using the active volatility regime multiplier and applies asset-specific weights and base liquidity haircuts. 🧮⚡
3. Slippage & Net Equity Calculation: Execution slippage is deducted alongside direct PnL loss to show realistic post-stress capital. 💰📉
4. Guardrail Classification: Each instrument is evaluated against the configured risk ceiling and haircut thresholds to generate actionable risk alerts. 🚨✅

📁 Project Structure 📂

1. ai-neural-shock-liquidity-radar/ 📦
2. engine/ai_liquidity_sentinel.py — Core Streamlit interface, stress-testing calculations, scenario curves, and risk matrix. 💻⚡
3. requirements.txt — Python dependencies (streamlit, pandas, numpy). 📦🛠️
4. README.md — Project documentation and setup instructions. 📖✨

🛠️ How to Run Locally 💻🚀

1. Clone the repository to your local machine and open the project folder in your terminal
   (git clone https://github.com/techrabiya/ai-neural-shock-liquidity-radar)

2. Install the required dependencies (pip install -r requirements.txt). 📦🔧

3. Run the Streamlit application (streamlit run engine/ai_liquidity_sentinel.py). ▶️🚀

🔗 Live Demo
Live Application:https://ai-neural-shock-liquidity-radar-6ek4jznkwnqgxb5w3wgjlx.streamlit.app/

👩‍💻 Created By 🌟🎓
  Rabia Razzaq Khan ✨7th-Grade Student | Aspiring Data Scientist & AI Risk Modeling Enthusiast 🧠📊🚀

Focused on building practical Python, SQL, and quantitative risk-analytics applications that turn real-world financial and data challenges into clean, interactive engineering solutions. 💡🔥
