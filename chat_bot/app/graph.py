

from langgraph.graph import END, START, StateGraph

from langgraph.prebuilt import ToolNode, tools_condition

from nodes import agent, rewrite, generate, grade_documents
from tools import retriever_tool
from langgraph.graph import MessagesState

retrieve = ToolNode([retriever_tool])


workflow = StateGraph(MessagesState)


workflow.add_node("agent", agent)
workflow.add_node("retrieve", retrieve)
workflow.add_node("rewrite", rewrite)
workflow.add_node("generate", generate)


workflow.add_edge(START, "agent")


workflow.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "retrieve",
        END: END,
    },
)


workflow.add_conditional_edges(
    "retrieve",
    grade_documents,
)

workflow.add_edge("generate", END)
workflow.add_edge("rewrite", "agent")

graph = workflow.compile()
