# gltool-extras
These are two extra scripts to help automating Rotwood image extraction, by going through "anim" subfolders and renaming all the files accordingly, as well as removing .tex, .xml and .bin files afterwards.

The script was written using ChatGPT when dealing with "anim" became a very time consuming hassle. Using it for "images" will likely mess up file naming system.

\\\\\\\\\\
How to use:
\\\\\\\\\\
1. First, make sure you have gltools-master on your computer.
	https://github.com/instant-noodles/gltools
2. Put both "removefiletypes.py" and "run_glt2p.py" into the "src" folder.
3. Copy contents of "anim" into "src", yes... It will be a mess of folders in "src".
4. Open cmd (Command Prompt) and navigate to the "src" folder using cd (Change directiory) command.
5. Type "python run_glt2p.py" and hit enter
6. All files should be located in "output" folder after it's done.

Feel free to edit the .py files, as I'd say GPT owns all the credit so whatever.
Let me know if you manage to make it a more user-friendly version!

Also... Huge thanks to instant-noodles for creating gltools.
