# FitScan AI - Site Web

Site web officiel de l'application FitScan AI - Suivez votre fitness avec une simple photo.

## Description

FitScan AI est une application mobile alimentée par l'IA qui permet de suivre facilement vos calories et nutriments. Il suffit de prendre une photo, scanner un code-barre, ou décrire votre repas pour obtenir instantanément les informations nutritionnelles.

## Fonctionnalités du Site

- ✨ Design moderne et épuré inspiré de Cal AI
- 📱 Mockups de téléphones interactifs avec animations
- 🎯 Section de fonctionnalités détaillées
- 📲 Liens vers App Store et Google Play
- 💻 Entièrement responsive (mobile, tablette, desktop)

## Structure du Projet

```
FitScan-AI-Site/
├── index.html      # Page principale
├── styles.css      # Styles CSS
└── README.md       # Documentation
```

## Lancement du Site

### Option 1 : Ouvrir directement
Double-cliquez sur `index.html` pour l'ouvrir dans votre navigateur.

### Option 2 : Serveur local
```bash
# Avec Python 3
python3 -m http.server 8000

# Avec Node.js (si http-server est installé)
npx http-server

# Puis ouvrez http://localhost:8000 dans votre navigateur
```

## Personnalisation

### Modifier les couleurs
Les couleurs principales sont définies dans `styles.css` :
- Noir : `#000` (header, footer)
- Fond clair : `#f5f5f5`
- Dégradés pour les écrans de téléphone

### Modifier le contenu
Éditez `index.html` pour changer :
- Le texte de la section hero
- Les fonctionnalités
- Les liens de navigation
- Le contenu du footer

### Ajouter de vraies images
Remplacez les mockups CSS par de vraies captures d'écran de votre application en ajoutant des balises `<img>` dans les sections `.phone-screen`.

## Technologies Utilisées

- HTML5
- CSS3 (Flexbox, Grid, Animations)
- Design responsive
- Aucune dépendance JavaScript

## Prochaines Étapes

- [ ] Ajouter de vraies captures d'écran de l'application
- [ ] Créer une page "Features" détaillée
- [ ] Ajouter une section témoignages/avis
- [ ] Intégrer un système de newsletter
- [ ] Ajouter une page de tarification
- [ ] Créer une page FAQ

## Licence

© 2025 FitScan AI. Tous droits réservés.
