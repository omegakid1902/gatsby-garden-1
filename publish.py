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
                for line in lines:
                    if line.startswith("UID:") or line.startswith("birth:") or line.startswith("death:") or line.startswith("created:"):
                        continue

                    f.write(line)
