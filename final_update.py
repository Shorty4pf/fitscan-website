#!/usr/bin/env python3
import re
import time

timestamp = str(int(time.time()))

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Mettre à jour les versions de cache
content = content.replace('v=20260210', f'v={timestamp}')
content = content.replace('v=20260601', f'v={timestamp}')
content = content.replace('v=1780514122', f'v={timestamp}')

# 2. Remplacer story1.png
content = content.replace('story1.png', f'IMG_0492.PNG?v={timestamp}')

# 3. Remplacer le contenu du phone-2
# Pattern pour trouver: <div class="phone-mockup phone-2">...</div>
pattern = r'(<div class="phone-mockup phone-2">\s*<div class="phone-screen">)(?:.*?)(<\/div>\s*<\/div>)'
replacement = f'\\1\n                        <img src="IMG_0492.PNG?v={timestamp}" alt="Blanc de Poulet Grillé" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;z-index:1;" loading="lazy">\n                    \\2'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'✓ index.html complètement mis à jour avec v={timestamp}')
