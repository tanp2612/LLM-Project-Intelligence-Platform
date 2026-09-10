from agents.summary_agent import SummaryAgent

agent = SummaryAgent()

result = agent.generate_summary()

print("=" * 80)
print("EXECUTIVE SUMMARY")
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