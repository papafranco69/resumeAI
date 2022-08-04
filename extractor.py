from text_class import Text
from matcher import Matchers, SkillsGetter
from utils import Utils
import json


class SkillExtractor:
    """Main class to annotate skills in a given text.
    """

    def __init__(
        self,
        nlp,
        skills_db,
        phraseMatcher,
    ):
        """Constructor of the class.

        Parameters
        ----------
        nlp : [type]
            NLP object loaded from spacy.
        skills_db : [type]
            A skill database used as a lookup table to annotate skills.
        phraseMatcher : [type]
            A phrasematcher loaded from spacy.
        """

        # params
        self.nlp = nlp
        self.skills_db = skills_db
        self.phraseMatcher = phraseMatcher

        # load matchers: all
        self.matchers = Matchers(
            self.nlp,
            self.skills_db,
            self.phraseMatcher,
        ).load_matchers()

        # init skill getters
        self.skill_getters = SkillsGetter(self.nlp)

        # init utils
        self.utils = Utils(self.nlp, self.skills_db)
        return

    def annotate(
        self,
        text: str,
        tresh: float = 0.5
    ) -> dict:
        """To annotate a given text and thereby extract skills from it.

        Parameters
        ----------
        text : str
            The target text.
        thresh : float, optional
            A threshold used to select skills in case of confusion, by default 0.5

        Returns
        -------
        dict
            returns a dictionnary with the text that was used and the annotated skills (see example).

        Examples
        --------
        >>> import spacy
        >>> from spacy.matcher import PhraseMatcher
        >>> from extractor import SkillExtractor
        >>> from general_params import SKILL_DB
        >>> nlp = spacy.load('en_core_web_sm')
        >>> skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
        >>> text = "Fluency in both english and french is mandatory"
        >>> skill_extractor.annotate(text)
        {'text': 'fluency in both english and french is mandatory',
        'results': {'full_matches': [],
        'ngram_scored': [{'skill_id': 'KS123K75YYK8VGH90NCS',
            'doc_node_id': [3],
            'doc_node_value': 'english',
            'type': 'lowSurf',
            'score': 1,
            'len': 1},
        {'skill_id': 'KS1243976G466GV63ZBY',
            'doc_node_id': [5],
            'doc_node_value': 'french',
            'type': 'lowSurf',
            'score': 1,
            'len': 1}]}}
        """


        # create text object
        text_obj = Text(text, self.nlp)
        # get matches
        skills_full, text_obj = self.skill_getters.get_full_match_skills(
            text_obj, self.matchers['full_matcher'])

        skills_abv, text_obj = self.skill_getters.get_abv_match_skills(
            text_obj, self.matchers['abv_matcher'])

        skills_uni_full, text_obj = self.skill_getters.get_full_uni_match_skills(
            text_obj, self.matchers['full_uni_matcher'])

        skills_low_form, text_obj = self.skill_getters.get_low_match_skills(
            text_obj, self.matchers['low_form_matcher'])

        skills_on_token = self.skill_getters.get_token_match_skills(
            text_obj, self.matchers['token_matcher'])
        full_sk = skills_full + skills_abv
        # process pseudo submatchers output conflicts
        to_process = skills_on_token + skills_low_form + skills_uni_full
        process_n_gram = self.utils.process_n_gram(to_process, text_obj)

        return {
            # 'text': text_obj.transformed_text, 
            'results': {
            'full_matches': full_sk,
            'ngram_scored': [match for match in process_n_gram if match['score'] >= tresh],

            }
        }

