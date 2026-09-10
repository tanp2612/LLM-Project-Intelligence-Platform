from pprint import pprint

from graph.health.workflow import health_graph


def test_health_workflow():

    state = {

        "question": "Generate AI Project Health Score",

        "documents": [],

        "summary": None,

        "risk": None,

        "timeline": None,

        "procurement": None,

        "health_score": None,
    }

    result = health_graph.invoke(state)

    print("=" * 80)
    print("PROJECT HEALTH REPORT")
    print("=" * 80)

    pprint(result["health_score"].model_dump())

    print("=" * 80)


if __name__ == "__main__":
    test_health_workflow()