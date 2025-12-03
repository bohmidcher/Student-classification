import streamlit as st
import pandas as pd
import joblib
import os

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Réussite Scolaire",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Charger le modèle et l'encoder
model_path = os.path.join(os.path.dirname(__file__), '../models/decision_tree.pkl')
encoder_path = os.path.join(os.path.dirname(__file__), '../models/ordinal_encoder.pkl')

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

# CSS personnalisé
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .section-header {
        color: #1f77b4;
        padding-bottom: 10px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .info-box {
        background-color: #0000;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête principal
st.markdown("<h1 class='main-header'>🎓 Prédicteur de Réussite Scolaire</h1>", unsafe_allow_html=True)
st.markdown("""
<div class='info-box'>
    <p><strong>📋 Remplissez le formulaire ci-dessous</strong> pour obtenir une prédiction personnalisée basée sur des données d'apprentissage machine.</p>
    <p><em>Répondez aux questions sur votre profil scolaire et personnel pour découvrir vos chances de réussite.</em></p>
</div>
""", unsafe_allow_html=True)

# Créer des colonnes pour organiser les inputs
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 class='section-header'>👤 Informations Personnelles</h2>", unsafe_allow_html=True)
    sex = st.selectbox("Sexe",["👨 Masculin", "👩 Féminin"], format_func=lambda x: x)
    sex = sex[0]  # Extraire M ou F
    age = st.slider("Âge", 15, 22, 16, help="L'âge de l'étudiant")
    address = st.selectbox("Lieu de résidence", ["🏙️ Urbain", "🌳 Rural"], format_func=lambda x: x)
    address = address[0]  # Extraire U ou R
    famsize = st.selectbox("Taille de la famille", ["👨‍👩‍👧 ≤ 3 personnes", "👨‍👩‍👧‍👦 > 3 personnes"], format_func=lambda x: x)
    famsize = "LE3" if "≤" in famsize else "GT3"
    Pstatus = st.selectbox("Situation familiale", ["💑 Parents ensemble", "👥 Parents séparés"], format_func=lambda x: x)
    Pstatus = Pstatus[0]  # Extraire T ou A

with col2:
    st.markdown("<h2 class='section-header'>📚 Formation Parentale</h2>", unsafe_allow_html=True)
    Medu = st.slider("Niveau d'études - Mère (0=Aucun, 4=Supérieur)", 0, 4, 2)
    Fedu = st.slider("Niveau d'études - Père (0=Aucun, 4=Supérieur)", 0, 4, 2)
    
    st.write("**Profession Mère :**")
    Mjob = st.selectbox("Sélectionnez", 
        ["👨‍🏫 Enseignant", "⚕️ Santé", "🏢 Services", "🏠 À domicile", "❓ Autre"],
        key="mjob", label_visibility="collapsed")
    Mjob_map = {"👨‍🏫 Enseignant": "teacher", "⚕️ Santé": "health", "🏢 Services": "services", 
                "🏠 À domicile": "at_home", "❓ Autre": "other"}
    Mjob = Mjob_map[Mjob]
    
    st.write("**Profession Père :**")
    Fjob = st.selectbox("Sélectionnez",
        ["👨‍🏫 Enseignant", "⚕️ Santé", "🏢 Services", "🏠 À domicile", "❓ Autre"],
        key="fjob", label_visibility="collapsed")
    Fjob_map = {"👨‍🏫 Enseignant": "teacher", "⚕️ Santé": "health", "🏢 Services": "services",
                "🏠 À domicile": "at_home", "❓ Autre": "other"}
    Fjob = Fjob_map[Fjob]

col3, col4 = st.columns(2)

with col3:
    st.markdown("<h2 class='section-header'>🎯 Motivations et Soutien</h2>", unsafe_allow_html=True)
    
    st.write("**Raison de choisir cette école :**")
    reason = st.selectbox("Sélectionnez",
        ["📖 Cursus spécifique", "⭐ Réputation", "🏠 Proximité", "❓ Autre"],
        key="reason", label_visibility="collapsed")
    reason_map = {"📖 Cursus spécifique": "course", "⭐ Réputation": "reputation", 
                  "🏠 Proximité": "home", "❓ Autre": "other"}
    reason = reason_map[reason]
    
    st.write("**Tuteur principal :**")
    guardian = st.selectbox("Sélectionnez",
        ["👩 Mère", "👨 Père", "👤 Autre"],
        key="guardian", label_visibility="collapsed")
    guardian_map = {"👩 Mère": "mother", "👨 Père": "father", "👤 Autre": "other"}
    guardian = guardian_map[guardian]
    
    schoolsup = st.checkbox("✅ Soutien scolaire", value=False)
    schoolsup = "yes" if schoolsup else "no"
    
    famsup = st.checkbox("✅ Soutien familial", value=True)
    famsup = "yes" if famsup else "no"
    
    paid = st.checkbox("✅ Cours particuliers payants", value=False)
    paid = "yes" if paid else "no"

with col4:
    st.markdown("<h2 class='section-header'>⏱️ Activités et Loisirs</h2>", unsafe_allow_html=True)
    
    traveltime = st.slider("⏱️ Temps de trajet (en classes de 15 min)", 1, 4, 1, 
                           help="1=<15 min, 2=15-30 min, 3=30-60 min, 4=>60 min")
    studytime = st.slider("📖 Temps d'étude hebdomadaire", 1, 4, 2,
                         help="1=<2h, 2=2-5h, 3=5-10h, 4=>10h")
    failures = st.slider("❌ Redoublements/échecs précédents", 0, 4, 0)
    
    activities = st.checkbox("🎨 Activités extrascolaires", value=True)
    activities = "yes" if activities else "no"
    
    nursery = st.checkbox("👶 A eu une garderie", value=False)
    nursery = "yes" if nursery else "no"
    
    higher = st.checkbox("🎓 Aspire à poursuivre études sup.", value=True)
    higher = "yes" if higher else "no"
    
    internet = st.checkbox("🌐 Accès à Internet à domicile", value=True)
    internet = "yes" if internet else "no"
    
    romantic = st.checkbox("💕 En relation amoureuse", value=False)
    romantic = "yes" if romantic else "no"

col5, col6 = st.columns(2)

with col5:
    st.markdown("<h2 class='section-header'>❤️ Bien-être et Santé</h2>", unsafe_allow_html=True)
    
    famrel = st.slider("👨‍👩‍👧 Qualité relation familiale", 1, 5, 4,
                      help="1=Très mauvaise | 5=Excellente")
    freetime = st.slider("🎮 Temps libre après école", 1, 5, 3,
                        help="1=Très peu | 5=Beaucoup")
    goout = st.slider("🚶 Fréquence de sorties avec amis", 1, 5, 3,
                     help="1=Très rarement | 5=Très souvent")
    Dalc = st.slider("🍷 Consommation alcool weekend", 1, 5, 1,
                    help="1=Très faible | 5=Très élevée")
    Walc = st.slider("🍷 Consommation alcool semaine", 1, 5, 1,
                    help="1=Très faible | 5=Très élevée")
    health = st.slider("💊 État de santé générale", 1, 5, 4,
                      help="1=Très mauvais | 5=Excellent")
    absences = st.slider("🚫 Nombre d'absences (année scolaire)", 0, 50, 5)

with col6:
    st.markdown("<h2 class='section-header'>📊 Performance Académique</h2>", unsafe_allow_html=True)
    
    st.write("**Notes des périodes précédentes (sur 20) :**")
    G1 = st.number_input("📈 Note 1ère période (G1)", 0, 20, 10, 
                        help="Note du premier trimestre/semestre")
    G2 = st.number_input("📈 Note 2e période (G2)", 0, 20, 10,
                        help="Note du deuxième trimestre/semestre")
    
    st.markdown("""
    <div class='info-box'>
        <strong>💡 Conseil :</strong><br>
        Les notes précédentes (G1, G2) sont les meilleurs prédicteurs de réussite.
        Assurez-vous qu'elles reflètent votre vrai niveau académique.
    </div>
    """, unsafe_allow_html=True)

# Bouton prédiction
st.divider()
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🔮 Analyser mon Profil et Obtenir la Prédiction", 
                               use_container_width=True, 
                               key="predict_btn")

if predict_button:
    try:
        # Créer le DataFrame avec tous les features dans le bon ordre
        input_data = pd.DataFrame({
            'sex': [sex],
            'age': [age],
            'address': [address],
            'famsize': [famsize],
            'Pstatus': [Pstatus],
            'Medu': [Medu],
            'Fedu': [Fedu],
            'Mjob': [Mjob],
            'Fjob': [Fjob],
            'reason': [reason],
            'guardian': [guardian],
            'traveltime': [traveltime],
            'studytime': [studytime],
            'failures': [failures],
            'schoolsup': [schoolsup],
            'famsup': [famsup],
            'paid': [paid],
            'activities': [activities],
            'nursery': [nursery],
            'higher': [higher],
            'internet': [internet],
            'romantic': [romantic],
            'famrel': [famrel],
            'freetime': [freetime],
            'goout': [goout],
            'Dalc': [Dalc],
            'Walc': [Walc],
            'health': [health],
            'absences': [absences],
            'G1': [G1],
            'G2': [G2]
        })
        
        # Identifier et encoder les colonnes catégoriques
        cat_cols = input_data.select_dtypes(include='object').columns
        input_data[cat_cols] = encoder.transform(input_data[cat_cols])
        
        # Faire la prédiction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        st.divider()
        
        # Affichage du résultat
        if prediction == 1:
            st.success("✅ **RÉUSSITE** - L'élève a de bonnes chances de réussir son année!", icon="🎉")
            confidence = probability[1]
            st.markdown(f"""
            <div style='background-color: #d4edda; padding: 20px; border-radius: 10px; border-left: 5px solid #28a745;'>
                <h2 style='color: #155724; margin: 0;'>Prédiction Positive 🌟</h2>
                <p style='color: #155724; margin-top: 10px; font-size: 18px;'>
                    <strong>Confiance du modèle : {confidence*100:.1f}%</strong>
                </p>
                <p style='color: #155724; margin-top: 10px;'>
                    Basé sur votre profil académique et personnel, le modèle prédit que vous avez 
                    <strong>{confidence*100:.1f}%</strong> de chance de réussir votre année scolaire.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("⚠️ **ALERTE** - L'élève risque d'avoir des difficultés!", icon="❌")
            confidence = probability[0]
            st.markdown(f"""
            <div style='background-color: #f8d7da; padding: 20px; border-radius: 10px; border-left: 5px solid #dc3545;'>
                <h2 style='color: #721c24; margin: 0;'>Prédiction Négative ⚠️</h2>
                <p style='color: #721c24; margin-top: 10px; font-size: 18px;'>
                    <strong>Confiance du modèle : {confidence*100:.1f}%</strong>
                </p>
                <p style='color: black; margin-top: 10px;'>
                    Le modèle prédit que vous pourriez rencontrer des difficultés. 
                    <strong>Nous recommandons :</strong>
                    <ul style='color: #721c24;'>
                        <li>Augmenter votre temps d'étude</li>
                        <li>Demander un soutien scolaire</li>
                        <li>Consulter vos enseignants régulièrement</li>
                        <li>Améliorer votre assiduité</li>
                    </ul>
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Affichage détaillé
        st.divider()
        st.markdown("<h2 style='color: #1f77b4;'>📊 Détails de l'Analyse</h2>", unsafe_allow_html=True)
        
        col_detail1, col_detail2 = st.columns(2)
        with col_detail1:
            st.metric("Probabilité Réussite", f"{probability[1]*100:.1f}%", 
                     delta=f"{(probability[1]-0.5)*100:.1f}% vs moyenne" if probability[1] > 0.5 else f"{(probability[1]-0.5)*100:.1f}% vs moyenne")
        with col_detail2:
            st.metric("Probabilité Échec", f"{probability[0]*100:.1f}%")
        
        st.markdown("""
        <div class='info-box'>
            <strong>📌 Note :</strong> Cette prédiction est basée sur un modèle d'apprentissage machine 
            entraîné sur des données d'étudiants. Elle ne remplace pas l'avis de vos enseignants 
            ou d'un conseiller pédagogique.
        </div>
        """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
        st.write("Veuillez vérifier vos données et réessayer.")
