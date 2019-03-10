This project include servel train data from real projects
including sanofi supply chain bot and the high talk bot in shanghai xuhui


if you want to train the high talk bot for classification, you can execute the following command
first enter into the root folder , then

python train.py -c sample_configs/config_embedding_bert_intent_classifier.yml --data data/examples/luis/HighTalkSQSWLuisAppStaging-GA-20180824.json --path projects/bert_gongan_v4


