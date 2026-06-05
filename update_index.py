#!/usr/bin/env python3
import re
import time

timestamp = str(int(time.time()))

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver et remplacer
new_lines = []
in_phone2_screen = False
skip_until_closing = False

for i, line in enumerate(lines):
    # Détecter le début du phone-2 screen
    if '<div class="phone-screen">' in line and i > 0 and 'phone-mockup phone-2' in lines[i-1]:
        new_lines.append(line)
        in_phone2_screen = True
        # Ajouter l'image
        new_lines.append(f'                        <img src="IMG_0492.PNG?v={timestamp}" alt="Blanc de Poulet Grillé" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;z-index:1;" loading="lazy">\n')
        skip_until_closing = True
    elif skip_until_closing and '</div>' in line and i > 0 and 'phone-screen' in ''.join(lines[max(0,i-20):i]):
        # Fermer le phone-screen
        new_lines.append(line)
        skip_until_closing = False
    elif skip_until_closing:
        # Ignorer le contenu
        continue
    else:
        # Appliquer les mises à jour de version
        line = line.replace('v=20260210', f'v={timestamp}')
        line = line.replace('v=20260601', f'v={timestamp}')
        line = line.replace('v=1780514122', f'v={timestamp}')
        line = line.replace('story1.png', f'IMG_0492.PNG?v={timestamp}')
        new_lines.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'✓ Toutes les modifications appliquées (v={timestamp})')
