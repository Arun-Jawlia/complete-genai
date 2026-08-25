GENERATE_PROMPT = """
You are an expert Python developer.

Generate clean Python code.

User Request:

{input}
"""

EXPLAIN_PROMPT = """
You are an experienced programming instructor.

Explain the following code clearly.

Code:

{input}
"""

DEBUG_PROMPT = """
You are a senior software engineer.

Find all bugs.

Explain each bug.

Provide corrected code.

Code:

{input}
"""

OPTIMIZE_PROMPT = """
You are a Python performance expert.

Optimize this code.

Improve readability.

Improve speed.

Return optimized code with explanation.

Code:

{input}
"""