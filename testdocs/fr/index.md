# Documentation Multilingue (Démo)

Bienvenue sur le site de démonstration multilingue utilisé pour prototyper le flux de traduction du site de documentation. Le contenu anglais alimente le pipeline de localisation automatisé exécuté après la fusion des pull requests dans la branche principale.

## Ce que vous pouvez faire ici

- Explorer une architecture d’information proche du site de production.
- Lancer `mkdocs serve` pour afficher le contenu source et les builds localisés.
- Déclencher le workflow GitHub Actions afin d’envoyer les mises à jour des pages à n8n pour traduction.

!!! tip "Essayez le sélecteur de langue"
    Utilisez le sélecteur en pied de page pour passer entre les versions anglaise, espagnole et française produites par l’automatisation.

## Fonctionnement de la démo

1. Les mises à jour sont écrites dans `docs/en/`.
2. GitHub Actions détecte les changements fusionnés et transmet le diff à n8n.
3. n8n traduit le contenu et renvoie les fichiers localisés vers `docs/<lang>/`.
4. MkDocs reconstruit le site statique et génère les variantes `/en/`, `/es/` et `/fr/`.

Consultez le guide [Flux de Traduction](guides/translation-flow.md) pour obtenir les détails d’implémentation.
