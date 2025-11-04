# Flux de Traduction

Ce guide décrit le processus de bout en bout qui maintient la documentation localisée du site à jour.

## Étapes principales

1. **Détection des changements** — GitHub Actions se déclenche sur les fusions vers `main`.
2. **Notification à n8n** — Le workflow envoie les métadonnées (SHA, fichiers modifiés, langues cibles) vers un webhook n8n.
3. **Traduction** — n8n récupère le Markdown modifié, contacte le service de traduction et renvoie le texte localisé.
4. **Persistance** — GitHub Actions écrit le Markdown traduit dans `docs/<lang>/`.
5. **Vérification** — MkDocs s’assure qu’aucune traduction ne manque et publie l’artefact.

## Fichiers concernés

- `.github/workflows/translate.yml` — Workflow CI qui coordonne la traduction.
- `scripts/request_translation.py` — Script qui prépare la charge utile pour n8n.
- `automation/prompts/` — Prompts et modèles destinés aux services de traduction.
- `automation/n8n/` — Instructions pour configurer le workflow compagnon dans n8n.

## Ajouter des langues

1. Étendre la section `languages` de `mkdocs.yml`.
2. Mettre à jour la matrice dans GitHub Actions pour inclure le nouveau locale.
3. Fournir glossaires ou prompts dédiés sous `automation/prompts/`.
4. Adapter le workflow n8n pour diffuser les demandes selon la langue.

## Suivi

- Les journaux GitHub Actions contiennent la charge utile envoyée à n8n, les durées et les erreurs.
- Paramétrez n8n pour relayer les échecs vers un canal d’alerte (email/Slack).
- Lorsque le volume augmente, envisagez de stocker les traductions dans un dépôt d’objets ou une base externe.
