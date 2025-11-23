# Exercise Description:

# Create a simple multiple-choice quiz game.
# Each question contains:

# a question text
# a list of options
# a correct answer

# The user must type the index of the correct option.
# The program validates input, checks answers, counts the score, and shows the final result.


questions = [
    {
        'question': 'What is 2 + 2?',
        'options': ['1', '3', '4', '5'],
        'answer': '4',
    },
    {
        'question': 'What is 5 * 5?',
        'options': ['25', '55', '10', '51'],
        'answer': '25',
    },
    {
        'question': 'What is 10 / 2?',
        'options': ['4', '5', '2', '1'],
        'answer': '5',
    },
]


def quiz_game():
    score = 0

    for q in questions:
        print(f"Question: {q['question']}")

        options = q['options']
        for i, option in enumerate(options):
            print(f'{i}) {option}')

        user_input = input('Answer: ')
        num_options = len(options)

        # Validate index
        if user_input.isdigit() and int(user_input) < num_options:
            user_input = int(user_input)

            if options[user_input] == q['answer']:
                score += 1
                print('Correct 👍')
            else:
                print('Incorrect ❌')
        else:
            print('Please enter a valid option number!')

        print()

    print(f'You got {score} out of {len(questions)} correct.')


quiz_game()

