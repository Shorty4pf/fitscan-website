#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

# Créer une image 853x1844 pour le screenshot
img = Image.new('RGB', (853, 1844), color='#e8e8e8')
draw = ImageDraw.Draw(img)

# Charger les fonts
try:
    title_font = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Bold.otf', 56)
    text_font = ImageFont.truetype('/System/Library/Fonts/SF-Pro-Display-Regular.otf', 32)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Status bar
draw.text((426, 100), '18:15', fill='#000000', font=title_font, anchor='mm')

# Back button et "Step 1/4"
draw.text((80, 150), '←', fill='#000000', font=title_font, anchor='lm')
draw.text((426, 150), 'Step 1/4', fill='#000000', font=text_font, anchor='mm')

# Zone grise pour le corps (simplified - rectangle gris clair)
draw.rectangle([100, 300, 753, 1400], fill='#d8d8d8')

# Ajouter du texte pour la personne debout
draw.text((426, 700), '👤', fill='#666666', font=ImageFont.load_default(), anchor='mm')

# Instructions au bas
draw.text((426, 1550), 'Stand up straight with your', fill='#000000', font=text_font, anchor='mm')
draw.text((426, 1620), 'arms at your sides.', fill='#000000', font=text_font, anchor='mm')

# Barre de progression en bas
draw.rectangle([100, 1750, 753, 1780], fill='#cccccc')
draw.rectangle([100, 1750, 250, 1780], fill='#000000')

img.save('IMG_0500.PNG')
print('✓ Image IMG_0500.PNG créée')
