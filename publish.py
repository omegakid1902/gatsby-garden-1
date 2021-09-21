import os
import frontmatter
from shutil import copy
dirname = os.getcwd()

if not os.path.exists('./_notes'):
    os.mkdir('./_notes')
    
for file in os.listdir("../zettelkasten/"):
    if file.endswith(".md"):
        with open(os.path.join("../zettelkasten/", file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys() and metadata['publish'] == True:
                print("Copy publish files from zettelkasten to content/")
                copy(os.path.join(dirname + "/../zettelkasten/", file), './_notes')
            else:
                pass

for root, dirs, files in os.walk("../zettelkasten/Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys():
                    print("Copy publish files from zettelkasten to content/")
                    print(os.path.join(root, file))
                    copy(os.path.join(root, file), './_notes')
                else:
                    pass

for root, dirs, files in os.walk("./_notes/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8", mode="r") as f:
                lines = f.readlines()

            with open(os.path.join(root, file), encoding="utf8", mode="w") as f:
                for line_id in range(len(lines)):
                    if lines[line_id].startswith("UID:") or lines[line_id].startswith("birth:") or lines[line_id].startswith("death:") or lines[line_id].startswith("created:"):
                        continue

                    if lines[line_id].startswith("aliases:") and lines[line_id+1].startswith("  - ") and (len(lines[line_id+1]) < 6):
                        lines[line_id+1] = "  - 'NA'\n"
                        
                    f.write(lines[line_id])
