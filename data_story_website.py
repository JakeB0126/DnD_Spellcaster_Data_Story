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

st.title("The Spellcaster’s Compendium: A Data-Driven Look at D&D’s Main Magic-Wielders")

st.write("""
Welcome, seeker of arcane knowledge. You stand before a vast collection of records detailing the choices of countless adventurers. This is no ordinary archive; 
it offers a glimpse into the very nature of spellcasters themselves.

These records originate from Dungeons & Dragons (D&D), a roleplaying game where players create characters, embark on adventures, and shape the world through 
their decisions. Among its many classes, spellcasters wield extraordinary power,  drawing magic from divine blessings, arcane study, or otherworldly pacts.

Yet, even in a world of limitless choice, patterns emerge.

While character creation is an art, it is shaped by storytelling, optimization, and personal preference. Across thousands of tables and millions of campaigns, 
the collective imagination of the D&D community begins to take form in trends that extend beyond a single roll of the dice.

This compendium of spellcasters uncovers the trends that define these magical classes. By analyzing real player choices, we reveal how meta, tradition, and 
storytelling shape spellcaster creation across countless campaigns.

Whether you’re crafting your first spellcaster or simply curious about the spellcasting realm of D&D, this exploration of data will unveil the hidden forces 
behind character trends, letting you step into the mind of thousands of players before you. Because in the world of fantasy roleplaying, even the most unique 
characters are shaped by the choices that came before them.
""")

st.subheader("The Quest for Data: A Research Journey")

st.write("""
Like any great adventure, this story started with a search for knowledge. So, like a Wizard sifting through ancient tomes, 
this research required patience and persistence. The main dataset was unearthed through Kaggle, a trove of user-generated data. The user created 
this dataset by extracting over 1.2 million entries of player information from D&D, the official online resource for Dungeons & Dragons.But while Kaggle 
was promising, a dataset with some more unique information was required.  

Through Reddit forums (modern-day taverns filled with countless explorers swapping tales), I encountered a question posed by a user about D&D. After clicking 
through the multitude of links and experiencing many unusable datasets, I finally managed to find one with promise. After removing duplicates through data cleaning, 
it shrank from over 10,000 entries to a more refined 7,000. This was the only 
""") 

st.subheader("The Evolution of the Story: Narrowing the Scope")

st.write("""
Originally, this study aimed to analyze all twelve D&D classes and even explore the geographical distribution of players. However, creating a data story is not a 
linear path but instead a journey with many twists and turns that must stay within the confines of the data.  

**Key Challenges:**
""")

st.write("""
1. **The Geography Dilemma:** At first, a geographic breakdown sounded exciting, but the dataset primarily covered only a handful of countries, which 
made for limited insights.  
2. **The Twelve-Class Chaos:** Attempting to visualize all 12 classes quickly turned the data into an unreadable conglomeration of numbers and charts.  
""")

st.write("""
Thus, a decision was made: focus solely on the six spellcasting classes—Bard, Cleric, Druid, Sorcerer, Warlock, and Wizard. These classes brought forth unique categories, 
such as favorite spells, which gave the data a clear purpose beyond just "who picks what." By limiting the scope, the story became more cohesive, highlighting what 
makes each member of the arcane distinct.
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
In a game as limitless as D&D, every player has their own interpretation of what a Warlock should look like or which spells a Wizard should prepare. Visualizing this data lets us uncover:
""")

st.write("""
- **Patterns in player choices:** Which spellcasters consistently favor specific races and backgrounds?  
- **Thematic contrasts:** How well do players tend to follow the general idea of their class?  
- **Unexpected trends:** Are there any metrics that defy expectations, challenging common assumptions?  
""")

st.write("""
With over a million character entries, these visualizations translate an unimaginable amount of raw numbers into digestible insights. This, in turn, 
makes the vast landscape of player choices more accessible to all.  
""")

st.subheader("The Dark Side of the Arcane: Potential Pitfalls")

st.write("""
Yet, even with a powerful spell like Wish, one cannot alter one fundamental truth: data is only as reliable as its source. While these datasets offer incredible insights, 
they are shaped by the players who chose to record their characters. This introduces potential biases:
""")

st.write("""
- **Certain players could be overrepresented:** Additional content—including more races, subclasses, and spells—is behind a paywall. This skews the 
data toward free options available to all players.  
- **The dataset comes from an online source:** This means it essentially excludes anyone who plays with paper and pencil.  
- **Zero-values may skew results:** Removing players with 0 gold or 0 personal notes might distort actual player trends.  
- **Handling outliers:** Setting a cap on gold (e.g., 350,000) may not have been the best way to manage extreme values.  
""")

st.write("""
These ethical considerations will be explored further in the analysis, but it’s essential to acknowledge the limitations of any dataset before drawing conclusions.
""")

st.write("""
### Preparing the Dataset for Analysis: General Transformations
To ensure the dataset was ready for meaningful visualizations, several transformations and cleaning steps were applied:
- **Duplicate Removal:** Removed duplicate entries from the smaller dataset to ensure each player character record was unique.
- **Filtering for Spellcasting Classes:** Filtered data to focus on six spellcasting classes—Bard, Cleric, Druid, Sorcerer, Warlock, and Wizard.
- **Counting Player Numbers:** The `value_counts()` function was used to calculate the total number of players for each class. This aggregation was necessary to compare class popularity directly.
- **Custom Color Mapping:** A custom color palette, directly inspired by the official D&D character sheet themes was applied to enhance the chart's aesthetic and readability.

These steps allowed the data to reveal clear and compelling insights about how players craft their spellcasters.
""")

# -----------------------------------------------------------
# First FIGURE / Start of ARC 1
# -----------------------------------------------------------

st.header("Arc 1: Foundations of Spellcasting")

st.write("""Before delving into specifics, we first need a broad understanding of spellcasting classes in D&D. Which classes dominate the player base? How does level progression 
impact class choices? These foundational insights set the stage for deeper exploration into spellcaster customization.""")

# Load big dataset
zip_path = "over_one_mil_chars.zip"
df = pd.read_csv(zip_path, compression='zip')

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
This bar chart provides an overview of the popularity of each spellcasting class among D&D players. Wizards emerge as the 
most popular class, closely followed by Clerics, indicating a preference for classes with versatility and strong roles in 
combat and strategy. Druids, while still popular, appear slightly less represented. This could be due to the fact that Druids
are less straightforward than Clerics and Wizards and somewhat unknown to newcomers. 
""")

st.subheader("Relevant Transformations:")

st.write("""
**Formatting Data for Visualization:** The aggregated data was converted into a DataFrame with two columns: "Class" and "Number of Players." This structure was ideal for generating a bar chart.
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
This grouped bar chart illustrates the relative popularity of the six spellcasting classes across different level ranges. By analyzing how player preferences 
change as characters level up, we can see further into the progression of campaigns and class dynamics.   

#### Key Observations:         
- **Lower Levels (1–5):** Wizards and Clerics dominate, likely due to their utility in the early stages of campaigns.
- **Mid-Levels (6–15):** Popularity balances out as most classes maintain steady representation, showcasing the general flexibility and likeability of spellcasters.
- **High Levels (16–20):** Wizards become overwhelmingly popular, reflecting their appeal as late-game powerhouses with unmatched magical potential. Later in the game,
Wizards get access to the greatest number of spells giving them an immensely powerful repertoire. 
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Binning Character Levels:** The `total_level` column was divided into four ranges: 1–5, 6–10, 11–15, and 16–20, allowing for analysis of player preferences across stages of character progression.
- **Grouping by Class and Level Range:** The dataset was grouped by `class_starting` and `level_range` to calculate the total number of players within each class-level range combination.
- **Converting Counts to Percentages:** Raw counts were converted into percentages of the total players within each level range to allow for meaningful comparisons.
""")

# ---------------------------------------------------------------------------------------------------------------------
# THIRD FIGURE / Start of ARC 2
# ---------------------------------------------------------------------------------------------------------------------

st.header("Arc 2: Defining the Arcane")

st.write("""Character creation is more than just choosing a class; it’s about crafting an identity. From racial traits to personal backgrounds, every choice adds layers to a spellcaster's story like an onion. These 
visualizations peel back the layers of the onion to reveal the most common races, backgrounds, and subclasses for each spellcasting class. These choices ultimately help players bring their characters to life.""")

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
This radial bar chart showcases the top three most popular races chosen for each of the six spellcasting classes. In Dungeons & Dragons (D&D), **race** defines a 
character's species and often provides specific traits, such as enhanced abilities, unique powers, or cultural background. Popular races like Humans, Elves, and 
Tieflings dominate the chart, illustrating their overall synergy with spellcasting classes.

#### Key Observations:
- **Wizards and Humans:** Humans are a popular race for Wizards, possibly due to their versatile ability bonuses, making them adaptable for any class.
- **Half-Elves' Charismatic Affinity:** Half-Elves, known in-game for their charismatic boost, align well with spellcasters such as Bards and Sorcerers which use their charisma in order to cast spells.
- **Tieflings and Warlocks:** Tieflings' dark heritage and inherent magical abilities make them a thematic fit for Warlocks who often make "deals with the devil."
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting Races by Class:** The dataset was grouped by `class_starting` and `race` to count the total number of players for each race-class combination.
- **Ranking Top 3 Races:** Races for each class were ranked based on their player counts, and only the top three were retained for clarity.
- **Mapping Race Angles:** Each race was assigned an angle to position it evenly around the radial chart, enabling a clear comparison.
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
This radial bar chart visualizes the top three most popular backgrounds chosen for each spellcasting class. In Dungeons & Dragons (D&D), a **background** represents a character's history, skills, and personal narrative, providing roleplaying opportunities and additional proficiencies. Popular backgrounds such as Sage, Acolyte, and Soldier frequently appear, reflecting their thematic alignment with spellcasting classes.

#### Key Observations:
- **Sage Dominates Wizards:** Sage, representing scholars and researchers, is an unsurprising favorite for Wizards due to their focus on knowledge and arcane studies.
- **Acolytes and Clerics:** Thematically tied to divine service, the Acolyte is a natural match for Clerics as it reinforces their connection to gods and temples.
- **Varied Preferences Among Bards:** Bards display diverse preferences with Entertainer and Folk Hero as frequently selected backgrounds. This highlighting their role as storytellers and performers in D&D.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting Backgrounds by Class:** Grouped data by `class_starting` and `background` to count the total number of players for each background-class combination.
- **Ranking Top 3 Backgrounds:** Limited the dataset to the top three backgrounds for each class, based on player counts.
- **Mapping Background Angles:** Similar to the previous chart, backgrounds were mapped to angles for placement in the radial chart.
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
This **sunburst chart** visualizes the top three most popular subclasses for each spellcasting class in Dungeons & Dragons (D&D). A **subclass** in D&D 
defines a character's specialization within their main class, offering unique abilities and further customization. The chart demonstrates how almost 
every spellcast class a very strong preference for one particular subclass, excluding druids. 
 
#### Key Observations:
- **Wizards and the School of Evocation:** The School of Evocation which focuses on powerful spells like Fireball, stands out as a dominant choice for Wizards. This school is an 
obvious choice for Wizards who yearn for mastery over the art of destruction. 
- **Clerics and Life Domain:** The Life Domain also tends to align with the "idea" of a Cleric as it emphasizes healing and support. Clerics often play the important role of healers 
in any given party, making the Life Domain the clear frontrunner.
- **Warlocks and The Fiend:** The Fiend subclass offers dark and destructive powers that perfectly align with the Warlock's theme of making pacts with evil entities. While all Warlock 
subclasses typically involve a pact, The Fiend represents the standard. 
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Counting Subclasses:** Grouped data by `class_starting` and `subclass_starting` to calculate the total number of players for each subclass-class combination.
- **Ranking Top 3 Subclasses:** Ranked subclasses within each class based on player counts and limited to the top three for clarity.
- **Mapping to Sunburst Path:** Created a hierarchical path (`class_starting` → `subclass_starting`) to structure the sunburst visualization.
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
This **grouped bar chart** highlights the most popular spells for Levels 0, 1, and 2 across the six spellcasting classes in Dungeons & Dragons. This is the only chart that utilizes
the smaller dataset as it contained spell data for each class. A **spell** in D&D represents a magical ability or 
effect that a character can cast during a campaign. By analyzing these spells, we uncover inntruiging insights into how players utilize their lower level spells. At low player levels, the number of spells
available to spellcasters is limited, meaning every spell holds great significance. Even at higher levels, when players can cast more spells, it is just as 
important to have meaningful low-level spells which are casted at a higher frequency. 

#### Key Observations:
- **Clerics and Healing Dominance:** Spells like *Cure Wounds* and *Spiritual Weapon* dominate at early levels, cementing the Cleric's role as a healer and support class.
- **Wizards and Offensive Power:** Spells such as *Fire Bolt* and *Magic Missile* highlight the Wizard’s offensive versatility, making them a staple in many campaigns. Magic Missle in 
particular is invaluable to many Wizards as it is garunteed to hit the target in almost every instance.
- **Unique Class Themes:** Each class’s popular spells reflect its thematic identity, such as *Eldritch Blast* for Warlocks and *Vicious Mockery* for Bards. Expanding upon Eldritch Blast, 
Warlocks are able to bolster this spell later in the game so that it can reach farther, hit harder, and even physically push enemies away.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Spell Parsing:** Extracted spell names and levels from the `processedSpells` column using a delimiter (*|*) and further split the details at an asterisk (*).
- **Filtering by Levels:** Focused on Levels 0, 1, and 2 to simplify the analysis and showcase early-game spellcasting behavior.
- **Top Spells per Class:** Grouped spells by class and level, then identified the most commonly used spell for each class at every level.
""")


# ---------------------------------------------------------------------------------------------------------------------
# FIGURE 7 / Start of ARC 3
# ---------------------------------------------------------------------------------------------------------------------

st.header("Arc 3: Arcane Intricacies")

st.write("""Beyond character creation, how do spellcasters function in gameplay? From gold distribution to spell preferences, these insights reveal the strategic decisions players make when shaping their spellcasting heroes. What resources do they prioritize? How much do they document 
their journeys? Let’s take a closer look.""")

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
This bar chart visualizes the **average amount of gold** possessed by characters in each of the six spellcasting classes in Dungeons & Dragons. 
In the context of D&D, **gold** represents a character’s wealth, used to purchase equipment, magical items, or services. The distribution of gold provides 
insight into how players prioritize resources for their characters.

#### Key Observations:
- **Wizards** have the highest average gold, possibly reflecting their need to purchase expensive spell components or scrolls. In order to copy down new spells 
into their book, they need gold, something that is much unlike the other spellcasting classes.
- **Sorcerers and Warlocks** follow closely, showcasing their affinity for acquiring magical items or services to enhance their innate powers.
- **Bards and Druids** have comparatively lower averages, possibly due to their reliance on versatility and innate class abilities rather than purchased items. Druids in particular
are known to commune with nature rather than get involved with the monetary value of things.
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Filtering Extreme Values:** Removed outliers by excluding characters with gold amounts exceeding 350,000, based on prior box plot analysis.
- **Excluding Zero Values:** Removed entries with 0 gold to ensure meaningful average calculations, as characters with no recorded gold could distort insights.
- **Calculating Averages:** Grouped by `class_starting` and calculated the mean gold for each class to highlight resource trends across spellcasters.
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
This lollipop chart visualizes the **average length of personal notes** written by players for each of the six spellcasting classes. 
In the context of D&D Beyond, where this data was pulled from, **notes** often represent detailed character backstories, motivations, or campaign-relevant information 
that players use to deepen their roleplaying experience.

#### Key Observations:
- **Warlocks** have the longest average note length, possibly due to the intricate lore tied to their otherworldly patrons and the thematic emphasis on story-driven gameplay.
- **Bards** follow closely, reflecting their narrative-heavy class identity, often involving performances and elaborate backstories.
- **Clerics and Wizards** have relatively shorter notes, suggesting a more mechanics-focused approach compared to narrative emphasis. Something that stuck out
to me about Wizards is the fact they are generally seen as the scribes of D&D. But, this data shows that the players behind
the Wizards typically right less than players of other classes. 
""")

st.subheader("Relevant Transformations:")

st.write("""
- **Excluding Zero-Length Notes:** Removed entries where `notes_len` was 0 to focus on meaningful note contributions, as characters with no notes could distort averages.
- **Calculating Averages:** Grouped data by `class_starting` and computed the mean note length for each class to provide a clear comparison.
- **Lollipop Chart Construction:** Used a scatter plot combined with vertical lines to create a lollipop effect, enhancing visual clarity and aesthetic appeal.
""")

# -----------------------------------------------------------
# WRITTEN REFLECTION
# -----------------------------------------------------------

st.header("Reflection")

st.subheader("How Did My Design Decisions Work for User Feedback and How Did They Fall Short?")
st.write("""
My design decisions were well-received by my test audience, primarily due to the clear organization of the visuals and the storytelling approach that made the data engaging and accessible. 
Classmates appreciated the interactive nature of the graphs, especially the radial bar charts and sunburst charts, which offered unique perspectives on the data. Matching the colors to the 
official D&D palette added an extra layer of immersion, making the visuals feel more thematic and aligned with the source material.

However, one area of feedback I noted was the need for **additional graphs** to explore the dataset more comprehensively. While the visuals I presented were informative, they did not exhaust 
the dataset's potential. Additionally, I personally recognized a need to improve the **labels** for clarity and precision. Some axes, titles, and legends could have been more descriptive to 
ensure users fully understood what was being presented at first glance.
""")

st.subheader("Failed Attempts at Visualization: How Did I Change Tactics to Improve Outcomes?")
st.write("""
One of the biggest changes I made during the project was limiting the number of variables being visualized. Initially, I aimed to include all 12 classes in D&D, but this led to chaotic and 
unreadable graphs. By narrowing the focus to the six spellcasting classes, I was able to create cleaner and more meaningful visualizations that effectively highlighted trends.

Another significant challenge was creating **readable radial bar charts.** I went through several iterations before arriving at the final design, experimenting with angle spacing, bar widths, 
and color schemes to strike the right balance of readability and aesthetic appeal.

Switching to **Plotly** for graph creation was also a pivotal decision. Unlike static graphs, Plotly enabled interactivity, allowing users to explore data more dynamically by hovering over 
elements for detailed insights. This interactivity enhanced the user experience and made the data more engaging.
""")

st.subheader("Where Might I Revise in Another Round of Iteration?")
st.write("""
If I had another round of iteration, I would:
1. **Expand the Spell Analysis:** Rather than focusing solely on the top three spells for each class, I would include more spells to provide a deeper look into player preferences. 
   This could involve analyzing spell usage by level or grouping spells by thematic categories.
2. **Explore Alternative Graph Formats:** While the current visuals are effective, experimenting with less conventional formats, such as heatmaps or network graphs, could add variety and 
   uncover new insights.
3. **Refine Labeling Further:** Even though the current labels are functional, additional iterations could make them even clearer. For instance, providing concise tooltips or explanations 
   within the charts might make the visuals even more user-friendly.
4. **Investigate Multi-Class Characters:** Many D&D players experiment with multi-classing, which my dataset largely omits. Adding this dimension could significantly enrich the data story.
""")

st.subheader("Are There Any Stories My Current Work Occludes, Marginalizes, or Minimizes?")
st.write("""
Yes, there are some limitations in the current work:
- **Spell Analysis Limitations:** Since the spell data came from the smaller dataset, the analysis was constrained by fewer data points. This limits the depth of insights into higher-level 
  spells and rarer choices. A larger dataset would allow for a more comprehensive view.
- **Marginalization of Non-Spellcasting Classes:** By focusing on the six spellcasting classes, the story excludes valuable data about the remaining six non-spellcasting classes, such as 
  Fighters and Rogues. While this was necessary for clarity, it minimizes their role in the broader D&D landscape.
- **Economic and Social Contexts:** The analysis could explore how player access to supplemental D&D materials (e.g., paywalled expansions) skews the dataset, potentially underrepresenting 
  certain player demographics. Including this context might offer a fuller understanding of the biases in the dataset.

An alternative direction for this work could involve expanding the scope to include all classes, analyzing paywalled versus free content, or delving deeper into how player demographics 
influence character creation.
""")

st.subheader("What Did I Like Best About Learning How to Create Data Narratives?")
st.write("""
One of my favorite aspects of this project was discovering and experimenting with different visualization techniques, such as **radial bar charts** and **sunburst charts.** These formats were 
not only visually striking but also provided unique ways to explore relationships in the data.

I particularly enjoyed matching the visuals to the **official D&D color palette**, which added thematic coherence and made the project feel more authentic. It was satisfying to bring the 
essence of D&D into the data story through aesthetics and design choices.

Lastly, learning how to effectively combine interactivity with storytelling was a rewarding challenge. It demonstrated how data can be transformed from abstract numbers into a compelling 
narrative that engages and informs the audience.
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
