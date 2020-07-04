## lookup:word
data/word.txt

##lookup:pregnancy_duration
data/duration.txt

## intent:glossary
- What is [1st stage of labor](word)
- What is [stage 1](word)
- What is [first stage](word)
- What is [stage one](word)
- What is [High-risk pregnancy](word)
- What is [High risk pregnancy](word)
- What is [Intrauterine growth restriction (IUGR)](word)
- What is [Mask of pregnancy](word)
- What is [MFM](word)
- Please tell me what is [Afterbirth](word)
- Please tell me what is [Amniotic fluid](word)
- Please tell me what is [Dilation](word)
- What is [Anesthesia](word)
- What is [Areola](word)
- What is [Blighted ovum](word)
- What is [Breech](word)
- What is [Cesarean](word)
- what is [C-Section](word)
- Who is a [midwife](word)
- Who is a [Obstetric anesthetists](word)
- Who is a [Perinatologists](word)
- What is [Cervix](word) 
- What is [Neural tube defect](word)
- What is [Preterm](word)
- What is [Preterm labor](word)
- What is [preterm labor](word)
- What is [Placenta](word)
- What is [placenta](word)
- What is [Toxoplasmosis](word)
- What is [Placental abruption](word)
- What is [Round ligament pain](word)
- what is [Umbilical cord](word)
- what is [Ectopic pregnancy](word)
- what is [External cephalic version](word)
- What is [Lamaze Technique](word)
- Tell me about [anesthesia](word)
- Tell me about [Quickening](word)
- Tell me about [Amniotic fluid](word)
- Tell me about [Down Syndrome](word)
- What is the meaning of [anesthesia](word) 
- What is the meaning of [Braxton Hicks](word)

## synonym:1st stage of labor
- 1st stage 
- first stage
- stage 1
- stage 1 of labor
- stage one
- stage one of labor
- first stage of labor

## synonym:2nd stage of labor
- 2nd stage 
- second stage
- stage 2
- stage 2 of labor
- stage two
- stage two of labor
- second stage of labor

## synonym:3rd stage of labor
- 3rd stage 
- third stage
- stage 3
- stage 3 of labor
- stage three
- stage three of labor
- third stage of labor

## synonym:Cesarean
- C-Section
- C section

## synonym:High-risk pregnancy
- High risk pregnancy
- risky pregnancy

## synonym:Intrauterine growth restriction (IUGR)
- IUGR
- growth restriction

## synonym:MFM
- maternal fetal medicine

## synonym:Obstetric anesthetists
- Obstetric anesthetist
- anesthetist
- anesthetists

## synonym:Perinatologists
- Perinatologist

## synonym:The neural tube
- neural tube
- Neural tube

## synonym:Placenta
- placenta

## synonym:Preterm labor
- preterm labor

## intent: ok
- ok
- okay
- right

## intent: more
- tell me more 
- more
- more information
- more info

## intent: thank
- thanks
- thank you
- thank you so much

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good
- I am fine

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:antenatal_visit_attendant
- Who will I be seeing at my [antenatal appointments](visit_type)?
- Who will be attending to me during my [antenatal appointments](visit_type)?
- My attendant during [appointments](visit_type)?
- Attendant at [hospital visits](visit_type)?
- Who will see me during [hospital visits](visit_type)?
- Will a nurse check me during my [visits](visit_type) or a doctor?
- Who will check me during my [antenatal visits](visit_type:antenatal appointments)?
- Who should I expect to see me during [antenatal care](visit_type:antenatal appointments)?
- Who will be seeing me during [antenatal appointments](visit_type)?


## intent:antenatal_visit_attendee
- Who can come along with me during my [visits](visit_type)?
- Should someone accompany me for [antenatal visits](visit_type:antenatal appointments)?
- Can my [partner](attendee) come along too?
- Can my [partner](attendee) accompany me during my [visits](visit_type)?
- Is my [partner](attendee) allowed to come with me for [antenatal visits](visit_type:antenatal appointments)?
- Should I bring my [husband](attendee) along for [visits](visit_type)?
- Can [father of the child](attendee:father) come along for [antenatal visits](visit_type:antenatal appointments)?
- I want to bring my [Husband](attendee) to my [antenatal visits](visit_type:antenatal appointments).
- Will [father](attendee) of the baby be allowed in [antenatal visits](visit_type:antenatal appointments)?
- Are [fathers](attendee:father) recommended to attend [visits](visit_type) as well?
- Should my [partner](attendee) go on [hospital visits](visit_type) with me?
- Can my [husband](attendee) accompany? 
- Can my [partner](attendee) come with me? 
- Can I bring my [husband](attendee) along? 
- Is it ok to bring [husband](attendee) with me? 
- Would it be okay to bring [husband](attendee)? 
- [Husband](attendee:husband) wants to come with me, is it okay?
- Can I bring my [mother](attendee:family member) to the [visits](visit_type)?
- Will bringing a [friend](attendee) to the [visits](visit_type) be fine?
- May I bring along a [family member](attendee:family member) to the [visits](visit_type)?


## intent:antenatal_visit_frequency
- How many times should I attend [antenatal care](visit_type:antenatal appointments)?
- How frequently should I have [antenatal visits](visit_type:antenatal appointments)?
- How many [antenatal appointments](visit_type) will I have?
- What number of times should i go for [antenatal appointments](visit_type)?
- What is the recommended no. of [visits](visit_type) for me?
- Number of [hospital visits](visit_type) required before giving birth.
- How many times should i see a doctor during pregnancy?
- Frequency of [hospital visits](visit_type) when pregnant.
- Ideal number of [visits](visit_type) when pregnant.
- How many times will I have to [see a doctor](visit_type) when pregnant?
- I am pregnant for the first time. How many times should i [visit the doctor](visit_type)


## intent:antenatal_visit_info_first_time
- What information should I take along when going for my first [antenatal visit](visit_type:antenatal appointments)?
- What should I know before [visiting the hospital](visit_type:hospital visits) for the first time?
- First Antenatal Visit. Tell me what i should know. 
- What is the first [antenatal visit](visit_type:antenatal appointments) about?
- First Antenatal Visit.
- What happens in the first hospital visit?


## intent:antenatal_visit_necessary
- Why should I go for [antenatal care](visit_type:antenatal appointments)?
- Why are [antenatal visits](visit_type:antenatal appointments) necessary?
- Why go to [antenatal appointments](visit_type)?
- What is the importance of [antenatal care](visit_type:antenatal appointments)?
- Are [antenatal appointments](visit_type) important?
- Importance of [antenatal care](visit_type:antenatal appointments)
- [Antenatal care](visit_type:antenatal appointments)'s importance
- Reasons to get [antenatal care](visit_type:antenatal appointments)
- [Antenatal care](visit_type:antenatal appointments)'s advantage
- Is it important to get [antenatal care](visit_type:antenatal appointments) during pregnancy?


## intent:antenatal_visit_not_attend
- I am too busy with work to attend [antenatal clinic](care_from_where), so what should I do?
- What if i can't attend [antenatal clinic](care_from_where)?
- My work schedule doesn't allow me to get [antenatal care](visit_type:antenatal appointments). What to do?
- Can I skip [antenatal visits](visit_type:antenatal appointments)?
- I don't feel the need to [see a doctor](visit_type). 
- I feel perfectly fine, so I can skip my [doctor's appointment](visit_type:see a doctor), right?
- I do not want to go for [antenatal visits](visit_type:antenatal appointments). What to do?
- I am a working woman. I cannot take time for [antenatal care](visit_type:antenatal appointments)

## intent:antenatal_visit_what_happens
- What happens during [antenatal visits](visit_type:antenatal appointments)?
- What happens at your [antenatal visit](visit_type:antenatal appointments)?
- What are [antenatal visits](visit_type:antenatal appointments) about?
- [Antenatal visits](visit_type:antenatal appointments)
- Will I be asked anything during my [antenatal visits](visit_type:antenatal appointments)?
- What to expect during [antenatal care](visit_type:antenatal appointments)?
- What will the [doctor visits](visit_type:antenatal appointments) include?
- I am going to get [antenatal care](visit_type:antenatal appointments). How should I prepare for it?
- I don't have any clue of what happens in [antenatal care](visit_type:antenatal appointments). Tell me something about it. 
- Tell me what happens at [antenatal visits](visit_type:antenatal appointments)

## intent:antenatal_visit_when_start
- When can I go for [antenatal care](visit_type:antenatal appointments)?
- When should I start having [antenatal care](visit_type:antenatal appointments)?
- I found out I am pregnant. Should I start getting [antenatal care](visit_type:antenatal appointments) immediately?
- What is the right time to [see a doctor](visit_type) during pregnancy?
- Should I [see a doctor](visit_type) now that I am pregnant?
- Ideal time to start getting [antenatal care](visit_type)


## intent:baby_due_date
- How do I know my baby's due date?
- When will my baby be born?
- Calculating baby due date.
- Baby will be born when?
- Tell me how to calculate my baby's due date
- When will the fetus be fully formed?
- Due Date Calculator 
- Calculate my due date
- When is the baby due?
- What is my due date?


## intent:baby_growth
- I am [two weeks](pregnancy_duration) pregnant. How grown is my baby?
- [3 week](pregnancy_duration) pregnant. What is my baby's size?
- Growth of my baby in [week 9](pregnancy_duration).
- How grown is my baby in [8 weeks](pregnancy_duration)?
- baby's size in [35 days](pregnancy_duration)
- [4 weeks](pregnancy_duration) of pregnancy. I want to know my baby's size.
- [Two months](pregnancy_duration) pregnant. Tell me how grown my baby is. 
- [14 days](pregnancy_duration) pregnant. What is my fetus size?
- Has my baby grown its ears?
- Does my baby have a beating heart by now?
- baby's size in [week sixth](pregnancy_duration)
- baby's size in [thirty-five days](pregnancy_duration)
- baby's size in [8 weeks](pregnancy_duration)
- baby's size in [eleventh week](pregnancy_duration)
- baby's size in [week ten](pregnancy_duration)
- baby's size in [12 weeks](pregnancy_duration)
- baby's size in [thirteenth week](pregnancy_duration)
- baby's size in [ninety eight days](pregnancy_duration)
- [hundred and five days](pregnancy_duration) pregnant. What is my fetus size?
- [18 weeks](pregnancy_duration) pregnant. What is my fetus size?
- [17 weeks](pregnancy_duration) pregnant. What is my fetus size?
- How grown is my baby in [hundred and twelve days](pregnancy_duration)?
- How grown is my baby in [19 weeks](pregnancy_duration)?
- How grown is my baby in [20 weeks](pregnancy_duration)?
- How big would my baby in [one and a half month](pregnancy_duration)?
- How big would my baby in [hundred and nineteen days](pregnancy_duration)?
- How big would my baby in [first trimester](pregnancy_duration)?
- How big would my baby in [trimester 2](pregnancy_duration)?
- How big would my baby in [trimester 3](pregnancy_duration)?
- I am [21 weeks](pregnancy_duration) pregnant. How grown is my baby?
- I am [22 weeks](pregnancy_duration) pregnant. How grown is my baby?
- I am [23 weeks](pregnancy_duration) pregnant. How grown is my baby?
- I am [24 weeks](pregnancy_duration) pregnant. How grown is my baby?
- I am [twenty-five weeks](pregnancy_duration) pregnant. How grown is my baby?
- [one hundred and seventy-five days](pregnancy_duration) pregnant. What is my fetus size?
- My pregnancy has been [six months old](pregnancy_duration). Update me on my baby's growth. 
- My pregnancy has been [one hundred and eighty-two days](pregnancy_duration) old. Update me on my baby's growth.
- My pregnancy has been [one hundred and eighty-nine days](pregnancy_duration) old. Update me on my baby's growth.


## intent:baby_moves_feel
- During my pregnancy what does my baby's kicking feel like?
- How would I know that my baby is moving?
- Describe baby's motion inside my stomach
- Tell me how babies move inside mothers.
- What would my baby feel like moving?
- How will I know my baby is kicking?
- How does baby kicks feel like?
- What does baby moving inside babies feel like?
- How does babies' motion change during pregnancy?
- Will my baby move differently as time passes?
- As my pregnancy progresses, will my baby's movement change?

## intent:baby_moves_monitor
- Should I monitor my baby's kicking during my pregnancy?
- Is it required of me to monitor baby's motion?
- Should I be checking up on my baby's movement?
- Do baby's irregular motion mean that there is something wrong?
- Is monitoring baby's movements important?
- My baby has started to move. Should I be wary of how it does?
- Is it recommended to keep track of how my baby moves when I am pregnant?
- Do I need to assess my baby's kicks?

## intent:baby_moves_not
- When should you call your doctor about your baby not moving during your pregnancy?
- Should I be worried that my baby is not moving frequently?
- Baby not moving regularly.
- Should I see a doctor if my baby has stopped moving?
- When is the right time to see a doctor if I can't feel my baby move?
- I can't feel my baby kick. Is it a problem?
- I am worried that my baby is not moving. Should I get it checked?
- Is my baby okay in there if it is not moving?
- Do I need to reach out to a doctor if I can't feel my baby kick?
- My baby has stopped moving.
- Baby doesn't kick.

## intent:baby_moves_start
- When during my pregnancy will I feel my baby kicking?
- My baby hasn't started kicking yet. When will it do?
- What is the time when babies start to move?
- How long do I have to wait to feel baby's motion?
- Baby movement start time
- When do babies generally start moving inside the mother?
- When would I feel my baby move for the first time?
- Would I feel my baby's kicks if it is my second time?
- Does baby kicks start early during second pregnancy?

## intent:calcium_amount
- How much calcium do you need during pregnancy?
- Required amount of calcium
- Why do I need to take in calcium if I am pregnant?
- Recommended calcium intake.
- Do I need to consume calcium during pregnancy?
- What amount of calcium is best for me to take?
- Should I take in some calcium?
- Is calcium intake important?
- Calcium intake amount
- Does my body need calcium and how much?

## intent:calcium_foods
- What are calcium-rich foods?
- What foods are high in calcium?
- List foods that contain calcium
- What food items should I take if my body needs calcium?
- My doctor recommended to take in more calcium-rich foods. Can you suggest them?
- I am pregnant and have calcium deficiency. Suggest me in what vegetables I can find them.
- What should be my diet if I have calcium deficiency?
- Diet that increases calcium 
- Best sources of calcium.
- What are some natural sources of calcium?
- Natural supplements of calcium.

## intent:calcium_side_effects
- Are there side-effects to taking calcium while pregnant?
- Disadvantage of consuming calcium supplements.
- Will my health deteriorate if I continue taking calcium?
- I don't feel well with all the calcium pills I have to take. Is it normal?
- Dangers of taking in too much calcium
- What happens if I take too much calcium while being pregnant?
- Is it safe to take calcium when expecting? 
- Can it be harmful to take in a lot of calcium during pregnancy?
- Can consuming too much calcium affect my baby or my pregnancy?
- Does taking in excessive amount of calcium have negative effects on my health?


## intent:calcium_supplements
- What do I need to know about calcium supplements?
- Calcium Supplements
- Tell me something about calcium supplements
- What are some types of calcium supplements?
- Types of calcium sources
- What is the best way to get calcium supplements?
- Artificial Calcium Pills
- Info on Calcium Supplements
- What are calcium supplements?
- Some forms of calcium supplement

## intent:blood_pregnancy_test
- Tell me more about the blood test
- I want to confirm pregnancy through blood test. Tell me something about it. 
- Blood Pregnancy Test
- Can a blood test tell me if I am expecting?
- How does the doctor confirm pregnancy through a blood test?
- Is blood test a reliable way to confirm if I will have a baby?
- How early can I get a blood test for pregnancy?
- Missing my period. Should I get a blood test?
- Will the doctor perform a blood test to check if I am pregnant?
- How reliable is a blood test for pregnancy?
- How does a blood test confirm pregnancy?

## intent:home_pregnancy_test_accuracy
- How do I know if my home pregnancy test is accurate?
- How to ensure accuracy of home pregnancy kit?
- Testing pregnancy at home. How to be sure its correct?
- Correct way to test pregnancy at home
- Making sure that home pregnancy test is reliable.
- Urine test for pregnancy
- Testing pregnancy without going to a doctor. How do I know its correct?


## intent:home_pregnancy_test_how
- How do I carry out a home pregnancy test?
- How to use home pregnancy test?


## intent:pregnancy_confirm
- Am I pregnant?
- Am I expecting?
- How to know if i am pregnant?
- Will I be having a baby?
- How do I test if I am pregnant?
- I missed my periods. Does it mean I am expecting?
- Pregnancy confirmation
- I want to confirm if I am pregnant.
- Am I preggy?
- How to confirm if I am with a child?
- I feel nauseous lately. Can I be expecting a baby?


## intent:pregnancy_test
- Suggests some tests that I can take to confirm that I am pregnant
- Pregnancy test
- Types of pregnancy test
- Tell me what tests confirm pregnancy
- How to test pregnancy?
- What tests are available in the market to be sure that you are pregnant?
- Is it necessary to go see a doctor to confirm pregnancy
- Tests that judge whether you are pregnant

## intent:pregnancy_test_internal_exam
- What happens in an internal examination?
- Internal Exam for pregnancy
- How is internal examination carried out?
- What does a doctor when checking pregnancy through internal examination.
- Apart from blood and urine test, what is the other way to doctors use to confirm if a women is expecting?
- I will be getting an internal examination done. Tell me something about it.
- Give me information on pregnancy confirmation via internal examination.
- Guide me regarding internal examination for pregnancy. 
- How does a doctor check if someone is pregnant without running tests?

## intent:diet_what_to_eat
- What should I eat during pregnancy?
- What can I eat while I am pregnant? 
- What to eat during pregnancy?
- I am pregnant, what should I eat? 
- Which food to eat during pregnancy 
- Which foods are good in pregnancy 
- Good food during pregnancy 
- What should I be eating during pregnancy 
- What should I be eating while I am pregnant? 
- What are some healthy foods to eat? 

## intent:diet_why_change
- Why should I change my diet during pregnancy?
- Why should I alter my diet during pregnancy ? 
- What are the reasons to alter diet during pregnancy? 
- What are the reasons to change diet when I am pregnant 
- What are the reasons to change diet during pregnancy 
- What is the reason to change diet during pregnancy 
- I am pregnant, why should I change diet 
- Why change diet
- Why do I make changes to my diet 
- Why do I make changes to my diet during pregnancy 

## intent:folate_benefits
- What are the benefits of folate intake?
- What are the advantages of folate intake? 
- Why is folate good? 
- Why should I take folate during pregnancy? 
- Is taking folate good for me? 
- How is folate beneficial? 
- Is folate good for health during pregnancy? 
- What is the benefit of folate? 
- Folate benefits 
- folate advantages 

## intent:folate_food_items
- In what food items can I find folate?
- Which food contains folate? 
- Where can I find folate? 
- What food items contain folate? 
- Tell me food that is high in folate 
- Which food has folate? 
- Folate rich food 
- Food high in folate 
- What should I eat for folate intake?
- Food containing folate

## intent:folate_how_to_increase
- How to get more folate?
- What should I do to increase folate?
- What are the ways to increase folate?
- How to consume more folate?
- How to raise folate levels in body?
- How to increase folate?
- Increase folate in body
- How to take more folate?
- Folate increase 
- Ways to increase folate

## intent:folate_when_more
- When would I need to take more folate?
- At what stage would I need to take more folate?
- When is it essential to take more folate? 
- When is more folate intake required? 
- When does the body need more folate? 
- When is it better to take more folate? 
- During pregnancy, when would it be needed to take more folate? 
- During pregnancy, when would it be needed to increase folate intake? 
- When would it be required to increase folate intake? 
- When would it be necessary to have more folate? 


## intent:folic_acid_check_doc
- Should you check with your doctor about your prenatal vitamin?
- Am I supposed to check with my doctor about my medicines?
- Will my doctor help me out with my medication?
- Why should I take advice of my OB for prenatal vitamins intake?
- For what medicines, should I consult a doctor?
- How can consulting a doctor for medication help?


## intent:folic_acid_dose
- What is the recommended dose of folic acid
- How much folic acid should I take? 
- Recommended dose of folic acid 
- Quantity of folic acid intake 
- How much folic acid is good for me 
- What is the appropriate dose of folic acid 
- How much folic acid is good for my body 
- What is a good quantity of folic acid 

## intent:folic_acid_food
- What foods are a good source of folic acid?
- Do cereals have folic acid?
- Is folic acid in beef liver?
- Can I get folic acid from lentils?
- Does spinach have folic acid?
- Are egg noodles a source of folic acid?
- Folic acid in Great Northern beans
- Foods with folic acid
- How much should I eat to get the required folic acid?

## intent:folic_acid_not
- What might happen to your baby if you do not have enough folic acid in your body?
- What are neural tube defects caused by?
- Is folic acid important for my baby's health?
- Do I need folic acid?
- Is a lack of folic acid harmful?
- What is spina bifida?
- What is anencephaly?
- Effect of lack of folic acid on baby

## intent:folic_acid_start_time
- When should you start taking folic acid?
- When do birth defects happen?
- Is it safe to consume folic acid before getting pregnant?
- Can I take folic acid with prenatal vitamins?
- Effect of folic acid on early delivery
- How early can I start taking folic acid?
- Taking folate in the first trimester
- Folic acid in which stage of pregnancy

## intent:folic_acid_take_time
- Why is folic acid taken before and during pregnancy?
- How can I prevent birth defects?
- What should I take along with folic acid?
- Benefits of folic acid
- Should I take folic acid every day?
- Does folic acid prevent birth defects?
- Folic acid and birth defects
- Will folic acid benefit my baby?

## intent:iron_foods
- What foods are high in iron?
- What are examples of iron-rich foods?
- What should I eat to not have iron deficiency?
- Do I need to take iron supplements?
- Can I get iron from plants?
- Sources of iron
- Does meat have iron?
- How can I get iron in my diet?

## intent:iron_increase_tips
- What are some tips for eating iron-rich foods while you're pregnant?
- How can I increase my iron intake?
- I can't get enough iron from my diet.
- Tips to get more iron 
- What foods harm my iron intake?
- Foods that let me get more iron
- Can I get iron from milk?
- Diet changes to increase iron

## intent:iron_why_deficient
- Why can it be hard to get enough iron from food while you're pregnant?
- How can I get more iron as a vegetarian?
- It's difficult to get iron from diet.
- Should I tell my doctor I'm a vegetarian?
- Is it hard to get iron from food during pregnancy?
- Can I get enough iron from my diet?
- I can't get enough iron
- Getting iron from diet

## intent:warning_signs
- What are some warning signs that should be reported immediately during pregnancy?
- What are the danger signs during pregnancy?
- Should I go to the doctor if I have really bad headaches?
- Signs of danger in pregnancy
- Is my pregnancy at risk?
- I have difficulty breathing.
- My abdomen hurts.
- Warning signs to look out for

## intent:warning_signs_anterior_placental
- What are the danger signs associated with anterior placental?
- Is anterior lying placenta normal?
- Can posterior lying placenta be dangerous?
- What is placenta previa?
- What should I do if I have placenta previa?
- Warning signs of anterior placental
- Position of placenta
- Which placenta position is harmful for the baby?

## intent:warning_signs_howto_deal
- What should I do when I encounter any danger signs?
- How can I deal with warning signs?
- What to do when I see any signs of danger?
- Something is wrong with my pregnancy
- My pregnancy is going bad
- How to manage danger signs in pregnancy
- Tips on dealing with pregnancy warning signs


## intent:delivery
- How do I plan for delivery? 
- What measures should I keep in mind before delivery?
- What should I eat when delivery is near?
- How can I keep myself healthy for delivery?
- What should I ask in my antenatal visits?
- Can the expected date of delivery change?
- Can the expected date of labor change?
- Can I make all my decisions for delivery?


## intent:signs_of_labor
- What are some signs of labor?
- How will I know when I'm in labour?
- Can I tell if labour is about to happen soon?
- What are the signs that birth may be on its way?
- Are the signs of labor the same for everyone?
- What is show?
- Is uterine contractions a sign of labor?


## intent:labor_expectation
- What should you expect during the active phase of labor?
- What happens in the active phase of labor?
- What will I feel during the active phase of labor?
- What happens when labor arrives?
- How will my doctor check how far the labor has progressed?
- Why is an IV line inserted when the labor arrives?
 

## intent:labor_pain_drug_free
- What are drug-free approaches to handling labor pain?
- How can I reduce labor pain without using drugs?
- Are there any herbal methods to reduce labour pain?
- What is Lamaze?
- What is the Bradley Method?
- What is the best drug free way to reduce labor pain?
- Will my doctor recommend a drug free approach for reduction of labor pain?
- Is walking a good way to reduce labor pain?
 

## intent:labor_pain_medication
- What are medications for labor pain?
- What are the best medicines that reduce labor pain?
- What medicines should I use for labor pain?
- How does anesthetics work?
- What medicine should I take to reduce pain in my lower body?
- What is the difference between anesthetics and Analgesics?
- Can I still feel things after using analgesics?
- What medicine will work on my whole body to reduce the pain?
 

## intent:premature_labor_symptoms
- What are the symptoms of premature labor?
- What are the signs of premature labour?
- How do I know that I am having premature labor?
- What are the warning signs for premature labor?
- What is a severe lower back pain an indication for?
- What symptoms will I feel when in premature labor?
- Will it be painful if I go into premature labor?


## intent:premature_labor_risk
- What are some of the risk factors associated with pre-term labour/delivery?
- What problems can I go through while having pre-term labour?
- Is pre-term labor risky?
- Will I face any problems if I go into pre-term labor?

## intent:premature_labor
- What happens if you are diagnosed with premature labor?
- What should I do in early labor?
- Any precautions that I need to take for early labor?
- How can I prepare for early labor?
- How does early labor feel?
- How is premature labor treated?
- What is used as a treatment for premature labor?
- Are their medicines to stop labor?


## intent:castor_oil_labor
- Can you use castor oil while pregnant to bring on labor?
- Will using castor oil harm me?
- Is using castor oil useful for bringing labor?
- Is it a good idea to use castor oil to bring on labor?
- Is castor oil recommended to start labor?
- How will I feel after taking a dose of castor oil?
- What are the benefits of castor oil if used for kick-starting the labor?
- What are the disadvantages of castor oil if used for kick-starting the labor?

## intent:labor_feels
- How does labour feel like?
- What are the pains that you feel in labor?
- What are the symptoms of labor?
- What do the symptoms of labor feel like?

## intent:active_labor
- How will I know when I've moved into active labour?
- When do I get into the active labor stage?
- When does the stage of active labor start?
- How do I know active labor has started?
- What are some signs of active labor?
- Active labor signs
- Indicator of active labor
- Is established labor painful?
- Are established labor and active labor the same thing?
- Should I go to the hospital if I am in established labor?
- The established labor phase.

## intent:contractions
- Can I have contractions and not be in labour?
- Is it possible these contractions are not sign of labour?
- Can contractions happen without being in labour?
- What are Braxton Hicks?
- How do I know I am having contractions for real?
- Braxton Hicks
- False alarm 
- What are practice contractions?
- How do I know if my contractions are not practice contractions?
- Practice contractions
- Can my midwife help me figure out if contractions are fake?

##intent: feedback_done

##intent: intro
- What is Rehnuma?
- Who is Rehnuma?
- what is your purpose?
- what do you do?
- Rehnuma
- Rahnuma
- the bot
- Your job.
- Tell me something about yourself
- Introduce yourself
- give me your intro. 


##synonym:2
- 2 weeks
- 2 week
- week 2
- 14 days
- second week
- sec week
- week sec
- fourteen days
- week two
- two weeks
- two week
- half a month

##synonym:3
- 3 weeks
- 3 week
- week 3
- 21 days
- third week
- week third
- week three
- three weeks
- three week
- twenty-one days

##synonym:4
- 4 weeks
- 4 week
- week 4
- 28 days
- four week
- twenty-eight days
- fourth week
- four weeks 
- week four
- almost a month
- almost 1 month

##synonym:5
- 5 weeks
- 5 week
- week 5
- 35 days
- fifth week
- five week
- week fifth
- thirty-five days
- fifth week
- five weeks 
- week five
- over a month 
- 1 month
- a month old
- first month

##synonym:6
- 6 weeks
- 6 week
- week 6
- 42 days
- sixth week
- six week
- week sixth
- forty two days
- six weeks 
- week six
- 1.5 months
- one and a half month

##synonym:7
- 7 weeks
- 7 week
- week 7
- 49 days
- seventh week
- seven week
- week seven
- forty nine days
- seven weeks 
- week seventh

##synonym:8
- 8 weeks
- 8 week
- week 8
- 56 days
- eighth week
- eight week
- week eight
- fifty six days
- eight weeks 
- week eighth
- almost 2 months 
- almost two months 


##synonym:9
- 9 weeks
- 9 week
- week 9
- 63 days
- ninth week
- nine week
- week nine
- sixty three days
- nine weeks
- week nine
- two months
- 2 months
- month 2

##synonym:10
- 10 weeks
- 10 week
- week 10
- 70 days
- tenth week
- ten week
- week ten
- seventy days
- week tenth
- ten weeks 

##synonym:11
- 11 weeks
- 11 week
- week 11
- 77 days
- eleventh week
- eleven week
- week eleven
- seventy seven days
- week eleventh
- eleven weeks

##synonym:12
- 12 weeks
- 12 week
- week 12
- 84 days
- twelfth week
- twelve week
- week twelve
- eighty four days
- week twelfth
- twelve weeks

##synonym:13
- 13 weeks
- 13 week
- week 13
- 91 days
- thirteenth week
- thirteen week
- week thirteen
- ninety one days
- week thirteenth
- thirteen weeks
- second trimester
- 2 trimester
- trimester 2

##synonym:14
- 14 weeks
- 14 week
- week 14
- 98 days
- fourteenth week
- fourteen week
- week fourteen
- ninety eight days
- week fourteenth
- fourteen weeks

##synonym:15
- 15 weeks
- 15 week
- week 15
- 105 days
- fifteenth week
- fifteen week
- week fifteen
- hundred and five days
- week fifteenth
- fifteen weeks

##synonym:16
- 16 weeks
- 16 week
- week 16
- 112 days
- sixteenth week
- sixteen week
- week sixteen
- hundred and twelve days
- week sixteenth
- sixteen weeks

##synonym:17
- 17 weeks
- 17 week
- week 17
- 119 days
- seventeen week
- seventeenth week
- week seventeen
- hundred and nineteen days
- week seventeenth
- seventeen weeks


##synonym:18
- 18 weeks
- 18 week
- week 18
- 126 days
- eighteen week
- eighteenth week
- week eighteen
- week eighteenth
- eighteen weeks
- hundred and twenty six days

##synonym:19
- 19 weeks
- 19 week
- week 19
- 133 days
- nineteen week
- nineteenth week
- week nineteen
- week nineteenth
- nineteen weeks
- hundred and thirty three days

##synonym:20
- 20 weeks
- 20 week
- week 20
- 140 days
- twenty week
- twentieth week
- week twenty
- week twentieth
- twenty weeks
- hundred and forty days

##synonym:21
- 21 weeks
- 21 week
- week 21
- 147 days
- twenty-first week
- twenty-one week
- week twenty-first
- one hundred and forty-seven days
- twenty-first week
- twenty-one weeks
- week twenty-one

##synonym:22
- 22 weeks
- 22 week
- week 22
- 154 days
- twenty-second week
- twenty-two week
- week twenty-second
- one hundred and fifty-four days
- twenty-second week
- twenty-two weeks
- week twenty-two

##synonym:23
- 23 weeks
- 23 week
- week 23
- 161 days
- twenty-third week
- twenty-three week
- week twenty-third
- one hundred and sixty-one days
- twenty-third week
- twenty-three weeks
- week twenty-three

##synonym:24
- 24 weeks
- 24 week
- week 24
- 168 days
- twenty-fourth week
- twenty-four week
- week twenty-fourth
- one hundred and sixty-eight days
- twenty-fourth week
- twenty-four weeks
- week twenty-four

##synonym:25
- 25 weeks
- 25 week
- week 25
- 175 days
- twenty-fifth week
- twenty-five week
- week twenty-fifth
- one hundred and seventy-five days
- twenty-fifth week
- twenty-five weeks
- week twenty-five
- six months old
- 6 months
- sixth month

##synonym:26
- 26 weeks
- 26 week
- week 26
- 182 days
- twenty-sixth week
- twenty-six week
- week twenty-sixth
- one hundred and eighty-two days
- twenty-sixth week
- twenty-six weeks
- week twenty-six

##synonym:27
- 27 weeks
- 27 week
- week 27
- 189 days
- twenty-seventh week
- twenty-seven week
- week twenty-seventh
- one hundred and eighty-nine days
- twenty-seventh week
- twenty-seven weeks
- week twenty-seven

##synonym:28
- 28 weeks
- 28 week
- week 28
- 196 days
- twenty-eighth week
- twenty-eight week
- week twenty-eighth
- one hundred and ninety-six days
- twenty-eighth week
- twenty-eight weeks
- week twenty-eight
- third trimester
- trimester 3
- 3 trimester

##synonym:29
- 29 weeks
- 29 week
- week 29
- 203 days
- twenty-ninth week
- twenty-nine week
- week twenty-ninth
- two hundred and three days
- twenty-ninth week
- twenty-nine weeks
- week twenty-nine
- 7 months
- seven months old
- seventh month

##synonym:30
- 30 weeks
- 30 week
- week 30
- 210 days
- thirtieth week
- thirty week
- week thirtieth
- two hundred and ten days
- thirtieth week
- thirty weeks
- week thirty

##synonym:31
- 31 weeks
- 31 week
- week 31
- 217 days
- thirty-first week
- thirty-one week
- week thirty-first
- two hundred and seventeen days
- thirty-first week
- thirty-one weeks
- week thirty-one

##synonym:32
- 32 weeks
- 32 week
- week 32
- 224 days
- thirty-second week
- thirty-two week
- week thirty-second
- two hundred and twenty-four days
- thirty-second week
- thirty-two weeks
- week thirty-two

##synonym:33
- 33 weeks
- 33 week
- week 33
- 231 days
- thirty-third week
- thirty-three week
- week thirty-third
- two hundred and thirty-one days
- thirty-third week
- thirty-three weeks
- week thirty-three
- eight months old
- 8 months
- eight month

##synonym:34
- 34 weeks
- 34 week
- week 34
- 238 days
- thirty-fourth week
- thirty-four week
- week thirty-fourth
- two hundred and thirty-eight days
- thirty-fourth week
- thirty-four weeks
- week thirty-four

##synonym:35
- 35 weeks
- 35 week
- week 35
- 245 days
- thirty-fifth week
- thirty-five week
- week thirty-fifth
- two hundred and forty-five days
- thirty-fifth week
- thirty-five weeks
- week thirty-five

##synonym:36
- 36 weeks
- 36 week
- week 36
- 252 days
- thirty-sixth week
- thirty-six week
- week thirty-sixth
- two hundred and fifty-two days
- thirty-sixth week
- thirty-six weeks
- week thirty-six

##synonym:37
- 37 weeks
- 37 week
- week 37
- 259 days
- thirty-seventh week
- thirty-seven week
- week thirty-seventh
- two hundred and fifty-nine days
- thirty-seventh week
- thirty-seven weeks
- week thirty-seven
- nine months old
- 9 months
- ninth month
- last month
- final month

##synonym:38
- 38 weeks
- 38 week
- week 38
- 266 days
- thirty-eighth week
- thirty-eight week
- week thirty-eighth
- two hundred and sixty-six days
- thirty-eighth week
- thirty-eight weeks
- week thirty-eight

##synonym:39
- 39 weeks
- 39 week
- week 39
- 273 days
- thirty-ninth week
- thirty-nine week
- week thirty-ninth
- two hundred and seventy-three days
- thirty-ninth week
- thirty-nine weeks
- week thirty-nine

##synonym:40
- 40 weeks
- 40 week
- week 40
- 280 days
- fortieth week
- forty week
- week fortieth
- two hundred and eighty days
- fortieth week
- forty weeks
- week forty

##synonym:41
- 41 weeks
- 41 week
- week 41
- 287 days
- forty-first week
- forty-one week
- week forty-first
- two hundred and eighty-seven days
- forty-first week
- forty-one weeks
- week forty-one

