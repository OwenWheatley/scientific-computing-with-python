def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = ''
    middle_row = ''
    bottom_row = ''
    answer_row = ''

    for problem in problems:
        parts = problem.split()

        # Ensure valid operator
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Ensure operands are digits and not too large
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the width of the problem (longest operand + 2)
        width = max(len(parts[0]), len(parts[2])) + 2

        # Format each row
        top_row += parts[0].rjust(width) + '    '
        middle_row += parts[1] + parts[2].rjust(width - 1) + '    '
        bottom_row += '-' * width + '    '

        # Calculate the answer if required
        if show_answers:
            if parts[1] == '+':
                result = str(int(parts[0]) + int(parts[2]))
            else:
                result = str(int(parts[0]) - int(parts[2]))
            answer_row += result.rjust(width) + '    '

    # Strip the extra spaces at the end and combine the rows
    arranged_problems = top_row.rstrip() + '\n' + middle_row.rstrip() + '\n' + bottom_row.rstrip()
    if show_answers:
        arranged_problems += '\n' + answer_row.rstrip()

    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
