from agents.timeline_agent import TimelineAgent

agent = TimelineAgent()

result = agent.extract_timeline()

print("=" * 80)
print("PROJECT TIMELINE")
print("=" * 80)

print(result["response"])

print("\n")
print("=" * 80)
print("SOURCES")
print("=" * 80)

for doc in result["sources"]:
    print(
        f"{doc.metadata['source']} | "
        f"Page {doc.metadata.get('page', '-')}"
    )