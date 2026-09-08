import json
import sys
import os

#THE CODE IS FUCKING SELF-DOCUMENTING.
word = None
meaning = None
example = None
pronunciation = None

if "--wrd" in sys.argv:
    index = sys.argv.index("--wrd")
    word = str(sys.argv[index + 1])
    
if "--mean" in sys.argv:
    index = sys.argv.index("--mean")
    meaning = str(sys.argv[index + 1])

if "--xmpl" in sys.argv:
    index = sys.argv.index("--xmpl")
    example = str(sys.argv[index + 1])

if "--pron" in sys.argv:
    index = sys.argv.index("--pron")
    pronunciation = str(sys.argv[index + 1])

if "--path" in sys.argv:
    index = sys.argv.index("--path")
    filename = str(sys.argv[index + 1])

def add_the_fucking_word(word, meaning, example, pronunciation, filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"vi": []}
    
    new_entry = {
        "name": word,
        "meaning": meaning,
        "example": example,
        "pronu": pronunciation
    }
    
    data["vi"].append(new_entry)
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Successfully added: {word}")

if word:
    add_the_fucking_word(word, meaning, example, pronunciation, filename)