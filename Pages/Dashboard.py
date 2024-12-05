import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset

df = pd.read_csv("cleaned_budget_data.csv")


# Streamlit app
st.title("Budget Data Visualization")

st.success("Expenses which bring a change to the government’s assets or liabilities (such as construction of roads or recovery of loans) are :orange[capital expenses], and all other expenses are :blue[revenue expenses] (such as payment of salaries or interest payments).")

# Filters
st.sidebar.header("Filters")
selected_ministry = st.sidebar.multiselect("Select Ministry", options=df["Ministry"].unique())
if not selected_ministry:
    selected_ministry = df["Ministry"].unique()

selected_category = st.sidebar.multiselect("Select Budget Category", options=df["Budget_Category"].dropna().unique(), default=df["Budget_Category"].dropna().unique())


# Total Budget Range Filter
min_budget, max_budget = st.sidebar.slider(
    "Select Total Budget Range",
    min_value=float(df["Budget_2023_Total"].min()),
    max_value=float(df["Budget_2023_Total"].max()),
    value=(float(df["Budget_2023_Total"].min()), float(df["Budget_2023_Total"].max()))
)

# Apply Filters
filtered_df = df[
    (df["Ministry"].isin(selected_ministry)) &
    (df["Budget_Category"].isin(selected_category)) &
    (df["Budget_2023_Total"].between(min_budget, max_budget))
]

# Total Budget of Ministries           (by total budget and category)
st.info(f"Total Budget of Ministries **(Selected Ministries: {len(selected_ministry)})**")
# fig_pie = px.pie(filtered_df, names="Ministry", values="Budget_2023_Total", title="Total Budget of Ministries")
fig = px.sunburst(filtered_df, path=["Ministry", "Budget_Category"], values="Budget_2023_Total", title="Total Budget of Ministries", color="Budget_2023_Total")
st.plotly_chart(fig)

st.markdown("---")

# Total Budget Revenue of Ministries
st.info(f"Total Budget **Revenue** of Ministries **(Top 10 Ministries)**")
top_10_Revenue = df.groupby("Ministry")["Budget_2023_Revenue"].sum().nlargest(10).reset_index()
fig = px.pie(top_10_Revenue, names="Ministry", values="Budget_2023_Revenue", title="Total Budget Revenue of Top 10 Ministries")
st.plotly_chart(fig)

st.markdown("---")

# Total Budget Capital of Ministries (Top 10)
st.info(f"Total Budget **Capital** of Ministries **(Top 10 Ministries)**")
top_10_capital = df.groupby("Ministry")["Budget_2023_Capital"].sum().nlargest(10).reset_index()
fig = px.pie(top_10_capital, names="Ministry", values="Budget_2023_Capital", title="Total Budget Capital of Top 10 Ministries")
st.plotly_chart(fig)

st.markdown("---")

# Revenue vs. Capital Budget         (groupby)
st.info(f"Revenue vs. Capital Budget **(Selected Ministries: {len(selected_ministry)})**") 
fig = px.scatter(filtered_df, x="Budget_2023_Revenue", y="Budget_2023_Capital", color="Ministry", title="Revenue vs. Capital Budget")
st.plotly_chart(fig)

st.markdown("---")

# Budget Category Distribution
st.info(f"Budget Category Distribution **({len(selected_category)} Categories**)")
pie_fig = px.pie(filtered_df, names="Budget_Category", values="Budget_2023_Total", title="Budget Category Distribution")
st.plotly_chart(pie_fig)

st.markdown("---")

# Revenue and Capital Budget by Ministry
st.info(f"Revenue and Capital Budget by Ministry **(Selected: {len(selected_ministry)})**")
fig = px.bar(filtered_df, x="Ministry", y=["Budget_2023_Revenue", "Budget_2023_Capital"], title="Revenue and Capital Budgets by Ministry", barmode="stack", color="Budget_Category")
st.plotly_chart(fig)

st.markdown("---")

# Top 10 Ministries by Total Budget     (budget category in lables)
st.info(f"Top **{min(10, len(filtered_df['Ministry'].unique()))}** Ministries by Total Budget")
top_10 = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().nlargest(10).reset_index()
top_10_bar_fig = px.bar(top_10, x="Ministry", y="Budget_2023_Total", title="Top 10 Ministries by Budget", labels={"Budget_2023_Total": "Total Budget (₹)"})
st.plotly_chart(top_10_bar_fig)

st.markdown("---")

# Top Demanding Ministries
st.info(f"Top Demanding Ministries **({len(df['Ministry'].unique())} Ministries)**")
top_ministries = df.groupby("Ministry")["Budget_2023_Total"].sum().sort_values(ascending=False)
fig = px.bar(top_ministries, x=top_ministries.index, y=top_ministries.values, title="Top Demanding Ministries", labels={"x": "Ministry", "y": "Demands"})
st.plotly_chart(fig)

st.markdown("---")

# Percentage Distribution of Top 10 Ministries
st.info(f"Percentage Distribution of Top **({top_10.shape[0]} Ministries)**")
top_10["Percentage"] = (top_10["Budget_2023_Total"] / filtered_df["Budget_2023_Total"].sum()) * 100
top_10_pie_fig = px.pie(top_10, values="Percentage", names="Ministry", title="Top Ministries Percentage Distribution")
st.plotly_chart(top_10_pie_fig)

st.markdown("---")

# Total Budget Over Ministries
st.info(f"Total Budget Over **({len(selected_ministry)} Ministries)**")
line_fig = px.line(filtered_df, x="Ministry", y="Budget_2023_Total", title="Total Budget Across Ministries")
st.plotly_chart(line_fig)

st.markdown("---")

# 10. Conclusion
st.info("**📌Conclusion**")

highest_budget_ministry = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().idxmax()
lowest_budget_ministry = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().idxmin()

# Highest Budget Ministry
highest_budget_ministry = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().idxmax()
highest_budget = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().max()
highest_capital_budget = filtered_df[filtered_df["Ministry"] == highest_budget_ministry]["Budget_2023_Capital"].sum()
highest_revenue_budget = filtered_df[filtered_df["Ministry"] == highest_budget_ministry]["Budget_2023_Revenue"].sum()

st.success(
    f"""
    🔸 **Highest Budget Ministry**: **{highest_budget_ministry}**  
    - **Total Budget**: ₹{highest_budget:,.2f}  
    - **Capital Budget**: ₹{highest_capital_budget:,.2f}  
    - **Revenue Budget**: ₹{highest_revenue_budget:,.2f}  
    """
)

# Lowest Budget Ministry
lowest_budget_ministry = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().idxmin()
lowest_budget = filtered_df.groupby("Ministry")["Budget_2023_Total"].sum().min()
lowest_capital_budget = filtered_df[filtered_df["Ministry"] == lowest_budget_ministry]["Budget_2023_Capital"].sum()
lowest_revenue_budget = filtered_df[filtered_df["Ministry"] == lowest_budget_ministry]["Budget_2023_Revenue"].sum()

st.warning(
    f"""
    🔹 **Lowest Budget Ministry**: **{lowest_budget_ministry}**  
    - **Total Budget**: ₹{lowest_budget:,.2f}  
    - **Capital Budget**: ₹{lowest_capital_budget:,.2f}  
    - **Revenue Budget**: ₹{lowest_revenue_budget:,.2f}  
    """
)


# Footer
st.sidebar.info("Use the filters to customize the charts!")

st.markdown("---")
st.info("Built with ❤️ using Streamlit and Plotly.")
