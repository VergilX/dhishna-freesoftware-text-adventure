"""
Generates story from database text file
"""
import ast
import sys

STORY_SOURCE_DIRECTORY = "../story/"
SAVE_FILE = f"{STORY_SOURCE_DIRECTORY}/save.txt"

def generate_story(file, id):
    """ Read story file and get content of story """

    DELIMITER = "`"

    with open(file, "r") as f:
        # Checking for story ID
        story_found = False
        while not story_found:
            line = f.readline()
            current_story_id = int(line.split("=")[1])

            if current_story_id != id:
                # Skipping to next story using delimiter
                for line in f:
                    if line.rstrip() == DELIMITER:
                        break
                else:
                    raise Exception(f"Story ID {id} not found")

            # If story is found
            else:
                story_found = True
                story_type = int(f.readline().split("=")[1])

                if story_type == 1:
                    data = {}
                    for line in f:
                        if line.rstrip() != DELIMITER:
                            key, value = line.split("=")
                            data[key] = value.rstrip()
                        else:
                            break

                    next_story_id = generate_text_story(data)

                elif story_type == 2:
                    print("Print map")
                    next_story_id = -1
                elif story_type == 3:
                    print("Play minigame")
                    next_story_id = -1
                else:
                    raise Exception("Invalid story type")

        return next_story_id

def generate_minigame():
    pass

def generate_map():
    pass

def generate_text_story(data):
    """ Generates story text, takes choice of user and returns id of next story """

    # Add music, slowness
    print(data["script"].replace("\\n", "\n"))
    choices = ast.literal_eval(data["choices"])

    # Change to dynamic choice using curses module
    choices_limit = 0
    for choice in choices:
        choice_no, choice_name = choice.split(",")
        choices_limit += 1

        print(f"{choice_no}. {choice_name}")

    while True:
        try:
            choice = int(input("Your choice: "))
            if not (0 < choice <= choices_limit):
                raise ValueError("Invalid range")
        except ValueError:
            # Can add funkier replies
            print("Are you retarded?")
        else:
            break

    next_story_id = int(data["next"])
    return next_story_id


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 processing.py <story_id>")
        sys.exit(0)
    else:
        id = int(sys.argv[1])
        file = STORY_SOURCE_DIRECTORY + "story.txt"
        try:
            generate_story(file, id)
        except Exception:
            print("Story not found")
