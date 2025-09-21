# Netflix movie search

This repository contains a Python script to automate movie search on Netflix via Home Assistant.

## Prerequisites

- Android Debug Bridge installed
- pyscript installed (from HACS)

---

## How It Works

The idea under the Python script is that the movie search on Netflix is performed through a grid, and so it is possible assigning a position to every letter/number. The starting position is the **lens icon** in Netflix.

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


It works considering that the starting position is the lense icon in Netflix.
5) From here, the following logical step would be to create an automation for voice control that uses this action: before the “pyscript.netflix_search”, you should first add the commands to access the search menu in order to be positioned on the lense icon (this part was not included in the Python script because could be subject to changes).
   As example you can use "TV_Search movie on Netflix" automation, being aware that I didn't test yet since I don't have a vocala ssistant yet.
