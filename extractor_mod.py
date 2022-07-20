from spacy import displacy
from  general_params import SKILL_DB

"""
Need:
1. Annotate
2. Connect to Skill_db
3. Display a dictionary/ json
"""

class extractor_mod:
    def __init__(self, nlp, skills_db, phraseMatcher):

        #params
        self.nlp =  nlp
        self.skills_db = skills_db
        self.phraseMatcher = phraseMatcher

        # Load matchers

        self.matchers = Matchers(
            self.nlp,
            self.skills_db
            self.phraseMatcher
        ).load_matchers()

        #initialize skill getters and utils
        self.skill_getters = SkillsGetter(self.nlp)
        self.utils - Utils(self.nlp, self.skills_db)

        return

    """The function takes in target text returns a skill dictionary"""
    def annotate(self, text:str) -> dict:

        # Create text obj
        text_obj = Text(text, self.nlp)
        # Get matches
        skills_full, text_obj - self.skill_getters.get_full_match_skills(
            text_obj, self.matchers['full_matcher']
        )

