from agents.risk_agent import RiskAgent

agent = RiskAgent()

result = agent.analyze_risks()

print("=" * 80)
print("PROJECT RISK ANALYSIS")
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