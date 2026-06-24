# Simple RAG

Ce projet est une implémentation simple d'un système RAG en Python. Il répond à des questions sur les chats en utilisant uniquement les informations présentes dans « data/cat-facts.txt ».

Le projet fonctionne entièrement en local avec [Ollama](https://ollama.com/).

## Fonctionnement

Au démarrage, l'application :

1. charge les faits depuis le fichier texte ;
2. crée un embedding pour chaque ligne avec « mxbai-embed-large » ;
3. compare la question aux lignes avec la similarité cosinus ;
4. conserve les trois lignes les plus proches ;
5. demande à « qwen3:8b » de répondre à partir de ce contexte.


## Prérequis

- Python 3.10 ou plus récent
- Ollama installé et lancé

Téléchargez les deux modèles utilisés par le projet :

~~~bash
ollama pull mxbai-embed-large
ollama pull qwen3:8b
~~~

## Installation

Créez un environnement virtuel, puis installez le client Python d'Ollama :

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install ollama
~~~

## Utilisation

Depuis la racine du projet, lancez :

~~~bash
python main.py
~~~

Posez ensuite une question, par exemple :

~~~text
How many hours do cats sleep?
~~~

Les données et les instructions du modèle sont en anglais. Les questions en anglais donnent donc de meilleurs résultats.

## Structure

~~~text
.
├── data/cat-facts.txt       # Base de connaissances
├── main.py                  # Point d'entrée et génération de la réponse
└── src/
    ├── config.py            # Modèles et chemin des données
    ├── cosine_similarity.py # Calcul de similarité
    ├── embeddings.py        # Création des embeddings
    ├── loader.py            # Chargement des données
    ├── rag.py               # Recherche des passages pertinents
    └── vector_store.py      # Stockage des vecteurs en mémoire
~~~

Pour utiliser un autre fichier ou d'autres modèles, modifiez les valeurs dans « src/config.py ».
