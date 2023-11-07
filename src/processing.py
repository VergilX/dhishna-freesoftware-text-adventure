"""
Generates story from database text file
"""
import sys

STORY_SOURCE_DIRECTORY = "../story/"
SAVE_FILE = f"{STORY_SOURCE_DIRECTORY}/save.txt"

def get_story(file, id):
    """
    Read story file and get content of story

    Returns True if story is found else False
    """

    DELIMITER = "`"

    with open(file, "r") as f:
        # Checking for story ID
        story_found = False
        while not story_found:
            current_story_id = int(f.readline().split("=")[1])

            if current_story_id != id:
                # Skipping to next story using delimiter
                for line in f:
                    if line == DELIMITER:
                        continue
                else:
                    return story_found

            # If story is found
            story_found = True
            story_type = int(f.readline().split("=")[1])

            if story_type == 1:
                data = {}
                for line in f:
                    key, value = line.split("=")
                    data[key] = value.rstrip()

                generate_text_story(data)

        return story_found

def generate_minigame():
    pass

def generate_map():
    pass

def generate_text_story(data):
    print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 processing.py <story_id>")
        sys.exit(0)
    else:
        id = int(sys.argv[1])
        file = STORY_SOURCE_DIRECTORY + "story.txt"
        if not get_story(file, id):
            print("Story not found")
