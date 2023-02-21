import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art frames for the animation
frames = [
    """
               _
             // \
    |\___/|/\\_//\\
    /0  0 `    ` |
   /   /         \\
   \__/          \\
   /o\           )\\
   `-'           //
  /   \         //
 /     \       //
|       |     //
\       /    //
`\_   _/ \  //
  `\\//  \//\\
   ^^^^^^^^
""",
    """
               _
             // \
    |\___/|/\\_//\\
   /0  0 `    ` |
  /   /         \\
  \__/          \\
 /o\           )\\
 `-'           //
/   \         //
     \       //
      |     //
     /      \\
    /        \\
   /          \\
   \_.-._.___\\
    `--^---'
""",
    """
               _
             // \
    |\___/|/\\_//\\
   /0  0 `    ` |
  /   /         \\
  \__/          \\
 /o\           )\\
 `-'           //
/   \         //
     \       //
      |     //
     / \    \\
    /   \    \\
   /     \    \\
   \_.-._.___\\
    `--^---'
"""
]

while True:
    for frame in frames:
        clear()
        print(frame)
        time.sleep(0.5)

