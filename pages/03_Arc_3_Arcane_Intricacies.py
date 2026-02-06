import streamlit as st
import pandas as pd
import plotly.express as px

import shared

shared.apply_theme()

st.header("Arc 3: Arcane Intricacies")

st.write("""Beyond character creation, how do spellcasters function in play? From gold distribution to notes, these insights reveal what players prioritize and document.""")

# -----------------------------------------------------------
# FIGURE 7 - GOLD
# -----------------------------------------------------------

# Load dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, usecols=["class_starting", "gold"])

# Filter for spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Remove extreme values
df_filtered = df_filtered[(df_filtered["gold"] > 0) & (df_filtered["gold"] < 350_000)]

# Directly calculate the average gold per class
df_avg_gold = df_filtered.groupby("class_starting", as_index=False)["gold"].mean()

# Rename column for clarity
df_avg_gold.rename(columns={"gold": "Average Gold"}, inplace=True)

# Bar chart of average gold per class
fig = px.bar(
    df_avg_gold,
    x="class_starting",
    y="Average Gold",
    title="Average Gold per Spellcasting Class",
    labels={"class_starting": "Class", "Average Gold": "Gold (Avg)"},
    color="class_starting",
    color_discrete_map=shared.CLASS_COLORS,
)

# Modify layout
fig.update_layout(
    width=700,
    height=600,
    xaxis_title="Character Class",
    yaxis_title="Average Gold",
    title_font_size=18,
)

# Show chart
with st.expander("Average Gold per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This bar chart shows **average gold** for each spellcasting class. In D&D, gold fuels equipment, spell components, and services, so the averages hint at how players prioritize resources.

#### Key Observations:
- **Wizards** lead, likely due to spell components and scroll costs.
- **Sorcerers and Warlocks** follow, reflecting investment in magical power.
- **Bards and Druids** sit lower, relying more on innate versatility.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Filtering Outliers:** Excluded gold > 350,000 and gold = 0.
- **Averages:** Computed mean gold by `class_starting`.
""")

# -----------------------------------------------------------
# FIGURE 8 - NOTES
# -----------------------------------------------------------

# Load dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, usecols=["class_starting", "notes_len"])

# Filter for only six spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Remove entries where 'notes_len' is 0
df_filt_nonzero = df_filtered[df_filtered["notes_len"] > 0]

# Calculate average note length per class
avg_note_length_per_class = df_filt_nonzero.groupby("class_starting")["notes_len"].mean().reset_index()

# Create interactive lollipop chart
fig = px.scatter(
    avg_note_length_per_class,
    x="class_starting",
    y="notes_len",
    text=avg_note_length_per_class["notes_len"].round(1),
    color="class_starting",
    color_discrete_map=shared.CLASS_COLORS,
    title="Average Note Length per Spellcasting Class",
    labels={"class_starting": "Class", "notes_len": "Average Note Length"},
)

# Add sticks for lollipop effect
for _, row in avg_note_length_per_class.iterrows():
    fig.add_shape(
        type="line",
        x0=row["class_starting"],
        x1=row["class_starting"],
        y0=0,
        y1=row["notes_len"],
        line=dict(color="gray", width=2),
    )

# Modify layout for readability
fig.update_traces(marker=dict(size=15, line=dict(width=2, color="black")), textposition="top center")
fig.update_layout(
    xaxis_title="Class",
    yaxis_title="Average Note Length",
    xaxis_tickangle=-25,
    height=600,
    width=700,
    showlegend=False,
)

# Show chart
with st.expander("Average Note Length per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This lollipop chart shows **average note length** by class. In D&D Beyond, notes often capture backstory and campaign details.

#### Key Observations:
- **Warlocks** write the most, fitting their lore-heavy identity.
- **Bards** follow, consistent with narrative-focused play.
- **Clerics and Wizards** are shorter on average, suggesting a more mechanics-first approach.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Exclude Zeros:** Removed entries with `notes_len` = 0.
- **Averages:** Computed mean note length by class.
- **Lollipop Layout:** Combined a scatter plot with vertical lines.
""")
