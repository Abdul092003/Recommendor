
import html
import random
import hashlib

import streamlit as st
from recommender import movies, recommend

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Recommendor | Discover Your Next Movie",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- DIFFERENT CINEMATIC IMAGES ----------------
# Har image ka apna unique ID hai.
# Internet connection zaroori hai.
IMAGE_IDS = [
    "photo-1489599849927-2ee91cede3ba",
    "photo-1440404653325-ab127d49abc1",
    "photo-1517604931442-7e0c8ed2963c",
    "photo-1478720568477-152d9b164e26",
    "photo-1500530855697-b586d89ba3ee",
    "photo-1518709268805-4e9042af9f23",
    "photo-1536440136628-849c177e76a1",
    "photo-1485846234645-a62644f84728",
    "photo-1500534623283-312aade485b7",
    "photo-1519608487953-e999c86e7455",
    "photo-1519681393784-d120267933ba",
    "photo-1470252649378-9c29740c9fa8",
    "photo-1500534314209-a25ddb2bd429",
    "photo-1518837695005-2083093ee35b",
    "photo-1464822759023-fed622ff2c3b",
    "photo-1511497584788-876760111969",
    "photo-1470770841072-f978cf4d019e",
    "photo-1501785888041-af3ef285b470",
    "photo-1519608487953-e999c86e7455",
    "photo-1500534623283-312aade485b7",
]

def get_random_image(key):
    """Movie title ke basis par different image choose karo."""
    digest = hashlib.md5(str(key).encode("utf-8")).hexdigest()
    index = int(digest, 16) % len(IMAGE_IDS)
    image_id = IMAGE_IDS[index]
    return (
        f"https://images.unsplash.com/{image_id}"
        "?auto=format&fit=crop&w=700&q=85"
    )

# ---------------- REUSABLE MOVIE CARD ----------------
def movie_card(title, rank=None):
    safe_title = html.escape(str(title))
    image_url = html.escape(get_random_image(title), quote=True)
    rank_html = (
        f'<div class="rank">#{rank:02d}</div>'
        if rank is not None else ""
    )

    st.markdown(
        f"""
        <div class="movie-card">
            <div class="poster">
                <img src="{image_url}" alt="{safe_title}">
                {rank_html}
                <div class="image-overlay">
                    <span>✦ RECOMMENDED</span>
                </div>
            </div>
            <div class="movie-info">
                <div class="movie-title">{safe_title}</div>
                <div class="movie-subtitle">YOUR NEXT WATCH 🍿</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- CUSTOM STYLING ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

    :root {
        --red: #e50914;
        --red-bright: #ff2633;
        --bg: #080808;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 85% 0%, #390b13 0%, transparent 35%),
            radial-gradient(ellipse at 0% 35%, #1d090c 0%, transparent 35%),
            #080808;
        color: white;
        font-family: 'DM Sans', sans-serif;
    }

    #MainMenu, footer, header[data-testid="stHeader"] {
        visibility: hidden;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    /* BRAND NAVIGATION */
    .nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0 22px;
        border-bottom: 1px solid #ffffff17;
        margin-bottom: 25px;
        animation: slideDown .7s ease both;
    }

    .brand {
        font-family: 'Outfit', sans-serif;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .brand span {
        color: var(--red);
        text-shadow: 0 0 22px #e5091466;
    }

    .brand-icon {
        display: inline-block;
        margin-right: 7px;
    }

    .nav-badge {
        color: #eee;
        font-size: 11px;
        letter-spacing: 1px;
        border: 1px solid #ffffff26;
        border-radius: 50px;
        padding: 9px 13px;
        background: #ffffff08;
    }

    /* CINEMATIC HERO */
    .hero {
        position: relative;
        overflow: hidden;
        padding: 55px 40px;
        min-height: 350px;
        border: 1px solid #ffffff20;
        border-radius: 24px;
        background:
            linear-gradient(90deg, #090909 0%, #090909ee 42%,
            #09090977 100%),
            url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1800&q=90')
            center/cover;
        box-shadow: 0 25px 80px #0008;
        animation: revealHero 1s ease both;
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 240px;
        height: 240px;
        right: 8%;
        top: 10%;
        border-radius: 50%;
        background: #e5091424;
        filter: blur(70px);
        animation: pulseGlow 4s ease-in-out infinite;
        pointer-events: none;
    }

    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 680px;
    }

    .hero-kicker {
        color: #ff5962;
        font-weight: 700;
        letter-spacing: 3px;
        font-size: 12px;
        margin-bottom: 17px;
    }

    .hero h1 {
        color: white;
        font-family: 'Outfit', sans-serif;
        font-size: clamp(43px, 6vw, 76px);
        font-weight: 800;
        letter-spacing: -2.5px;
        line-height: 1;
        margin: 0 0 20px;
    }

    .hero h1 span {
        color: var(--red-bright);
        text-shadow: 0 0 35px #e5091444;
    }

    .hero-description {
        color: #d2d2d2;
        font-size: 15px;
        line-height: 1.9;
        max-width: 530px;
    }

    .hero-label {
        display: inline-block;
        margin-top: 16px;
        color: #fff;
        background: #e5091426;
        border: 1px solid #e5091470;
        border-radius: 30px;
        padding: 10px 15px;
        font-size: 12px;
    }

    /* SECTION HEADINGS */
    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 28px;
        font-weight: 700;
        margin: 35px 0 5px;
    }

    .section-title span {
        color: var(--red-bright);
    }

    .section-description {
        color: #a9a9a9;
        font-size: 13px;
        margin-bottom: 22px;
    }

    /* SELECT BOX */
    div[data-baseweb="select"] > div {
        background: #171717 !important;
        border: 1px solid #393939 !important;
        border-radius: 12px !important;
        min-height: 48px;
    }

    div[data-baseweb="select"] * {
        color: white !important;
    }

    .stSelectbox label {
        color: #e7e7e7 !important;
        font-weight: 600 !important;
    }

    /* BUTTON */
    div.stButton > button {
        background: linear-gradient(135deg, #ff2633, #a8000a);
        color: white;
        border: 1px solid #ffffff20;
        border-radius: 12px;
        min-height: 48px;
        font-weight: 700;
        transition: all .25s ease;
        box-shadow: 0 7px 25px #e5091430;
    }

    div.stButton > button:hover {
        transform: translateY(-3px);
        color: white;
        border-color: #ff5962;
        box-shadow: 0 12px 30px #e5091466;
    }

    /* MOVIE CARDS */
    .movie-card {
        background: linear-gradient(160deg, #1c1c1c, #0e0e0e);
        border: 1px solid #ffffff13;
        border-radius: 15px;
        overflow: hidden;
        margin-bottom: 16px;
        transition: transform .3s ease, box-shadow .3s ease;
        animation: cardRise .65s ease both;
    }

    .movie-card:hover {
        transform: translateY(-9px);
        border-color: #e5091499;
        box-shadow: 0 15px 32px #e5091428;
    }

    .poster {
        position: relative;
        aspect-ratio: 2 / 3;
        overflow: hidden;
        background: #202020;
    }

    .poster img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: transform .55s ease, filter .4s ease;
    }

    .movie-card:hover .poster img {
        transform: scale(1.08);
        filter: brightness(.72);
    }

    .rank {
        position: absolute;
        top: 10px;
        left: 10px;
        color: white;
        background: #e50914ee;
        border-radius: 7px;
        padding: 6px 9px;
        font-size: 12px;
        font-weight: 800;
    }

    .image-overlay {
        position: absolute;
        inset: auto 0 0;
        padding: 20px 8px 12px;
        background: linear-gradient(transparent, #000d);
        color: #ff777e;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1px;
        opacity: 0;
        transform: translateY(8px);
        transition: all .3s ease;
    }

    .movie-card:hover .image-overlay {
        opacity: 1;
        transform: translateY(0);
    }

    .movie-info {
        padding: 13px 11px 15px;
        min-height: 83px;
    }

    .movie-title {
        font-size: 13px;
        color: white;
        font-weight: 700;
        line-height: 1.5;
        overflow-wrap: anywhere;
    }

    .movie-subtitle {
        color: #999;
        font-size: 9px;
        letter-spacing: 1px;
        margin-top: 8px;
    }

    /* SELECTED MOVIE PANEL */
    .selected-panel {
        background: linear-gradient(110deg, #201014, #131313);
        border: 1px solid #e509143b;
        border-radius: 16px;
        padding: 24px;
        min-height: 135px;
        margin-top: 10px;
    }

    .selected-label {
        color: #ff5962;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .selected-title {
        color: white;
        font-family: 'Outfit', sans-serif;
        font-size: 27px;
        font-weight: 700;
        margin-top: 8px;
    }

    .selected-caption {
        color: #aaa;
        font-size: 13px;
        margin-top: 8px;
    }

    .footer {
        margin-top: 50px;
        padding: 30px 0 10px;
        text-align: center;
        border-top: 1px solid #ffffff16;
        color: #777;
        font-size: 12px;
    }

    .footer-brand {
        font-family: 'Outfit', sans-serif;
        font-size: 22px;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
    }

    .footer-brand span {
        color: var(--red);
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes revealHero {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes cardRise {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulseGlow {
        0%, 100% { opacity: .45; transform: scale(.9); }
        50% { opacity: .9; transform: scale(1.12); }
    }

    @media (max-width: 650px) {
        .hero { padding: 32px 22px; min-height: 300px; }
        .hero h1 { letter-spacing: -1px; }
        .brand { font-size: 23px; }
        .nav-badge { font-size: 9px; }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: .01ms !important;
            transition-duration: .01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- NAVIGATION ----------------
st.markdown(
    """
    <div class="nav">
        <div class="brand">
            <span class="brand-icon">▶</span> REHMAN<span>FLIX</span>
        </div>
        <div class="nav-badge">✦ YOUR PERSONAL MOVIE UNIVERSE</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- HERO ----------------
movie_options = sorted(movies["title"].dropna().unique().tolist())

if not movie_options:
    st.error("Movies dataset mein nahi milin. CSV file check karo.")
    st.stop()

st.markdown(
    """
    <div class="hero">
        <div class="hero-content">
            <div class="hero-kicker">✦ WELCOME TO Recommendor</div>
            <h1>Your next<br>movie <span>obsession.</span></h1>
            <div class="hero-description">
                One movie can lead you to a thousand stories.
                Choose what you love and discover your next
                unforgettable watch.
            </div>
            <div class="hero-label">🍿 PERSONALIZED MOVIE DISCOVERY</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- SEARCH ----------------
st.markdown(
    """
    <div class="section-title">Discover <span>your next watch</span></div>
    <div class="section-description">
        Select a movie you enjoy. Recommendor will find similar titles
        using your recommendation model.
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([3, 1], vertical_alignment="bottom")

with left:
    default_index = (
        movie_options.index("Avatar") if "Avatar" in movie_options else 0
    )
    selected_movie = st.selectbox(
        "Search your favourite movie",
        movie_options,
        index=default_index,
    )

with right:
    find_movies = st.button(
        "✦ Discover Movies",
        type="primary",
        use_container_width=True,
    )

# ---------------- SELECTED MOVIE ----------------
if selected_movie:
    st.markdown(
        f"""
        <div class="selected-panel">
            <div class="selected-label">YOUR PICK TONIGHT</div>
            <div class="selected-title">
                {html.escape(selected_movie)}
            </div>
            <div class="selected-caption">
                Ready for a new adventure? Let's find your next favourite.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- RECOMMENDATIONS ----------------
if find_movies:
    with st.spinner("🍿 Searching your next movie obsession..."):
        results = recommend(selected_movie, limit=10)

    if not results:
        st.warning("Is movie ke liye recommendations nahi milin.")

    elif results[0].startswith("Movie dataset"):
        st.warning(results[0])

    else:
        st.markdown(
            f"""
            <div class="section-title">
                Because you love
                <span>{html.escape(selected_movie)}</span>
            </div>
            <div class="section-description">
                Ten discoveries selected just for your next movie night.
            </div>
            """,
            unsafe_allow_html=True,
        )

        for start in range(0, len(results), 5):
            batch = results[start:start + 5]
            columns = st.columns(5, gap="medium")

            for offset, title in enumerate(batch):
                rank = start + offset + 1
                with columns[offset]:
                    movie_card(title, rank)

        st.success(
            f"Found {len(results)} recommendations. "
            "Enjoy your movie night! 🍿"
        )

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class="footer">
        <div class="footer-brand">REHMAN<span>FLIX</span> 🎬</div>
        Your taste. Your next obsession.
        <br><br>
        Built with Python, Streamlit & Machine Learning
    </div>
    """,
    unsafe_allow_html=True,
)
