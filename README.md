# SickleDeepRasa
 
 This is the repository for Sickle Deep Chatbot on Rasa in French. Currently we use the DIET classifier and TED for prediction and classification. The input is using CountVectotFeaturizer. For English we can change to SpacY that will give us better accuracy in the long run, but right now does not make a difference. To deploy using Rasa-X follow the RASA-X tutorial. 
The downside of Rasa-X is that we cannot directly get Telegram ID, I am looking into a work around.  Otherwise we can always use Rasa Open Source with changes to channels.py in the library, but deployment is harder and not standard. 
The English Branch has the english version. It is not complete yet. 

QnA
For Question and Answers it is decided that we wil have a fixed set questions like an FAQ and an open domain system in case the user's question is not in the FAQ. 
A demo of the Open Domain QnA can be found here (https://colab.research.google.com/drive/1OTBPw2HuI1EOEHa2Yec7huS5jAcuq5px?usp=sharing) to integrate this model will have to be hosted an the endpoint will have to query it. 

Notifications:
For notifications we need to follow this (https://rasa.com/docs/rasa/reaching-out-to-user/) a bulk of which has been implemented. 

Backend:
On the backend, we have to decide what is the way to identify/authenticate users. We are operating with the assumption that Telegram ID is enough, in the long run it may not be. For reads and writes, the code need to be put in actions.py. The tracker dictionary has all the slot values that need to be written. The draw_graph method is a good place to save the daily questionairre results. 

Telegram Integration:
We can integrate straightforwardly. But to get Telegram ID, we need to make the modification here: (https://forum.rasa.com/t/deploy-to-server-with-custom-facebook-connector/30427/2), replacing Telegram with Facebook and overriding the get_metadata() function to return requests.json. 


 TODO 
 1) Add SSL server
 2) Add Backend
 3) Question and Answers
 4) English version
