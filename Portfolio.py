import streamlit as st
from PIL import Image
import time  # Added for manual text animation
import pandas as pd
from datetime import datetime
from pathlib import Path

# Set up the main structure of the portfolio
st.set_page_config(page_title="My Portfolio", layout="wide")
'''''
# Sidebar for navigation
def styled_sidebar():
    # Add custom CSS for styling the sidebar
    st.markdown(
        """
        <style>
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #1a1a1a, #333);
            color: white;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .sidebar-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #f39c12;
            margin-bottom: 20px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
        }
        .menu-item {
            text-align: center;
            background: #444;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            margin: 10px 0;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.2s ease;
        }
        .menu-item:hover {
            background: #f39c12;
            transform: scale(1.05);
        }
        .menu-item.active {
            background: #0073e6;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar container
    st.sidebar.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-title">Navigation</div>', unsafe_allow_html=True)

    # Navigation options
    options = ["Home", "Blogs & Research Paper", "Projects", "Contact"]

    # Handle button clicks
    clicked_button = None
    for option in options:
        if st.sidebar.button(option):
            clicked_button = option

    st.sidebar.markdown('</div></div>', unsafe_allow_html=True)

    return clicked_button or "Home"  # Default to Home if no button is clicked


'''
# Header Section with manual animation
def animated_text(lines, speed=0.05):
    placeholder = st.empty()
    for line in lines:
        placeholder.markdown(f"### {line}")
        time.sleep(speed)
    placeholder.empty()


def header_section():
    # Add a gradient background with styling
    
    # Add CSS for floating animation and overall styling
    st.markdown(
        """
        <style>
        @keyframes floatUp {
            0% {
                opacity: 0;
                transform: translateY(50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header-section {
            background: linear-gradient(135deg, #1a1a1a, #333);
            border-radius: 10px;
            padding: 20px;
            color: white;
            animation: floatUp 1.5s ease-out;
        }

        .header-title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            animation: floatUp 2s ease-out;
        }

        .header-description {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #b3b3b3;
            animation: floatUp 2.5s ease-out;
        }

        .highlight {
            color: #f39c12;
            font-weight: bold;
        }

        .image-container {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Render the section
    st.markdown('<div class="header-section">', unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns([1, 2])

    # Add the image in the first column
    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(
            "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/view-3d-man-holding-laptop-removebg.png",
            caption="Crafting Solutions, One Line of Code at a Time.",
            use_container_width=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Add the text in the second column
    with col2:
        st.markdown(
            """
            <div class="header-title">DataHashArunava</div>
            <div class="header-description">
                Hi, I’m <span class="highlight">Arunava Chakraborty</span>, a tech enthusiast driven by curiosity and a passion for problem-solving.<br>
                As a <span class="highlight">CSE undergraduate</span>, I specialize in crafting innovative solutions in 
                <span class="highlight">Data Science</span>, <span class="highlight">Data Analysis</span>, and <span class="highlight">Machine Learning</span>.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Add dynamic highlights
        st.markdown(
            """
            <div class="header-description">
                🌟 <b>Passionate About Tech, Driven by Curiosity.</b><br>
                🚀 <b>Let’s Build Something Amazing Together!</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

# About Me Section
def about_section():
    st.header("Blogs & Research Papers")
    st.write(
        """Hello! I'm Arunava Chakraborty , a passionate software developer and data enthusiast with a knack for solving complex challenges. 
        My expertise lies in [specific skills or tools, e.g., Python, Machine Learning, Full-Stack Development], and I love working on 
        projects that make a difference.
        
        When I'm not coding, you can find me exploring new technologies, writing blogs, or enjoying [hobby, e.g., photography]."""
    )
    
    Blogs = [
        {"title":"Python- For Everyone and Everywhere","description":"IN this blog you will find in which field and how python can be used tools , libraries , frameworks and many more","link":""},
        {"title": "Machine Learning-A Complete Roadmap","description":"A Full Fledge machine learning roadmap from beginner to advance", "link":""},
        {"title":"Tools and Technologies for Machine Learning","description":"The blog consists of what are the tools and tech should be known for building a machine learning project. It covers which tech how it helps and many more","link":""},
        {"title":"MlOps-Deploy your machine learning models","description":"Read this blog if you are interested about how we deploy the machine learning models in real world use case","link":""},
        {"title":"5 Data Science Projects and the source code of the projects","description":"In this blog there is % projects that can be added to your portfolio with source code and resources","link":""},
        {"title":"All Concepts Of Machine Learning","description":"In this blog I wrote each and every machine learning concepts overview that will help you to start your journey as a ml engineer","link":""},
        {"title":"All Concepts of DBMS","description":"In this blog you will find each and every dbms concepts overview that you need to know","link":""},
        {"title":"Statistics-Pillar of Data Science and Machine Learning","description":"In this blog you will find each and every concepts that will help you understand the core concepts behind the machine learning models.","link":""},
        {"title":"Machine Learning Behind The Scene- Support Vector Machine","description":"In this blog you will find working of one of the widely used ml algorithm SVM and the maths ,concepts behind the scene.","link":""},
        {"title":"Machine Learning Behind The Scene- K-Nearest Neighbor","description":"In this blog you will find the working principle of the KNN algorithm and the maths and core concept behind it","link":""},
        {"title":"Machine Learning Behind The Scene- Principle Component Analysis","description":"In this blog you will find one of the vastly use dimensionality reduction technique PCA the working principle of it and the core concept behind it","link":""},
        {"title":"Machine Learning Behind The Scene- Regression Techniques","description":"In this blog you will find the Regression techniques both Linear and Logistic regression","link":""},
        {"title":"Machine Learning Behind The Scene- Random Forest","description":"In this blog you will find the comprehensive guide for the Random Forest Algorithm","link":""},
        {"title":"Machine Learning Behind The Scene- Decision Trees", "description":"In this blog you will find the comprehensive guide for the decision tree Algorithm and the maths and core concepts behind it","link":""}
    ]
    for blog in Blogs:
        with st.container():
            st.markdown("<div style='border: 1px solid #ddd; padding: 2px;margin-top:10px; margin-bottom: 25px;'>", unsafe_allow_html=True)
            col1, col2 = st.columns([4, 1])
            with col1:
                st.subheader(f"**{blog['title']}**")
                st.write(blog["description"])
            with col2:
                st.button("Read Blog", key=blog['title'], help=f"Read more about {blog['title']}")
            st.markdown("</div>", unsafe_allow_html=True)

# Projects Section
def projects_section():
    st.header("My Projects")
    st.write("Here are some highlights of my work:")

    projects = [
        {"title": "E-commerce Chatbot", "description": "An interactive chatbot capable of negotiating prices for e-commerce platforms.", "link": "https://github.com/your-repo/chatbot", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Web Traffic Forecasting", "description": "A machine learning model to predict and optimize web traffic trends and forecast about it.", "link": "https://github.com/your-repo/web-traffic", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Portfolio Website- Data#Arunava", "description": "This very portfolio built with Python and Streamlit! dive down in my projects and interests", "link": "https://github.com/your-repo/portfolio", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Media Sentiment Analysis", "description": "Analyze social media data for sentiment insights and give feedback and predictions.", "link": "https://github.com/your-repo/social-sentiment", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Stock Price Prediction", "description": "Machine learning model to predict stock prices.", "link": "https://github.com/your-repo/stock-prediction", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Personal Finance Dashboard", "description": "A dashboard to visualize and manage personal finances.", "link": "https://github.com/your-repo/finance-dashboard", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Image Classifier Model", "description": "An image classification model using CNN.", "link": "https://github.com/your-repo/image-classifier", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"},
        {"title": "Recommendation System", "description": "A recommendation system for e-commerce platforms.", "link": "https://github.com/your-repo/recommendation", "image_url": "https://raw.githubusercontent.com/Arunava-Chakraborty/portfolio-website/main/thumbnails.png"}
    ]

    rows = len(projects) // 4 + (1 if len(projects) % 4 != 0 else 0)

    # Inject hover effect CSS for Streamlit containers
    hover_css = """
    <style>
    .stImage:hover {
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.02);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    </style>
    """
    st.markdown(hover_css, unsafe_allow_html=True)

    for row in range(rows):
        cols = st.columns(4)
        for col, project in zip(cols, projects[row * 4:(row + 1) * 4]):
            with col:
                st.image(project["image_url"], use_container_width=True)
                st.subheader(project["title"])
                st.write(project["description"])
                if st.button(f"View {project['title']}", key=project["title"]):
                    st.write(f"Open the project [here]({project['link']}).")






# Contact Section
def contact_section():
    st.header("Get in Touch")
    

    # Display contact information as a footer
    st.markdown(
        """
        <footer style='margin-top: 20px;'>
            <div style='display: flex; justify-content: center; gap: 50px; flex-wrap: wrap; margin-bottom: 20px;'>
                <div style='text-align: center;'>
                    <a href='tel:+919775872890' target='_self'>
                        <img src='https://img.icons8.com/color/48/000000/phone.png' alt='Phone' style='width: 40px; height: 40px;'>
                    </a>
                    <p style='margin: 5px 0;'><strong>Phone</strong></p>
                    <p style='margin: 0;'></p>
                </div>
                <div style='text-align: center;'>
                    <a href='mailto:arunavaa.dev@gmail.com'>
                        <img src='https://img.icons8.com/color/48/000000/email.png' alt='arunavaa.dev@gmail.com' style='width: 40px; height: 40px;'>
                    </a>
                    <p style='margin: 5px 0;'><strong>arunavaa.dev@gmail.com</strong></p>
                    <p style='margin: 0;'></p>
                </div>
                <div style='text-align: center;'>
                    <a href='https://www.linkedin.com/in/arunava-chakraborty-095553258/' target='_blank'>
                        <img src='https://img.icons8.com/color/48/000000/linkedin.png' alt='LinkedIn' style='width: 40px; height: 40px;'>
                    </a>
                    <p style='margin: 5px 0;'><strong>LinkedIn</strong></p>
                    <p style='margin: 0;'></p>
                </div>
                <div style='text-align: center;'>
                    <a href='https://github.com/Arunava-Chakraborty' target='_blank'>
                        <img src='https://img.icons8.com/color/48/000000/github.png' alt='GitHub' style='width: 40px; height: 40px;'>
                    </a>
                    <p style='margin: 5px 0;'><strong>GitHub</strong></p>
                    <p style='margin: 0;'></p>
                </div>
            </div>
        </footer>
        """,
        unsafe_allow_html=True
    )

    # Initialize the CSV file for storing messages
    messages_file = "messages.csv"

    st.write("I'd love to hear from you!")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            # Append the new message to the CSV file
            message_data = {
                "Name": name,
                "Email": email,
                "Message": message,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            try:
                # If the file exists, append the data; otherwise, create a new file
                if Path(messages_file).exists():
                    existing_data = pd.read_csv(messages_file)
                    updated_data = pd.concat([existing_data, pd.DataFrame([message_data])], ignore_index=True)
                else:
                    updated_data = pd.DataFrame([message_data])
                
                updated_data.to_csv(messages_file, index=False)
                st.success(f"Thank you, {name}! Your message has been received.")
            except Exception as e:
                st.error("An error occurred while saving your message. Please try again.")
                st.error(f"Error details: {e}")

    # Provide a way to view the messages (for the owner only)
    if st.button("View Messages (Admin Only)"):
        if Path(messages_file).exists():
            messages = pd.read_csv(messages_file)
            st.dataframe(messages)
        else:
            st.write("No messages received yet.")

# Render selected section
'''''
choice = styled_sidebar()
if choice == "Home":
    header_section()
elif choice == "Blogs & Research Paper":
    about_section()
elif choice == "Projects":
    projects_section()
elif choice == "Contact":
    contact_section()

# Footer
st.markdown("---")
'''
