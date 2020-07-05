# Rehnuma: A Conversational Agent for Women's Health
This repository contains code base for the titled Final Year (Kaavish) Project.
### Abstract 
This project aims to make it easier for Pakistani women to understand their health without the fear of being judged. For this purpose, we have developed a chatbot called Rehnuma. It is based on the RASA framework and is hosted on a web app so that it can be accessed from any device. The chatbot is restricted to the domain of maternity for this project, but it can be scaled to the general domain of women’s health by changing the dataset provided for training. The chatbot works well for queries that are similar to the ones in its training set. With the integration of interactive learning, its performance could be enhanced to work for diﬀerent queries as well.
### Team:
- Reeba Aslam - ra02528@st.habib.edu.pk
- Nisha Shaikh - ns02530@st.habib.edu.pk
- Abeera Tariq - at02787@st.habib.edu.pk
- Mir Mehdi Ali Baqri - mb03027@st.habib.edu.pk
### Supervisor
* Dr. Syeda Saleha Raza, 
Assistant Professor - Computer Science,
Dhanani School of Science and Engineering,
Habib University


### Required Packages

Following python libraries are required to setup the RASA framework used by model and action server in the sub-directory 1. Rehnuma Bot:

    rasa == 1.7.0
    rasa-nlu == 0.15.1
    rasa-sdk == 1.7.0
    Pyrebase == 3.0.27
    Pandas
    
The model was created and trained on Windows 10, so version specifications may differ depending on OS and any updates by RASA.  
To setup the web application have installed Angular and Node.js on your system.

### Running model and action server
##### Model 
Open command prompt in the 1. Rehnuma Bot  directory and run the following command:

    rasa run -m models --endpoints endpoints.yml --cors "*" --debug

##### Action 
Open command prompt in the 1. Rehnuma Bot  directory and run the following command:

    rasa run actions
    
##### Training
If you want to train the bot, run the following command in the same directory:

    rasa train

### Running Angular Web Application
Open command prompt in the dashboard folder in the 2. Rehnuma App directory and run the following commands:

    npm install
    npm start

To chat with the bot using the application on local host, change socketURL to the port on which RASA model is running on. 
Run the model and action server before opening the application. 

### Deployed URL
You can chat with the deployed model in this repository at https://chatbot-6cdf9.web.app/

    

