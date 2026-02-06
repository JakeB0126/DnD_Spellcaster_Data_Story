import streamlit as st
import pandas as pd
import plotly.express as px

import shared

shared.apply_theme()

st.header("Arc 1: Foundations of Spellcasting")

st.write("""Before delving into specifics, we first need a broad understanding of spellcasting classes in D&D. Which classes dominate the player base? How does level progression
impact class choices? These foundational insights set the stage for deeper exploration into spellcaster customization.""")

# -----------------------------------------------------------
# FIGURE 1
# -----------------------------------------------------------

# Load big dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, compression='zip', usecols=["class_starting"])

# Filter for only spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Count number of players per class
class_count = df_filtered["class_starting"].value_counts().reset_index()
class_count.columns = ["Class", "Number of Players"]

# Create interactive bar chart
fig = px.bar(
    class_count,
    x="Class",
    y="Number of Players",
    text="Number of Players",
    title="Number of Players Per Spellcasting Class",
    labels={"Class": "Character Class", "Number of Players": "Count"},
    color="Class",
    color_discrete_map=shared.CLASS_COLORS,
)

# Modify layout
fig.update_layout(
    xaxis_title="Spellcasting Class",
    yaxis_title="Number of Players",
    xaxis_tickangle=-45,
    height=600,
    width=700,
)

# Show chart
with st.expander("Number of Players Per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Context & Insight:")

st.write("""
This bar chart shows overall class popularity. Wizards lead, with Clerics close behind, suggesting a strong preference for versatile roles. Druids are slightly less represented, possibly due to their higher learning curve.
""")

st.subheader("Relevant Transformations:")

st.write("""
**Formatting for Visualization:** Aggregated counts were reshaped into a simple two-column table for plotting.
""")

# -----------------------------------------------------------
# FIGURE 2
# -----------------------------------------------------------

# Load dataset
zip_path = shared.DATA_BIG_ZIP
df = pd.read_csv(zip_path, compression='zip', usecols=["class_starting", "total_level"])

# Define level bins and create some labels
bins = [1, 5, 10, 15, 20]
labels = ["1-5", "6-10", "11-15", "16-20"]
df["level_range"] = pd.cut(df["total_level"], bins=bins, labels=labels)

# Filter for spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Count classes by designated level ranges
df_grouped = df_filtered.groupby(["class_starting", "level_range"], observed=True).size().reset_index(name="count")

# Convert to percentages for readability
df_total = df_grouped.groupby("level_range")["count"].sum().reset_index(name="total_count")
df_percent = df_grouped.merge(df_total, on="level_range")
df_percent["percentage"] = (df_percent["count"] / df_percent["total_count"]) * 100

# Create interactive Plotly grouped bar chart
fig = px.bar(
    df_percent,
    x="level_range",
    y="percentage",
    color="class_starting",
    text="percentage",
    title="Class Popularity Across Level Ranges",
    labels={"level_range": "Level Range", "percentage": "Percent of Players (%)", "class_starting": "Class"},
    barmode="group",
    color_discrete_map=shared.CLASS_COLORS,
)

# Modify layout
fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(
    xaxis_title="Level Range",
    yaxis_title="Percentage of Players",
    xaxis_tickangle=-45,
    height=600,
    width=1000,
    legend_title="Class",
)

# Show chart
with st.expander("Spellcasting Class Popularity Across Level Ranges"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This grouped bar chart compares class popularity across level ranges, showing how preferences shift as characters level up.

#### Key Observations:
- **Lower Levels (1-5):** Wizards and Clerics dominate, likely due to their utility in the early stages of campaigns.
- **Mid-Levels (6-15):** Popularity evens out as most classes stay steady.
- **High Levels (16-20):** Wizards surge, reflecting late-game spell power and versatility.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Binning Levels:** `total_level` was grouped into four ranges.
- **Grouping and Percentages:** Counts per class-range were converted to percentages for comparison.
""")
