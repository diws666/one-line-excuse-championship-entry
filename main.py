# Verified entry line: exactly 125 characters, UTF-8, single line, no trailing newline.
LINE = "I deleted your file to free up space. It was the only copy, and I have already apologized to the backup, which never existed."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))
