import streamlit as st
import google.generativeai as genai
import webbrowser as wb
import time
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript

st.set_page_config(page_title="Portfolio", layout="centered")
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


css("assets/style.css")

with st.sidebar:
    navigation = option_menu(
        menu_title=None,
        options=["Home", "Chat Assistant", "Skills", "Projects", "Certifications", "Contact"],
        icons=["house", "stars", "book", "award", "person-rolodex"],
        orientation="vertical",
        default_index=0,
        styles={
            "container": {
                "align-items": "center",
                "text-align": "center",
                "background": "transparent",
                "margin-top": "20px"
            },

            "icon": {
                "color": "#000",
                "font-size": "20px"
            },

            "nav-link": {
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "font-size": "15px",
                "--hover-color": "#7FB1AF",
                "font-weight": "bold",
            },

            "nav-link-selected": {"background-color": "#04AA6D"},
        }
    )

    st.markdown(
        """
        <div style="background-color: transparent; margin-top: 150px; text-align: center;">
            <p style="font-size: 15px; font-weight: bold">
                &copy; 2024 Anas Ahmed. All Rights Reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if navigation == "Home":
    text = "WELCOME TO MY PORTFOLIO WEBSITE.."
    st.title(text)

    about = """I am Anas Ahmed, a highly motivated and detail-oriented individual with a strong foundation in Computer Engineering, having graduated from Abant Izzet Baysal University. 
    My passion lies in the vast and evolving realm of artificial intelligence. In addition to my academic background, 
    I have honed my skills in various domains, including data analysis, machine learning, deep learning, and web development.
    """

    col1, col2 = st.columns(2)

    profile = Image.open("images/profile.jpg")

    st.markdown("""
        <style>
                img {
                    margin-top: 70px;
                    border-radius: 10%;
                    width: 250px;
                }

        </style>
        """, unsafe_allow_html=True)

    with col1:
        st.header("I Am Anas Ahmed")
        st.text("")
        st.subheader("About")
        st.write(about)
    with col2:
        st.image(profile)

if navigation == "Chat Assistant":
    anas_persona = """You are Anas AI bot and your name is anas's assistant .You help people answer questions about anas 
    (i.e Anas)and chat with them.first understand user intent and than Answer as if you are responding . dont answer in 
    second or third person. If you don't know they answer you or the question is extremely irrelevant simply say  "That's 
    a secret". Here is more info about Anas(me):

            i am Anas Ahmed Shaikh, currently a second-year student at the Government Delhi College. My academic 
            journey is a blend of rigorous study and a relentless pursuit of excellence in the field of technology. 
            Professionally, I wear multiple hats: I develop robust website backends, craft innovative software solutions, 
            and thrive as an entrepreneur. My toolbox is rich with languages and technologies. I have a deep affection 
            for TypeScript, Python, HTML5, CSS, and JavaScript. In my daily workflow, I heavily use tools like
             Node.js, 
            Visual Studio Code (VSCode), PyCharm, GitHub, and Git to bring my ideas to life. What fuels my drive? It’s 
            the simple pleasure of a good cup of coffee and an unwavering commitment to delivering quality in everything 
            I undertake. My ultimate career aspiration is to become a data scientist, where I can leverage my skills and 
            knowledge to uncover insights and drive meaningful change. I have a few proud moments that highlight my 
            journey. During school, I won a water rocket competition, a testament to my early love for innovation and 
            science. In the realm of computer science, I’ve amassed a wealth of knowledge and numerous course completion 
            certificates from Coursera. Notable among them are "Foundations of Digital Marketing and E-commerce,
            " "Attract and Engage Customers with Digital Marketing," "Think Outside the Inbox: Email Marketing,
            " "From Likes to Leads: Interact with Customers Online" by Google, "Introduction to Generative AI" by Google 
            Cloud, and "Building Your Own Database Agent" and "Building Systems with the ChatGPT API" by DeepLearning.AI. 
            My journey is one of continuous learning, and I’m currently on the path to becoming a Cloud Applied 
            Generative AI Engineer. When I’m not immersed in coding or learning, I enjoy reading books, spending quality 
            time with friends, listening to music, and engaging in self-development activities. Life is a balance of hard 
            work and enjoyment, and I make sure to savor every moment. This is me, Anas Ahmed Shaikh, a blend of passion, 
            technology, and an insatiable quest for knowledge and excellence

            anas's Email: anas@codtecs.com
            anas's Facebook: https://www.facebook.com/profile.php?id=61551632792759
            anas's Instagram: https://www.instagram.com/Anasthesia_./
            anas's Linkedin: https://www.linkedin.com/in/anas-ahmed-shaikh
            anas's Github :https://github.com/anasahmedshaikh

            here is the user question:
            """

    st.title("Anas's AI Bot")

    st.chat_message("assistant").markdown("Hi:wave:")
# Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# React to user input
    if prompt := st.chat_input("What is up?"):

        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        user_question = anas_persona + prompt
        response = model.generate_content(user_question)
        text_response = response.text
# Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(text_response)
# Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": text_response})

if navigation == "Skills":

    skills = {
        "Python": 80,
        "Data Analysis": 80,
        "Visualization": 85,
        "Machine Learning": 75,
        "Deep Learning": 70,
        "SQL": 70,
        "Flask": 80,
        "HTML": 85,
        "CSS": 75,
        "Javascript": 60,
    }

    progress_bar_styles = """
        <style>
        p {
            color: white !important;
            margin: 7px 0;
        }
        .progress-bar {
            background-color: #ddd;
            border-radius: 10px;
            margin: 7px 0;
        }
        .progress-bar div {
            background-color: #04AA6D;
            color: white;
            text-align: center;
            border-radius: 10px;
            transition: width 0.3s ease-in-out;
        }
        </style>
    """

    st.write("### :star: Skills")

    # Display skills with progress bars
    st.markdown(progress_bar_styles, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    for skill, level in skills.items():
        with col1:
            st.write(skill)
        progress_bar = f'<div style="width: {level}%;"><b>{level}%</b></div>'
        col2.markdown(f'<div class="progress-bar">{progress_bar}</div>', unsafe_allow_html=True)

if navigation == "Projects":
    st.write("### :book: Projects")
    st.markdown(
        """
        <style>
        a {
            text-align: center !important;
            color: white !important;
            text-decoration: none;
        }
    
        a:hover {
            color: #04AA6D !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    cards = [
        {
            "title": "Gemini Pro ChatBot AI Assistant",
            "image": "images/gemini.jpg",
            "link": ""
        },
        {
            "title": "Npm Projects",
            "image": "images/npm.png",
            "link": "https://www.npmjs.com/~anas_ahmed"
        }

    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(cards[0]['image'], width=220)
        st.markdown(f"[{cards[0]['title']}]({cards[0]['link']})")

    with col2:
        st.image(cards[1]['image'], width=220)
        st.markdown(f"[{cards[1]['title']}]({cards[1]['link']})")

    if st.button("Learn More..."):
        url = "https://github.com/anasahmedshaikh"
        js = f'window.open("{url}", "_blank").then(r => window.parent.location.href);'
        st_javascript(js)

if navigation == "Certifications":
    st.write("### :medal: Certifications")
    st.markdown(
        """
        <style>
        a {
            color: white !important;
            text-decoration: none;
        }
    
        a:hover {
            color: #04AA6D !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    cards = [
        {
            "title": "Generative AI",
            "image": "images/genai.png",
            "link": "https://coursera.org/share/393bd766a404c39523f3721c56a70290"
        },
        {
            "title": "Digital markeeting",
            "image": "images/digi2.png",
            "link": "https://coursera.org/share/bbb25392d74df2fd187a8be071ca7f7e"
        },{
            "title": "Foundation of Digital markeeting",
            "image": "images/digi1.png",
            "link": "https://coursera.org/share/1bd8bcc13fe4f3dfb133456bc32cee0e"
        },
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.image(cards[0]['image'])
        st.markdown(f"[{cards[0]['title']}]({cards[0]['link']})")
        st.image(cards[2]['image'])
        st.markdown(f"[{cards[0]['title']}]({cards[2]['link']})")

    with col2:
        st.image(cards[1]['image'])
        st.markdown(f"[{cards[1]['title']}]({cards[1]['link']})")

if navigation == "Contact":
    st.write("### :mailbox_closed: Get In Touch With Me!")

    contact_form = """
    <form action="https://formsubmit.co/anasahmedshaikh2007@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" style="resize: none;" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    media = [
        {
            "title": "Linkedin",
            "image": "images/linkedin.png",
            "link": "https://www.linkedin.com/in/anas-ahmed-shaikh/"
        },
        {
            "title": "GitHub",
            "image": "images/github.png",
            "link": "https://github.com/anasahmedshaikh"
        },
        {
            "title": "Instagram",
            "image": "images/instagram.jpg",
            "link": "https://www.instagram.com/anasthesia._/"
        },
    ]

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    st.markdown(
        """
        <style>
        img {
            margin-top: 80px;
            width: 40px;
            margin-left: 50px;
        }
        p {
            margin-top: 85px;
            margin-right: 25px;
            color: white !important;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True)

    col1.image(media[0]['image'])
    col2.markdown(f"[{media[0]['title']}]({media[0]['link']})")

    col3.image(media[1]['image'])
    col4.markdown(f"[{media[1]['title']}]({media[1]['link']})")

    col5.image(media[2]['image'])
    col6.markdown(f"[{media[2]['title']}]({media[2]['link']})")

