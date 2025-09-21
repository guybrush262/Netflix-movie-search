# Netflix movie search

Automate movie search on Netflix in Home Assistant via Python script. I am using an Amazon Fire TV (through Android Debug Bridge), but the Python script should also work with native TV integrations (e.g. LG WebOS TV) with some minor fixes (as well as be adapted to Amazon Prime Video or Disney+).

## Prerequisites

- Android Debug Bridge installed
- pyscript installed (from HACS)

---

## How It Works

The idea under the Python script is that the movie search on Netflix is performed through a grid, and so it is possible assigning a position to every letter/number. The starting position is the **lens icon** on the top of the grid in Netflix.

<img src="https://github.com/user-attachments/assets/b2c30fa5-d06e-4e09-b851-015ca1dfa9df" width="400"/>

---

## Installation

1) Add `netflix_search.py` to `config/pyscript/`.
2) Restart Home Assistant.
3) You will find a new action: `pyscript.netflix_search`.

---

## Usage

Example of using the action:


```yaml
action: pyscript.netflix_search
data:
  entity_id: media_player.fire_tv_adb
  text: matrix
```````

---

## Next Steps

To create a full voice-controlled automation:
1) Add commands to navigate to the search menu first, to position the cursor on the lens icon.
2) Then call the pyscript.netflix_search action with your movie title.

You can find my example: "TV_Search movie on Netflix" automation, but note that I didn't test the automation yet since I don't currently have a voice assistant.
