import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

import shared

shared.apply_theme()

st.header("Arc 2: Defining the Arcane")

st.write("""Character creation is more than choosing a class; it is crafting an identity. These visuals highlight common races, backgrounds, and subclasses that bring each spellcaster to life.""")

# -----------------------------------------------------------
# FIGURE 3 - RACES
# -----------------------------------------------------------

# Load dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, usecols=["class_starting", "race"])

# Keep only six spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Count number of each race per class
df_counts = df_filtered.groupby(["class_starting", "race"]).size().reset_index(name="count")

# Rank races for each class; keep only top 3
df_counts["ranks"] = df_counts.groupby("class_starting")["count"].rank(method="dense", ascending=False)
df_top_races = df_counts[df_counts["ranks"] <= 3]

# Get unique classes and sorted races
unique_classes = sorted(df_top_races["class_starting"].unique())
sorted_races = sorted(df_top_races["race"].unique())

# Map from race to angles (evenly spaced around circle)
race_to_angle = {race: angle for race, angle in zip(sorted_races, np.linspace(0, 360, len(sorted_races), endpoint=False))}

# Ensure largest count per race is plotted first
df_sorted = df_top_races.sort_values(["race", "count"], ascending=[False, True])

# Create figure
fig = go.Figure()

# Loop through each race and add bars for each class
for race in sorted_races:
    race_data = df_sorted[df_sorted["race"] == race]

    for _, row in race_data.iterrows():
        cls = row["class_starting"]
        angle = race_to_angle[race]
        count = row["count"]

        # Add a radial bar for each class-race pair
        fig.add_trace(
            go.Barpolar(
                r=[count],
                theta=[angle],
                width=[360 / len(sorted_races) * 0.9],
                marker_color=shared.CLASS_COLORS[cls],
                name=f"{cls} - {race}",
                hoverinfo="text",
                text=f"{cls} ({count})",
                showlegend=False,
            )
        )

# Make it so that the legend is only the 6 classes and not the 18 different combinations
for cls in unique_classes:
    fig.add_trace(
        go.Barpolar(
            r=[0],
            theta=[0],
            marker_color=shared.CLASS_COLORS[cls],
            name=cls,
            hoverinfo="skip",
        )
    )

# Modify layout
fig.update_layout(
    title="Top 3 Races for Each Class",
    polar=dict(
        radialaxis=dict(showticklabels=True, tickfont_size=12, color="black"),
        angularaxis=dict(showticklabels=True, tickmode="array", tickvals=list(race_to_angle.values()), ticktext=sorted_races),
    ),
    showlegend=True,
    margin=dict(l=120, r=120, t=80, b=80),
    height=700,
    width=700,
)

# Show chart
with st.expander("Top 3 Races for Each Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("D&D Races")

st.image(shared.IMAGE_FILES[6], caption="", use_container_width=True)

st.subheader("Context & Insights")

st.write("""
This radial bar chart shows the top three races for each spellcasting class. In D&D, race provides traits and cultural flavor that shape a character's identity. Humans, Elves, and Tieflings appear often, reflecting their broad synergy with spellcasters.

#### Key Observations:
- **Wizards and Humans:** Versatile bonuses make Humans a safe, flexible pick.
- **Half-Elves and Charisma Classes:** Half-Elves align well with Bards and Sorcerers.
- **Tieflings and Warlocks:** Thematic fit reinforces the pact-based identity.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting and Ranking:** Races were grouped by class and the top three were retained.
- **Radial Layout:** Each race was assigned an angle for even spacing.
""")

# -----------------------------------------------------------
# FIGURE 4 - BACKGROUNDS
# -----------------------------------------------------------

# Load dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, usecols=["class_starting", "background"])

# Keep only six spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Count backgrounds per class
df_counts = df_filtered.groupby(["class_starting", "background"]).size().reset_index(name="count")

# Rank backgrounds for each class; keep only top 3
df_counts["ranks"] = df_counts.groupby("class_starting")["count"].rank(method="dense", ascending=False)
df_top_backgrounds = df_counts[df_counts["ranks"] <= 3]

# Get unique classes and sorted backgrounds
unique_classes = sorted(df_top_backgrounds["class_starting"].unique())
sorted_backgrounds = sorted(df_top_backgrounds["background"].unique())

# Map from background to angles
background_to_angle = {
    background: angle for background, angle in zip(sorted_backgrounds, np.linspace(0, 360, len(sorted_backgrounds), endpoint=False))
}

# Ensure largest count per background is plotted first
df_sorted = df_top_backgrounds.sort_values(["background", "count"], ascending=[False, True])

fig = go.Figure()

for background in sorted_backgrounds:
    background_data = df_sorted[df_sorted["background"] == background]

    for _, row in background_data.iterrows():
        cls = row["class_starting"]
        angle = background_to_angle[background]
        count = row["count"]

        fig.add_trace(
            go.Barpolar(
                r=[count],
                theta=[angle],
                width=[360 / len(sorted_backgrounds) * 0.9],
                marker_color=shared.CLASS_COLORS[cls],
                name=f"{cls} - {background}",
                hoverinfo="text",
                text=f"{cls} ({count})",
                showlegend=False,
            )
        )

for cls in unique_classes:
    fig.add_trace(
        go.Barpolar(
            r=[0],
            theta=[0],
            marker_color=shared.CLASS_COLORS[cls],
            name=cls,
            hoverinfo="skip",
        )
    )

fig.update_layout(
    title="Top 3 Backgrounds for Each Class",
    polar=dict(
        radialaxis=dict(showticklabels=True, tickfont_size=12, color="black"),
        angularaxis=dict(showticklabels=True, tickmode="array", tickvals=list(background_to_angle.values()), ticktext=sorted_backgrounds),
    ),
    showlegend=True,
    margin=dict(l=120, r=120, t=80, b=80),
    height=700,
    width=700,
)

with st.expander("Top 3 Backgrounds for Each Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This radial bar chart shows the top three backgrounds per spellcasting class. In D&D, a background reflects a character's history and skills. Sage, Acolyte, and Soldier appear often, aligning closely with classic spellcaster themes.

#### Key Observations:
- **Wizards and Sage:** Scholars fit the wizard identity.
- **Clerics and Acolyte:** Divine service reinforces their role.
- **Bards and Entertainer/Folk Hero:** Storyteller backgrounds stand out.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting and Ranking:** Backgrounds were grouped by class and the top three retained.
- **Radial Layout:** Backgrounds were mapped to angles for spacing.
""")

# -----------------------------------------------------------
# FIGURE 5 - SUBCLASSES
# -----------------------------------------------------------

# Load dataset
df = pd.read_csv(shared.DATA_BIG_ZIP, usecols=["class_starting", "subclass_starting"])

# Filter for six spellcasting classes
df_filtered = df[df["class_starting"].isin(shared.SELECTED_CLASSES)]

# Count number of each subclass per class
df_counts = df_filtered.groupby(["class_starting", "subclass_starting"]).size().reset_index(name="count")

# Rank subclasses for each class; keep only top 3
df_counts["ranks"] = df_counts.groupby("class_starting")["count"].rank(method="dense", ascending=False)
df_top_subclasses = df_counts[df_counts["ranks"] <= 3]

fig_sunburst = px.sunburst(
    df_top_subclasses,
    path=["class_starting", "subclass_starting"],
    values="count",
    title="Top 3 Subclasses per Spellcasting Class",
    color="class_starting",
    color_discrete_map=shared.CLASS_COLORS,
)

with st.expander("Top 3 Subclasses for Each Spellcasting Class"):
    st.plotly_chart(fig_sunburst, use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This **sunburst chart** shows the top three subclasses for each spellcasting class. A **subclass** defines a class specialization and adds unique abilities. Most classes show a clear favorite, with Druids more evenly spread.

#### Key Observations:
- **Wizards and Evocation:** Direct damage and iconic spells keep Evocation popular.
- **Clerics and Life Domain:** Healing and support align with core cleric play.
- **Warlocks and The Fiend:** The classic pact theme remains a strong draw.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting and Ranking:** Subclasses were grouped by class and the top three retained.
- **Sunburst Path:** Built the `class_starting -> subclass_starting` hierarchy.
""")

# -----------------------------------------------------------
# FIGURE 6 - SPELLS
# -----------------------------------------------------------

# Load dataset
file_path = shared.DATA_SMALL_CSV
df = pd.read_csv(file_path)

# Filter for six spellcasting classes
df_filtered = df[df["justClass"].isin(shared.SELECTED_CLASSES)]

# Dictionary to store spell counts per class and level
class_spell_counts = {cls: {0: {}, 1: {}, 2: {}} for cls in shared.SELECTED_CLASSES}

# Extract spells by parsing through spell lists
for _, row in df_filtered.iterrows():
    cls = row["justClass"]
    if pd.notna(row["processedSpells"]):
        spell_list = row["processedSpells"].split("|")
        for spell in spell_list:
            parts = spell.split("*")
            if len(parts) == 2:
                spell_name, level = parts[0].strip(), parts[1].strip()
                if level.isdigit():
                    level = int(level)
                    if level in [0, 1, 2]:
                        class_spell_counts[cls][level][spell_name] = class_spell_counts[cls][level].get(spell_name, 0) + 1

# Find most popular spell per class per level
top_class_spells = []
for cls in shared.SELECTED_CLASSES:
    for level in [0, 1, 2]:
        if class_spell_counts[cls][level]:
            top_spell = max(class_spell_counts[cls][level], key=class_spell_counts[cls][level].get)
            count = class_spell_counts[cls][level][top_spell]
            top_class_spells.append({
                "Class": cls,
                "Spell Level": f"Level {level}",
                "Spell": top_spell,
                "Count": count,
            })

# Convert to DataFrame for visualization
df_top_class_spells = pd.DataFrame(top_class_spells)

# Create interactive grouped bar chart using Plotly
fig = px.bar(
    df_top_class_spells,
    x="Spell Level",
    y="Count",
    color="Class",
    text="Spell",
    barmode="group",
    title="Most Popular Spells of Levels 0, 1, and 2 per Class",
    labels={"Count": "Spell Popularity", "Spell Level": "Spell Level"},
    hover_data={"Spell": True, "Class": True, "Count": True},
    color_discrete_map=shared.CLASS_COLORS,
)

fig.update_layout(
    xaxis_title="Spell Level",
    yaxis_title="Spell Popularity (Count)",
    legend_title="Class",
    bargap=0.15,
    height=700,
    width=1000,
)

with st.expander("Most Popular Spells of Levels 0, 1, and 2 per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Spell Example")

st.image(shared.IMAGE_FILES[7], caption="", use_container_width=True)

st.subheader("Context & Insights:")

st.write("""
This **grouped bar chart** highlights the most popular spells for Levels 0, 1, and 2 across the six spellcasting classes. It is the only chart using the smaller dataset, which includes spell lists. Early-level spells matter because they are cast most often across a campaign.

#### Key Observations:
- **Clerics and Healing Dominance:** Spells like *Cure Wounds* and *Spiritual Weapon* dominate at early levels, cementing the Cleric's role as a healer and support class.
- **Wizards and Offensive Power:** Spells like *Fire Bolt* and *Magic Missile* reflect their offensive versatility.
- **Unique Class Themes:** Signature spells like *Eldritch Blast* and *Vicious Mockery* reinforce class identity.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Spell Parsing:** Extracted spell names and levels from `processedSpells`.
- **Filtering by Levels:** Focused on Levels 0, 1, and 2.
- **Top Spells per Class:** Identified the most common spell per class and level.
""")
