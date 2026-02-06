import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import base64

# -----------------------------------------------------------
# Website formatting
# -----------------------------------------------------------

st.markdown("""
    <style>
    /* Background for entire app */
    .stApp {
        background-color: #001f3f; /* Midnight Blue */
        color: #ffffff; /* White text */
    }

    /* Custom Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Almendra+SC&display=swap');

    /* Title and Header */
    .stApp h1, .stApp h2 {
        font-family: 'Cinzel', serif;
        color: #5dade2; /* Glacial Blue for main title */
        text-shadow: 2px 2px 5px rgba(173, 216, 230, 0.6); /* Give it that Ice Glow effect. */
    }

    /* Subheaders */
    .stApp h3 {
        font-family: 'Cinzel', serif;
        color: #b3cde0; /* Icy silver */
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.5); /* MORE GLOW */
    }

    /* Paragraphs */
    .stApp p {
        font-family: 'Almendra SC', serif;
        font-size: 18px;
        line-height: 1.5; /* better readability */
        color: #ffffff; /* more white text */
    }

    /* Style for code blocks */
    .stApp code {
        background-color: #102a43; /* Darker Blue */
        color: #a3e4d7; /* Pale Aqua */
        font-family: 'Courier New', monospace;
        padding: 6px 8px;
        border-radius: 4px;
        box-shadow: 0px 0px 8px rgba(163, 228, 215, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# INTRODUCTION
# -----------------------------------------------------------

st.title("The Spellcaster's Compendium: A Data-Driven Look at D&D's Main Magic-Wielders")

st.write("""
Welcome, seeker of arcane knowledge. This archive captures how players build spellcasters in Dungeons & Dragons, where magic comes from study, faith, or pacts.

Even with endless choice, patterns emerge. By examining real player data, we can see how tradition, optimization, and storytelling shape spellcaster creation.

Whether you are crafting your first spellcaster or simply curious, this compendium highlights the trends that define these magical classes.
""")

st.subheader("The Quest for Data: A Research Journey")

st.write("""
Like any great adventure, this story began with a search for knowledge. The main dataset came from Kaggle, built from over 1.2 million D&D Beyond entries. 
To capture richer details, I found a second dataset through Reddit. After cleaning duplicates, it narrowed from 10,000+ entries to about 7,000 usable records.
""") 

st.subheader("The Evolution of the Story: Narrowing the Scope")

st.write("""
Originally, this study aimed to analyze all twelve classes and player geography. The data itself made that scope less useful, so the story narrowed to what it could support.

**Key Challenges:**
""")

st.write("""
1. **The Geography Dilemma:** At first, a geographic breakdown sounded exciting, but the dataset primarily covered only a handful of countries, which 
made for limited insights.  
2. **The Twelve-Class Chaos:** Attempting to visualize all 12 classes quickly turned the data into an unreadable conglomeration of numbers and charts.  
""")

st.write("""
Thus, the focus became the six spellcasting classes: Bard, Cleric, Druid, Sorcerer, Warlock, and Wizard. This kept the story cohesive and enabled deeper categories, 
like spell choice, that reveal what makes each class distinct.
""")

# Image file paths
image_files = [
    "Bard_DS.png",  # Bard
    "Cleric_DS.png",  # Cleric
    "Druid_DS.png",  # Druid
    "Sorcerer_DS.png",  # Sorcerer
    "Warlock_DS.png",  # Warlock
    "Wizard_DS.png",   # Wizard
    "DnD_Races.png",    # Races
    "Magic_Missile.png" # Magic Missile
]

# Display the images in rows
st.header("D&D Spellcasting Classes")

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    st.image(image_files[0], caption="", use_container_width=True)
with col2:
    st.image(image_files[1], caption="", use_container_width=True)
with col3:
    st.image(image_files[2], caption="", use_container_width=True)

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    st.image(image_files[3], caption="", use_container_width=True)
with col5:
    st.image(image_files[4], caption="", use_container_width=True)
with col6:
    st.image(image_files[5], caption="", use_container_width=True)

st.subheader("Unveiling the Magic: Why Data Visualization Matters")

st.write("""
In a game as limitless as D&D, every player has their own take on a Warlock or Wizard. Visualizing the data helps reveal:
""")

st.write("""
- **Patterns in player choices:** Which spellcasters consistently favor specific races and backgrounds?  
- **Thematic contrasts:** How well do players tend to follow the general idea of their class?  
- **Unexpected trends:** Are there any metrics that defy expectations, challenging common assumptions?  
""")

st.write("""
With over a million character entries, these visuals turn raw numbers into clear, accessible insights.  
""")

st.subheader("The Dark Side of the Arcane: Potential Pitfalls")

st.write("""
Even a Wish spell cannot change one truth: data reflects who chose to record it. These datasets offer insight, but carry biases:
""")

st.write("""
- **Paywalled content bias:** Free options may be overrepresented.  
- **Online-only source:** Paper-and-pencil players are largely excluded.  
- **Zero values and outliers:** Removing zeros and capping gold can shift averages.  
""")

st.write("""
These limits do not invalidate the data, but they do shape how we interpret it.
""")

st.write("""
### Preparing the Dataset for Analysis: General Transformations
To prepare the data for visualization, I:
- Removed duplicate entries from the smaller dataset.
- Filtered to six spellcasting classes.
- Counted class totals for direct comparison.
- Applied a custom D&D-inspired color palette.

These steps keep the analysis focused and readable.
""")

# -----------------------------------------------------------
# First FIGURE / Start of ARC 1
# -----------------------------------------------------------

st.header("Arc 1: Foundations of Spellcasting")

st.write("""Before delving into specifics, we first need a broad understanding of spellcasting classes in D&D. Which classes dominate the player base? How does level progression 
impact class choices? These foundational insights set the stage for deeper exploration into spellcaster customization.""")

# Load big dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, compression='zip', usecols=["class_starting"])

# Filter for only spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

# Count number of players per class
class_count = df_filtered["class_starting"].value_counts().reset_index()
class_count.columns = ["Class", "Number of Players"]

# Custom colors
class_colors = {
    "Bard": "#AB6DAC",     # Bard Rogue
    "Cleric": "#91A1B2",   # Cleric Silver
    "Druid": "#7A853B",    # Druid Moss
    "Sorcerer": "#992E2E", # Sorcerer Blood
    "Warlock": "#7B469B",  # Warlock Iris
    "Wizard": "#2A50A1"    # Wizard Cobalt
}

# Create interactive bar chart
fig = px.bar(
    class_count,
    x="Class",
    y="Number of Players",
    # Show count labels on bars
    text="Number of Players",  
    title="Number of Players Per Spellcasting Class",
    labels={"Class": "Character Class", "Number of Players": "Count"},
    color="Class",
    # Apply custom color scheme
    color_discrete_map=class_colors 
)

# Modify layout
fig.update_layout(
    xaxis_title="Spellcasting Class",
    yaxis_title="Number of Players",
    # Rotate x-axis labels to improve readability
    xaxis_tickangle=-45,  
    height=600, width=700
)

# Show chart
with st.expander("Number of Players Per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# First Figure Explanation
# -----------------------------------------------------------

st.subheader("Context & Insight:")

st.write("""
This bar chart shows overall class popularity. Wizards lead, with Clerics close behind, suggesting a strong preference for versatile roles. Druids are slightly less represented, possibly due to their higher learning curve.
""")

st.subheader("Relevant Transformations:")

st.write("""
**Formatting for Visualization:** Aggregated counts were reshaped into a simple two-column table for plotting.
""")

# ---------------------------------------------------------------------------------------------------------------------
# SECOND FIGURE
# ---------------------------------------------------------------------------------------------------------------------

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, compression='zip', usecols=["class_starting", "total_level"])

# Define level bins and create some labels
bins = [1, 5, 10, 15, 20]
labels = ["1-5", "6-10", "11-15", "16-20"]
df["level_range"] = pd.cut(df["total_level"], bins=bins, labels=labels)

# Filter for spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

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
    color_discrete_map=class_colors
)

# Modify layout
fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(
    xaxis_title="Level Range",
    yaxis_title="Percentage of Players",
    # Rotate x-axis labels for better readability
    xaxis_tickangle=-45,  
    height=600, width=1000,
    legend_title="Class"
)

# Show chart
with st.expander("Spellcasting Class Popularity Across Level Ranges"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# SECOND Figure Explanation
# -----------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------
# THIRD FIGURE / Start of ARC 2
# ---------------------------------------------------------------------------------------------------------------------

st.header("Arc 2: Defining the Arcane")

st.write("""Character creation is more than choosing a class; it is crafting an identity. These visuals highlight common races, backgrounds, and subclasses that bring each spellcaster to life.""")

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, usecols=["class_starting", "race"])

# Keep only six spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

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
        fig.add_trace(go.Barpolar(
            r=[count],
            # Position around the circle
            theta=[angle],  
            # Adjust width of the bars
            width=[360 / len(sorted_races) * 0.9],  
            marker_color=class_colors[cls],
            name=f"{cls} - {race}",
            hoverinfo="text",
            text=f"{cls} ({count})",
            # Hide from legend
            showlegend=False  
        ))
        
# Make it so that the legend is only the 6 classes and not the 18 different 
# combinations of class and race
for cls in unique_classes:
    fig.add_trace(go.Barpolar(
        # Invisible bar
        r=[0], theta=[0],  
        marker_color=class_colors[cls],
        # Only the class name appears in the legend
        name=cls,  
        hoverinfo="skip",
    ))

# Modify layout
fig.update_layout(
    title="Top 3 Races for Each Class",
    polar=dict(
        radialaxis=dict(showticklabels=True, tickfont_size=12, color="black"),
        angularaxis=dict(showticklabels=True, tickmode="array", tickvals=list(race_to_angle.values()), ticktext=sorted_races)
    ),
    showlegend=True,
    margin=dict(l=120, r=120, t=80, b=80),
    height=700, width=700
)

# Show chart
with st.expander("Top 3 Races for Each Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# THIRD Figure Explanation
# -----------------------------------------------------------

st.subheader("D&D Races")

st.image(image_files[6], caption="", use_container_width=True)

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

# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 4
# ---------------------------------------------------------------------------------------------------------------------

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, usecols=["class_starting", "background"])

# Keep only six spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

# Count number of each background per class
df_counts = df_filtered.groupby(["class_starting", "background"]).size().reset_index(name="count")

# Rank backgrounds for each class; keep only top 3
df_counts["ranks"] = df_counts.groupby("class_starting")["count"].rank(method="dense", ascending=False)
df_top_backgrounds = df_counts[df_counts["ranks"] <= 3]

# Get unique classes and sorted backgrounds
unique_classes = sorted(df_top_backgrounds["class_starting"].unique())
sorted_backgrounds = sorted(df_top_backgrounds["background"].unique())  

# Map from background to angles (evenly spaced around circle)
background_to_angle = {background: angle for background, angle in zip(sorted_backgrounds, np.linspace(0, 360, len(sorted_backgrounds), endpoint=False))}

# Ensure largest count per background is plotted first
df_sorted = df_top_backgrounds.sort_values(["background", "count"], ascending=[False, True])

# Create figure
fig = go.Figure()

# Loop through each background and add bars for each class
for background in sorted_backgrounds:
    background_data = df_sorted[df_sorted["background"] == background]

    for _, row in background_data.iterrows():
        cls = row["class_starting"]
        angle = background_to_angle[background]
        count = row["count"]

        # Add a radial bar for each class-background pair
        fig.add_trace(go.Barpolar(
            r=[count],
            theta=[angle],  # Position around the circle
            width=[360 / len(sorted_backgrounds) * 0.9],  # Adjust width of the bars
            marker_color=class_colors[cls],
            name=f"{cls} - {background}",
            hoverinfo="text",
            text=f"{cls} ({count})",
            showlegend=False  # Hide from legend
        ))
        
# Make it so that the legend is only the 6 classes and not the 18 different 
# combinations of class and background
for cls in unique_classes:
    fig.add_trace(go.Barpolar(
        r=[0], theta=[0],  
        marker_color=class_colors[cls],
        name=cls,  # Only the class name appears in the legend
        hoverinfo="skip",
    ))

# Modify layout
fig.update_layout(
    title="Top 3 Backgrounds for Each Spellcasting Class",
    polar=dict(
        radialaxis=dict(showticklabels=True, tickfont_size=12, color="black"),
        angularaxis=dict(showticklabels=True, tickmode="array", tickvals=list(background_to_angle.values()), ticktext=sorted_backgrounds)
    ),
    showlegend=True,
    margin=dict(l=120, r=120, t=80, b=80),
    height=700, width=700
)

# Show chart
with st.expander("Top 3 Backgrounds for Each Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# FOURTH Figure Explanation
# -----------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 5
# ---------------------------------------------------------------------------------------------------------------------

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, usecols=["class_starting", "subclass_starting"])

# Filter for six spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

# Count number of each subclass per class
df_counts = df_filtered.groupby(["class_starting", "subclass_starting"]).size().reset_index(name="count")

# Rank subclasses for each class; keep only top 3
df_counts["ranks"] = df_counts.groupby("class_starting")["count"].rank(method="dense", ascending=False)
df_top_subclasses = df_counts[df_counts["ranks"] <= 3]

# Custom color scheme for D&D spellcasting classes
class_colors = {
    "Bard": "#AB6DAC",
    "Cleric": "#91A1B2",
    "Druid": "#7A853B",
    "Sorcerer": "#992E2E",
    "Warlock": "#7B469B",
    "Wizard": "#2A50A1"
}

# Create Sunburst Chart
# Only thing I thought of was the candy, but this is no candy
# After making the radial this was much easier
fig_sunburst = px.sunburst(
    df_top_subclasses,
    path=["class_starting", "subclass_starting"],
    values="count",
    title="Top 3 Subclasses for Each Spellcasting Class",
    color="class_starting",
    color_discrete_map=class_colors
)

# Modify for better readability
fig_sunburst.update_layout(
    width=700,
    height=700,
    font=dict(size=16),
    # Adjust margins
    margin=dict(t=80, l=10, r=10, b=10)  
)

# Show chart
with st.expander("Top 3 Subclasses for Each Spellcasting Class"):
    st.plotly_chart(fig_sunburst, use_container_width=True)
    
# -----------------------------------------------------------
# FIFTH Figure Explanation
# -----------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 6
# ---------------------------------------------------------------------------------------------------------------------

# Load dataset
file_path = "cleaned_data_DnD_smaller.csv"
df = pd.read_csv(file_path)

# Filter for six spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["justClass"].isin(selected_classes)]

# Dictionary to store spell counts per class and level
class_spell_counts = {cls: {0: {}, 1: {}, 2: {}} for cls in selected_classes}

# Extract spells by parsing through spell lists
# Count them based on levels
for _, row in df_filtered.iterrows():
    cls = row["justClass"]
    if pd.notna(row["processedSpells"]):
        # Split using '|' as the spell divider
        spell_list = row["processedSpells"].split("|")  
        for spell in spell_list:
            # Split at asterisk to separate spell name and level
            parts = spell.split("*")  
            if len(parts) == 2:
                # Extract spell name and level
                spell_name, level = parts[0].strip(), parts[1].strip()  
                if level.isdigit():
                    level = int(level)
                    # Only process levels 0, 1, and 2
                    if level in [0, 1, 2]:  
                        class_spell_counts[cls][level][spell_name] = class_spell_counts[cls][level].get(spell_name, 0) + 1

# Find most popular spell per class per level
top_class_spells = []
for cls in selected_classes:
    for level in [0, 1, 2]:
        # Ensure spells exist at this level
        if class_spell_counts[cls][level]:  
            top_spell = max(class_spell_counts[cls][level], key=class_spell_counts[cls][level].get)
            count = class_spell_counts[cls][level][top_spell]
            top_class_spells.append({
                "Class": cls, 
                "Spell Level": f"Level {level}", 
                "Spell": top_spell, 
                "Count": count
            })

# Convert to DataFrame for visualization
df_top_class_spells = pd.DataFrame(top_class_spells)

# Create interactive grouped bar chart using Plotly
fig = px.bar(
    df_top_class_spells, 
    x="Spell Level", 
    y="Count", 
    color="Class", 
    text="Spell",  # Set spell names as hover labels
    barmode="group",
    title="Most Popular Spells of Levels 0, 1, and 2 per Class",
    labels={"Count": "Spell Popularity", "Spell Level": "Spell Level"},
    # Show spell name on hover
    hover_data={"Spell": True, "Class": True, "Count": True}, 
    # Apply custom color scheme 
    color_discrete_map=class_colors  
)

# Improve readability
fig.update_layout(
    xaxis_title="Spell Level",
    yaxis_title="Spell Popularity (Count)",
    legend_title="Class",
    bargap=0.15,  # Adjust bar width
    height=700, width=1000
)

# Show chart
with st.expander("Most Popular Spells of Levels 0, 1, and 2 per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# SIXTH Figure Explanation
# -----------------------------------------------------------

st.subheader("Spell Example")

st.image(image_files[7], caption="", use_container_width=True)

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


# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 7 / Start of ARC 3
# ---------------------------------------------------------------------------------------------------------------------

st.header("Arc 3: Arcane Intricacies")

st.write("""Beyond character creation, how do spellcasters function in play? From gold distribution to notes, these insights reveal what players prioritize and document.""")

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, usecols=["class_starting", "gold"])

# Filter for spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

# Remove extreme values
# Tested this rigorously with a box plot first. Saw very few dots above 350,000
# Tried standard deviation and IQR but both looked weird, so this was the compromise
df_filtered = df_filtered[(df_filtered["gold"] > 0) & (df_filtered["gold"] < 350_000)]

# Directly calculate the average gold per class
df_avg_gold = df_filtered.groupby("class_starting", as_index=False)["gold"].mean()

# Rename column for clarity
df_avg_gold.rename(columns={"gold": "Average Gold"}, inplace=True)

# Bar chart of average gold per class
fig = px.bar(df_avg_gold, x="class_starting", y="Average Gold",
             title="Average Gold per Spellcasting Class",
             labels={"class_starting": "Class", "Average Gold": "Gold (Avg)"},
             color="class_starting",color_discrete_map=class_colors)

# Modify layout
fig.update_layout(
    width=700, 
    height=600,  
    xaxis_title="Character Class",
    yaxis_title="Average Gold",
    title_font_size=18
)

# Show chart
with st.expander("Average Gold per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)
    
# -----------------------------------------------------------
# SEVENTH Figure Explanation
# -----------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 8
# ---------------------------------------------------------------------------------------------------------------------

# Load dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, usecols=["class_starting", "notes_len"])

# Filter for only six spellcasting classes
selected_classes = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
df_filtered = df[df["class_starting"].isin(selected_classes)]

# Remove entries where 'notes_len' is 0
df_filt_nonzero = df_filtered[df_filtered["notes_len"] > 0]

# Calculate average note length per class
avg_note_length_per_class = df_filt_nonzero.groupby("class_starting")["notes_len"].mean().reset_index()

# Create interactive lollipop chart
# Learning I could make a chart of lollipops was amazing
fig = px.scatter(
    avg_note_length_per_class,
    x="class_starting",
    y="notes_len",
    text=avg_note_length_per_class["notes_len"].round(1),
    color="class_starting",
    color_discrete_map=class_colors,
    title="Average Note Length per Spellcasting Class",
    labels={"class_starting": "Class", "notes_len": "Average Note Length"},
)

# Add sticks for lollipop effect
for i, row in avg_note_length_per_class.iterrows():
    fig.add_shape(
        type="line",
        x0=row["class_starting"], x1=row["class_starting"],
        y0=0, y1=row["notes_len"],
        line=dict(color="gray", width=2),
    )

# Modify layout for readability
fig.update_traces(marker=dict(size=15, line=dict(width=2, color="black")), textposition="top center")
fig.update_layout(
    xaxis_title="Class",
    yaxis_title="Average Note Length",
    xaxis_tickangle=-25,
    height=600, width=700,
    showlegend=False
)

# Show chart
with st.expander("Average Note Length per Spellcasting Class"):
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------
# EIGTH Figure Explanation
# -----------------------------------------------------------

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

# -----------------------------------------------------------
# WRITTEN REFLECTION
# -----------------------------------------------------------

st.header("Reflection")

st.subheader("How Did My Design Decisions Work for User Feedback and How Did They Fall Short?")
st.write("""
Feedback was positive on organization, storytelling, and interactivity, especially the radial and sunburst charts. The D&D color palette helped the visuals feel authentic.

The main critique was coverage: more graphs and clearer labels would improve first-glance comprehension.
""")

st.subheader("Failed Attempts at Visualization: How Did I Change Tactics to Improve Outcomes?")
st.write("""
Early attempts to show all 12 classes were cluttered, so I narrowed the focus to six spellcasters. Radial bars required multiple layout tweaks for readability.

Switching to Plotly added interactivity that made exploration easier and more engaging.
""")

st.subheader("Where Might I Revise in Another Round of Iteration?")
st.write("""
If I had another round of iteration, I would:
1. Expand spell analysis beyond the top three, possibly by level or theme.
2. Try alternative formats like heatmaps or network graphs.
3. Tighten labels and tooltips for faster reading.
4. Explore multiclass characters if data allows.
""")

st.subheader("Are There Any Stories My Current Work Occludes, Marginalizes, or Minimizes?")
st.write("""
Yes, there are limits that shape the story:
- **Smaller spell dataset:** Fewer data points limit higher-level spell insights.
- **Non-spellcasting classes omitted:** Fighters, Rogues, and others are absent for clarity.
- **Paywalled content bias:** Free options may be overrepresented.

Future work could expand class coverage, compare free vs paid content, and explore player demographics.
""")

st.subheader("What Did I Like Best About Learning How to Create Data Narratives?")
st.write("""
I enjoyed experimenting with radial and sunburst charts, and aligning visuals with the official D&D palette. Combining interactivity with storytelling was especially rewarding.
""")

st.subheader("References")
st.write("""
AutumnArchfey. (2023, February 20). Dungeons and Dragons Races Lineup [Digital art]. 
    DeviantArt. https://www.deviantart.com/autumnarchfey/art/Dungeons-and-Dragons-Races-Lineup-954300538
   
Bonnin, M. (2022). DnD characters [Data set]. Kaggle. 
    Retrieved from https://www.kaggle.com/datasets/maximebonnin/dnd-characters-test

Booker, B. M. (2021, June 18). Common terms new Dungeons & Dragons players should learn. 
    D&D Beyond. Retrieved from https://www.dndbeyond.com/posts/1026-common-terms-new-dungeons-dragons-players-should 

Herena, E. L. (2022). D&D 5e Spells [Digital art]. ArtStation. Retrieved from https://www.artstation.com/artwork/LeDzkP

Mancarcı, B. O. (2020). dnddata [Data set]. GitHub. Retrieved from https://github.com/oganm/dnddata

Varela, R. (2024, August 20). DND Classes [Pixel art]. Lospec. Retrieved from https://lospec.com/gallery/rpvarela/dnd-classes
""")
