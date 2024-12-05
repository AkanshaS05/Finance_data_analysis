import streamlit as st
import pandas as pd

# Title and Banner Image
st.title("Financial Data Analytics")
st.image("https://th.bing.com/th/id/OIP.8ujhi0aeF1GWkR1uTNs3bAHaEK?w=278&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

# Introduction text
st.write(":green[A simple data app to analyze Finance data]")

# Sidebar for section selection
section = st.sidebar.selectbox("Select a section to explore:", 
                               ["About the Project", "Union Budget Overview", "Dataset Information"])

# About Project Section
if section == "About the Project":
    st.markdown(''' 
        # About Project
    The Indian Economy is currently the 5th Largest Economy in the world. And it aims to reach among the Top 3 in the next 3-4 years. It has registered tremendous economic growth over the last decade.

    The 2023 Union Budget of India was presented by the Minister of Finance of India on February 01, 2023.

    The Union Budget for FY 2023-24 aims to further strengthen India's economic status. In the 75th Year of India's Independence, the World has recognized the Indian Economy as a 'bright star' with its Economic Growth estimated at 7 per cent, which is the highest among all major economies.

    The Vision for :orange[Amrit Kaal] articulated in the Union Budget for FY 2023-24 is centered around:

    - Opportunities for Citizens with focus on youth
    - Growth & Job creation
    - Strong & Stable Macro-Economic Environment
    ''')
    


# Union Budget Overview Section
elif section == "Union Budget Overview":
    st.markdown(''' 
        ## Union Budget 2023-24 Overview
    The Union Budget for FY 2023-24 is designed to address the goals of economic growth and development. It focuses on areas such as:

    - **Inclusive Development**
    - **Green Growth**
    - **Youth Power**
    - **Financial Sector Development**
    ''')

    # Explanation about capital and revenue expenses
    st.success("Expenses which bring a change to the government’s assets or liabilities (such as construction of roads or recovery of loans) are :orange[capital expenses], and all other expenses are :blue[revenue expenses] (such as payment of salaries or interest payments).")

    # Budget focus area to explore
    budget_focus = st.radio("What area of the Union Budget would you like to explore?", 
                            ["Inclusive Development", "Green Growth", "Youth Power", "Financial Sector"])

    if budget_focus == "Inclusive Development":
        st.write("This section focuses on reaching the last mile and infrastructure investment.")
        st.info("Inclusive development aims to ensure that the benefits of economic growth reach all segments of society, with a particular emphasis on marginalized communities.")
        
    elif budget_focus == "Green Growth":
        st.write("This section focuses on sustainable and environmentally-friendly development.")
        st.info("Green growth emphasizes eco-friendly initiatives, investment in renewable energy, and sustainable development goals.")

    elif budget_focus == "Youth Power":
        st.write("This section focuses on empowering the youth of India.")
        st.info("Youth power focuses on skill development, education, and providing opportunities for youth to engage in the workforce.")
    
    elif budget_focus == "Financial Sector":
        st.write("This section focuses on strengthening India's financial system.")
        st.info("The financial sector includes initiatives to improve banking infrastructure, fintech, and policies to enhance financial inclusion.")


# Dataset Information Section
elif section == "Dataset Information":
    st.markdown('''
        ## Dataset Information
    The dataset contains the financial allocation of India's Union Budget for the fiscal year 2023-24, with details about various ministries, their respective budget categories, and allocation amounts.

    The dataset includes the following columns:

    - **Ministry**: The name of the government ministry responsible for the allocated budget.
    - **Budget Category**: Categorization of the budget (e.g., Revenue, Capital, etc.).
    - **Budget 2023 - Total**: The total budget allocation for the year 2023-24.
    - **Budget 2023 - Revenue**: The portion of the budget allocated for revenue expenditures.
    - **Budget 2023 - Capital**: The portion of the budget allocated for capital expenditures.
    
    **You can explore the data further by applying filters and viewing charts on this dashboard.**
    ''')


