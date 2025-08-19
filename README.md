# Infinite-Craft-file-editor
allows you edit save files </br>

# i made this with ChatGPT, here is how it works (AI made the rest of this desc tool)

Infinite Craft Save Tool (ic_tool.py)

A Python utility for decoding and re-encoding Infinite Craft save files (.ic).
This lets you inspect, edit, and restore your saves in a readable format.

✨ Features

Decode .ic → .json
Convert Infinite Craft binary save files into human-readable JSON.

Edit your save
Open the decoded JSON in VS Code (or any editor) and tweak values.

Re-encode .json → .ic
Convert your edited JSON back into a valid Infinite Craft save file.

Supports multiple compression formats
Automatically detects and works with gzip, zlib, or brotli.

⚙️ Requirements

Python 3.7+

brotli library (install via pip):

pip install brotli

🚀 Usage
1. Decode a save file
python ic_tool.py save.ic save.json


Converts save.ic into a readable save.json.

Prints which compression method was used (gzip, zlib, or brotli).

JSON output is pretty-printed for easy editing.

2. Edit your save

Open save.json in VS Code (or any text editor).
You can adjust discovered elements, stats, or anything else in the JSON.

3. Re-encode the save file
python ic_tool.py save.json new_save.ic --encode gzip


Re-encodes the edited JSON back into .ic format.

Replace gzip with the method shown during decoding (gzip, zlib, or brotli).

4. Load it back into Infinite Craft

Use your new_save.ic file in place of the old save.

🛡️ Notes

Always keep a backup of your original .ic file before editing.

If you use the wrong compression method when re-encoding, the game won’t load the save. Just try again with the correct one.

If decoding fails, your save may use an unsupported format.

📜 License

MIT
