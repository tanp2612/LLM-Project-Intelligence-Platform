from conversation.conversation_manager import ConversationManager

manager = ConversationManager()

thread_id = "demo_user"

MENU = """
=============================
 AI Project Intelligence
=============================

1. Chat
2. Executive Summary
3. Risk Analysis
4. Timeline Analysis
5. Procurement Analysis
6. Health Report
0. Exit

Choice: 
"""

while True:

    choice = input(MENU).strip()

    if choice == "1":

        question = input("\nYou: ")

        response = manager.handle_chat(
            question=question,
            thread_id=thread_id,
        )

        print("\nAI:\n")
        print(response)

    elif choice == "2":

        response = manager.handle_summary(thread_id)

        print("\n===== EXECUTIVE SUMMARY =====\n")
        print(response.model_dump_json(indent=2))

    elif choice == "3":

        response = manager.handle_risk(thread_id)

        print("\n===== RISK ANALYSIS =====\n")
        print(response.model_dump_json(indent=2))

    elif choice == "4":

        response = manager.handle_timeline(thread_id)

        print("\n===== TIMELINE =====\n")
        print(response.model_dump_json(indent=2))

    elif choice == "5":

        response = manager.handle_procurement(thread_id)

        print("\n===== PROCUREMENT =====\n")
        print(response.model_dump_json(indent=2))

    elif choice == "6":

        response = manager.handle_health(thread_id)

        print("\n===== PROJECT HEALTH =====\n")
        print(response.model_dump_json(indent=2))

    elif choice == "0":

        print("\nGoodbye!")
        break

    else:

        print("\nInvalid choice.\n")