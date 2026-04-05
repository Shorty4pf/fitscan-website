# Guide de déploiement FitScan-AI-Site sur Vercel

## 1. Structure du projet
- Tous les fichiers (index.html, styles.css, etc.) doivent être à la racine du dossier `FitScan-AI-Site`.
- Le fichier `vercel.json` doit aussi être à la racine.

## 2. Configuration Vercel
1. Sur https://vercel.com, va dans ton projet `fitscan-website`.
2. Va dans **Settings > General**.
3. Dans **Root Directory**, mets :
   
   ```
   FitScan-AI-Site
   ```
   (ou laisse vide si tu déploies déjà depuis ce dossier)
4. Sauvegarde.

## 3. Domaine personnalisé
1. Va dans l’onglet **Domains**.
2. Vérifie que `fitscanai.app` est bien assigné à ce projet.
3. Si besoin, ajoute-le et vérifie la configuration DNS (CNAME ou A record selon Vercel).

## 4. Redéploiement
1. Clique sur **Deploy** ou pousse un commit sur la branche principale.
2. Attends que le statut soit "Ready".

## 5. Vérification
- Va sur https://fitscanai.app
- Si le site ne s’affiche pas, vide le cache de ton navigateur ou teste en navigation privée.

## 6. Problèmes fréquents
- **404 Not Found** :
  - Mauvais dossier racine (Root Directory)
  - Fichier `index.html` absent ou mal placé
  - Domaine mal assigné
- **Solution** : Reprends chaque étape ci-dessus.

---

Pour toute modification, recommence à partir de l’étape 1.
