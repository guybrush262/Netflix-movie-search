# Netflix movie search

Using a script Python, I defined an automation to search for the movie that I would like to watch.

Prerequisites:
- Android Debug Bridge installed
- pyscript installed (from HACS)

The idea of the Python script is that the movie search on Netflix is a grid and so we can assign a position to every letter/number.
![PXL_20250921_103130649](https://github.com/user-attachments/assets/b2c30fa5-d06e-4e09-b851-015ca1dfa9df)

1) In config/pyscript/ add “netflix_search.py”.
2) Restart Home Assistant
3) You will see the new action “pyscript.netflix_search” to be used with the following logic:
   - action: pyscript.netflix_search
     data:
       entity_id: media_player.fire_tv_adb
       text: matrix
It works considering that the starting position is the lense icon in Netflix.
4) From here, the following logical step would be to create an automation for voice control that uses this action: before the “pyscript.netflix_search”, you should first add the commands to access the search menu in order to be positioned on the lense icon (this part was not included in the Python script because could be subject to changes).
   As examle you can use "TV_Search movie on Netflix" automation, being aware that I didn't test yet since I don't have a vocala ssistant yet.
