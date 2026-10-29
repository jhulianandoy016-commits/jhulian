from pathlib import Path
from flask import Flask, render_template_string

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    static_url_path="/static"
)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jhulian Claire B. Andoy | Portfolio</title>

    <style>
        :root {
            --bg: #080d19;
            --panel: #111a2b;
            --mint: #9bf5d0;
            --blue: #8bbcff;
            --purple: #c3a5ff;
            --white: #f4f7ff;
            --muted: #a8b4c9;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        /* SIMPLE GRAPHIC BACKGROUND */
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: var(--bg);
            background-image:
                radial-gradient(circle at 15% 20%, #9bf5d010 0, transparent 25%),
                radial-gradient(circle at 85% 40%, #8bbcff12 0, transparent 30%),
                radial-gradient(circle at 50% 85%, #c3a5ff0c 0, transparent 30%),
                linear-gradient(#8bbcff0a 1px, transparent 1px),
                linear-gradient(90deg, #8bbcff0a 1px, transparent 1px),
                linear-gradient(135deg, #080d19, #0b1220, #080d19);
            background-size:
                auto,
                auto,
                auto,
                45px 45px,
                45px 45px,
                auto;
            background-attachment: fixed;
            color: var(--white);
            line-height: 1.7;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        button {
            font: inherit;
            cursor: pointer;
        }

        /* WELCOME SCREEN */
        .welcome {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            text-align: center;
            background:
                radial-gradient(circle at 10% 10%, #153b42, transparent 45%),
                radial-gradient(circle at 90% 90%, #2c204d, transparent 45%),
                var(--bg);
        }

        .welcome-card {
            width: 100%;
            max-width: 650px;
            padding: 40px 25px;
            border: 1px solid #344052;
            border-radius: 28px;
            background: rgba(17, 26, 43, .85);
            box-shadow: 0 20px 60px #0006;
        }

        .welcome-photo {
            width: 175px;
            height: 175px;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
            border: 4px solid var(--mint);
            margin-bottom: 22px;
            box-shadow: 0 0 30px #9bf5d044;
        }

        .eyebrow {
            color: var(--mint);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        h1 {
            font-size: clamp(30px, 6vw, 48px);
            line-height: 1.2;
            margin-bottom: 18px;
        }

        .gradient-text {
            background: linear-gradient(
                90deg, var(--mint), var(--blue), var(--purple)
            );
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .welcome-description {
            color: var(--muted);
            margin-bottom: 25px;
        }

        .primary-button {
            display: inline-block;
            padding: 12px 23px;
            border: none;
            border-radius: 30px;
            background: var(--mint);
            color: #07130f;
            font-weight: bold;
            transition: .25s;
        }

        .primary-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px #9bf5d044;
        }

        .dashboard {
            display: none;
        }

        /* NAVIGATION */
        .topbar {
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
            padding: 15px 7%;
            background: #080d19ee;
            backdrop-filter: blur(15px);
            border-bottom: 1px solid #ffffff20;
        }

        .brand {
            font-size: 21px;
            font-weight: bold;
            color: var(--mint);
        }

        .back-button {
            padding: 8px 14px;
            border: 1px solid var(--mint);
            border-radius: 25px;
            background: transparent;
            color: var(--mint);
        }

        /* HERO SECTION */
        .hero {
            min-height: 70vh;
            display: flex;
            align-items: center;
            padding: 80px 9%;
            background:
                radial-gradient(circle at 90% 20%, #334b7333, transparent 40%),
                radial-gradient(circle at 10% 90%, #145c4c33, transparent 40%);
        }

        .hero-content {
            max-width: 850px;
        }

        .status-label {
            display: inline-block;
            padding: 7px 13px;
            margin-bottom: 22px;
            border: 1px solid #9bf5d044;
            border-radius: 25px;
            color: var(--mint);
            font-size: 12px;
            letter-spacing: 1px;
        }

        .hero h2 {
            font-size: clamp(36px, 7vw, 70px);
            line-height: 1.15;
            margin-bottom: 22px;
        }

        .hero p {
            max-width: 650px;
            color: var(--muted);
            margin-bottom: 25px;
        }

        /* GENERAL SECTIONS */
        .section {
            padding: 75px 9%;
            scroll-margin-top: 70px;
        }

        .section:nth-child(even) {
            background: #ffffff05;
        }

        .section-heading {
            margin-bottom: 30px;
        }

        .section-number {
            color: var(--mint);
            font-size: 12px;
            letter-spacing: 3px;
            font-weight: bold;
        }

        .section-title {
            font-size: clamp(28px, 4vw, 40px);
            margin: 8px 0;
        }

        .section-description {
            color: var(--muted);
            max-width: 700px;
        }

        .heading-line {
            width: 75px;
            height: 4px;
            margin-top: 15px;
            border-radius: 5px;
            background: linear-gradient(90deg, var(--mint), var(--purple));
        }

        /* CARDS */
        .card {
            min-width: 0;
            padding: 25px;
            border: 1px solid #ffffff20;
            border-radius: 20px;
            background: linear-gradient(145deg, #162236, #0c1321);
            transition: .25s;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: #9bf5d077;
        }

        .card h3 {
            color: var(--mint);
            font-size: 20px;
            margin-bottom: 10px;
        }

        .card p {
            color: var(--muted);
            overflow-wrap: anywhere;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 20px;
        }

        /* PERSONAL INFORMATION */
        .personal-layout {
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            gap: 22px;
        }

        .profile-side {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .profile-symbol {
            font-size: 45px;
            color: var(--mint);
            margin-bottom: 15px;
        }

        .info-list {
            display: grid;
            gap: 12px;
        }

        .info-item {
            padding: 14px 17px;
            border-radius: 12px;
            background: #ffffff08;
            border: 1px solid #ffffff12;
            overflow-wrap: anywhere;
        }

        .info-item strong {
            display: block;
            color: var(--mint);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* EDUCATION */
        .education-timeline {
            display: grid;
            gap: 20px;
        }

        .education-year {
            display: inline-block;
            color: var(--mint);
            font-size: 12px;
            margin-bottom: 10px;
        }

        /* SKILLS */
        .skill-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 17px;
        }

        .skill-card {
            padding: 22px 15px;
            border: 1px solid #ffffff20;
            border-radius: 18px;
            background: var(--panel);
            text-align: center;
            transition: .25s;
        }

        .skill-card:hover {
            transform: translateY(-4px);
            border-color: var(--mint);
        }

        .skill-icon {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .skill-card h3 {
            font-size: 15px;
        }

        .skill-card p {
            color: var(--muted);
            font-size: 12px;
            margin-top: 5px;
        }

        /* PROJECT TAGS */
        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 18px 0 22px;
        }

        .project-tags span {
            padding: 5px 10px;
            border: 1px solid #9bf5d044;
            border-radius: 20px;
            color: var(--mint);
            font-size: 12px;
        }

        /* CERTIFICATES */
        .certificate-gallery {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 22px;
        }

        .certificate-frame {
            padding: 10px;
            border: 1px solid #ffffff20;
            border-radius: 16px;
            background: var(--panel);
        }

        .certificate-gallery img {
            display: block;
            width: 100%;
            height: auto;
            object-fit: contain;
            border-radius: 10px;
        }

        /* SOCIAL MEDIA */
        .social-links {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 15px;
        }

        .social-links a {
            padding: 18px 12px;
            border: 1px solid #ffffff20;
            border-radius: 15px;
            background: var(--panel);
            text-align: center;
            transition: .25s;
        }

        .social-links a:hover {
            color: var(--mint);
            border-color: var(--mint);
            transform: translateY(-4px);
        }

        /* CLOSING MESSAGE */
        .closing-card {
            margin-top: 35px;
            padding: 30px 20px;
            border: 1px solid #9bf5d044;
            border-radius: 20px;
            text-align: center;
            background: #111a2b;
        }

        .closing-card h3 {
            font-size: 25px;
            margin-bottom: 8px;
        }

        .closing-card p {
            color: var(--muted);
        }

        /* FOOTER */
        footer {
            padding: 25px;
            border-top: 1px solid #ffffff20;
            text-align: center;
            color: var(--muted);
            font-size: 13px;
        }

        footer span {
            color: var(--mint);
            font-weight: bold;
        }

        /* BACK TO TOP */
        .back-to-top {
            position: fixed;
            display: none;
            right: 20px;
            bottom: 20px;
            width: 45px;
            height: 45px;
            border: 1px solid var(--mint);
            border-radius: 50%;
            background: var(--panel);
            color: var(--mint);
            font-size: 22px;
            z-index: 90;
        }

        /* TABLET */
        @media (max-width: 800px) {
            .personal-layout {
                grid-template-columns: 1fr;
            }

            .skill-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .hero {
                padding: 65px 7%;
            }

            .section {
                padding: 60px 7%;
            }
        }

        /* MOBILE */
        @media (max-width: 550px) {
            .topbar {
                padding: 12px 5%;
            }

            .brand {
                font-size: 17px;
            }

            .back-button {
                font-size: 12px;
            }

            .card-grid,
            .certificate-gallery,
            .social-links {
                grid-template-columns: 1fr;
            }

            .skill-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 10px;
            }

            .welcome-photo {
                width: 145px;
                height: 145px;
            }
        }
    </style>
</head>

<body>

    <!-- WELCOME SCREEN -->
    <section class="welcome" id="welcome">
        <div class="welcome-card">

            <img
                class="welcome-photo"
                src="{{ url_for('static', filename='images/andoy.png') }}"
                alt="Portfolio profile photo"
            >

            <p class="eyebrow">Personal Portfolio</p>

            <h1>
                Welcome to
                <span class="gradient-text">My World</span>
            </h1>

            <p class="welcome-description">
                Discover my personal information, education, skills,
                projects, certificates, and more.
            </p>

            <button class="primary-button" id="enterButton">
                Explore My Portfolio →
            </button>

        </div>
    </section>

    <!-- MAIN PORTFOLIO -->
    <div class="dashboard" id="dashboard">

        <header class="topbar">
            <div class="brand">JCA.</div>

            <button class="back-button" id="backButton">
                ← Back to Welcome
            </button>
        </header>

        <!-- HERO -->
        <section class="hero">
            <div class="hero-content">

                <div class="status-label">
                    MY PERSONAL PORTFOLIO
                </div>

                <h2>
                    Hello, I'm
                    <span class="gradient-text">
                        Jhulian Claire B. Andoy
                    </span>
                </h2>

                <p>
                    Welcome to my personal portfolio. This website presents
                    my background, educational journey, skills, projects,
                    certificates, and social media links.
                </p>

                <a class="primary-button" href="#personal">
                    Get to Know Me ↓
                </a>

            </div>
        </section>

        <!-- PERSONAL INFORMATION -->
        <section class="section" id="personal">

            <div class="section-heading">
                <span class="section-number">01 / ABOUT ME</span>
                <h2 class="section-title">Personal Information</h2>
                <p class="section-description">
                    A brief introduction to who I am.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="personal-layout">

                <article class="card profile-side">
                    <div class="profile-symbol">✦</div>
                    <h3>Jhulian Claire B. Andoy</h3>
                    <p>Student • Learner • Future Professional</p>
                </article>

                <div class="info-list">

                    <div class="info-item">
                        <strong>Full Name</strong>
                        Jhulian Claire B. Andoy
                    </div>

                    <div class="info-item">
                        <strong>Age</strong>
                        19 years old
                    </div>

                    <div class="info-item">
                        <strong>About Me</strong>
                        I am a student who continues to learn, improve
                        my abilities, and work toward my personal and
                        academic goals.
                    </div>

                    <div class="info-item">
                        <strong>Interests</strong>
                        Technology, creativity, learning new skills,
                        and personal development.
                    </div>

                    <div class="info-item">
                        <strong>Goal</strong>
                        To gain knowledge and experience that will help
                        me build a successful future.
                    </div>

                </div>
            </div>
        </section>

        <!-- EDUCATIONAL BACKGROUND -->
        <section class="section" id="education">

            <div class="section-heading">
                <span class="section-number">02 / MY JOURNEY</span>
                <h2 class="section-title">Educational Background</h2>
                <p class="section-description">
                    My educational journey and the experiences that
                    helped me grow.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="education-timeline">

                <article class="card">
                    <span class="education-year">2013 – 2019</span>
                    <h3>Dangcagan Central Elementary School</h3>
                    <p>
                        Completed my elementary education and developed
                        my foundational knowledge, values, and learning skills.
                    </p>
                </article>

                <article class="card">
                    <span class="education-year">2019 – 2025</span>
                    <h3>Dangcagan National High School</h3>
                    <p>
                        Completed my secondary education and strengthened
                        my academic knowledge and personal skills.
                    </p>
                </article>

                <article class="card">
                    <span class="education-year">2025 – 2029</span>
                    <h3>Bachelor of Science in Information Technology (BSIT)</h3>
                    <p>
                        TCC
                        <br>
                        Developing my knowledge of programming, computer systems,
                        and information technology.
                    </p>
                </article>

            </div>
        </section>

        <!-- SKILLS -->
        <section class="section" id="skills">

            <div class="section-heading">
                <span class="section-number">03 / WHAT I CAN DO</span>
                <h2 class="section-title">My Skills</h2>
                <p class="section-description">
                    Skills and abilities I continue to develop through
                    learning and practice.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="skill-grid">

                <article class="skill-card">
                    <div class="skill-icon">💻</div>
                    <h3>Computer Literacy</h3>
                    <p>Using digital tools</p>
                </article>

                <article class="skill-card">
                    <div class="skill-icon">🌐</div>
                    <h3>Internet Research</h3>
                    <p>Finding information</p>
                </article>

                <article class="skill-card">
                    <div class="skill-icon">🎨</div>
                    <h3>Creativity</h3>
                    <p>Creating new ideas</p>
                </article>

                <article class="skill-card">
                    <div class="skill-icon">🤝</div>
                    <h3>Teamwork</h3>
                    <p>Working with others</p>
                </article>

                <article class="skill-card">
                    <div class="skill-icon">🗣️</div>
                    <h3>Communication</h3>
                    <p>Sharing ideas clearly</p>
                </article>

                <article class="skill-card">
                    <div class="skill-icon">📚</div>
                    <h3>Willingness to Learn</h3>
                    <p>Improving every day</p>
                </article>

            </div>
        </section>

        <!-- PROJECTS -->
        <section class="section" id="projects">

            <div class="section-heading">
                <span class="section-number">04 / MY WORK</span>
                <h2 class="section-title">My Projects</h2>
                <p class="section-description">
                    Projects I have developed to apply my knowledge
                    and improve my technical skills.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="card-grid">

                <article class="card">
                    <div class="profile-symbol">💰</div>

                    <h3>Allowance Tracker System</h3>

                    <p>
                        A web-based project designed to help users manage
                        and track their allowance and budget.
                    </p>

                    <div class="project-tags">
                        <span>Web Application</span>
                        <span>Allowance Tracking</span>
                        <span>Budget Management</span>
                    </div>

                    <a
                        class="primary-button"
                        href="https://allowancetrackingsystem.netlify.app/"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View Project ↗
                    </a>
                </article>

            </div>
        </section>

        <!-- CERTIFICATES AND IMAGES -->
        <section class="section" id="certificates">

            <div class="section-heading">
                <span class="section-number">05 / MY ACHIEVEMENTS</span>
                <h2 class="section-title">Certificates and Images</h2>
                <p class="section-description">
                    Images and accomplishments from my learning journey.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="certificate-gallery">

                <div class="certificate-frame">
                    <img
                        src="{{ url_for('static', filename='images/jhulian.png') }}"
                        alt="Certificate image"
                        loading="lazy"
                    >
                </div>

                <div class="certificate-frame">
                    <img
                        src="{{ url_for('static', filename='images/claire.png') }}"
                        alt="Certificate image"
                        loading="lazy"
                    >
                </div>

            </div>
        </section>

        <!-- CONTACT -->
        <section class="section" id="contact">

            <div class="section-heading">
                <span class="section-number">06 / GET IN TOUCH</span>
                <h2 class="section-title">Contact Me</h2>
                <p class="section-description">
                    Feel free to contact me through my phone number
                    or email address.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="card-grid">

                <article class="card">
                    <div class="profile-symbol">📱</div>
                    <h3>Phone Number</h3>
                    <p>09129094350</p>
                    <br>
                    <a class="primary-button" href="tel:09129094350">
                        Call Me
                    </a>
                </article>

                <article class="card">
                    <div class="profile-symbol">✉️</div>
                    <h3>Email Address</h3>
                    <p>jhulianandoy016@gmail.com</p>
                    <br>
                    <a
                        class="primary-button"
                        href="mailto:jhulianandoy016@gmail.com"
                    >
                        Send an Email
                    </a>
                </article>

            </div>

        </section>

        <!-- SOCIAL MEDIA -->
        <section class="section" id="social">

            <div class="section-heading">
                <span class="section-number">07 / LET'S CONNECT</span>
                <h2 class="section-title">Social Media</h2>
                <p class="section-description">
                    Connect with me through my social media platforms.
                    Replace these links with your personal profile URLs.
                </p>
                <div class="heading-line"></div>
            </div>

            <div class="social-links">

                <a
                    href="https://www.facebook.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    📘 Facebook
                </a>

                <a
                    href="https://www.instagram.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    📸 Instagram
                </a>

                <a
                    href="https://www.tiktok.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    🎵 TikTok
                </a>

            </div>

            <div class="closing-card">
                <h3>Thank You for Visiting!</h3>
                <p>
                    Thank you for taking the time to explore my personal
                    portfolio. I look forward to learning, growing,
                    and achieving more.
                </p>
            </div>

        </section>

        <footer>
            Created by <span>Jhulian Claire B. Andoy</span>
            <p>© <span id="currentYear"></span> My Personal Portfolio</p>
        </footer>

    </div>

    <button
        class="back-to-top"
        id="backToTop"
        aria-label="Back to top"
    >↑</button>

    <script>
        const welcome = document.getElementById("welcome");
        const dashboard = document.getElementById("dashboard");
        const enterButton = document.getElementById("enterButton");
        const backButton = document.getElementById("backButton");
        const backToTop = document.getElementById("backToTop");

        enterButton.addEventListener("click", function () {
            welcome.style.display = "none";
            dashboard.style.display = "block";
            window.scrollTo({ top: 0, behavior: "smooth" });
        });

        backButton.addEventListener("click", function () {
            dashboard.style.display = "none";
            welcome.style.display = "flex";
            backToTop.style.display = "none";
            window.scrollTo({ top: 0, behavior: "smooth" });
        });

        window.addEventListener("scroll", function () {
            backToTop.style.display =
                window.scrollY > 400 ? "block" : "none";
        });

        backToTop.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });

        document.getElementById("currentYear").textContent =
            new Date().getFullYear();
    </script>

</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5003,
        debug=True
    )