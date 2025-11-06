---
titre : Vue d'ensemble du cadre de développement du réseau
description : Substrate est un cadre de développement de blockchain construit en langage de programmation Rust qui rationalise et accélère le processus de développement de nouveaux réseaux.
icône : octicons-home-24
catégories : Basiques
---

# Vue d'ensemble du cadre de développement du réseau { : #network-dev-framework-overview }

## Introduction { : #introduction }

Construire un réseau à partir de zéro est une tâche très complexe qui nécessite des connaissances approfondies dans un large éventail de domaines, y compris (mais sans s'y limiter) :

- **Algorithmes de consensus** - le consensus garantit que tous les participants au réseau blockchain sont d'accord sur la validité des transactions. Parmi les mécanismes de consensus les plus répandus figurent la preuve de travail (PoW) et la preuve d'enjeu (PoS).

- Cryptographie** - la cryptographie joue un rôle crucial dans la sécurisation de la blockchain. Vous aurez besoin d'algorithmes cryptographiques pour des tâches telles que la création de signatures numériques, la vérification des transactions et le cryptage des données.

- Réseau distribué** - une architecture de réseau permettant aux nœuds de communiquer, de valider les transactions et de synchroniser les données de la blockchain est essentielle pour maintenir un grand livre partagé dans un réseau décentralisé.

- Structures de données** - outre la liste des blocs, où chaque bloc contient un ensemble de transactions ainsi qu'une référence au bloc précédent, une stratégie optimisée et performante est nécessaire pour stocker l'état du réseau.

- Gouvernance** - si le réseau est conçu pour être sans permission, un mécanisme de vote est important pour le faire évoluer et refléter la volonté de la communauté.

- Évolutivité** - il est nécessaire de définir clairement comment évoluer, comment les modifications sont mises en œuvre et comment les conflits sont résolus au sein du réseau.

Heureusement, il n'est pas nécessaire de construire ces composants de blockchain à partir de zéro, grâce à un excellent cadre open-source appelé [Substrate](https://docs.polkadot.com/develop/parachains/intro-polkadot-sdk/){target=\_blank}. Tanssi lui-même est construit avec ce cadre, tirant parti de ses implémentations de base complètes, de sa modularité et de sa flexibilité pour atteindre un niveau élevé de personnalisation.

## Substrate Framework { : #substrate-framework}

Substrate est un cadre extrêmement performant, flexible, modulaire et hautement personnalisable pour construire des blockchains. Ce cadre est la base et le moteur de nombreux projets à travers l'écosystème Web3, y compris le réseau Tanssi lui-même et les réseaux déployés à travers Tanssi.

Beaucoup de ses grandes caractéristiques, telles que la performance, la facilité d'utilisation et la modularité, résultent du langage de programmation choisi pour son développement. C'est là que le [langage de programmation Rust] (#rust-programming-language) brille : Il est rapide, portable, et fournit un modèle merveilleux pour gérer la mémoire, parmi d'autres raisons détaillées dans la [section suivante](#rust-programming-language).

Lors du développement d'un réseau, Substrate représente une bonne longueur d'avance en fournissant un ensemble d'implémentations prêtes à l'emploi des principaux blocs de construction dont un projet a besoin :

- **Algorithmes de consensus** - il existe plusieurs moteurs de consensus intégrés, tels que Aura (Proof of Authority), Babe (Proof of Stake), et Grandpa (finalité du bloc), mais en raison du haut degré de personnalisation offert par Substrate, les équipes peuvent toujours choisir de développer leur propre consensus pour s'adapter aux besoins du cas d'utilisation, comme l'a fait l'équipe Moonbeam avec le [Nimbus Parachain Consensus Framework](https://docs.moonbeam.network/learn/features/consensus){target=\_blank}

- Modules d'exécution** - de nombreux modules intégrés (expliqués en détail dans la section [modules](/learn/framework/modules/){target=\_blank}) peuvent être sélectionnés et configurés dans votre réseau, tels que les comptes, les soldes, le jalonnement, la gouvernance, l'identité, etc.

- Réseautage** - protocoles et bibliothèques intégrés pour établir des connexions, propager des transactions et des blocs, synchroniser l'état de la blockchain et gérer les interactions du réseau.

- Stockage** - mécanismes de stockage intégrés pour un stockage et une récupération efficaces des données.

- File d'attente des transactions** - système intégré de file d'attente des transactions qui gère la validation, la priorisation et l'inclusion des transactions dans les blocs, garantissant ainsi la cohérence et l'intégrité de l'état du réseau.

- API RPC** - Le Substrat fournit des API RPC (Remote Procedure Call) qui permettent aux applications externes d'interagir avec le réseau en interrogeant les données de la blockchain, en soumettant des transactions et en accédant à diverses fonctionnalités exposées par le runtime.

Chaque fonctionnalité offerte par Substrate peut être utilisée telle quelle, étendue, personnalisée ou remplacée pour répondre aux exigences spécifiques du cas d'utilisation du réseau.

Substrate rationalise et accélère le processus de développement de nouveaux réseaux. Lorsqu'il est utilisé en conjonction avec Tanssi, qui aide à gérer l'infrastructure et à superviser le déploiement, la tâche de lancement d'un nouveau réseau devient considérablement plus simple !

## Langage de programmation Rust { : #rust-programming-language}

[Rust](https://www.rust-lang.org){target=\_blank} est un langage de programmation dont les caractéristiques uniques en ont fait le langage le plus apprécié pour la septième année consécutive, selon [l'enquête annuelle de Stack Overflow auprès des développeurs](https://survey.stackoverflow.co/2022#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages){target=blank}.

En plus d'offrir une excellente expérience aux développeurs, Rust excelle dans de nombreux domaines :

- **Sécurité de la mémoire** - Le compilateur Rust applique des contrôles stricts au moment de la compilation afin d'éviter les erreurs de programmation courantes telles que les déréférences de pointeurs nuls, les débordements de mémoire tampon et les courses aux données. De plus, la mémoire est gérée par un nouveau système de propriété (vérifié par le compilateur), ce qui élimine la nécessité d'un ramasse-miettes.

- Performances** - Rust atteint des performances comparables à celles de C et C++ en fournissant un contrôle de bas niveau sur les ressources du système et en minimisant les frais généraux d'exécution. Il a un principe d'abstraction à coût zéro, similaire à "ce que vous n'utilisez pas, vous ne payez pas pour" du C++, ce qui signifie que les abstractions n'ont pas de surcoût supplémentaire.

- Concurrence** - Rust possède des fonctionnalités intégrées qui facilitent l'écriture de code concurrent et parallèle sans introduire de course aux données. Il fournit des threads légers (tâches) et un puissant modèle de propriété qui garantit le partage sécurisé des données entre les threads.

- Abstractions expressives et sûres** - Rust offre un ensemble riche de fonctionnalités de langage moderne, telles que le filtrage, les types de données algébriques, les fermetures et l'inférence de type, permettant aux développeurs d'écrire et de lire un code expressif et concis. Le compilateur Rust applique le système de type fort, évitant ainsi de nombreuses erreurs d'exécution au moment de la compilation.

- Compatibilité multiplateforme** - Rust est conçu pour fonctionner sur une grande variété de plateformes et d'architectures. Il prend en charge les principaux systèmes d'exploitation tels que Windows, macOS et Linux, ainsi que les systèmes embarqués et WebAssembly. Cette polyvalence permet aux développeurs d'écrire du code qui peut être déployé dans différents environnements.

- Un écosystème en pleine expansion** - Rust dispose d'un écosystème en pleine expansion avec une communauté dynamique et une riche collection de bibliothèques et d'outils. Le gestionnaire de paquets officiel, Cargo, simplifie la gestion des dépendances, la construction et les tests.

- Interopérabilité** - Rust offre une interopérabilité transparente avec les bases de code existantes écrites en C et C++. Il dispose d'une interface de fonction étrangère (FFI) qui permet au code Rust de s'interfacer avec du code écrit dans d'autres langages, ce qui permet aux développeurs d'introduire progressivement Rust dans des projets existants, tels que le noyau Linux.
