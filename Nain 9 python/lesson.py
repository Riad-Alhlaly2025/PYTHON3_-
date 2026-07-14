


# اختبار تفاعلي بلغة بايثون
# يدعم التحقق من الإجابات وإعطاء النتيجة النهائية

def run_quiz():
    questions = [
        {
            "question": "ما نوع البيانات الناتج من العملية: 5 / 2 ؟",
            "options": ["A) int", "B) float", "C) str", "D) bool"],
            "answer": "B"
        },
        {
            "question": "أي من التالي يُستخدم لتعريف دالة في بايثون؟",
            "options": ["A) function", "B) def", "C) func", "D) define"],
            "answer": "B"
        },
        {
            "question": "ما ناتج: len('Python') ؟",
            "options": ["A) 5", "B) 6", "C) 7", "D) خطأ"],
            "answer": "B"
        }
    ]

    score = 0
    print("=== اختبار لغة بايثون ===\n")

    for i, q in enumerate(questions, start=1):
        print(f"سؤال {i}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        answer = input("إجابتك (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✔ إجابة صحيحة!\n")
            score += 1
        else:
            print(f"✘ إجابة خاطئة. الإجابة الصحيحة هي: {q['answer']}\n")

    print(f"نتيجتك النهائية: {score} من {len(questions)}")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nتم إيقاف الاختبار.")
