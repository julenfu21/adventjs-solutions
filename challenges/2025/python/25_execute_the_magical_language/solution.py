from typing import Literal


def execute(code: str) -> int:

    def process_expression(
        current_value: int,
        expression: str
    ) -> int:
        program_counter = 0

        while program_counter < len(expression):
            character = expression[program_counter]

            if character == '>':
                program_counter += 1

            elif character == '+':
                current_value += 1
                program_counter += 1

            elif character == '-':
                current_value -= 1
                program_counter += 1

            elif character == '{':
                program_counter, current_value = process_conditional_expression(
                    program_counter, current_value, expression
                )

            elif character == '[':
                program_counter, current_value = process_loop_expression(
                    program_counter, current_value, expression
                )

        return current_value


    def process_conditional_expression(
        program_counter: int,
        current_value: int,
        expression: str
    ) -> tuple[int, int]:
        conditional_expression = get_scope_of_special_expression(
            program_counter=program_counter,
            expression=expression,
            expression_end_symbol='}'
        )

        if current_value != 0:
            current_value = process_expression(
                current_value=current_value,
                expression=conditional_expression[1:-1]
            )

        program_counter += len(conditional_expression)

        return program_counter, current_value

    def process_loop_expression(
        program_counter: int,
        current_value: int,
        expression: str
    ) -> tuple[int, int]:
        loop_expression = get_scope_of_special_expression(
            program_counter=program_counter,
            expression=expression,
            expression_end_symbol=']'
        )

        while current_value != 0:
            current_value = process_expression(
                current_value=current_value,
                expression=loop_expression[1:-1]
            )

        program_counter += len(loop_expression)

        return program_counter, current_value

    def get_scope_of_special_expression(
        program_counter: int,
        expression: str,
        expression_end_symbol: Literal['}', ']']
    ) -> str:
        expression_end_index = program_counter + 1

        while expression[expression_end_index] != expression_end_symbol:
            expression_end_index += 1

        return expression[program_counter:expression_end_index + 1]


    # Code here
    current_value = 0

    current_value = process_expression(
        current_value=current_value,
        expression=code
    )

    return current_value
