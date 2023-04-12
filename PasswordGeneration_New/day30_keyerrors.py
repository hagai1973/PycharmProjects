facebook_post = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 21, 'Comments': 2, 'Shares': 3},
    {'Comments': 2, 'Shares': 2},
    {'Comments': 2, 'Shares': 1},
    {'Likes': 19, 'Comments': 2}
]

try:
    print(f"item 1 likes: {facebook_post[3]['Likes']}")
except KeyError:
    print(f"item key was not found")

