from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import ast

# Load the Codegen model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

# Create a pipeline
generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

import ast

def explain_code(code: str) -> str:
    """
    This function takes Python code as input and returns a detailed explanation
    of what the code does.
    """
    try:
        # Parse the Python code into an Abstract Syntax Tree (AST)
        tree = ast.parse(code)

        explanation = []

        # Walk through the AST to explain each node
        for node in ast.walk(tree):
            # Handling variable assignments
            if isinstance(node, ast.Assign):
                explanation.append("This is an assignment statement.")
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        explanation.append(f"Variable `{target.id}` is assigned a value.")
                if isinstance(node.value, ast.Num):
                    explanation.append(f"The value assigned is the number `{node.value.n}`.")
                elif isinstance(node.value, ast.Str):
                    explanation.append(f"The value assigned is the string `{node.value.s}`.")
                elif isinstance(node.value, ast.Name):
                    explanation.append(f"The value assigned is the variable `{node.value.id}`.")

            # Handling function calls (e.g., print)
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "print":
                    explanation.append("The `print()` function is used to output a value to the console.")
                    for arg in node.args:
                        if isinstance(arg, ast.Str):
                            explanation.append(f"The string `{arg.s}` will be printed.")
                        else:
                            explanation.append("A non-string value is being passed to `print()`.")
            
            # Handling if-else statements
            elif isinstance(node, ast.If):
                explanation.append("This is an if-else statement.")
                explanation.append("It evaluates a condition and executes different blocks of code based on whether the condition is true or false.")

            # Handling for loops
            elif isinstance(node, ast.For):
                explanation.append("This is a for loop.")
                explanation.append(f"It will iterate over a sequence. The variable `{node.target.id}` takes the value of each item in the sequence.")
                explanation.append("The loop body will execute for each item in the sequence.")

            # Handling function definitions
            elif isinstance(node, ast.FunctionDef):
                explanation.append(f"Function `{node.name}` is defined.")
                explanation.append(f"This function takes the following parameters: {[arg.arg for arg in node.args.args]}.")

            # Handling return statements
            elif isinstance(node, ast.Return):
                explanation.append("This is a return statement. It returns a value from a function to the caller.")

            # Handling string literals
            elif isinstance(node, ast.Str):
                explanation.append(f"A string is used here: `{node.s}`.")
                
            # Handling numeric literals
            elif isinstance(node, ast.Num):
                explanation.append(f"A number is used here: `{node.n}`.")
                
        if explanation:
            return " ".join(explanation)
        else:
            return "Unable to explain this code."

    except Exception as e:
        return f"⚠️ Error: Could not parse code. Reason: {str(e)}"