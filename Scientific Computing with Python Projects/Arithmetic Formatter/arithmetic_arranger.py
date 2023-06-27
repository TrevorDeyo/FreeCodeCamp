def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''

    # check if the format is correct
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # helper functions
    def contains_letters(problem):
        return any(char.isalpha() for char in problem)

    def contains_multiplication_or_division(problem):
        return "*" in problem or "/" in problem

    def has_number_length_greater_than_four(problem):
        for num in problem.split():
            if len(num) > 4:
                return True
        return False

    # validate the problems
    if contains_letters(" ".join(problems)):
        return 'Error: Numbers must only contain digits.'

    if contains_multiplication_or_division(" ".join(problems)):
        return "Error: Operator must be '+' or '-'."

    if has_number_length_greater_than_four(" ".join(problems)):
        return 'Error: Numbers cannot be more than four digits.'

    # break the problems up into their base elements
    first_numbers = []
    operators = []
    second_numbers = []

    for problem in problems:
        split_problem = problem.split()
        first_numbers.append(split_problem[0])
        operators.append(split_problem[1])
        second_numbers.append(split_problem[2])

    # build the rows
    top_row = ""
    bottom_row = ""
    dash_row = ""
    answer_row = ""

    for i in range(len(problems)):
        first_num = first_numbers[i]
        operator = operators[i]
        second_num = second_numbers[i]

        # Calculate the answer
        if operator == "+":
            answer = str(int(first_num) + int(second_num))
        elif operator == "-":
            answer = str(int(first_num) - int(second_num))

        # Determine the length of the longest number
        max_len = max(len(first_num), len(second_num))

        # Format the rows
        top_row += f"{first_num:>{max_len+2}}    "
        bottom_row += f"{operator} {second_num:>{max_len}}    "
        dash_row += f"{'-'*(max_len+2)}    "
        answer_row += f"{answer:>{max_len+2}}    "

    # Remove extra spaces at the end of each row
    top_row = top_row.rstrip()
    bottom_row = bottom_row.rstrip()
    dash_row = dash_row.rstrip()
    answer_row = answer_row.rstrip()

    # Concatenate the rows
    arranged_problems = f"{top_row}\n{bottom_row}\n{dash_row}"

    # Include the answer row if show_answers is True
    if show_answers:
        arranged_problems += f"\n{answer_row}"

    return arranged_problems