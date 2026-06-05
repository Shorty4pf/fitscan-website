#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

# Créer une image 853x1844
img = Image.new('RGB', (853, 1844), color='#0f0f0f')
draw = ImageDraw.Draw(img)

# Essayer d'utiliser des fonts
try:
    font_title = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Bold.otf', 72)
    font_subtitle = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Regular.otf', 44)
    font_label = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Regular.otf', 28)
    font_value = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Bold.otf', 64)
except:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_label = ImageFont.load_default()
    font_value = ImageFont.load_default()

# Status bar
draw.text((426, 80), '9:41', fill='white', font=font_title, anchor='mm')

# Title
draw.text((426, 350), 'Blanc de Poulet', fill='white', font=font_title, anchor='mm')
draw.text((426, 460), 'Grillé', fill='white', font=font_title, anchor='mm')

# Portion
draw.text((426, 560), '200g', fill='#888888', font=font_subtitle, anchor='mm')

# Cards 2x2
cards = [
    (120, 700, 'Calories', '330'),
    (580, 700, 'Protéines', '62g'),
    (120, 1100, 'Glucides', '0g'),
    (580, 1100, 'Lipides', '7g'),
]

for x, y, label, value in cards:
    draw.rectangle([x-150, y-90, x+150, y+90], fill='#1a1a1a', outline='#333333', width=2)
    draw.text((x, y-30), label, fill='#666666', font=font_label, anchor='mm')
    draw.text((x, y+40), value, fill='white', font=font_value, anchor='mm')

# Health score box
draw.rectangle([100, 1350, 753, 1480], fill='#2a2a1a', outline='#ccaa00', width=3)
draw.text((426, 1390), 'Score santé', fill='white', font=font_subtitle, anchor='mm')
draw.text((426, 1460), '9/10', fill='#ffdd00', font=font_value, anchor='mm')

# Done button
draw.rectangle([100, 1580, 753, 1700], fill='#ffdd00')
draw.text((426, 1640), 'Terminé', fill='#000000', font=font_subtitle, anchor='mm')

img.save('screenshot-nutrition.png')
print('✓ Image screenshot-nutrition.png créée avec succès')
