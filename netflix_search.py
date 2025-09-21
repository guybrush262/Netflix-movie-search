@service
def netflix_search(entity_id: str, text: str):
    """
    Types a title into the Netflix search on Fire TV.
    The final confirmation selects the suggestion below the last row of the grid.
    Usage:
      service: pyscript.netflix_search
      data:
        entity_id: media_player.fire_tv_adb
        text: "matrix"
    """

    # Netflix keyboard mapping with top row for space and backspace
    mapping = {
        " ": (-1,0),   # space (above 'a')
        "<": (-1,3),   # backspace (above 'd')
        "a": (0,0),"b": (0,1),"c": (0,2),"d": (0,3),"e": (0,4),"f": (0,5),
        "g": (1,0),"h": (1,1),"i": (1,2),"j": (1,3),"k": (1,4),"l": (1,5),
        "m": (2,0),"n": (2,1),"o": (2,2),"p": (2,3),"q": (2,4),"r": (2,5),
        "s": (3,0),"t": (3,1),"u": (3,2),"v": (3,3),"w": (3,4),"x": (3,5),
        "y": (4,0),"z": (4,1),"1": (4,2),"2": (4,3),"3": (4,4),"4": (4,5),
        "5": (5,0),"6": (5,1),"7": (5,2),"8": (5,3),"9": (5,4),"0": (5,5)
    }

    text = text.lower()

    def send(cmd):
        service.call(
            "androidtv",        # domain
            "adb_command",      # service
            entity_id=entity_id,
            command=cmd
        )
        task.sleep(0.45)       # increased delay to avoid duplicate letters

    # Initial step: from the magnifying glass, go down to 'a'
    send("DOWN")
    pos = (0,0)  # now on 'a'

    # Loop through each character
    for char in text:
        if char not in mapping:
            continue

        target = mapping[char]
        dr = target[0] - pos[0]
        dc = target[1] - pos[1]

        # move vertically
        for _ in range(abs(dr)):
            send("DOWN" if dr > 0 else "UP")

        # move horizontally
        for _ in range(abs(dc)):
            send("RIGHT" if dc > 0 else "LEFT")

        # select character
        send("ENTER")

        pos = target

    # At the end: select suggestion below the last row of the grid
    total_rows = 6  # grid rows (0-5)
    down_steps = total_rows - pos[0]  # how many rows to move down
    for _ in range(down_steps):
        send("DOWN")
    send("ENTER")
    task.sleep(0.6)
    send("ENTER")
    task.sleep(0.6)
    send("ENTER")
