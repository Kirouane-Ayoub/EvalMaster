import re
from typing import Optional, Tuple


def pairwise_parser_function(
    outputs: str,
) -> Tuple[Optional[bool], Optional[float], Optional[str]]:
    parts = outputs.split("[RESULT]")
    if len(parts) == 2:
        feedback, result = parts[0].strip(), parts[1].strip()
        if result == "A":
            return True, 0.0, feedback
        elif result == "B":
            return True, 1.0, feedback
    return None, None, None


def correctness_parser_function(output_str: str) -> Tuple[float, str]:
    # Pattern to match the feedback and response
    # This pattern looks for any text ending with '[RESULT]' followed by a number
    pattern = r"(.+?) \[RESULT\] (\d)"

    # Using regex to find all matches
    matches = re.findall(pattern, output_str)

    # Check if any match is found
    if matches:
        # Assuming there's only one match in the text, extract feedback and response
        feedback, score = matches[0]
        score = float(score.strip()) if score is not None else score
        return score, feedback.strip()
    else:
        return None, None
