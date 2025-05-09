import random

class PakFact:
    def __init__(self):
        self.facts = [
            "🇵🇰 Pakistan is the first Muslim country to have nuclear power.",
            "🏔️ It has the world’s second-highest mountain – K2.",
            "🌍 Pakistan has one of the world’s largest irrigation systems.",
            "🔬 Dr. Abdul Qadeer Khan played a key role in making Pakistan a nuclear power, leading the development of the atomic bomb tested on May 28, 1998 in Chagai.",
            "🧪 Dr. Abdus Salam won a Nobel Prize in Physics for Pakistan.",
            "🎓 Pakistan produces over 20,000 IT graduates every year.",
            "🌾 It is the 4th largest producer of cotton in the world."
        ]

    def show_fact(self):
        print("\n🧠 Fact: " + random.choice(self.facts))


app = PakFact()

print("✨ Welcome to PakFact – Know something amazing about Pakistan!")
while True:
    cmd = input("\nPress Enter to get a new fact or type 'q' to quit: ").strip().lower()
    if cmd == 'q':
        print("👋 Khuda Hafiz!")
        break
    app.show_fact()
