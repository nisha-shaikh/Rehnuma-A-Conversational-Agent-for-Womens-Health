## Glossary custom action
* glossary
	- utter_on_it
	- action_get_glossary
	- slot{"word": null}
		

## fallback story
* out_of_scope
  - action_default_fallback


	## GENERAL CONVERSATIONS

## introduction
* intro
  - utter_intro

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

<!-- ## say goodbye only
* goodbye
  - utter_goodbye
 -->
## bot challenge
* bot_challenge
  - utter_iamabot

## bye + ask for rating + yes
* goodbye
	- utter_ask_feedback
* affirm
	- action_feedback


## bye + ask for rating + no
* goodbye
	- utter_ask_feedback
* deny	
	- utter_goodbye
	
## ask more
* more
	- utter_more

## thanks
* thank
	- utter_thank
* affirm
	- utter_help_offer
	
## thanks + not
* thank
	- utter_thank
* deny
	- utter_glad_bye
	
## ok
* ok
	- utter_ok
* affirm
	- utter_help_offer
	
## ok + not
* ok
	- utter_ok
* deny
	- utter_glad_bye

	##BUTTON MAPPING

## feedback done
* feedback_done
	- utter_feedback_done


	
	## ANTENATAL CARE

## story_1
* antenatal_visit_attendant
	- utter_antenatal_visit_attendant_1
	- utter_antenatal_visit_attendant_2
	- utter_antenatal_visit_attendant_3
	- utter_antenatal_visit_attendant_4

## story_2
* antenatal_visit_attendee
	- utter_antenatal_visit_attendee

## story_3
* antenatal_visit_frequency
	- utter_antenatal_visit_frequency_1
	- utter_antenatal_visit_frequency_2
	- utter_antenatal_visit_frequency_3

## story_4
* antenatal_visit_info_first_time
	- utter_antenatal_visit_info_first_time

## story_5
* antenatal_visit_necessary
	- utter_antenatal_visit_necessary

## story_6
* antenatal_visit_not_attend
	- utter_antenatal_visit_not_attend

## story_7
* antenatal_visit_what_happens
	- utter_antenatal_visit_what_happens_1
	- utter_antenatal_visit_what_happens_2
	- utter_antenatal_visit_what_happens_3

## story_8
* antenatal_visit_when_start
	- utter_antenatal_visit_when_start
	 
## inquire_antenatal nec + when start + what happens
* greet
	-utter_greet
* antenatal_visit_necessary
	-utter_antenatal_visit_necessary
* antenatal_visit_when_start
	-utter_antenatal_visit_when_start
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
	
## antenatal, what+ ask if first + reply Yes
* greet
	-utter_greet
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
	-utter_ask_first
* affirm
	-utter_antenatal_visit_info_first_time
	
## antenatal, what+ ask if first + reply No
* greet
	-utter_greet
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
	-utter_ask_first
* deny
	-utter_antenatal_visit_info_first_time	

## antenatal, what+frequency+not attend
* greet 
	-utter_greet
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
* antenatal_visit_frequency
	-utter_antenatal_visit_frequency_1
	-utter_antenatal_visit_frequency_2
	-utter_antenatal_visit_frequency_3
* antenatal_visit_not_attend
	-utter_antenatal_visit_not_attend

## antenatal, ALL
* greet 
	-utter_greet
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
* antenatal_visit_frequency
	-utter_antenatal_visit_frequency_1
	-utter_antenatal_visit_frequency_2
	-utter_antenatal_visit_frequency_3
* antenatal_visit_attendant
	-utter_antenatal_visit_attendant_1
	-utter_antenatal_visit_attendant_2
	-utter_antenatal_visit_attendant_3
	-utter_antenatal_visit_attendant_4
* antenatal_visit_attendee
	-utter_antenatal_visit_attendee
* antenatal_visit_when_start
	-utter_antenatal_visit_when_start
* antenatal_visit_necessary
	-utter_antenatal_visit_necessary
* antenatal_visit_info_first_time
	-utter_antenatal_visit_info_first_time
* antenatal_visit_not_attend
	-utter_antenatal_visit_not_attend
* goodbye
	- utter_ask_feedback

## antenatal with what happens+ thanks + attendant 
* greet
	-utter_greet
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
* thank
	-utter_thank
* affirm
	-utter_help_offer
* antenatal_visit_attendant
	-utter_antenatal_visit_attendant_1
	-utter_antenatal_visit_attendant_2
	-utter_antenatal_visit_attendant_3
	-utter_antenatal_visit_attendant_4

## antenatal with what happens + more + frequency
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
* more
	-utter_more
* antenatal_visit_frequency
	-utter_antenatal_visit_frequency_1
	-utter_antenatal_visit_frequency_2
	-utter_antenatal_visit_frequency_3
	
## antenatal with what happens + more + more + necessary
* antenatal_visit_what_happens
	-utter_antenatal_visit_what_happens_1
	-utter_antenatal_visit_what_happens_2
	-utter_antenatal_visit_what_happens_3
* more
	-utter_more
* more
	-utter_antenatal_visit_necessary
	
	
	## BABY MOVEMENTS

## baby due date
* baby_due_date
	- utter_baby_due_date
	
## baby growth- custom function
* baby_growth
	- action_baby_growth
	
## baby moves feel
* baby_moves_feel
	- utter_baby_moves_feel
	
## baby_moves_monitor
* baby_moves_monitor
	- utter_baby_moves_monitor
	
## baby moves not
* baby_moves_not
	- utter_baby_moves_not
	
## baby_moves_start
* baby_moves_start
	- utter_baby_moves_start

## greet + Baby movements ALL + thank
* greet
	- utter_greet
* baby_moves_not
	- utter_baby_moves_not
* baby_moves_start
	- utter_baby_moves_start
* baby_moves_feel
	- utter_baby_moves_feel
* baby_moves_monitor
	- utter_baby_moves_monitor
* thank
	- utter_thank

## growth + due date + thank
* baby_growth
	- action_baby_growth 
* baby_due_date
	- utter_baby_due_date
* thank	
	- utter_thank
	
## feel +monitor 
* baby_moves_feel
	- utter_baby_moves_feel
* baby_moves_monitor
	- utter_baby_moves_monitor
	
	## CALCIUM

## story 01
* calcium_amount
	- utter_calcium_amount
	
## story 02
* calcium_foods
	- utter_calcium_foods
	
## story 03
* calcium_side_effects
	- utter_calcium_side_effects
	
## story 04
* calcium_supplements
	- utter_calcium_supplements 
	
## story 05
* greet
	- utter_greet
* calcium_foods
	- utter_calcium_foods
* calcium_side_effects
	- utter_calcium_side_effects
* calcium_supplements
	- utter_calcium_supplements
* calcium_amount
	- utter_calcium_amount
	
	## PREGNANCY TESTS

## story 01
* blood_pregnancy_test
	- utter_blood_pregnancy_test 

## story 02
* home_pregnancy_test_accuracy
	- utter_home_pregnancy_test_accuracy 

## story 03
* home_pregnancy_test_how
	- utter_home_pregnancy_test_how_1
	- utter_home_pregnancy_test_how_2 
	
## story 04
* pregnancy_confirm
	- utter_pregnancy_confirm 
	
## story 05
* pregnancy_test
	- utter_pregnancy_test 
	- utter_dont_worry
	
## stoy 06
* pregnancy_test_internal_exam
	- utter_pregnancy_test_internal_exam 

## story 07
* pregnancy_confirm
	- utter_pregnancy_confirm
* pregnancy_test
	- utter_pregnancy_test
	- utter_dont_worry

## story 08
* pregnancy_test
	- utter_pregnancy_test
	- utter_dont_worry
* home_pregnancy_test_how
	- utter_home_pregnancy_test_how_1
	- utter_home_pregnancy_test_how_2
* home_pregnancy_test_accuracy
	- utter_home_pregnancy_test_accuracy
	
		## DIET
		
## story 01
* diet_what_to_eat
	- utter_diet_what_to_eat 
	
## story 02
* diet_why_change
	- utter_diet_why_change
	
## story 03
* diet_what_to_eat
	- utter_diet_what_to_eat
* diet_why_change
	- utter_diet_why_change
	
		## FOLATE

## story 01
* folate_benefits
	- utter_folate_benefits

## story 02  
* folate_food_items
	- utter_folate_food_items

## story 03	
* folate_how_to_increase
	- utter_folate_how_to_increase

## story 04  
* folate_when_more
	- utter_folate_when_more

## story 05  
* folic_acid_check_doc
  - utter_folic_acid_check_doc

## story 06  
* folic_acid_dose
	- utter_folic_acid_dose

## story 07  
* folic_acid_food
	- utter_folic_acid_food

## story 08
* folic_acid_not
	- utter_folic_acid_not

## story 09
* folic_acid_start_time
	- utter_folic_acid_start_time

## story 10
* folic_acid_take_time
	- utter_folic_acid_take_time
	
## story 11
* folate_when_more
	- utter_folate_when_more
* folate_how_to_increase
	- utter_folate_how_to_increase
* folate_food_items
	- utter_folate_food_items
* folate_benefits
	- utter_folate_benefits

## story 12
* folic_acid_take_time
	- utter_folic_acid_take_time
* folic_acid_start_time
	- utter_folic_acid_start_time
* folic_acid_dose
	- utter_folic_acid_dose
* folic_acid_food
	- utter_folic_acid_food
* folic_acid_not
	- utter_folic_acid_not
* folic_acid_check_doc
	- utter_folic_acid_check_doc
		
  
		## IRON
## story 1
* iron_foods
	- utter_iron_foods

## story 2
* iron_increase_tips
	- utter_iron_increase_tips

## story 3  
* iron_supplements_side_effects
	- utter_iron_supplements_side_effects

## story 5  
* iron_why_deficient
	- utter_iron_why_deficient
	
## story 6
* iron_increase_tips
	- utter_iron_increase_tips
* iron_foods
	- utter_iron_foods  
* iron_why_deficient
	- utter_iron_why_deficient
* iron_supplements_side_effects
	- utter_iron_supplements_side_effects

  
		## WARNING SIGNS
## story 1
* warning_signs
	- utter_warning_signs
	- utter_warning_signs_howto_deal

## story 2
* warning_signs_anterior_placental
	- utter_warning_signs_anterior_placental
	- utter_dont_worry

## story 3
* warning_signs_howto_deal
	- utter_warning_signs_howto_deal
  
		## DELIVERY AND LABOR
## story 1
* delivery
	- utter_delivery

## story 2  
* signs_of_labor
	- utter_signs_of_labor

## story 3
* labor_expectation
	- utter_labor_expectation

## story 4
* labor_pain_drug_free
	- utter_labor_pain_drug_free_1
	- utter_labor_pain_drug_free_2
	- utter_labor_pain_drug_free_3

## story 5  
* labor_pain_medication
	- utter_labor_pain_medication	
	
## story 6
* premature_labor_symptoms
	- utter_premature_labor_symptoms
  
## story 6
* premature_labor_risk
	- utter_premature_labor_risk_0              
	- utter_premature_labor_risk_1
	- utter_premature_labor_risk_2
	- utter_premature_labor_risk_3
	- utter_premature_labor_risk_4
	- utter_premature_labor_risk_5
	- utter_premature_labor_risk_6
	- utter_premature_labor_risk_7
	- utter_premature_labor_risk_8
	- utter_premature_labor_risk_9

## story 7  
* premature_labor
	- utter_premature_labor

## story 8  
* castor_oil_labor
	- utter_castor_oil_labor

## story 9  
* labor_feels
	- utter_labor_feels

## story 10
* active_labor
	- utter_active_labor_1
	- utter_active_labor_2
	- utter_active_labor_3

## story 11
* contractions
	- utter_contractions_1
	- utter_contractions_2
	- utter_contractions_3

## story12 labor expectations
* labor_feels
	- utter_labor_feels
* signs_of_labor
	- utter_signs_of_labor
* labor_expectation
	- utter_labor_expectation
* labor_pain_medication
	- utter_labor_pain_medication
* labor_pain_drug_free
	- utter_labor_pain_drug_free_1
	- utter_labor_pain_drug_free_2
	- utter_labor_pain_drug_free_3

## story 13 active labor
* castor_oil_labor
	- utter_castor_oil_labor
* active_labor
	- utter_active_labor_1
	- utter_active_labor_2
	- utter_active_labor_3
* contractions
	- utter_contractions_1
	- utter_contractions_2
	- utter_contractions_3
	
## story 14 premature labor
* premature_labor_symptoms
	- utter_premature_labor_symptoms
* premature_labor
	- utter_premature_labor
* premature_labor_risk
	- utter_premature_labor_risk_0              
	- utter_premature_labor_risk_1
	- utter_premature_labor_risk_2
	- utter_premature_labor_risk_3
	- utter_premature_labor_risk_4
	- utter_premature_labor_risk_5
	- utter_premature_labor_risk_6
	- utter_premature_labor_risk_7
	- utter_premature_labor_risk_8
	- utter_premature_labor_risk_9


