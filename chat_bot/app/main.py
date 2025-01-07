from graph import graph
import pprint

from dotenv import load_dotenv


load_dotenv()


inputs = {
    "messages": [
        ("user", "quelles sont les compétences de Thomas ?"),
    ]
}
for output in graph.stream(inputs):
    for key, value in output.items():
        pprint.pprint(f"Output from node '{key}':")
        pprint.pprint("---")
        pprint.pprint(value, indent=2, width=80, depth=None)
    pprint.pprint("\n---\n")

