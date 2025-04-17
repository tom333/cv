from crewai_tools import FileReadTool, GithubSearchTool, MDXSearchTool


#scrape_tool = GithubSearchTool()
read_resume = FileReadTool(file_path="../data/CV.md")
semantic_search_resume = MDXSearchTool(
    mdx="/home/moi/projets/perso/cv/src/data/CV.md",
    config=dict(
        llm=dict(
            provider="openai",
            config=dict(
                model="gpt-4o-mini",
                # Optional parameters can be included here.
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="openai",
        ),
    ),
)
