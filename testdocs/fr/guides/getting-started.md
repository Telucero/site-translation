# Bien démarrer

Suivez ces étapes pour prévisualiser la documentation sur votre machine.

## 1. Créez l’environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Servez le site en anglais

```bash
mkdocs serve
```

Le site est accessible sur `http://127.0.0.1:8000/en/`.

## 3. Construisez le site multilingue

```bash
mkdocs build
```

La commande génère des répertoires localisés dans `site/` pour chaque langue configurée.

## 4. Mettez le contenu à jour

Rédigez le contenu dans `docs/en/`. Le pipeline automatique copiera et traduira le matériel dans les autres dossiers de langue.

!!! info "Ajouter une nouvelle langue ?"
    Modifiez `mkdocs.yml` pour enregistrer le locale puis étendez l’automatisation afin de fournir la traduction dans `docs/<lang>/`.
