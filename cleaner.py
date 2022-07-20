"""
Class used to clean the input
Need to:
Remove *redundant word, punctuation, extra spaces
Stemming
Lemmatization

"""

from nltk.stem import PorterStemmer
from typing import List
from general_params import LIST_PUNCTUATIONS, GRAM_REDUNDANT


def remove_punctuation(
    text: str, 
    list_punctuations: List[str] = LIST_PUNCTUATIONS
    ) -> str:

    for punc in LIST_PUNCTUATIONS:
        text = text.replace(punc, " ")

    return text.strip()

def remove_redundancy(
    text: str,
    redundant_words: List[str] = GRAM_REDUNDANT
) -> str:

    for phrase in redundant_words:
        text = text.replace(phrase, " ")
    return text.strip()
# rest api take grab data from app to the table (upsert)

def remove_extra_space(
    text: str
) ->str:

    return " ".join(text.split())
# """
# Function to determine the indexes of words in a phrase given a text.
# Returns a list of the indexes of words in phrase. 
# An empty list is returned if phrase is not in text.
# """
# def find_index_phrase(
#     text: str,
#     target: str
# ) ->List:
    
#     if target in text:
#         list_words = text.split()

def lem_text(
    text: str,
    nlp
) ->str:

    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def stem_text(
    text: str,
    stemmer=PorterStemmer()
) -> str:

    return " ".join([stemmer.stem(word) for word in text.split(" ")])


cleaning_func = [
    "remove_punctuation",
    "remove_redundancy",
    "remove_extra_space",
    "lem_text",
    "stem_text"
]

# gather all cleaning functions in a dict
dict_cleaning_functions = {
    "remove_punctuation": remove_punctuation,
    "remove_redundancy": remove_redundancy,
    "remove_extra_space": remove_extra_space,
    "stem_text": stem_text,
    "lem_text": lem_text,
}


class Cleaner:

    """
    Class to build pipeline to clean text
    """

    def __init__(
        self,
        to_lowercase: bool = True,
        include_cleaning_functions: List[str] = cleaning_func,
        exclude_cleaning_function: List[str] = [],
    ):
        """the constructor of the class.
        Parameters
        ----------
        to_lowercase : bool, optional
            whether to lowercase the text before cleaning it, by default True
        include_cleaning_functions : List, optional
            List of cleaning operations to include in the pipeline, by default all_cleaning
        exclude_cleaning_function : List, optional
            List of cleaning operations to exclude for the pipeline, by default []
        """

        # store params
        self.to_lowercase = to_lowercase
        self.include_cleaning_functions = include_cleaning_functions
        self.exclude_cleaning_functions = exclude_cleaning_function

        def __call__(
            self,
            text: str
        ) -> str:
            """To apply the initiallized cleaning pipeline on a given text.
            Parameters
            ----------
            text : str
                text to clean
            Returns
            -------
            str
                returns the text after applying all cleaning operations on it.
            """

            if(self.to_lowercase):
                text = text.lower()

            # perform cleaning while ignoring exclude_cleaning_function
            if len(self.exclude_cleaning_functions):
                for cleaning_name in dict_cleaning_functions.keys():
                    if cleaning_name not in self.exclude_cleaning_functions:
                        text = dict_cleaning_functions[cleaning_name](text)

            # if exclude_cleaning_function was provided then include_cleaning_functions will be ignored
            else:
                for cleaning_name in dict_cleaning_functions.keys():
                    if cleaning_name in self.include_cleaning_functions:
                        text = dict_cleaning_functions[cleaning_name](text)

            return text

