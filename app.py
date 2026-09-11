import streamlit as st
import random
from pathlib import Path

# ============================================================
# RUHI ❤️ — Pilly Ally Michiel
# Streamlit Love App
# ============================================================

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="RUHI ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path(__file__).parent
PHOTO_DIR = BASE_DIR / "ruhi"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
    ========================= */

    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Manrope:wght@300;400;500;600;700&display=swap');

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 20% 10%,
                rgba(116, 20, 54, 0.28),
                transparent 30%
            ),
            radial-gradient(
                circle at 80% 80%,
                rgba(151, 45, 78, 0.18),
                transparent 30%
            ),
            #090609;
        color: #f8edf1;
        font-family: 'Manrope', sans-serif;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* =========================
       TEXT
    ========================= */

    .eyebrow {
        text-align: center;
        color: #d89aaa;
        font-size: 0.75rem;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(5rem, 15vw, 11rem);
        font-weight: 500;
        line-height: 0.75;
        text-align: center;
        letter-spacing: 0.04em;
        background: linear-gradient(
            135deg,
            #fff4f7,
            #e8a5b7,
            #fff4f7
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .hero-subtitle {
        text-align: center;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        color: #f4d7df;
        margin-top: 1.2rem;
    }

    .hero-description {
        max-width: 680px;
        margin: 1.5rem auto 0 auto;
        text-align: center;
        color: #cdbec3;
        line-height: 1.9;
        font-size: 1rem;
    }

    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.7rem, 7vw, 5rem);
        text-align: center;
        font-weight: 500;
        color: #f8e8ed;
        margin-bottom: 0.5rem;
    }

    .section-subtitle {
        text-align: center;
        color: #a9989e;
        margin-bottom: 3rem;
    }

    /* =========================
       CARDS
    ========================= */

    .love-card {
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.055),
                rgba(255,255,255,0.018)
            );
        border: 1px solid rgba(255, 185, 205, 0.12);
        border-radius: 24px;
        padding: 2rem;
        height: 100%;
        box-shadow: 0 20px 60px rgba(0,0,0,0.25);
        transition: 0.3s ease;
    }

    .love-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255, 185, 205, 0.3);
        box-shadow: 0 25px 70px rgba(0,0,0,0.4);
    }

    .love-card h3 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        color: #f1b4c5;
        margin-top: 0;
    }

    .love-card p {
        color: #c8bbc0;
        line-height: 1.8;
    }

    /* =========================
       PHOTO
    ========================= */

    .photo-caption {
        text-align: center;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        color: #e8b3c1;
        margin-top: 0.7rem;
    }

    .photo-number {
        text-align: center;
        color: #776a70;
        font-size: 0.7rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
    }

    /* =========================
       QUOTE
    ========================= */

    .quote-box {
        padding: 3rem 2rem;
        border-top: 1px solid rgba(255,255,255,0.08);
        border-bottom: 1px solid rgba(255,255,255,0.08);
        text-align: center;
        margin: 3rem 0;
    }

    .quote {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2rem, 5vw, 3.8rem);
        font-style: italic;
        line-height: 1.25;
        color: #f0d8df;
    }

    .quote-author {
        margin-top: 1rem;
        color: #967f87;
        font-size: 0.8rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
    }

    /* =========================
       LETTER
    ========================= */

    .letter {
        max-width: 800px;
        margin: auto;
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 25px;
        padding: clamp(2rem, 6vw, 5rem);
        box-shadow: 0 30px 100px rgba(0,0,0,0.3);
    }

    .letter p {
        color: #d0c1c6;
        line-height: 2;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.35rem;
    }

    .letter-signature {
        text-align: right;
        margin-top: 3rem;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        color: #e6a7b8;
    }

    /* =========================
       FINAL
    ========================= */

    .final-box {
        text-align: center;
        padding: 5rem 1rem;
    }

    .final-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(3rem, 8vw, 6rem);
        color: #f4d9e1;
        line-height: 1;
    }

    .final-text {
        max-width: 650px;
        margin: 2rem auto;
        color: #ad9ca2;
        line-height: 1.9;
    }

    .footer {
        text-align: center;
        margin-top: 7rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.07);
        color: #675c61;
        font-size: 0.75rem;
        letter-spacing: 0.12em;
    }

    .heart {
        color: #e96b8c;
    }

    /* =========================
       BUTTONS
    ========================= */

    div.stButton > button {
        border-radius: 999px;
        border: 1px solid rgba(255, 170, 195, 0.35);
        background: rgba(255,255,255,0.04);
        color: #f3dfe5;
        padding: 0.7rem 1.5rem;
        transition: 0.25s ease;
    }

    div.stButton > button:hover {
        border-color: #e99ab0;
        background: rgba(205, 75, 112, 0.18);
        color: white;
    }

    /* =========================
       MOBILE
    ========================= */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            font-size: 5rem;
        }

        .hero-subtitle {
            font-size: 1.5rem;
        }

        .hero-description {
            font-size: 0.9rem;
        }

        .love-card {
            padding: 1.5rem;
        }

        .letter p {
            font-size: 1.15rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "opened" not in st.session_state:
    st.session_state.opened = False

if "rizz" not in st.session_state:
    st.session_state.rizz = "Click the button and let me cook... 😏"

if "missed" not in st.session_state:
    st.session_state.missed = False

if "secret" not in st.session_state:
    st.session_state.secret = False


# ============================================================
# INTRO
# ============================================================

if not st.session_state.opened:

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="eyebrow">A little something for you</div>

        <div class="hero-title">
            RUHI
        </div>

        <div class="hero-subtitle">
            For my favorite person ❤️
        </div>

        <p class="hero-description">
            Some things are difficult to say out loud...
            so I made you a little place where I could put them.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button(
            "Open my heart ❤️",
            use_container_width=True,
        ):
            st.session_state.opened = True
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="photo-number">
            made with love • just for you
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.stop()


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="eyebrow">
        For Pilly Ally Michiel
    </div>

    <div class="hero-title">
        RUHI
    </div>

    <div class="hero-subtitle">
        For my favorite person ❤️
    </div>

    <p class="hero-description">
        Pilly Ally Michiel — there are people you meet,
        people you remember, and then there are people
        who quietly become part of your heart.
        You became the third one.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)


# ============================================================
# HERO PHOTO — P1
# ============================================================

hero_photo = PHOTO_DIR / "p1.jpg"

if hero_photo.exists():
    st.image(
        str(hero_photo),
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="photo-caption">
            The face I could look at a thousand times ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning("p1.jpg was not found inside the ruhi folder.")


st.markdown("<br><br>", unsafe_allow_html=True)


# ============================================================
# PHOTO STORY
# ============================================================

st.markdown(
    """
    <div class="eyebrow">Our little story</div>
    <div class="section-title">Moments I Keep</div>

    <div class="section-subtitle">
        Every picture has a little piece of you in it.
    </div>
    """,
    unsafe_allow_html=True,
)


story = [
    (
        "p2.jpg",
        "The kind of smile that stays with me.",
    ),
    (
        "p3.jpg",
        "A moment I would happily replay.",
    ),
    (
        "p4.jpg",
        "You being you — and somehow that's enough.",
    ),
    (
        "p5.jpg",
        "One of those moments that feels special.",
    ),
    (
        "p6.jpg",
        "A memory worth keeping forever.",
    ),
    (
        "p7.jpg",
        "And somehow, you keep getting more beautiful.",
    ),
]


for index in range(0, len(story), 2):

    columns = st.columns(2)

    for column, item in zip(columns, story[index:index + 2]):

        filename, caption = item
        image_path = PHOTO_DIR / filename

        with column:

            if image_path.exists():

                st.image(
                    str(image_path),
                    use_container_width=True,
                )

                st.markdown(
                    f"""
                    <div class="photo-number">
                        {filename.replace(".jpg", "").upper()}
                    </div>

                    <div class="photo-caption">
                        {caption}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:
                st.warning(f"{filename} was not found.")


st.markdown("<br><br>", unsafe_allow_html=True)


# ============================================================
# WHY I LOVE YOU
# ============================================================

st.markdown(
    """
    <div class="eyebrow">Things I notice</div>

    <div class="section-title">
        Why I Love You
    </div>

    <div class="section-subtitle">
        Not just because you're beautiful.
        It's deeper than that.
    </div>
    """,
    unsafe_allow_html=True,
)


why_cards = [
    (
        "01",
        "Your Presence",
        "You have this way of making ordinary moments feel different. "
        "Even when nothing special is happening, having you around makes it special."
    ),
    (
        "02",
        "Your Heart",
        "There is something about the way you carry yourself, "
        "the way you care, and the little things you do that stay in my mind."
    ),
    (
        "03",
        "Your Smile",
        "Honestly... your smile should come with a warning. "
        "One look and my whole mood changes."
    ),
    (
        "04",
        "Your Energy",
        "There is an energy about you that feels familiar, warm, "
        "and somehow peaceful at the same time."
    ),
    (
        "05",
        "Your Beauty",
        "Not only the kind people see in a picture. "
        "I'm talking about the kind that becomes more beautiful when you know the person."
    ),
    (
        "06",
        "Just You",
        "Maybe the simplest answer is the best one: "
        "I love you because you're you."
    ),
]


for index in range(0, len(why_cards), 3):

    columns = st.columns(3)

    for column, card in zip(
        columns,
        why_cards[index:index + 3]
    ):

        number, title, text = card

        with column:

            st.markdown(
                f"""
                <div class="love-card">

                    <div class="photo-number">
                        {number}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {text}
                    </p>

                </div>
                """,
                unsafe_allow_html=True,
            )


st.markdown("<br><br>", unsafe_allow_html=True)


# ============================================================
# OUR ENERGY
# ============================================================

st.markdown(
    """
    <div class="eyebrow">Us</div>

    <div class="section-title">
        Our Energy
    </div>
    """,
    unsafe_allow_html=True,
)


quotes = [
    "Some connections don't need explanations.",
    "You feel like a favorite song I never get tired of.",
    "If comfort had a person, I'd probably call it you.",
    "Some people enter your life quietly and become everything.",
]


for quote in quotes:

    st.markdown(
        f"""
        <div class="quote-box">

            <div class="quote">
                “{quote}”
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RIZZ DEPARTMENT
# ============================================================

st.markdown(
    """
    <div class="eyebrow">Warning: excessive sweetness</div>

    <div class="section-title">
        Rizz Department 😏
    </div>

    <div class="section-subtitle">
        Officially certified compliments for Ruhi.
    </div>
    """,
    unsafe_allow_html=True,
)


rizz_lines = [
    "Are you Wi-Fi? Because I feel a connection every time you're around. ❤️",
    "I was going to write something smooth... then I remembered you're already the smooth one. 😭❤️",
    "You're actually unfair. How am I supposed to concentrate when you look like that?",
    "If beautiful was a crime, you'd definitely need a lawyer.",
    "I don't need Google Maps. Somehow my heart keeps finding its way back to you.",
    "You're my favorite notification. Every single time.",
    "I could explain why I like you... but we'd probably be here all night.",
]


if st.button(
    "Generate some rizz 😏",
    use_container_width=True,
):

    st.session_state.rizz = random.choice(rizz_lines)


st.markdown(
    f"""
    <div class="quote-box">

        <div class="quote">
            {st.session_state.rizz}
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MISS YOU
# ============================================================

st.markdown(
    """
    <div class="section-title">
        One Little Question
    </div>

    <div class="section-subtitle">
        Be honest...
    </div>
    """,
    unsafe_allow_html=True,
)


col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button(
        "Do you know how much I miss you? 🥺",
        use_container_width=True,
    ):

        st.session_state.missed = True


if st.session_state.missed:

    st.markdown(
        """
        <div class="quote-box">

            <div class="quote">
                More than I probably know how to explain. ❤️
            </div>

            <div class="quote-author">
                — Your favorite person
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SECRET
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button(
        "There might be a secret here 👀",
        use_container_width=True,
    ):

        st.session_state.secret = not st.session_state.secret


if st.session_state.secret:

    st.success(
        "SECRET UNLOCKED ❤️ — If you are reading this, "
        "just know that somebody out there is smiling because of you."
    )


# ============================================================
# LOVE LETTER
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="eyebrow">
        From my heart
    </div>

    <div class="section-title">
        A Little Letter
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="letter">

        <p>
            Dear Ruhi,
        </p>

        <p>
            I don't know if words can ever completely explain
            what someone means to you. Sometimes you just know.
            You feel it in the quiet moments, in the random smiles,
            in the way one person's name can instantly change your mood.
        </p>

        <p>
            That's what you became for me.
        </p>

        <p>
            I appreciate your presence, your smile, your heart,
            your personality, and all those little things that make
            you exactly who you are.
        </p>

        <p>
            I don't want something that is only beautiful for a moment.
            I want something genuine. Something peaceful.
            Something built with patience, respect, honesty,
            and eventually, inshaAllah, something that can make us
            both proud.
        </p>

        <p>
            Until then, I will keep appreciating you,
            making du'a for good things,
            and being grateful that I got to know someone like you.
        </p>

        <p>
            You are special to me.
            More than this little website could ever explain.
        </p>

        <div class="letter-signature">
            — Hans ❤️
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FINAL PHOTO — P8
# ============================================================

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="eyebrow">
        One last thing
    </div>

    <div class="section-title">
        Before You Go...
    </div>
    """,
    unsafe_allow_html=True,
)


final_photo = PHOTO_DIR / "p8.jpg"

if final_photo.exists():

    st.image(
        str(final_photo),
        use_container_width=True,
    )

else:

    st.warning(
        "p8.jpg was not found inside the ruhi folder."
    )


st.markdown(
    """
    <div class="final-box">

        <div class="final-title">
            You are loved.
        </div>

        <p class="final-text">
            Not because you're perfect.
            Not because everything is always easy.
            But because you are you.
            And somehow, that's more than enough.
        </p>

        <div class="quote">
            “May Allah protect what is good between us
            and guide us toward what is best.”
        </div>

        <br>

        <div class="heart">
            ❤️ ❤️ ❤️
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        MADE WITH ❤️ FOR RUHI
        <br><br>
        Designed by hans_boe
    </div>
    """,
    unsafe_allow_html=True,
)
