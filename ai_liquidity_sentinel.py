import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AI Neural Shock & Liquidity Radar",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ AI Neural Shock & Liquidity Radar")
st.caption(
    "Real-time AI-driven stress intelligence for market crashes, volatility surges, and liquidity slippage."
)

st.sidebar.header("🎛️ AI Stress & Shock Parameters")
crash_pct = st.sidebar.slider("Market Crash Shock (%)", min_value=-45.0, max_value=0.0, value=-20.0, step=1.0)
vol_spike = st.sidebar.slider("AI Volatility Regime Multiplier", min_value=1.0, max_value=4.5, value=2.5, step=0.1)
liquidity_stress = st.sidebar.slider("Liquidity Dry-Up Haircut (%)", min_value=0.0, max_value=65.0, value=28.0, step=1.0)
risk_ceiling = st.sidebar.slider("Hard Risk Ceiling (% of Book)", min_value=5.0, max_value=25.0, value=12.5, step=0.5)

book_df = pd.DataFrame(
    [
        {"Instrument": "NIFTY_FUT", "Desk": "Quant Alpha", "Capital": 500000.0, "Weight": 0.38, "Base_Haircut": 10.0},
        {"Instrument": "BANKNIFTY_FUT", "Desk": "Quant Alpha", "Capital": 400000.0, "Weight": 0.32, "Base_Haircut": 15.0},
        {"Instrument": "USDINR_FUT", "Desk": "Macro FX", "Capital": 350000.0, "Weight": 0.18, "Base_Haircut": 8.0},
        {"Instrument": "GOLD_FUT", "Desk": "Commodities AI", "Capital": 250000.0, "Weight": 0.12, "Base_Haircut": 12.0},
    ]
)

total_book = book_df["Capital"].sum()
ai_regime_factor = (crash_pct / 100.0) * (1.0 + (vol_spike - 1.0) * 0.25)

book_df["Shock_PnL"] = book_df["Capital"] * ai_regime_factor * (0.75 + book_df["Weight"])
book_df["Impact_Pct"] = (book_df["Shock_PnL"] / total_book) * 100.0
book_df["Haircut_Pct"] = np.clip(book_df["Base_Haircut"] + liquidity_stress * 0.6, 0.0, 85.0)
book_df["Slippage_Loss"] = np.abs(book_df["Shock_PnL"]) * (book_df["Haircut_Pct"] / 100.0)
book_df["Net_Stress_Loss"] = book_df["Shock_PnL"] - book_df["Slippage_Loss"]


def ai_guardrail_signal(impact_pct: float, haircut: float, ceiling: float) -> str:
    mag = abs(impact_pct)
    if mag >= ceiling or haircut >= 45.0:
        return "🚨 AI HARD BREAKER"
    if mag >= ceiling * 0.65 or haircut >= 28.0:
        return "⚠️ TRIM EXPOSURE"
    return "✅ NORMAL REGIME"


book_df["AI_Signal"] = [
    ai_guardrail_signal(ip, hc, risk_ceiling)
    for ip, hc in zip(book_df["Impact_Pct"], book_df["Haircut_Pct"])
]

total_shock_pnl = book_df["Shock_PnL"].sum()
total_slippage = book_df["Slippage_Loss"].sum()
remaining_book = total_book + total_shock_pnl - total_slippage
net_change_pct = ((total_shock_pnl - total_slippage) / total_book) * 100.0

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Book Capital", f"₹{total_book:,.0f}")
m2.metric("Shock PnL", f"₹{total_shock_pnl:,.0f}", f"{(total_shock_pnl / total_book) * 100:.2f}%")
m3.metric("Liquidity Slippage", f"-₹{total_slippage:,.0f}", f"{liquidity_stress:.0f}% haircut")
m4.metric("Post-Stress Capital", f"₹{remaining_book:,.0f}", f"{net_change_pct:.2f}% net")

st.divider()

st.subheader("📈 AI Stress Trajectory Across Market Shocks (0% to -45%)")
shock_axis = np.linspace(-45, 0, 46)
sim_curve = pd.DataFrame(
    {
        "Shock_%": shock_axis,
        "Raw_Shock_Impact_%": shock_axis * (0.85 * (1.0 + (vol_spike - 1.0) * 0.2)),
        "AI_Liquidity_Adjusted_Impact_%": shock_axis
        * (0.85 * (1.0 + (vol_spike - 1.0) * 0.2))
        * (1.0 + (liquidity_stress / 100.0) * 0.45),
    }
).set_index("Shock_%")

st.line_chart(sim_curve, height=290)

st.subheader("🧠 Asset-Level AI Risk Matrix")
st.dataframe(
    book_df[
        [
            "Instrument",
            "Desk",
            "Capital",
            "Shock_PnL",
            "Haircut_Pct",
            "Slippage_Loss",
            "Net_Stress_Loss",
            "AI_Signal",
        ]
    ].style.format(
        {
            "Capital": "₹{:,.0f}",
            "Shock_PnL": "₹{:,.0f}",
            "Haircut_Pct": "{:.1f}%",
            "Slippage_Loss": "₹{:,.0f}",
            "Net_Stress_Loss": "₹{:,.0f}",
        }
    ),
    use_container_width=True,
)
