import os
import time
import random

# this section defines ANSI color codes for colored console output
RESET = "\033[0m"
COLORS = {
    "yellow": "\033[93m",
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
}

# this section defines the tree pattern; Y, R, G, B mark ornament positions
TREE_PATTERN = """Y
                           YYY
                          *****
                         *R***G*
                        ******Y**
                       ****G******
                      *********B***
                     *Y***R*****G***
                    *****************
                   *G****B***Y****R***
                  *********************
                 ************Y***G******
                ***G*****Y***************
               ***R****Y***G*****B****R***
              *****************************
             *******************************
            *********************************
           ***********************************
                            ||
                            ||
                            ||
                            ||
                            ||
                        \\========/
"""

# this section initializes the tree data and collects ornament positions by color
def init_tree(pattern: str):
    tree_chars = list(pattern)
    yellow, red, green, blue = [], [], [], []

    for i, ch in enumerate(tree_chars):
        if ch == "Y":
            yellow.append(i)
            tree_chars[i] = "•"
        elif ch == "R":
            red.append(i)
            tree_chars[i] = "•"
        elif ch == "G":
            green.append(i)
            tree_chars[i] = "•"
        elif ch == "B":
            blue.append(i)
            tree_chars[i] = "•"

    return tree_chars, yellow, red, green, blue

# this section clears the terminal and prints the current tree frame
def render_tree(chars):
    os.system("cls" if os.name == "nt" else "clear")
    print("".join(chars))

# this section animates the tree with a "twinkling" effect
def animate_twinkle(tree_chars, yellow, red, green, blue, frames=200, delay=0.08):
    base = tree_chars[:]
    all_positions = yellow + red + green + blue

    for _ in range(frames):
        frame = base[:]
        for idx in all_positions:
            if random.random() < 0.6:
                color_name = random.choice(list(COLORS.keys()))
                color_code = COLORS[color_name]
                frame[idx] = f"{color_code}•{RESET}"
            else:
                frame[idx] = "•"

        render_tree(frame)
        time.sleep(delay)

# this section animates the tree by cycling one color after another
def animate_color_cycle(tree_chars, yellow, red, green, blue, cycles=20, delay=0.18):
    base = tree_chars[:]
    color_sets = [
        ("yellow", yellow),
        ("red", red),
        ("green", green),
        ("blue", blue),
    ]

    for _ in range(cycles):
        for color_name, positions in color_sets:
            frame = base[:]
            color_code = COLORS[color_name]
            for idx in positions:
                frame[idx] = f"{color_code}•{RESET}"
            render_tree(frame)
            time.sleep(delay)

# this section is the program entry point
if __name__ == "__main__":
    tree_chars, yellow, red, green, blue = init_tree(TREE_PATTERN)
    render_tree(tree_chars)
    time.sleep(1.5)
    animate_color_cycle(tree_chars, yellow, red, green, blue, cycles=10, delay=0.15)
    animate_twinkle(tree_chars, yellow, red, green, blue, frames=250, delay=0.06)
