#!/usr/bin/env python3
from flask import Flask
from flask import render_template

# This api will list information on characters in your next canon D&D party, are you prepared?

app = Flask(__name__)

# Holds all the information on our Heroes
data = [
        {
            'character': [
                {
                    'name': 'JSON the Returned',
                    'image': 'https://media.makeameme.org/created/brace-yourself-json.jpg'
                },
            ],
            
            'inventory': ['Cloak Of Billowing', 'Poor Plot Armor', 'Magic Sword: "Ceiling Biter"'],
            'stats': {
                'STR': 17,
                'DEX': 12,
                'CON': 16,
                'INT': 8,
                'WIS': 10,
                'CHA': 18,
                'INIT': +1,
                'HP': 13,
                'AC': 18
            }
        },

        {
            # Barbarian with a snake skin jacket
            'character': [
                {
                    'name': 'Nicolas Rage, the Barbarian',
                    'image': 'https://a2.tvspielfilm.de/imedia/7399/9787399,a+4ShU3udNL43bdPOveXZhCpl79mjRpQTLOBB+zNkLbGkIrwf7LPvuDNumM92sebbZxEddBmysvXhMyp4E2r6Q==.jpg'
                },
            ],

            'inventory': ['Weapon Of Warning (Sentient)', 'Bag Of Beans', ],
            'stats': {
                'STR': 18,
                'DEX': 13,
                'CON': 16,
                'INT': 10,
                'WIS': 10,
                'CHA': 12,
                'INIT': +1,
                'HP': 13,
                'AC': 18
            }
        },

        {
            'character': [
                {
                    'name': 'Gurgglenoise the Murloc, the Bard',
                    'image': 'https://p.kindpng.com/picc/s/157-1570248_latestcb-20141215223152-jar-jar-binks-transparent-hd-png.png'
                },
            ],
                    
            'inventory': ['Cheese', 'Cursed Luckstone', 'Big Red Button'],
            'stats': {
                'STR': 10,
                'DEX': 20,
                'CON': 20,
                'INT': 8,
                'WIS': 12,
                'CHA': 5,
                'INIT': +2,
                'HP': 11,
                'AC': 18
            }
        },

        {
            'character': 
            [
                    {
                        'name': 'Kerplunk Noodlefeet, the Wizard',
                        'image': 'https://media.stack.com/stack-content/uploads/2016/07/12010934/Leg-Day-STACK-.jpg'
                    },
            ],

            'inventory': ['Wand Of Smiles', 'Dust Of Sneezing', 'Dust Of Eczema' ],
            'stats': {
                'STR': 9,
                'DEX': 17,
                'CON': 15,
                'INT': 19,
                'WIS': 12,
                'CHA': 6,
                'INIT': +3,
                'HP': 8,
                'AC': 13
            }
        },

        {
            'character': [
                {
                    'name': 'Nibbles Tibbles McGibbles, the Artificer',
                    'image': 'https://preview.redd.it/o7t2v6ttfpb81.png?width=960&crop=smart&auto=webp&s=41e3ed206e1a05b7a546da12d459dbbc95ca908d'
                }
            ],

            'inventory': ['Unusually Wise Hermit Crab', 'Beef', 'Cheese'],
            'stats': {
                'STR': 16,
                'DEX': 14,
                'CON': 16,
                'INT': 11,
                'WIS': 19,
                'CHA': 16,
                'INIT': +2,
                'HP': 11,
                'AC': 18
            }
        }
    ]


# This route displays all the data in the browser
@app.route("/")
def name():
    return data

# This is the route to view one of the 5 party members for your next non-cannon D&D session
# For example: http://127.0.0.1:2224/0 will show the first character in the browser
@app.route("/<int:name>")
def characters(name):
    character_screen = render_template("characters.html", character_info = data[name]['character'], character_stats = data[name]['stats'], inventory = data[name]['inventory'])
    return character_screen

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)