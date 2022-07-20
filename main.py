import spacy

from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
import json

import sys

print(sys.path)

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

JD = """At least 2 years hands-on Software Engineering
Experience using Agile practices in a professional or academic environment
Client-facing experience building strong and collaborative client relationships
Understanding of Pivotal Cloud Foundry (PCF)* application development architecture such as microservices and full stack development
Understanding of development frameworks (Spring, ReactJS, AngularJS, NodeJS, Ruby on Rails)  """

annotations = skill_extractor.annotate(JD)
print(skill_extractor.describe(annotations))

print(skill_extractor.display(JD))
# print(annotations)
