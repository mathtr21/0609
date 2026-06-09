import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="📈 글로벌 TOP 10 주식 대시보드",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global Top 10 Stocks (2026 기준) ─────────────────────────────────────────
TOP_10_STOCKS = {
    "NVDA":  {"name": "NVIDIA",            "icon": "🟢", "color": "#76B900", "sector": "AI / 반도체"},
    "AAPL":  {"name": "Apple",             "icon": "🍎", "color": "#A2AAAD", "sector": "소비자 가전"},
    "GOOGL": {"name": "Alphabet (Google)", "icon": "🔍", "color": "#4285F4", "sector": "인터넷 / AI"},
    "MSFT":  {"name": "Microsoft",         "icon": "🪟", "color": "#00A4EF", "sector": "클라우드 / SW"},
    "AMZN":  {"name": "Amazon",            "icon": "📦", "color": "#FF9900", "sector": "이커머스 / 클라우드"},
    "META":  {"name": "Meta Platforms",    "icon": "👥", "color": "#1877F2", "sector": "SNS / AI"},
    "TSM":   {"name": "TSMC",              "icon": "💎", "color": "#E50000", "sector": "반도체 파운드리"},
    "BRK-B": {"name": "Berkshire Hathaway","icon": "🏦", "color": "#B8860B", "sector": "지주회사 / 투자"},
    "TSLA":  {"name": "Tesla",             "icon": "⚡", "color": "#E31937", "sector": "전기차 / 로보틱스"},
    "AVGO":  {"name": "Broadcom",          "icon": "🔌", "color": "#CC092F", "sector": "반도체 / 통신"},
}

# ── CSS Styling ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Space+Grotesk:wght@400;600;700&display=swap');

* { font-family: 'Noto Sans KR', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1729 100%);
}
#MainMenu, footer, header { visibility: hidden; }

.hero-title {
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(90deg, #00f5a0, #00d9f5, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin: 1rem 0 0.3rem 0;
}
.hero-sub {
    text-align: center;
    color: rgba(255,255,255,0.6);
    font-size: 1rem;
    margin-bottom: 1.5rem;
}
.section-header {
    font-size: 1.2rem;
    font-weight: 700;
    color: rgba(255,255,255,0.95);
    margin: 1.5rem 0 1rem 0;
    padding-left: 0.8rem;
    border-left: 4px solid #00f5a0;
}
.metric-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
    transition: all 0.3s ease;
}
.metric-card:hover {
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.04) 100%);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.4);
}
.metric-ticker {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.5);
    font-weight: 600;
    letter-spacing: 0.05em;
}
.metric-name {
    font-size: 1.1rem;
    color: white;
    font-weight: 700;
    margin: 0.3rem 0 0.5rem 0;
}
.metric-price {
    font-size: 1.6rem;
    font-weight: 800;
    font-family: 'Space Grotesk', sans-serif;
    color: white;
}
.metric-change-up {
    color: #00f5a0;
    font-weight: 700;
    font-size: 0.95rem;
}
.metric-change-down {
    color: #ff4d6d;
    font-weight: 700;
    font-size: 0.95rem;
}
.metric-sector {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.45);
    margin-top: 0.4rem;
}
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,245,160,0.4), rgba(167,139,250,0.4), transparent);
    margin: 1.5rem 0;
}
.info-box {
    background: rgba(0,245,160,0.08);
    border: 1px solid rgba(0,245,160,0.3);
    border-radius: 14px;
    padding: 1rem 1.3rem;
    color: rgba(255,255,255,0.8);
    font-size: 0.88rem;
    line-height: 1.6;
    margin-top: 1rem;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1729 0%, #0a0e27 100%);
}
[data-testid="stSidebar"] * {
    color: rgba(255,255,255,0.9);
}
.footer {
    text-align: center;
    padding: 2rem 0 1rem 0;
    color: rgba(255,255,255,0.35);
    font-size: 0.82rem;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 대시보드 설정")
    st.markdown("---")

    selected_tickers = st.multiselect(
        "📌 종목 선택 (다중 가능)",
        options=list(TOP_10_STOCKS.keys()),
        default=list(TOP_10_STOCKS.keys()),
        format_func=lambda x: f"{TOP_10_STOCKS[x]['icon']} {x} - {TOP_10_STOCKS[x]['name']}",
    )

    st.markdown("---")
    period_option = st.selectbox(
        "📅 조회 기간",
        ["1개월", "3개월", "6개월", "1년", "2년", "5년"],
        index=3,
    )
    period_map = {"1개월": "1mo", "3개월": "3mo", "6개월": "6mo",
                  "1년": "1y", "2년": "2y", "5년": "5y"}
    period = period_map[period_option]

    st.markdown("---")
    chart_type = st.radio(
        "📊 차트 유형",
        ["📈 가격 (실제)", "🔄 정규화 (상대 비교)", "💰 누적 수익률 (%)"],
        index=1,
    )

    st.markdown("---")
    st.markdown("#### 📚 데이터 출처")
    st.caption("Yahoo Finance (yfinance)")
    st.caption(f"업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">📈 글로벌 TOP 10 주식 대시보드 💹</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">2026년 시가총액 기준 글로벌 TOP 10 기업의 주가 흐름을 실시간으로 분석합니다 🚀</div>',
    unsafe_allow_html=True,
)

if not selected_tickers:
    st.warning("⚠️ 왼쪽 사이드바에서 종목을 하나 이상 선택해주세요!")
    st.stop()

# ── Data Fetching ────────────────────────────────────────────────────────────
@st.cache_data(ttl=600, show_spinner=False)
def fetch_stock_data(tickers, period):
    """yfinance로 여러 종목의 주가 데이터를 한 번에 가져옵니다."""
    data = yf.download(
        tickers=tickers,
        period=period,
        interval="1d",
        group_by="ticker",
        auto_adjust=True,
        progress=False,
        threads=True,
    )
    return data

@st.cache_data(ttl=600, show_spinner=False)
def fetch_company_info(ticker):
    """개별 종목의 회사 정보를 가져옵니다."""
    try:
        info = yf.Ticker(ticker).info
        return {
            "market_cap": info.get("marketCap", 0),
            "pe_ratio": info.get("trailingPE", None),
            "dividend_yield": info.get("dividendYield", 0),
            "fifty_two_high": info.get("fiftyTwoWeekHigh", None),
            "fifty_two_low": info.get("fiftyTwoWeekLow", None),
        }
    except Exception:
        return {}

with st.spinner("📡 야후 파이낸스에서 데이터를 불러오는 중..."):
    raw_data = fetch_stock_data(selected_tickers, period)

# 단일 / 복수 종목 처리
if len(selected_tickers) == 1:
    ticker = selected_tickers[0]
    close_prices = pd.DataFrame({ticker: raw_data["Close"]})
    volumes = pd.DataFrame({ticker: raw_data["Volume"]})
else:
    close_prices = pd.DataFrame({t: raw_data[t]["Close"] for t in selected_tickers})
    volumes = pd.DataFrame({t: raw_data[t]["Volume"] for t in selected_tickers})

close_prices = close_prices.dropna(how="all")
volumes = volumes.dropna(how="all")

# ── Summary Metrics (카드) ───────────────────────────────────────────────────
st.markdown('<div class="section-header">💎 종목별 현재 시세</div>', unsafe_allow_html=True)

cols_per_row = 5
rows_needed = (len(selected_tickers) + cols_per_row - 1) // cols_per_row

for row in range(rows_needed):
    cols = st.columns(cols_per_row)
    for col_idx in range(cols_per_row):
        idx = row * cols_per_row + col_idx
        if idx >= len(selected_tickers):
            break
        ticker = selected_tickers[idx]
        meta = TOP_10_STOCKS[ticker]
        series = close_prices[ticker].dropna()
        if len(series) < 2:
            continue
        latest = series.iloc[-1]
        first = series.iloc[0]
        change_pct = (latest - first) / first * 100
        change_color_class = "metric-change-up" if change_pct >= 0 else "metric-change-down"
        arrow = "▲" if change_pct >= 0 else "▼"

        with cols[col_idx]:
            card = (
                f'<div class="metric-card" style="border-left: 4px solid {meta["color"]};">'
                f'<div class="metric-ticker">{meta["icon"]} {ticker}</div>'
                f'<div class="metric-name">{meta["name"]}</div>'
                f'<div class="metric-price">${latest:,.2f}</div>'
                f'<div class="{change_color_class}">{arrow} {change_pct:+.2f}%</div>'
                f'<div class="metric-sector">{meta["sector"]}</div>'
                f'</div>'
            )
            st.markdown(card, unsafe_allow_html=True)

# ── Main Chart ───────────────────────────────────────────────────────────────
st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-header">📊 주가 추이 ({period_option})</div>', unsafe_allow_html=True)

fig = go.Figure()

if chart_type == "📈 가격 (실제)":
    plot_df = close_prices
    y_title = "주가 (USD)"
    hover_fmt = "$%{y:,.2f}"
elif chart_type == "🔄 정규화 (상대 비교)":
    plot_df = close_prices.div(close_prices.iloc[0]).mul(100)
    y_title = "정규화 지수 (시작일 = 100)"
    hover_fmt = "%{y:.2f}"
else:  # 누적 수익률
    plot_df = close_prices.pct_change().fillna(0).add(1).cumprod().sub(1).mul(100)
    y_title = "누적 수익률 (%)"
    hover_fmt = "%{y:+.2f}%"

for ticker in selected_tickers:
    meta = TOP_10_STOCKS[ticker]
    fig.add_trace(
        go.Scatter(
            x=plot_df.index,
            y=plot_df[ticker],
            mode="lines",
            name=f"{meta['icon']} {ticker}",
            line=dict(color=meta["color"], width=2.2),
            hovertemplate=f"<b>{meta['name']}</b><br>%{{x|%Y-%m-%d}}<br>{hover_fmt}<extra></extra>",
        )
    )

fig.update_layout(
    template="plotly_dark",
    height=550,
    plot_bgcolor="rgba(15, 23, 41, 0.5)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Noto Sans KR", size=12, color="rgba(255,255,255,0.85)"),
    hovermode="x unified",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor="rgba(0,0,0,0)",
    ),
    xaxis=dict(
        title="날짜",
        gridcolor="rgba(255,255,255,0.08)",
        showspikes=True,
        spikemode="across",
        spikedash="dot",
        spikecolor="rgba(255,255,255,0.3)",
        spikethickness=1,
    ),
    yaxis=dict(
        title=y_title,
        gridcolor="rgba(255,255,255,0.08)",
    ),
    margin=dict(l=20, r=20, t=30, b=20),
)
st.plotly_chart(fig, use_container_width=True)

# ── 거래량 차트 ──────────────────────────────────────────────────────────────
st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">📊 일평균 거래량 비교</div>', unsafe_allow_html=True)

avg_volumes = volumes.mean().sort_values(ascending=True)
colors_bar = [TOP_10_STOCKS[t]["color"] for t in avg_volumes.index]

fig_vol = go.Figure(
    go.Bar(
        x=avg_volumes.values,
        y=[f"{TOP_10_STOCKS[t]['icon']} {t}" for t in avg_volumes.index],
        orientation="h",
        marker=dict(color=colors_bar, line=dict(color="rgba(255,255,255,0.15)", width=1)),
        text=[f"{v/1e6:,.1f}M" for v in avg_volumes.values],
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>일평균 거래량: %{x:,.0f}주<extra></extra>",
    )
)
fig_vol.update_layout(
    template="plotly_dark",
    height=max(300, 40 * len(selected_tickers) + 100),
    plot_bgcolor="rgba(15, 23, 41, 0.5)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Noto Sans KR", color="rgba(255,255,255,0.85)"),
    xaxis=dict(title="일평균 거래량 (주)", gridcolor="rgba(255,255,255,0.08)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.08)"),
    margin=dict(l=20, r=60, t=20, b=20),
)
st.plotly_chart(fig_vol, use_container_width=True)

# ── 통계 테이블 ──────────────────────────────────────────────────────────────
st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">📋 종목별 통계 요약</div>', unsafe_allow_html=True)

stats_rows = []
for ticker in selected_tickers:
    series = close_prices[ticker].dropna()
    if len(series) < 2:
        continue
    meta = TOP_10_STOCKS[ticker]
    returns = series.pct_change().dropna()
    stats_rows.append({
        "종목": f"{meta['icon']} {ticker}",
        "회사명": meta["name"],
        "시작가": f"${series.iloc[0]:,.2f}",
        "현재가": f"${series.iloc[-1]:,.2f}",
        "최고가": f"${series.max():,.2f}",
        "최저가": f"${series.min():,.2f}",
        "수익률": f"{(series.iloc[-1]/series.iloc[0]-1)*100:+.2f}%",
        "변동성(연환산)": f"{returns.std()*(252**0.5)*100:.2f}%",
    })

stats_df = pd.DataFrame(stats_rows)
st.dataframe(
    stats_df,
    use_container_width=True,
    hide_index=True,
)

# ── 상관관계 히트맵 ──────────────────────────────────────────────────────────
if len(selected_tickers) >= 2:
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🔥 종목 간 수익률 상관관계</div>', unsafe_allow_html=True)

    returns_df = close_prices.pct_change().dropna()
    corr = returns_df.corr()

    fig_corr = go.Figure(
        go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale=[
                [0.0, "#ff4d6d"],
                [0.5, "#1a1f3a"],
                [1.0, "#00f5a0"],
            ],
            zmin=-1, zmax=1,
            text=corr.round(2).values,
            texttemplate="%{text}",
            textfont=dict(size=11, color="white"),
            hovertemplate="%{x} ↔ %{y}<br>상관계수: %{z:.3f}<extra></extra>",
            colorbar=dict(title="상관계수"),
        )
    )
    fig_corr.update_layout(
        template="plotly_dark",
        height=max(400, 50 * len(selected_tickers) + 150),
        plot_bgcolor="rgba(15, 23, 41, 0.5)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Noto Sans KR", color="rgba(255,255,255,0.85)"),
        margin=dict(l=20, r=20, t=20, b=20),
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    st.markdown(
        '<div class="info-box">'
        '💡 <strong>상관관계 해석</strong><br>'
        '• <span style="color:#00f5a0;">+1에 가까움</span>: 두 종목이 함께 움직임 (동조 현상)<br>'
        '• <span style="color:#ff4d6d;">-1에 가까움</span>: 두 종목이 반대로 움직임 (헤지 효과)<br>'
        '• <strong>0에 가까움</strong>: 두 종목의 움직임이 독립적 (분산투자 효과)'
        '</div>',
        unsafe_allow_html=True,
    )

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">'
    '📈 Global TOP 10 Stock Dashboard &nbsp;|&nbsp; '
    '💹 Powered by Yahoo Finance &amp; Plotly &nbsp;|&nbsp; '
    '💜 Made with Streamlit'
    '</div>',
    unsafe_allow_html=True,
)
