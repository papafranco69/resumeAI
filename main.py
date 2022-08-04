import spacy

from spacy.matcher import PhraseMatcher
from general_params import SKILL_DB
from extractor import SkillExtractor
import json

# from skillNer.general_params import SKILL_DB
# from skillNer.skill_extractor_class import SkillExtractor


nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

JD = """  Work closely with our business partners in sales and trading, 
risk management, compliance, operations, research and other technology teams at Morgan Stanley.
Get deeply involved in testing and deploying strategic and tactical solutions for trading strategies, 
monitoring tools, improving scalability, performance and efficiency of the strategies.
Work with a leading international team which spans the globe
Take a leading position in partnering with senior stakeholders
Bachelor’s degree Computer Science or in other related fields
Proven experience in C++ development
Linux/Unix, Perl, python, Databases
Experience in large scale plant management / operational support / risk management
Experience in the Algo / SOR / Electronic Trading business
Strong communications skills and experience in working with senior stakeholders
People management skills are a nice to have """

"""
results:
'doc_node_value': 'business partner', 'score': 1}, 
'doc_node_value': 'risk management', 'score': 1}, 
'doc_node_value': 'operation research', 'score': 1},
'doc_node_value': 'trading strategy', 'score': 1}, 
 'doc_node_value': 'computer science', 'score': 1},
  'doc_node_value': 'risk management', 'score': 1},
  'doc_node_value': 'electronic trading', 'score': 1},
  'doc_node_value': 'people management', 'score': 1}], 
  'ngram_scored': 
  'doc_node_id': [7], 'doc_node_value': 'sales', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [39], 'doc_node_value': 'scalability', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [78], 'doc_node_value': 'c++', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [80], 'doc_node_value': 'linux', 'type': 'lowSurf', 'score': 1.0, 'len': 1},
  'doc_node_id': [81], 'doc_node_value': 'unix', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [82], 'doc_node_value': 'perl', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [83], 'doc_node_value': 'python', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [88], 'doc_node_value': 'scale', 'type': 'fullUni', 'score': 1, 'len': 1},
  'doc_node_id': [90], 'doc_node_value': 'management', 'type': 'lowSurf', 'score': 1.0, 'len': 1},
'doc_node_id': [90, 91], 'doc_node_value': 'management operational', 'type': 'oneToken', 'score': 0.6, 'len': 2}
'doc_node_id': [90, 91], 'doc_node_value': 'management operational', 'type': 'oneToken', 'score': 0.6, 'len': 2}
'doc_node_id': [104, 105], 'doc_node_value': 'communications skills', 'type': 'oneToken', 'score': 0.5666666666666668, 'len': 2},
'doc_node_id': [118], 'doc_node_value': 'nice', 'type': 'fullUni', 'score': 1, 'len': 1}]}}

"""

test2 = """
Proven track record of delivering products with Unity and C#
Strong understanding of all aspects of the software development lifecycle
Good communicator with the ability to work as part of a team of diverse skillsets
Experience with AR/VR, mobile apps, desktop applications or games
"""

"""
results:
{'full_matches':
doc_node_value': 'c #', 'score': 1}
'doc_node_value': 'software development', 'score': 1}
'doc_node_value': 'mobile app', 'score': 1}],
'ngram_scored':
'doc_node_id': [1], 'doc_node_value': 'track', 'type': 'fullUni', 'score': 1, 'len': 1}
'doc_node_id': [38], 'doc_node_value': 'ar', 'type': 'lowSurf', 'score': 1, 'len': 1

"""

test3 = """
need 

"""
annotations = skill_extractor.annotate(test2)
print(annotations)

# json.dumps(annotations)