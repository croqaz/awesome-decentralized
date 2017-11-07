#/usr/bin/python3

import re

README = 'README.md'
MARKER = '<div id="marker" markdown="1">(.+?)</div>'

readme = open(README).read()
target = re.search(MARKER, readme, flags=re.S).group(1).split('\n')
target.sort(key=str.lower)
target = '\n'.join(t.strip() for t in target if t.strip())

with open(README, 'w') as new_readme:
    t = re.sub(MARKER,
        '<div id="marker" markdown="1">\n\n{}\n\n</div>'.format(target),
        readme, flags=re.S)
    new_readme.write(t)

print('Done. Sorted {} entries.'.format(len(target.split('\n'))))
