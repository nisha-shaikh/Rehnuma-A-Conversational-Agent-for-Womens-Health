install mitie
pip install git+https://github.com/mit-nlp/MITIE.git
pip install rasa_nlu[mitie]
(to use mitie pipeline)

run this command:
rasa train
rasa shell
rasa run actions(on another cmd)
rasa run -m models --endpoints endpoint.yml --cors "*" --debug
to convert nlu.json to nlu.md:
rasa data convert nlu --data ./data/nlu.json --out ./data/nlu.md --format md


