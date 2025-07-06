# # CodeQuest: The Island of Logic (Text-Based Prototype)
#
# import random
#
# # Player data
# player = {
#     "name": "",
#     "position": [0, 0],
#     "inventory": []
# }
#
# # Level data
# levels = [
#     {
#         "name": "The Jungle Path",
#         "goal": "reach the treasure",
#         "obstacles": [(2, 2), (3, 3)],
#         "goal_position": (4, 4),
#         "description": "You are in a dense jungle. Find the path to reach the treasure chest!",
#         "commands": ["move", "turn"]
#     },
#     {
#         "name": "Quicksand Field",
#         "goal": "cross the field",
#         "obstacles": [(1, 1), (2, 2), (3, 1)],
#         "goal_position": (4, 0),
#         "description": "You're crossing a dangerous quicksand field. Watch your steps carefully!",
#         "commands": ["move", "turn", "if", "else"]
#     }
# ]
#
#
# # Define functions for gameplay mechanics
#
# def display_instructions(level):
#     print(f"\nLevel: {level['name']}")
#     print(level['description'])
#     print("Goal:", level['goal'])
#     print("Available Commands:", ", ".join(level['commands']))
#     print("Obstacles at positions:", level['obstacles'])
#     print("Goal position:", level['goal_position'], "\n")
#
#
# def move_player(player, direction):
#     if direction == "up":
#         player["position"][1] += 1
#     elif direction == "down":
#         player["position"][1] -= 1
#     elif direction == "left":
#         player["position"][0] -= 1
#     elif direction == "right":
#         player["position"][0] += 1
#
#
# def is_obstacle(position, level):
#     return tuple(position) in level["obstacles"]
#
#
# def reached_goal(position, level):
#     return tuple(position) == level["goal_position"]
#
#
# def play_level(level):
#     display_instructions(level)
#
#     while True:
#         print(f"Current position: {player['position']}")
#         command = input("Enter command (move <direction>/check): ").strip().lower()
#
#         if command.startswith("move"):
#             _, direction = command.split()
#             move_player(player, direction)
#
#             if is_obstacle(player["position"], level):
#                 print("Oops! You hit an obstacle. Try a different path.")
#                 move_player(player, opposite_direction(direction))  # Move back to the previous position
#             elif reached_goal(player["position"], level):
#                 print("Congratulations! You've reached the goal!")
#                 break
#             else:
#                 print("Moved", direction)
#
#         elif command == "check":
#             print("Checking surroundings...")
#             if is_obstacle(player["position"], level):
#                 print("There's an obstacle here!")
#             else:
#                 print("The path is clear.")
#
#         else:
#             print("Invalid command! Try again.")
#
#
# def opposite_direction(direction):
#     return {
#         "up": "down",
#         "down": "up",
#         "left": "right",
#         "right": "left"
#     }[direction]
#
#
# # Start the game
# print("Welcome to CodeQuest: The Island of Logic!")
# player["name"] = input("Enter your character's name: ")
#
# for level in levels:
#     print(f"\nStarting level: {level['name']}...")
#     player["position"] = [0, 0]  # Reset position at the beginning of each level
#     play_level(level)
#
# print("\nCongratulations, you've completed CodeQuest: The Island of Logic!")


import tkinter as tk
from tkinter import messagebox

# Initialize the main game window
root = tk.Tk()
root.title("CodeQuest: The Island of Logic")
root.geometry("400x500")

# Player data and level information
player = {"position": [0, 0], "name": ""}
levels = [
    {
        "name": "The Jungle Path",
        "goal": "Reach the treasure",
        "obstacles": [(1, 2), (2, 2)],
        "goal_position": (3, 3),
        "description": "Navigate through the jungle to reach the treasure chest!",
    }
]

# Set up the canvas grid and player position
grid_size = 5
tile_size = 60

canvas = tk.Canvas(root, width=grid_size * tile_size, height=grid_size * tile_size, bg="lightgreen")
canvas.pack(pady=10)


# Draw the initial grid and elements
def draw_grid():
    canvas.delete("all")
    for i in range(grid_size):
        for j in range(grid_size):
            x1, y1 = i * tile_size, j * tile_size
            x2, y2 = x1 + tile_size, y1 + tile_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="gray", fill="white")

    # Place obstacles
    for obstacle in levels[0]["obstacles"]:
        x, y = obstacle
        canvas.create_rectangle(x * tile_size, y * tile_size,
                                (x + 1) * tile_size, (y + 1) * tile_size,
                                fill="darkred")

    # Place goal
    gx, gy = levels[0]["goal_position"]
    canvas.create_rectangle(gx * tile_size, gy * tile_size,
                            (gx + 1) * tile_size, (gy + 1) * tile_size,
                            fill="gold")

    # Place player
    px, py = player["position"]
    canvas.create_oval(px * tile_size + 10, py * tile_size + 10,
                       (px + 1) * tile_size - 10, (py + 1) * tile_size - 10,
                       fill="blue", outline="black")


# Check if player has reached the goal or hit an obstacle
def check_position():
    if tuple(player["position"]) in levels[0]["obstacles"]:
        messagebox.showinfo("Oops!", "You hit an obstacle! Try a different direction.")
        reset_position()
    elif tuple(player["position"]) == levels[0]["goal_position"]:
        messagebox.showinfo("Congratulations!", "You've reached the goal!")
        next_level()


# Reset player position if they hit an obstacle
def reset_position():
    player["position"] = [0, 0]
    draw_grid()


# Move the player based on direction
def move(direction):
    x, y = player["position"]
    if direction == "up" and y > 0:
        player["position"][1] -= 1
    elif direction == "down" and y < grid_size - 1:
        player["position"][1] += 1
    elif direction == "left" and x > 0:
        player["position"][0] -= 1
    elif direction == "right" and x < grid_size - 1:
        player["position"][0] += 1

    draw_grid()
    check_position()


# Load the next level (future levels can be added to this function)
def next_level():
    messagebox.showinfo("Level Complete!", "You've unlocked the next level!")
    reset_position()  # Reset for the next level


# Game Controls (buttons for movement)
control_frame = tk.Frame(root)
control_frame.pack()

tk.Label(root, text=levels[0]["description"], font=("Arial", 12), wraplength=300).pack()

# Define movement buttons and add color for visual appeal
move_up_button = tk.Button(control_frame, text="Up", command=lambda: move("up"), bg="lightblue", width=8, height=2)
move_up_button.grid(row=0, column=1)

move_left_button = tk.Button(control_frame, text="Left", command=lambda: move("left"), bg="lightblue", width=8,
                             height=2)
move_left_button.grid(row=1, column=0)

move_right_button = tk.Button(control_frame, text="Right", command=lambda: move("right"), bg="lightblue", width=8,
                              height=2)
move_right_button.grid(row=1, column=2)

move_down_button = tk.Button(control_frame, text="Down", command=lambda: move("down"), bg="lightblue", width=8,
                             height=2)
move_down_button.grid(row=2, column=1)


# Initial instructions
def start_game():
    player["name"] = player_name.get()
    if player["name"]:
        messagebox.showinfo("Welcome!", f"Good luck, {player['name']}! Let's start the adventure!")
        draw_grid()
    else:
        messagebox.showwarning("Name Required", "Please enter your character's name to start.")


# Entry for player name and start button
player_name_frame = tk.Frame(root)
player_name_frame.pack(pady=10)

tk.Label(player_name_frame, text="Enter your name: ").pack(side=tk.LEFT)
player_name = tk.Entry(player_name_frame)
player_name.pack(side=tk.LEFT)

start_button = tk.Button(root, text="Start Game", command=start_game, bg="green", fg="white", width=15, height=2)
start_button.pack(pady=10)

# Initialize grid
draw_grid()

root.mainloop()

