#!/usr/bin/env python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# challenge 1: pull strings eyes, goggles, and nothing from challenge list
print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

# challenge 2: pull strings eyes, goggles, nothing from trial list
print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")

# challenge 3: pull strings eyes, goggles, and nothing from nightmare list
print(f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")
