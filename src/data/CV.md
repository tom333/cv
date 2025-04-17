**Thomas Guyader**

**Architecte Data**

[https://www.linkedin.com/in/thomas-guyader-444418a6/](https://www.linkedin.com/in/thomas-guyader-444418a6/)  
[https://github.com/tom333](https://github.com/tom333)

# Compétences

## Data
 Python, Jupyter Notebook, Tensorflow, Torch, scikit learn, MLflow, MLOps, Pandas, PySpark, apache beam … 

## Algorithmes 
 Decision tree, Linear regression, Logistic regression, K-means, Gradient boosting …

## architecture
  Google Cloud Plateform ,
  MlOps, 
  Datamesh architecture, 
  Kubernetes, Argo CD,
  Microservices,
  CI/CD / Github actions ,
  Terraform,
  GitOps, 
  DevOps, 
  12 factors applications, cloud native applications.


 ## Développement logiciel
  Spring boot 
  Angular
  Typescript / Javascript
  HTML5 / CSS3 
  Django / Flask / FastApi
  postgresql / Oracle
  Git, maven  

 ## Gestion de projet et management
 SCRUM PMI Management 3.0 

 ## Langues
 Anglais technique

 ## Intérêts
 Cuisine Guitare

# Vie personnelle
Thomas est marié, père de 3 enfants, 2 garçons de 11 et 9 ans et une fille de 3 ans.

# Projet personnels
* Server Kubernetes personnel
  * Géré avec Argocd avec le pattern "Apps of Apps", publié à 100% sur github mais avec un accès sécurisé via github et les secrets sont externalisés sur un service tiers, Le cluster a accès au GPU du serveur pour augmenter la puissance de calcul 
  * **MLOps, ArcgoCD, Github, open source** 

* Analyse d’activité professionnel  
  * Sur guichet unique entreprise, les usagers saisissent une description de leurs activités professionnelles. Le modèle développé suggère alors le code NAF associé. Conception entièrement automatisé du modèle, du téléchargement des données au déploiement du modèle, en passant par l'entraînement et le tuning des hyperparamètres  
  * **MLOps, Tensorflow, NLP, Airflow**  

* Kubeflow on Kubernetes with argocd  
  * [https://github.com/tom333/argocd-kubeflow](https://github.com/tom333/argocd-kubeflow)  
  * Déploiement de Kubeflow ( plateforme de machine learning industrialisée et à  l’échelle) sur Kubernetes avec ArcgoCD  
  * **MLOps, Tensorflow, Jupyter notebook, data workflows, AutoML**  

* Contributeur à Kalliope   
  * [https://kalliope-project.github.io/](https://kalliope-project.github.io/)  
  * Assistant personnel hors ligne  
  * **Natural Language Processing, Natural Language Generating, Intent detection**  

* Dataviz  
  * [https://github.com/tom333/dataviz](https://github.com/tom333/dataviz)  
  * [https://tom333.github.io/dataviz/intro.html](https://tom333.github.io/dataviz/intro.html)  
  * Data Visualisation basées sur data.gouv.nc  

  * **Python, Jupyter, Jupyter book, pandas, github actions**

# 

# Expérience professionnelle

## 2023 \- à aujourd’hui

**Gouvernement de la Nouvelle Calédonie \- Direction du Numérique et de la Modernisation**

## ---

### Architecte data
* **EN COURS** : Chatbot interne à destination des agents de la fonction publique de la Nouvelle Calédonie
    * Chatbot intégré au système d'information existant
    * Fonctionnalités :
        * Chatbot avec mémoire des conversations
        * Upload et analyse de documents
        * Intégration avec gmail
        * Intégration avec Jira

    * L'objectif étant de fournir un accès à un chatbot tout en le maîtrisant
    * ** RAG, crewai, langchain, streamlit, mcp, qdrant, mem0ai

* **EN COURS** : Chatbot sur le code du travail calédonien
    * chatbot pour un support de premier niveau sur le ode du travail de la Nouvelle Calédonie
    * L'objectif est de soulager les équipes de la direction
    * **RAG, Langchain, Langraph, chainlit, qdrant, gemini, adaptive RAG, Query analysis, self corrective RAG **

* **EN COURS** : Création d'une api entreprises
    * Centralisation de toutes les données concernant les entreprises calédoniennes
    * Développement spécifique en fastapi
    * Création d'un RAG pour récupérer et consolidé les données des différentes sources
    * les données ont différentes formes et format, certaines viennent de big query, d'autres de FPT, d'autres d'API...
    * Il faut agréger toutes ces données toutes en les faisant correpondre aux différentiels officiels publiés sur les plateformes open data data.gouv.nc ou data.gouv.fr
    * Outils de traitement de données : mage.ai
    * **mage.ai, duckdb, bigquery **

* **EN COURS** : Déploiement d’une modern data stack on premise  
  * Pour certaines données “sensibles” qui ne peuvent être mises sur GCP et par volonté politique, le choix a été fait de rapatrier sur les infrastructures interne, la chaine de traitement de la donnée.
  * Le projet consiste à mettre en place une solution entièrement hébergée on premise permettant de gérer tout le cycle de vie de la donnée.
  * Les outils doivent au maximum se baser sur des solutions open source
  * La solution envisagée est une modern data stack basée sur une architcture data mesh
  * ClickHouse, Apache SuperSet, Knative, …  
  *   

* Création d’un “clone de [https://labonneboite.francetravail.fr/](https://labonneboite.francetravail.fr/)  
  * Projet annulé avant la mise en production à cause des dernières émeutes, le marché de l'emploi ayant été trop perturbé
  * **Catboost, scikit learn** 

* Création d'api publiques.
  * Dans la cadre de la stratégie Data du Gouvernement de La Nouvelle Calédonie, à laquelle il a participé à la création, Il est en charge du suivi et de l'architecture des api entreprises et adresses, équivalent des api de métropôle. 

* Outil d’évaluation de la masse salariale de la DRHPFNC  
  * outil de simulation d’évolution du coup de la masse salariale, en fonction du nombre d’agents et de l’évolutions de leurs carrière 
  * Création d'un frontend avec Graio permettant de modifier les paramètres d'entrée de l'évolution de la masse salariale. Combinaison de plusieurs modèles conjointement, un modéle de changement de corps, un modèle de 
  * **Scikit learn, gradio**

* Chatbot pour service-public.nc  
  * Création d’un chatbot avec le contenu du site
  * Mise en place d'un process MLOPs avec récupération automatique des données, recalcul automatique des embeddings et stockage des données
  * **RAG, Langchain, Langraph, chainlit, qdrant, gemini, adaptive RAG, Query analysis, self corrective RAG **

* Alimentation automatique de contenu pour service-public.nc  
  * récupération automatique de contenu des sites des partenaires avec résumé et formattage pour alimenter automatiquement le site service-public.n²c
  * 
  * **Langchain, gemini**

* Mise en place d’une nouvelle infrastructure dédiée à la data sur google cloud plateform  
  * Architecture réseau “Hub and Spoke”  
  * Secrets versionnés sur git  
  * Logs et monitoring centralisée  
  * Projets orientés data avec gestion des droits et accès  
  * [https://github.com/gouv-nc-data/](https://github.com/gouv-nc-data/)  
  * **Terraform, github, github action**  
      
* Créations de modules terraform pour automatiser et faciliter le transfert de données on premise vers Google Cloud BigQuery  
  * Cloud Run: scripts python  
  * Dataproc (pyspark): copie automatique de bdd vers BigQuery  
  * Schedule et monitoring automatique  
  * **Terraform, github, github action**

* Mise à disposition de données métier pour exploitation dans BigQuery, datastudio ou Spreadsheet  
  * Automatisation des copies de données  
  * Accompagnement au changement et montée en compétence des agents
  * **BigQuery, Dataform, Looker studio, sql, Google Spreadsheet**

## 2021 \- 2023

**Gouvernement de la Nouvelle Calédonie \- Direction du Numérique et de la Modernisation**

## ---

### Architecte des systèmes d’informations

* Stratégie de migration vers kubernetes

Définition d’une stratégie de migration des nouvelles applications et des anciennes sur une nouvelle infrastructure basée sur kubernetes.
La première étape a été de faire produire des containers Docker par les équipes de développement.
Les équipes OPS ont pu en parallèle se former à Kubernetes et déployer un cluster bare metal.
Proposition de monter une équipe DevOps pour décloisoner les équipes, mais refusé par la direction.

* Accompagnement des équipes aux changements 
* DevSecOps  
* Infrastructure as code  
* Application Cloud Native
* **ArgoCD, Github, Helm, **

* Stratégie de migration sur le cloud

Définition d’une stratégie d'hébergement d’applications métier sur Google Cloud Plateform avec création d'une petite équipe DevOps dédièe sur un projet
Projet abandonné car jugé trop ambitieux à mener en parallèle du projet kubernetes par les équipes opérationnelles

## 2018

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**

## ---

### Chef de projet NC Connect

[https://connect.gouv.nc](https://connect.gouv.nc)

Plateforme unique d’authentification du Gouvernement de la Nouvelle Calédonie.
Avec gestion des identées vérifiées ajoutée en urgence pendant la crise covid pour permettre la délivrance de passe sanitaire.
Gestion du projet selon PMI.
Architecture orientée microservices avec découpage et découplage des responsabilités avec mises en cluster des services critiques avec tolérance à la panne d'une partie des services.
C'est le plus gros service en terme de connexions en Nouvelle Calédonie.

### Technologies

- OpenId Connect, Spring boot, Angular, Postgresql, Haute disponibilité, Déploiement continue, Micro services

## 2013 \- 2016

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**  
---

### Architecte logiciel

Mise en oeuvre d’architectures logiciels sur les différents projets et téléservices du gouvernement en fonction des besoins et de l’existant

### Technologies

- WOA, Microservices, CQRS / ES, Redux, PWA, Applications mobiles hybrides

## 2013 \- 2016

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**  
---

### Architecte logiciel

Mise en place d’un nouveau framework de développement  
Remplacement d’un socle payant (oracle) par de l’open source

- Frontend Angular :  
  - angular  
  - NgRx  
  - Typescript  
  - Saas  
  - Progressive Webapp

- Backend Spring boot  
- Java 11 (LTS)  
- Base postgresql, flyway  
- Architecture orientée microservices  
- Outils spring cloud, serveurs de configuration (spring cloud config), annuaire de services (spring cloud netflix eureka), Circuit breaker (Spring cloud netflix hystrix), Spring boot admin  
- Chaîne d’intégration continue et déploiement continu :   
  - Jenkins / pipeline  
  - Gitlab  
  - Git flow  
  - Sonarqube  
  - Artifactory  
- Tests unitaires, tests d’intégrations, tests de bout en bout, tests de montée en charge  
- Gestion du changement (accompagnement, formation, ateliers, …)  
- Mise en oeuvre participative (Atelier de co création, serious games, …)  
- Ouverture d’une partie du code source sur github  
- POC docker  
- Authentification centralisée basée sur OpenId Connect  
- Intégration avec le SI existant : GED alfresco et SAE docubase (CMIS), jira, SIG  
- Support aux développeurs et chefs de projets

## 2017

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**  
---

### Architecte logiciel

Modernisation du socle de développement ADF 11 et 10

### Technologies:

	Oracle ADF 12 essentials  
	Java 11  
	Tomcat embarqué  
	POC de migration de Oracle DB vers Postgresql

## 

## 2013 à 2017

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**

### ---

### Manager de proximité

Chef de section AXI (Architecture de cadre commun d'interopérabilité)

* Management d’une équipe de 5 personnes  
* activité de support  
* formation  
* organisation et animation de présentations techniques et de veille technologique hebdomadaires

## 

## 2014

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**

### ---

### Concepteur développeur

Application mobile de résultats en temps réel des élections provinciales pour ipad  
[https://samobile.gouv.nc](https://samobile.gouv.nc)

### Technologies:

	python / django  
	angularjs  
	websocket

	

## 2008 à 2013

**Gouvernement de la Nouvelle Calédonie \- Direction des Technologies des Système d’Informations**

### ---

### Concepteur Développeur Oracle ADF / Architecte logiciel

à la DTSI sur les projets Gaip, Sefora, Sigales et Panda

### Technologies:

	ADF 10 et 11  
	Java 5 et 6  
	Oracle DB  
	JasperReport  
	Maven

## 2007 à 2008

**IdSoft**

### ---

### Concepteur Développeur

### Technologies:

Java, J2e, Access, iText, Python, Django, ReportLab, Oracle10g, JSF, Spring, Hibernate, IceFaces, Jasper report.

## 2005 à 2007

---

### Stages en entreprises

Développement d’un logiciel de suivi de service après vente

Simulation d’agents collaboratifs émotionnels

Conception et développement d’un méta-modèle multi-agents d’une colonne d’eau

Développement d’un portail web de consultation de données océanographiques pour 	l’IRD de Nouméa (Modélisation et conception de la base de données PostgreSQL, Reprise des données Oracle vers PostgreSQL, développement du portail).

### Technologies:

 Delphi, Access, C++, OpenGL, Java/J2EE, Oracle, PostgreSQL, JSF, Spring, Hibernate.

# Formations

**2022:** Spécialisation Preparing for Google Cloud Certification: Cloud Data Engineer (Parcours de 6 formations)  
This program provides the skills you need to advance your career in data engineering and provides a pathway to earn the industry-recognized Google Cloud Professional Data Engineer certification. Through a combination of presentations, demos, and labs, you'll enable data-driven decision making by collecting, transforming, and publishing data; and you'll gain real world experience through a number of hands-on Qwiklabs projects that you can share with potential employers.

You'll also have the opportunity to practice key job skills, including designing, building, and running data processing systems; and operationalizing machine-learning models. For learners looking to get certified, this program will also provide sample questions similar to those on the exam, including solutions and practice exam quizzes that simulate the exam-taking experience.

Upon successful completion of this program, you will earn a certificate of completion to share with your professional network and potential employers. If you'd like to earn your Google Cloud certification, you will need to register for and pass the certification exam. Please note that this program helps equip you with the skills you need to take the certification exam, but the certification and certification fee is not included in the cost of this training program.

Projet d'apprentissage appliqué

 This Professional Certificate incorporates hands-on labs using our Qwiklabs platform.

These hands on components will let you apply the skills you learn in the video lectures. Projects will incorporate topics such as Google BigQuery, which are used and configured within Qwiklabs. You can expect to gain practical hands-on experience with the concepts explained throughout the modules.

**2022:** Spécialisation Machine learning with Tensorflow on Google Cloud (Parcours de 5 formations)  
Qu'est-ce que le machine learning et quels types de problèmes permet-il de résoudre ? Quelles sont les cinq phases permettant de traiter un cas d'utilisation à l'aide du machine learning, et pourquoi chaque étape est-elle essentielle ? Pourquoi les réseaux de neurones sont-ils désormais si courants ? Comment définir un problème d'apprentissage supervisé et trouver une solution adaptée et généralisable à l'aide de la descente de gradient et d'une méthode pertinente de création d'ensembles de données ? Apprenez à créer des modèles de machine learning distribués qui pourront évoluer dans TensorFlow, à adapter l'entraînement de ces modèles pour bénéficier d'une évolutivité horizontale et à obtenir des prédictions très performantes. Convertissez les données brutes en caractéristiques de sorte que les processus de ML soient en mesure d'identifier les propriétés importantes dans les données et générez des insights qui ont du sens en rapport avec la problématique. Enfin, découvrez comment intégrer à la fois la combinaison de paramètres permettant d'obtenir des modèles précis et généralisés, et une connaissance de la théorie indispensable pour résoudre des types spécifiques de problèmes de ML.

Vous expérimenterez le ML de bout en bout en commençant par créer une stratégie centrée sur le ML, puis en progressant dans le processus d'entraînement, d'optimisation et de production de modèles grâce à des ateliers pratiques faisant appel à Google Cloud Platform.


**2022:** Spécialisation Preparing for Google Cloud Certification: Machine Learning Engineer (Parcours de 9 formations)  
Un Professional Machine Learning Engineer conçoit, évalue, met en production et optimise des modèles de ML en s'appuyant sur les technologies Google Cloud, et sur sa connaissance des techniques et modèles éprouvés. Il gère des ensembles de données volumineux et complexes, et crée du code reproductible et réutilisable. Il tient compte de l'IA responsable et de l'équité tout au long du processus de développement des modèles de ML. Il travaille en étroite collaboration avec d'autres équipes pour assurer la réussite à long terme des applications basées sur le ML. Le ML Engineer possède de solides compétences en programmation, et une expérience des plates-formes de données et des outils de traitement des données distribués. Le ML Engineer maîtrise les aspects de l'architecture des modèles, de la création de pipelines de données et de ML, ainsi que de l'interprétation des métriques. En outre, il doit être familier des principes de base du MLOps, du développement d'applications, de la gestion d'infrastructure, de l'ingénierie et de la gouvernance des données. Il rend le ML accessible et aide les équipes de l'entreprise à s'en servir. Le ML Engineer conçoit et crée des solutions évolutives et performantes en entraînant, en réentraînant, en déployant, en planifiant, en surveillant et en améliorant des modèles.


**2022:** Preparing for Google Cloud Certification: Cloud Architect Certificat Professionnel
This program provides the skills you need to advance your career in cloud architecture and provides a pathway to earn the industry-recognized Google Cloud Professional Cloud Architect certification. You'll deploy solution elements, including infrastructure components such as networks, systems and applications services, and you'll gain real world experience through hands-on Qwiklabs projects that you can share with potential employers.

You'll also have the opportunity to practice key job skills, including case analysis, identifying technical watchpoints, and developing proposed solutions. Test your basic abilities with Activity Tracking Challenge Labs. For learners looking to get certified, this program will provide sample questions similar to those on the exam, including solutions and practice exam quizzes that simulate the exam-taking experience.

Upon successful completion of this program, you will earn a certificate of completion to share with your professional network and potential employers. If you'd like to earn your Google Cloud certification, you will need to register for and pass the certification exam. Please note that this program helps equip you with the skills you need to take the certification exam, but the certification and certification fee is not included in the cost of this training program.

**2021** : Architecting with Google Kubernetes Engine
The Architecting with Google Kubernetes Engine specialization will
teach you how to implement solutions using Google Kubernetes
Engine, or GKE, including building, scheduling, load balancing, and
monitoring workloads, as well as providing for discovery of services,
managing role-based access control and security, and providing
persistent storage to these applications

**2016** : RSSI Sécurité dans les développements, architectures et administration des SI  
**2016** : Agile avancé  
**2015** : Formation management  
**2015 :** Javascript Avancé  
**2014** : certification Scrum Master  
**2014** : Introduction aux innovations games  
**2014** : Oracle fusion middleware  
**2012** : Java performances et optimisation  
**2012** : Design Patterns Java EE  
**2007** : IUP Ingénierie Informatique (Université de Bretagne Ouest), Master Conception et développement logiciel