# Liste de contrôle de l'intégratio
n

Utilisez cette liste de contrôle lorsque vous connectez un nouveau référentiel documentaire au pipeline de traduction automatique.

## 1. Dépôt GitHu
b

- Le flux de travail `translate.yml` est présent et passe sur `main`.
- [ ] `TARGET_LANGUAGES` mis à jour avec les locales que vous prévoyez de générer.
- Le secret `N8N_WEBHOOK_URL_TR` est configuré et testé avec le drapeau dry-run.
- Les règles de protection des branches autorisent les commits de `GITHUB_TOKEN`.

## 2. Flux de travail n8
n

- L'URL du Webhook correspond au secret stocké dans GitHub.
- Les nœuds de validation, de filtrage, de traduction et de formatage sont activés.
- Canal d'alerte configuré pour notifier les échecs de vérification.
- Le glossaire et les variables d'invite sont chargés pour chaque langue.

## 3. Projet MkDoc
s

- Le nouveau contenu anglais se trouve dans `docs/en/`.
- [ ] `mkdocs.yml` nav mis à jour et entrées `nav_translations` fournies.
- [ ] `mkdocs build` réussit localement avec `mkdocs-material` et `mkdocs-static-i18n`.

## 4. Test de fumé
e

1. Créez un court changement d'anglais et ouvrez une RP.
2. Fusionner avec `main` et surveiller le flux de travail **Translate Documentation**.
3. Confirmer que les fichiers localisés apparaissent dans `docs/<lang>/`.
4. Lancer `mkdocs serve` et revoir les pages `/es/` et `/fr/`.

Documentez tous les bloqueurs et capturez les logs dans le runbook des opérations partagées.


## Exemple d'étapes de vérificatio
n

- Confirmer que les journaux du pipeline de traduction contiennent l'ID du travail dans `provider_metadata`.
- Comparer le Markdown traduit avec le glossaire pour s'assurer que la terminologie et le ton sont corrects.
