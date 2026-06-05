#!/usr/bin/env python3
import re
import time

timestamp = str(int(time.time()))

with open('index.html', 'r') as f:
    content = f.read()

# Remplacer le contenu du phone-2
old_pattern = r'(<div class="phone-mockup phone-2">\s*<div class="phone-screen">).*?(</div>\s*</div>)'
new_content = f'\\1\n                        <img src="IMG_0492.PNG?v={timestamp}" alt="Blanc de Poulet Grillé" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;z-index:1;" loading="lazy">\n                    \\2'

content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print(f'✓ Phone-2 mis à jour avec IMG_0492.PNG (v={timestamp})')
