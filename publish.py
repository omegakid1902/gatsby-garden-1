import os
import frontmatter
from shutil import copy
import os

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
