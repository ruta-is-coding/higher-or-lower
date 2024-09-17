from art import logo, vs
from game_data import data
from random import choice


def celebrity_details(celebrity):
    """Format celebrity data into a printable format"""
    return f"{celebrity['name']}, {celebrity['description']}, from {celebrity['country']}."


continue_playing = True
score = 0
celebrities = {
    'b': choice(data),
}

while continue_playing:
    # Rearrange the celebrities
    celebrities['a'] = celebrities['b']
    celebrities['b'] = choice(data)

    if celebrities['a'] == celebrities['b']:
        celebrities['b'] = choice(data)

    print(logo)
    # Print their details and the VS logo
    print("Compare A: " + celebrity_details(celebrities['a']))
    print(vs)
    print("Against B: " + celebrity_details(celebrities['b']))

    # Check who has a higher follower count
    highest_count = 0
    celeb_winner = ''

    for key in celebrities:
        follower_count = celebrities[key]['follower_count']
        if follower_count > highest_count:
            highest_count += follower_count
            celeb_winner = key

    # Guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)

    # Continue playing if the guess was right
    if guess == celeb_winner:
        score += 1  # Increment the score
        print(f"You're right! Current score: {score}")  # Give user feedback
    else:
        # Print the final message
        print(f"I'm sorry, you lost :( ! Final score: {score}")
        continue_playing = False
