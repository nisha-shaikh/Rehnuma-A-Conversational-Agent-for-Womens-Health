## antenatal, what+ ask if first + reply Yes
* greet
    - utter_greet
* antenatal_visit_what_happens
    - utter_antenatal_visit_what_happens_1
    - utter_antenatal_visit_what_happens_2
    - utter_antenatal_visit_what_happens_3
    - utter_ask_first   <!-- predicted: action_listen -->
* affirm
    - utter_antenatal_visit_info_first_time


## antenatal, what+ ask if first + reply No
* greet
    - utter_greet
* antenatal_visit_what_happens
    - utter_antenatal_visit_what_happens_1
    - utter_antenatal_visit_what_happens_2
    - utter_antenatal_visit_what_happens_3
    - utter_ask_first   <!-- predicted: action_listen -->
* deny
    - utter_antenatal_visit_info_first_time


## say goodbye only
* goodbye
    - utter_goodbye   <!-- predicted: utter_performance -->


