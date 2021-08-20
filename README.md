# SickleDeepRasa
 
 This is the repository for Sickle Deep Chatbot on Rasa in French. Currently we use the DIET classifier and TED for prediction and classification. The input is using CountVectotFeaturizer. For English we can change to SpaCY that will give us better accuracy in the long run, but right now does not make a difference. To deploy using Rasa-X follow the RASA-X tutorial. 
The downside of Rasa-X is that we cannot directly get Telegram ID, I am looking into a work around. 
 
 Otherwise we can always use Rasa Open Source with changes to channels.py in the library, but deployment is harder and not standard.
 
 TODO 
 1) Add SSL server
 2) Add Backend
 3) Question and Answers
 4) English version
 5) Minor French Fixes
