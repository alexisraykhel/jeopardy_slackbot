from typing import List


# todo: maybe use fuzzywuzzy matching library
def find_match(potential_category: str, categories: List[str]):
    """
    When a user asks for a potential_category, rank
    the possible categories by relevance and return the top match

    :param potential_category: str - like "aliens"
    :param categories: list[str] - like ["1950s","American History","alien stories"]
    :return: "alien stories"
    """
    pass