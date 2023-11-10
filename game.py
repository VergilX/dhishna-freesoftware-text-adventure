"""
Starts the game

Author: @AbhinandDManoj
"""
from src.processing import generate_story

STORY_SOURCE_DIRECTORY = "story/"
STORY_FILE = "story.txt"

def main():
    # id set to -1 when game ends
    id = 1

    # Set terminal color theme


    # Game loop
    try:
        while (id != -1):
            file = STORY_SOURCE_DIRECTORY + STORY_FILE
            id = generate_story(file, id)
    except KeyboardInterrupt:
        # Do you want to exit or not
        pass
    """
    except Exception as e:
        print(f"Error: {e}")
        """

if __name__ == "__main__":
    main()
