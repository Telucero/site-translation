# Vue d'ensemble de l'API

La plateforme fournit une API REST qui alimente les contenus dynamiques tels que les notes de version, la recherche multilingue et l’onboarding personnalisé. Les sections suivantes illustrent des endpoints fictifs pour tester le pipeline de traduction.

## Authentification

- `POST /api/v1/token` — échange des identifiants client contre un jeton bearer.
- `GET /api/v1/token/refresh` — renouvelle un jeton proche de l’expiration.

## Endpoints de localisation

- `GET /api/v1/pages/{slug}` — récupère le Markdown localisé pour le slug spécifié.
- `POST /api/v1/pages` — crée ou remplace du Markdown localisé.
- `GET /api/v1/languages` — liste les locales actives du site.

## Codes d’erreur

| Code | Signification | Action recommandée |
| ---- | ------------- | ------------------ |
| 400 | Erreur de validation | Vérifier le payload et les champs obligatoires. |
| 401 | Non autorisé | S’assurer que le jeton d’accès est fourni et valide. |
| 404 | Introuvable | Confirmer que le slug existe pour la langue demandée. |
| 503 | Service indisponible | Réessayer avec un backoff exponentiel. |

!!! warning "API de démonstration"
    Ces endpoints sont factices; ils servent uniquement à éprouver la configuration de traduction et ne reflètent pas l’API de production.
