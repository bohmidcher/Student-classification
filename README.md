# 🎓 Student Classification

> Un système de prédiction de réussite scolaire basé sur le Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7+-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Description

Ce projet propose un pipeline complet d'analyse et de prédiction de la réussite scolaire des étudiants. En utilisant des techniques de Machine Learning, il permet de prédire si un étudiant réussira (pass) ou échouera (fail) en se basant sur des variables socio-démographiques, comportementales et académiques.

### ✨ Fonctionnalités principales

- 📊 Analyse exploratoire des données (EDA)
- 🤖 Modèle de classification (Decision Tree)
- 🎨 Interface utilisateur interactive (Streamlit)
- 💾 Sauvegarde et chargement de modèles
- 📈 Visualisations et statistiques détaillées

## 🗂️ Structure du projet

```
Student-classification/
├── 📱 app/
│   ├── interface.py           # Application Streamlit
├── 📊 data/
│   └── student-mat.csv        # Dataset des étudiants
├── 🤖 models/
│   ├── decision_tree.pkl      # Modèle entraîné
│   └── ordinal_encoder.pkl    # Encodeur sauvegardé
├── 📓 notebooks/
│   ├── exploration.ipynb      # Analyse exploratoire
│   └── train_model.ipynb      # Entraînement du modèle
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation
```

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Cloner le repository**

```bash
git clone https://github.com/ahmedchermiti/Student-classification.git
cd Student-classification
```

2. **Créer un environnement virtuel** (recommandé)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

### Dépendances principales

- `pandas` - Manipulation de données
- `scikit-learn` - Machine Learning
- `streamlit` - Interface utilisateur
- `joblib` - Sauvegarde de modèles
- `matplotlib` & `seaborn` - Visualisations

## 💻 Utilisation

### Lancer l'application web

```bash
streamlit run app/interface.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

### Réentraîner le modèle

1. Ouvrez le notebook `notebooks/train_model.ipynb`
2. Exécutez toutes les cellules
3. Le nouveau modèle sera sauvegardé dans `models/`

### Explorer les données

Consultez `notebooks/exploration.ipynb` pour voir :
- Distribution des notes
- Corrélations entre variables
- Facteurs influençant la performance
- Analyses démographiques
- Impact de la consommation d'alcool

## 📊 Dataset

Le dataset `student-mat.csv` contient des informations sur des étudiants en mathématiques :

- **Variables démographiques** : âge, sexe, adresse
- **Variables familiales** : éducation des parents, taille de la famille
- **Variables scolaires** : notes G1, G2, G3, absences, temps d'étude
- **Variables comportementales** : consommation d'alcool, temps libre, sorties

**Variable cible** : `pass_fail` (1 si G3 ≥ 10, sinon 0)

## 🎯 Méthodologie

### 1. Préparation des données
- Création de la variable cible binaire
- Sélection des features pertinentes
- Encodage des variables catégoriques avec `OrdinalEncoder`

### 2. Entraînement
- Algorithme : Decision Tree Classifier
- Paramètres : `max_depth=5`, `random_state=42`
- Split : 80% train / 20% test

### 3. Évaluation
- Métriques d'accuracy affichées dans le notebook
- Matrice de confusion
- Courbes de performance

### 4. Déploiement
- Sauvegarde du modèle avec `joblib`
- Interface Streamlit pour les prédictions en temps réel

## 🎨 Interface utilisateur

L'application Streamlit offre :
- 📝 Formulaire de saisie des caractéristiques de l'étudiant
- 🔮 Prédiction instantanée (Pass/Fail)
- 📊 Probabilités de réussite/échec
- 🎨 Design moderne et responsive

## 🔧 Personnalisation

### Modifier l'interface

Éditez `app/templates/ui.html` pour personnaliser le CSS et le HTML de l'entête.

### Changer le modèle

Dans `notebooks/train_model.ipynb`, testez d'autres algorithmes :

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Exemple avec Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
```

### Gérer les catégories inconnues

L'`OrdinalEncoder` est configuré avec `handle_unknown='use_encoded_value'` et `unknown_value=-1`. Pour d'autres stratégies, explorez `OneHotEncoder` ou des techniques d'encodage avancées.

## ⚠️ Avertissements

- Les prédictions sont basées sur un modèle statistique et doivent être utilisées comme **support d'information** uniquement
- Ce n'est pas un diagnostic définitif de la performance scolaire
- Vérifiez toujours la qualité des données avant utilisation en production

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Ahmed Chermiti**

## 🙏 Remerciements

- Dataset fourni par l'UCI Machine Learning Repository
- Communauté Streamlit pour l'excellente documentation
- Tous les contributeurs qui ont participé à ce projet

---

⭐ N'oubliez pas de mettre une étoile si ce projet vous a aidé !

