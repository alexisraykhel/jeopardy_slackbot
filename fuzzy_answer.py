from fuzzywuzzy import fuzz

def check_answer(real_answer, given_answer):
    real_answer_cleaned = real_answer[:real_answer.index("(")] if "(" in real_answer else real_answer

    threshold = 10 ** (2 - (len(real_answer_cleaned.split(" "))) / 20)
    answer_similarity = fuzz.ratio(real_answer_cleaned.lower(), given_answer.lower())

    return answer_similarity >= threshold