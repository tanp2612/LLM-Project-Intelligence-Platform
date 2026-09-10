from agents.procurement_agent import ProcurementAgent

agent = ProcurementAgent()

result = agent.analyze_procurement()

print("=" * 80)
print("PROCUREMENT ANALYSIS")
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