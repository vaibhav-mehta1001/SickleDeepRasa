# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def check_options(self, user_choice):
        options = {"Tout à fait d'accord",
                   "D'accord",
                   "Indifférent",
                    "Pas d'accord",
                    "Pas du tout d'accord"}
        return user_choice in options

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        if slot_value.isnumeric():
            print("fff")
            return {"age": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a number!")
            print("fgfg")
            return {"age": None}

    def validate_prendre_du_recul(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"prendre_du_recul": None}
        else:
            return {"prendre_du_recul": slot_value}

    def validate_atteindre_des_objectifs(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"atteindre_des_objectifs": None}
        else:
            return {"atteindre_des_objectifs": slot_value}

    def validate_surmont_les_obstacles(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"surmont_les_obstacles": None}
        else:
            return {"surmont_les_obstacles": slot_value}

    def validate_faire_face_au_stress(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"faire_face_au_stress": None}
        else:
            return {"faire_face_au_stress": slot_value}

    def validate_demander_du_sotein(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"demander_du_sotein": None}
        else:
            return {"demander_du_sotein": slot_value}

    def validate_maintenir_la_motivation(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"maintenir_la_motivation": None}
        else:
            return {"maintenir_la_motivation": slot_value}

    def validate_choisir_de_maniere_informe(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"choisir_de_maniere_informe": None}
        else:
            return {"choisir_de_maniere_informe": slot_value}

    def validate_Remettre_en_question(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Remettre_en_question": None}
        else:
            return {"Remettre_en_question": slot_value}


    def validate_Réduire_des_douleurs(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Réduire_des_douleurs": None}
        else:
            return {"Réduire_des_douleurs": slot_value}

    def validate_Vivre_sans_être_interrompu_par_la_maladie(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Vivre_sans_être_interrompu_par_la_maladie": None}
        else:
            return {"Vivre_sans_être_interrompu_par_la_maladie": slot_value}

    def validate_Empêcher_les_perturbations_nocturnes(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Empêcher_les_perturbations_nocturnes": None}
        else:
            return {"Empêcher_les_perturbations_nocturnes": slot_value}

    def validate_Gérer_alternativement_les_douleurs(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Gérer_alternativement_les_douleurs": None}
        else:
            return {"Gérer_alternativement_les_douleurs": slot_value}

    def validate_Contrôler_la_fatigue(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Contrôler_la_fatigue": None}
        else:
            return {"Contrôler_la_fatigue": slot_value}

    def validate_Gérer_la_dépression(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Gérer_la_dépression": None}
        else:
            return {"Gérer_la_dépression": slot_value}

    def validate_Vivre_de_manière_autonome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Vivre_de_manière_autonome": None}
        else:
            return {"Vivre_de_manière_autonome": slot_value}

    def validate_Vivre_sans_limites(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Vivre_sans_limites": None}
        else:
            return {"Vivre_sans_limites": slot_value}

    def validate_Surmonter_les_frustrations(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        if not self.check_options(slot_value) :
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Surmonter_les_frustrations": None}
        else:
            return {"Surmonter_les_frustrations": slot_value}


class ActionWarnDry(Action):
    """Informs the user that a plant needs water."""

    def name(self) -> Text:
        return "remind_questionnaire"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hi, just reminding you that you haven't filled in the questionnaire!")

        return []