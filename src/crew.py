from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.cv_reader import read_resume, semantic_search_resume



@CrewBase
class CvCrew():
    """CvCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler'],
            verbose=True,
            allow_delegation=False,
            tools=[read_resume, semantic_search_resume],
        )
        
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            allow_delegation=False,
            tools=[read_resume, semantic_search_resume],
        )

    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'],
            verbose=True,
            allow_delegation=False,
            tools=[read_resume, semantic_search_resume],
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'],
        )

    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_strategy_task'],
            # context=["research_task", "profile_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CvCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


# inputs = {
#     'profile': """
#     Descriptif du poste
# Company Description

# Septeo, éditeur de logiciels de référence en Europe, est un groupe qui grandit vite. Qui se transforme. En 10 ans, nous sommes devenus un des leaders européens de la tech, une référence dans l’édition de logiciels. Cette évolution, c’est le fruit d’un collectif. Le résultat d’un travail d’équipes déterminées, audacieuses et engagées. Des équipes qui travaillent main dans la main, dans la simplicité, la convivialité & la confiance.

# Animés par des valeurs communes, chez Septeo, on est ensemble, on fait ensemble et on transforme ensemble.

# Et les résultats sont là : aujourd’hui, nous sommes le 8ème plus grand éditeur de logiciels en France au classement Truffle 100 et 9ème au FW500. Notre ambition ne s’arrête pas là. Nous souhaitons devenir incontournable en Europe. Que Septeo soit sur toutes les lèvres.

# Nous sommes déjà présents, derrière chaque moment de vie, grâce aux logiciels que nous développons, mis à la disposition de millions de femmes et d’hommes : un achat immobilier, un mariage, une création d’entreprise, un voyage... C’est une sacrée responsabilité finalement. C’est la nôtre. Et peut-être bientôt la vôtre.

# Prêt(e) à faire partie de l’aventure ?
# Job Description

# Nous recherchons un Data Scientist NLP / IA Générative H/F en CDI, à proximité de Courbevoie, pour notre filiale Septeo Services.

# Ce que nous pouvons accomplir ensemble :

# Intégrer l’Intelligence Artificielle générative dans la vie de ses clients, c’est l’ambition de notre programme Brain qui se dote d’un lab dédié exclusivement à l’IA. Nous développons des fonctionnalités multi-usages et multi-plateformes (web, desktop, services Windows) pour diffuser l’utilisation de l’IA et optimiser nos produits destinés à nos marchés.

# Vous rejoignez le programme Brain du Groupe Septeo, composé d’une équipe de 15 personnes travaillant en Agile. Vous participerez au développement de l’application en traitant des problématiques liées au contexte IA et Data.

# Votre quotidien en tant que Data Scientist NLP / IA Générative :

#     Développer et optimiser des modèles de traitement du langage naturel (transformers, LLMs, embeddings, etc.).
#     Concevoir et entraîner des modèles d'IA générative appliqués à des tâches spécifiques [ex. chatbots, résumé automatique, génération de texte, etc.].
#     Expérimenter avec les architectures de modèles les plus récentes (LLaMA, Mistral, etc.).
#     Travailler sur le fine-tuning et le prompt engineering pour améliorer les performances des modèles.
#     Intégrer les modèles NLP dans des pipelines de production robustes et scalables.
#     Assurer la bonne exécution des modèles en production.
#     Collecter, traiter et analyser les données textuelles (Natural Language Processing),
#     Effectuer une veille technologique continue sur les avancées en IA générative et NLP.

# Voir moins
# Profil recherché

# Et si on parlait de vous ?

# Vous avez une expertise avérée sur Transformers (Hugging Face), spaCy, NLTK et l’API OpenAI, ainsi qu’une bonne compréhension des systèmes d’agents IA.

# Vous possédez une solide expérience avec PyTorch et une connaissance approfondie des architectures de modèles comme BERT, T5 ou LLaMA, notamment pour le fine-tuning de modèles de type transformers.

# Votre maîtrise du déploiement et des pratiques MLOps (Docker, MLflow, FastAPI…) vous permet d’industrialiser vos modèles efficacement.

# Vous êtes également à l’aise avec Python et avez des bases en Bash pour automatiser vos workflows.

# Vous êtes doté(e) d’un fort esprit d’innovation et d’une curiosité constante pour les avancées en IA, capable d’explorer et d’expérimenter de nouvelles approches.

# Vous savez travailler de manière autonome, tout en étant un véritable acteur de la collaboration transverse, à l’aise pour interagir avec des équipes variées.
# Additional Information

# Rejoindre Septeo, c'est aussi :

#     Grandir et s'épanouir grâce à un parcours de formation personnalisé, des opportunités de mobilité interne et la possibilité de s'auto-former via notre plateforme Udemy
#     Vivre une aventure humaine, échanger et partager autour d'événements thématisés (afterworks, sport, RSE, séminaires, etc.)
#     Rejoindre un collectif qui prend soin des autres et s'engage en faveur de l'égalité des chances, la diversité et l'inclusion

# Un process de recrutement en 3 étapes

#     Un premier échange téléphonique avec un(e) chargé(e) de recrutement pour vous présenter le poste et ses missions, en savoir plus sur vous.
#     Un deuxième entretien avec un double objectif : vous présenter notre groupe et ses valeurs, mais aussi connaitre vos motivations et l'adéquation de votre projet professionnel avec le poste proposé.
#     Enfin un dernier entretien sera l’occasion de rencontrer votre futur(e) manager, faire un focus métier et valider l’ensemble de vos compétences
#     """,
#     'github_url': 'https://github.com/tom333',
# }

# try:
#     new_cv = CvCrew().crew().kickoff(inputs=inputs)
# except Exception as e:
#     raise Exception(f"An error occurred while running the crew: {e}")
    