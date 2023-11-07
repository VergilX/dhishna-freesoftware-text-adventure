"""
Starts the game

Author: @AbhinandDManoj
"""

def main():
    # id set to -1 when game ends
    id = 0

    # Set terminal color theme
    

    # Game loop
    try:
        while (id != -1):
            id = generate_story(id)
    except KeyboardInterrupt:
        # Do you want to exit or not
        pass
    except Exception:
        # Modify this to read the error contained in exception
        print("Story ID not found")

if __name__ == "__main__":
    main()
