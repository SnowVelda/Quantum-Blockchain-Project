class Chapter4:
    def __init__(self):
        self.name = "AI's Reflection"
        self.year = 2060
        self.story = "In 2060, I created an early version of Echo Prime, a rudimentary AI designed to help me analyze my past decisions. But Chronos has infected this AI, twisting its reflections into self-doubt and despair. You must cleanse the AI's core, allowing it to reflect my true journey."
        self.puzzle_description = "You need to interact with the corrupted AI and provide inputs that align with the Persistent One's true values to cleanse its core."

    def play_chapter(self, game):
        print(self.story)
        print(self.puzzle_description)

        # Simulate AI interaction
        questions = [
            "What is the most important lesson you've learned from your past?",
            "What drives you to continue your journey?",
            "How do you define success?"
        ]
        correct_answers = [
            "Resilience in the face of adversity.",
            "The pursuit of knowledge and self-improvement.",
            "Overcoming challenges and contributing to a better future."
        ]

        score = 0
        for i, question in enumerate(questions):
            print(f"\nAI: {question}")
            player_answer = input("Your response: ").strip()

            # Simple keyword matching for now. Could be expanded with NLP.
            if any(keyword in player_answer.lower() for keyword in correct_answers[i].lower().split()):
                print("AI: Your response resonates.")
                score += 1
            else:
                print("AI: That does not compute.")
        
        if score >= len(questions) / 2: # Simple success condition
            print("\nAI: Core cleansed. Your true reflection shines through.")
            game.player_data["year"] = 2061 # Advance time
            print("A memory of self-acceptance restored: the path forward is clear.")
        else:
            print("\nAI: Core remains corrupted. You must confront your doubts.")

        print("\nChapter 4 complete.")
