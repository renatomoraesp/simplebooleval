import re

class RegexRoutines:
    def _evaluate_boolean_expression(self, expression, values):
        for key in values:
            # Use a regular expression to find all occurrences of the key in the expression
            pattern = r"\b" + re.escape(key) + r"\b"
            quoted_key = self._wrap_substring_in_quotes(str(
                values[key])) if not isnumber(values[key]) else str(values[key])
            expression = re.sub(pattern, quoted_key, expression)s
        return expression

    def _wrap_substring_in_quotes(self, substring):
        # Use a regular expression to find the substring in the string
        if not (substring[0] == "'" and substring[-1] == "'"):
            # Wrap the substring in single quotes
            substring = "'" + substring + "'"
        return substring

    def _evaluate_comparisons(expression, values):
        # Use a regular expression to find all numerical comparisons in the expression
        pattern = r"(\b[a-zA-Z0-9_]+\b) *([<>=]+|[<>]=) *(\d+)"
        matches = re.finditer(pattern, expression)
        for match in matches:
            left_operand, operator, right_operand = self.__get_operators_and_operands(match)
            # Replace the comparison with the result of its evaluation
            if left_operand in values:
                result = eval(f"{values[left_operand]} {operator} {right_operand}")
                expression = expression.replace(match.group(0), str(result))
            else:
                expression = expression.replace(match.group(0), 'False')
        return expression

    def __get_operators_and_operands(self, match):
        return match.group(1), match.group(2), int(match.group(3))