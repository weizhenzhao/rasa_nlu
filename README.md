
# Supply Chain Bot for intent classification<br>
This project include servel trainning data from real projects<br>
including sanofi supply chain bot and the high talk bot in shanghai xuhui<br>


## Trainning with bert model<br>

#### First <br>

you should clone the Tecent's bert as service project or pip install it directly<br>
```
pip install bert-serving-server<br>
pip install bert-serving-client<br>
```


#### Second <br>
Download the bert's Chinese model from the following link<br>

[bert_Chinese_model](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)


#### Thirdly<br>
Start the Bert serving to load the high talk data sets for classification<br>
```
bert-serving-start -model_dir D:\chinese_L-12_H-768_A-12 -num_worker=1<br>
```




#### Fourth<br>
train rasa nlu with the bert words vectors
```
python train.py -c sample_configs/config_embedding_bert_intent_classifier.yml --data data/examples/luis/HighTalkSQSWLuisAppStaging-GA-20180824.json --path projects/bert_gongan_v4
```

#### Lastly
an example video with chatbot for reference

[![Watch the video](https://github.com/weizhenzhao/rasa_nlu/raw/master/QQ截图20190310111321.png)](https://github.com/weizhenzhao/rasa_nlu/raw/master/speech.mp4)

