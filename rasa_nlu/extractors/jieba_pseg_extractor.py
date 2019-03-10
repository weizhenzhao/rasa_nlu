from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import warnings

from builtins import str
from typing import Any
from typing import Dict
from typing import Optional
from typing import Text

from rasa_nlu import utils
from rasa_nlu.extractors import EntityExtractor
from rasa_nlu.model import Metadata
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData
from rasa_nlu.utils import write_json_to_file



class JiebaPsegExtractor(EntityExtractor):
    #name = "jieba_pseg_extractor"

    provides = ["entities"]

    defaults = {
        "part_of_speech": ['nr'] # nr：人名，ns：地名，nt：机构名
    }

    def __init__(self, component_config=None):
        # type: (Optional[Dict[Text, Text]]) -> None

        super(JiebaPsegExtractor, self).__init__(component_config)

    def train(self, training_data, config, **kwargs):
        # type: (TrainingData) -> None

        self.component_config = config.for_component_name(self.name, self.defaults)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        extracted = self.add_extractor_name(self.posseg_cut_examples(message))

        message.set("entities", extracted, add_to_output=True)


    def posseg_cut_examples(self, example):
        raw_entities = example.get("entities", [])
        example_posseg = self.posseg(example.text)
        for (item_posseg, start, end) in example_posseg:
            part_of_speech = self.component_config["part_of_speech"]
            for (word_posseg, flag_posseg) in item_posseg:
                if flag_posseg in part_of_speech:
                    raw_entities.append({
                        'start': start,
                        'end': end,
                        'value': word_posseg,
                        'entity': flag_posseg
                    })
        return raw_entities

    @staticmethod
    def posseg(text):
        # type: (Text) -> List[Token]

        import jieba
        import jieba.posseg as pseg

        result = []
        for (word, start, end) in jieba.tokenize(text):
            pseg_data = [(w, f) for (w, f) in pseg.cut(word)]
            result.append((pseg_data, start, end))

        return result

    @classmethod
    def load(cls,
             component_meta,
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[Component]
             **kwargs  # type: **Any
             ):

        meta = model_metadata.for_component_old(cls.name)

        return cls(meta)
