import re

VALID_SUBJECTS = {'Grammar', 'Physics', 'Chemistry', 'Maths', 'Mathematics'}
VALID_OPTIONS = {'A', 'B', 'C', 'D'}
VALID_DIFFICULTIES = {'High', 'Medium', 'Hard', 'Advanced'}

def normalize_question_text(text: str) -> str:
    """
    Normalizes text by lowercasing, removing punctuation, and stripping extra spaces
    to enable strict duplicate detection.
    """
    if not text:
        return ""
    cleaned = text.lower()
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def validate_question_data(q_data: dict, existing_normalized_texts: set = None) -> tuple:
    """
    Validates a question data dictionary according to system requirements:
    - Exactly 4 non-empty options.
    - correct_option is 'A', 'B', 'C', or 'D'.
    - Question is not empty and not duplicate.
    - Explanation is provided.
    - Subject and difficulty are valid.
    
    Returns (is_valid: bool, reason: str)
    """
    question_text = q_data.get('question_text', '').strip()
    if not question_text:
        return False, "Question text cannot be empty."

    norm_text = normalize_question_text(question_text)
    if existing_normalized_texts is not None and norm_text in existing_normalized_texts:
        return False, f"Duplicate question detected: '{question_text[:40]}...'"

    opt_a = str(q_data.get('option_a', '')).strip()
    opt_b = str(q_data.get('option_b', '')).strip()
    opt_c = str(q_data.get('option_c', '')).strip()
    opt_d = str(q_data.get('option_d', '')).strip()

    if not opt_a or not opt_b or not opt_c or not opt_d:
        return False, "Every question must have exactly 4 non-empty options."

    options = [opt_a, opt_b, opt_c, opt_d]
    if len(set(options)) < 4:
        return False, "Question options must be distinct (no duplicate options allowed)."

    correct_option = q_data.get('correct_option', '').strip().upper()
    if correct_option not in VALID_OPTIONS:
        return False, f"Invalid correct_option '{correct_option}'. Must be 'A', 'B', 'C', or 'D'."

    explanation = q_data.get('explanation', '').strip()
    if not explanation:
        return False, "Explanation must be provided for every question."

    subject = q_data.get('subject', '').strip()
    if subject and subject not in VALID_SUBJECTS:
        return False, f"Invalid subject '{subject}'."

    difficulty = q_data.get('difficulty', 'High').strip()
    if difficulty and difficulty not in VALID_DIFFICULTIES:
        return False, f"Invalid difficulty '{difficulty}'."

    return True, "Valid"
