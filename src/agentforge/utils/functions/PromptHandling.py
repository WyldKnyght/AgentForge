import re


class PromptHandling:
    # Define a pattern to find all occurrences of {variable_name}
    pattern = r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}"

    def extract_prompt_variables(self, template):
        # Regular expression to match valid Python variable names inside {}
        return re.findall(self.pattern, template)

    def handle_prompt_template(self, prompt_template, data):
        """Return the template if all its required variables are present in the data and are not empty."""
        if required_vars := self.extract_prompt_variables(prompt_template):
                # Check if all required_vars are in data and not empty
            return prompt_template if all(data.get(var) for var in required_vars) else None
        else:
            return prompt_template

    def render_prompt_template(self, template, data):
        """Replace each variable in the template with its value from data"""

        def replacement_function(match):
            variable_name = match.group(1)  # Extract the variable name from the match
            result = data.get(variable_name, match.group(0))  # Fetch the data or return the original if not found
            return str(result)

        variable_pattern = re.compile(self.pattern)
        prompt = variable_pattern.sub(replacement_function, template)

        return prompt
