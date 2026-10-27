#Student Feedback Sentiment Analysis

print("STUDENT FEEDBACK SENTIMENT ANALYSIS")

feedback = input("Enter student feedback: ")
feedback = feedback.lower()
words = feedback.split()

positive_words = [
    "good", "excellent", "helpful",
    "interesting", "great", "best"
]

negative_words = [
    "bad", "poor", "boring",
    "difficult", "worst", "waste"
]

score = 0

for word in words:
    word = word.strip(".,!?")

    if word in positive_words:
        score += 1
    elif word in negative_words:
        score -= 1

print("\n--- Feedback Analysis ---")
print("Feedback:", feedback)
print("Sentiment score:", score)

if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
