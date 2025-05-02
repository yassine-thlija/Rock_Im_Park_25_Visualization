from pyvis.network import Network
import networkx as nx
from datetime import datetime


#####################################
############# Functions #############
#####################################

# Create the graph
G = nx.Graph()

def add_day_data(day_name, date_str, headliners, supporting_acts):
    date_obj = datetime.strptime(date_str, "%B %d")
    formatted_date = date_obj.strftime("%a %b %d")
    day_node = f"{day_name}\n({formatted_date})"
    
    G.add_node(day_node, size=25, color='#ff6b6b', title=day_node, group='day')
    
    for band, genres in headliners:
        add_band(band, genres, day_node, is_headliner=True)
    
    for genre, bands in supporting_acts.items():
        G.add_node(genre, size=15, color='#74b9ff', title=genre, group='genre')
        G.add_edge(day_node, genre)
        
        for band_info in bands:
            if isinstance(band_info, tuple):
                band, genres = band_info
            else:
                band, genres = band_info, [genre]
            add_band(band, genres, day_node, is_headliner=False)

def add_band(band_name, genres, day_node, is_headliner):
    color = '#feca57' if is_headliner else '#1dd1a1'
    size = 20 if is_headliner else 15
    G.add_node(band_name, size=size, color=color, title=f"{band_name}\nGenres: {', '.join(genres)}", group='band')
    G.add_edge(day_node, band_name)
    
    for genre in genres:
        if genre not in G:
            G.add_node(genre, size=15, color='#74b9ff', title=genre, group='genre')
        G.add_edge(band_name, genre)

#####################################
######### Rock im Park data #########
#####################################

# Friday data (Rock im Park)
friday_headliners = [
    ("Slipknot", ["Nu Metal", "Alternative Metal", "Heavy Metal"]),
    ("Rise Against", ["Melodic Hardcore", "Punk Rock", "Alternative Rock"]),
    ("Kontra K", ["German Rap", "Hip-Hop", "Gangsta Rap"])
]

friday_supporting = {
    "Metal": [
        ("Bullet For My Valentine", ["Metalcore", "Heavy Metal", "Hard Rock"]),
        ("Heaven Shall Burn", ["Melodic Death Metal", "Metalcore"]),
        ("In Flames", ["Melodic Death Metal", "Alternative Metal"]),
        ("Spiritbox", ["Progressive Metalcore", "Alternative Metal"]),
        ("Defects", ["Metalcore", "Progressive Metal"]),
        ("Imminence", ["Metalcore", "Post-Hardcore"]),
        ("Kittie", ["Nu Metal", "Alternative Metal"]),
        ("Northlane", ["Progressive Metalcore", "Djent"]),
        ("Nothing More", ["Alternative Metal", "Hard Rock"]),
        ("Skillet", ["Christian Rock", "Alternative Metal", "Hard Rock"])
    ],
    "Hard Rock": [
        ("Airbourne", ["Hard Rock", "Heavy Metal", "Blues Rock"]),
        ("Future Palace", ["Post-Hardcore", "Alternative Rock"]),
        ("Holy Wars", ["Alternative Rock", "Post-Hardcore"]),
        ("Smash Into Pieces", ["Alternative Rock", "Electronic Rock"])
    ],
    "Punk/Rock": [
        ("SDP", ["German Pop Rock", "Indie Rock"]),
        ("Me First and the Gimme Gimmes", ["Punk Rock", "Cover Band"]),
        ("Millencolin", ["Skate Punk", "Melodic Hardcore"]),
        ("Turbostaat", ["Punk Rock", "Garage Rock"]),
        ("Zebrahead", ["Punk Rock", "Rapcore", "Alternative Rock"]),
        ("Grade 2", ["Street Punk", "Oi!"]),
        ("Kris Barras Band", ["Blues Rock", "Southern Rock"])
    ],
    "Alternative/Post-Hardcore": [
        ("Touché Amoré", ["Post-Hardcore", "Emo"]),
        ("Seven Hours After Violet", ["Post-Rock", "Alternative Rock"]),
        ("Spiritual Cramp", ["Post-Punk", "Garage Punk"]),
        ("Still Talk", ["Alternative Rock", "Indie Rock"]),
        ("Superheaven", ["Grunge Revival", "Alternative Rock"]),
        ("Teen Mortgage", ["Noise Rock", "Post-Hardcore"]),
        ("Trophy Eyes", ["Pop Punk", "Post-Hardcore"])
    ],
    "Other": [
        ("Evil Jared x Krogi", ["Alternative Hip-Hop", "Experimental"]),
        ("SiM", ["Reggae Punk", "Hardcore Punk"])
    ]
}

# Saturday data (Rock im Park)
saturday_headliners = [
    ("Korn", ["Nu Metal", "Alternative Metal", "Industrial Metal"]),
    ("Falling in Reverse", ["Post-Hardcore", "Metalcore", "Rap Rock"]),
    ("Sleep Token", ["Progressive Metal", "Alternative Metal", "Ambient"])
]

saturday_supporting = {
    "Metal": [
        ("Lorna Shore", ["Deathcore", "Symphonic Metal"]),
        ("Powerwolf", ["Power Metal", "Heavy Metal"]),
        ("Fit For An Autopsy", ["Deathcore", "Progressive Metal"]),
        ("Jinjer", ["Progressive Metalcore", "Groove Metal"]),
        ("Polaris", ["Metalcore", "Melodic Hardcore"]),
        ("Stray From The Path", ["Hardcore Punk", "Rap Metal"]),
        ("The Ghost Inside", ["Melodic Hardcore", "Metalcore"]),
        ("Whitechapel", ["Deathcore", "Technical Death Metal"]),
        ("Thrown", ["Metalcore", "Nu Metalcore"]),
        ("I See Stars", ["Electronicore", "Post-Hardcore"])
    ],
    "Punk/Hardcore": [
        ("Beatsteaks", ["Punk Rock", "Alternative Rock"]),
        ("IDLES", ["Post-Punk", "Art Punk"]),
        ("Terror", ["Hardcore Punk", "Youth Crew"]),
        ("ZSK", ["Punk Rock", "German Punk"]),
        ("Drug Church", ["Post-Hardcore", "Alternative Rock"]),
        ("Pain of Truth", ["Hardcore", "Beatdown Hardcore"])
    ],
    "Rock/Alternative": [
        ("The Warning", ["Hard Rock", "Alternative Rock"]),
        ("Dead Poet Society", ["Alternative Rock", "Art Rock"]),
        ("Deafheaven", ["Blackgaze", "Post-Metal"]),
        ("Deine Cousine", ["Indie Rock", "German Pop"]),
        ("Brutalismus 3000", ["Techno Punk", "Industrial"])
    ],
    "Other": [
        ("AViVA", ["Dark Pop", "Alternative Rock"]),
        ("Amira Elfeky", ["Indie Pop", "R&B"]),
        ("Jerry Cantrell", ["Grunge", "Hard Rock"]),
        ("Leftovers", ["Hardcore", "Punk"]),
        ("Massendefekt", ["German Rap", "Alternative Hip-Hop"]),
        ("The Red Flags", ["Indie Rock", "Garage Rock"]),
        ("VOWWS", ["Darkwave", "Post-Punk"]),
        ("Zetra", ["Gothic Rock", "Post-Punk"])
    ]
}

# Sunday data (Rock im Park)
sunday_headliners = [
    ("Bring Me The Horizon", ["Metalcore", "Alternative Rock", "Electronic Rock"]),
    ("The Prodigy", ["Big Beat", "Electronic Rock", "Rave"]),
    ("K.I.Z", ["German Hip-Hop", "Satirical Rap", "Comedy Hip-Hop"])
]

sunday_supporting = {
    "Rock/Alternative": [
        ("A Day to Remember", ["Pop Punk", "Metalcore"]),
        ("Biffy Clyro", ["Alternative Rock", "Post-Hardcore"]),
        ("Weezer", ["Alternative Rock", "Power Pop"]),
        ("Frank Turner & The Sleeping Souls", ["Folk Punk", "Alternative Rock"]),
        ("Myles Kennedy", ["Hard Rock", "Blues Rock"]),
        ("Olli Schulz & Band", ["German Pop", "Singer-Songwriter"]),
        ("Tocotronic", ["Indie Rock", "German Rock"])
    ],
    "Punk/Hardcore": [
        ("Feine Sahne Fischfilet", ["Punk Rock", "German Punk"]),
        ("Boston Manor", ["Pop Punk", "Post-Hardcore"]),
        ("Soft Play", ["Hardcore Punk", "Noise Rock"]),
        ("FJØRT", ["Post-Hardcore", "Screamo"]),
        ("Nasty", ["Hardcore", "Beatdown Hardcore"])
    ],
    "Metal/Electronic": [
        ("Electric Callboy DJ Set", ["Electronicore", "Dance Metal"]),
        ("Frog Leap", ["Metal Covers", "Comedy Metal"]),
        ("House of Protection", ["Electronic Rock", "Industrial"]),
        ("Static Dress", ["Post-Hardcore", "Screamo"])
    ],
    "Indie/Other": [
        ("Adam Angst", ["German Pop", "Singer-Songwriter"]),
        ("Creeper", ["Horror Punk", "Gothic Rock"]),
        ("Destroy Boys", ["Punk Rock", "Garage Punk"]),
        ("Die Nerven", ["Noise Rock", "Post-Punk"]),
        ("Drangsal", ["Indie Pop", "German Rock"]),
        ("Mia Morgan", ["German Pop", "Singer-Songwriter"]),
        ("Poppy", ["Nu Metal", "Bubblegum Pop"]),
        ("Christin Nichols", ["Indie Pop", "Alternative"]),
        ("Fleshwater", ["Shoegaze", "Alternative Metal"]),
        ("LØLØ", ["Pop Punk", "Alternative Pop"]),
        ("Survive Said the Prophet", ["J-Rock", "Post-Hardcore"]),
        ("Tulpe", ["Indie Pop", "German Pop"]),
        ("Unpeople", ["Alternative Rock", "Post-Punk"])
    ]
}

# Add data to the graph
add_day_data("Rock im Park Friday", "June 6", friday_headliners, friday_supporting)
add_day_data("Rock im Park Saturday", "June 7", saturday_headliners, saturday_supporting)
add_day_data("Rock im Park Sunday", "June 8", sunday_headliners, sunday_supporting)

#####################################
######### Network Creation ##########
#####################################

# Create the PyVis network
net = Network(
    height='800px',
    width='100%',
    bgcolor='#222222',
    font_color='white',
    select_menu=True,
    filter_menu=True,
    cdn_resources='in_line'
)

# Set the physics options directly (remove the show_buttons call)
net.options = {
    "nodes": {
        "borderWidth": 1,
        "borderWidthSelected": 2,
        "opacity": 1,
        "font": {
            "size": 14,
            "face": "arial",
            "strokeWidth": 0
        },
        "shadow": {
            "enabled": True,
            "color": "rgba(0,0,0,0.3)",
            "size": 10,
            "x": 5,
            "y": 5
        }
    },
    "edges": {
        "color": {
            "inherit": True
        },
        "smooth": {
            "enabled": True,
            "type": "continuous"
        },
        "width": 0.8,
        "selectionWidth": 1.5
    },
    "physics": {
        "forceAtlas2Based": {
            "gravitationalConstant": -50,
            "centralGravity": 0.01,
            "springLength": 200,
            "springConstant": 0.08,
            "damping": 0.4
        },
        "minVelocity": 0.75,
        "solver": "forceAtlas2Based",
        "timestep": 0.5,
        "stabilization": {
            "enabled": True,
            "iterations": 1000,
            "updateInterval": 25
        }
    },
    "interaction": {
        "hover": True,
        "multiselect": True,
        "navigationButtons": True,
        "tooltipDelay": 200
    }
}

# Add nodes and edges to the PyVis network
for node in G.nodes:
    net.add_node(
        node,
        label=node.split('\n')[0],
        title=G.nodes[node].get('title', node),
        color=G.nodes[node].get('color', '#666666'),
        size=G.nodes[node].get('size', 10),
        group=G.nodes[node].get('group', 'other')
    )

for edge in G.edges:
    net.add_edge(edge[0], edge[1])

#####################################
########### Visualization ###########
#####################################

# Save the network
net.show('rock_im_park_pyvis.html', notebook=False)
print("Graph saved to rock_im_park_pyvis.html")