from typing import Any, Text, Dict, List, Optional

from rasa_sdk import Action, Tracker
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
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
        if not self.check_options(slot_value):
            dispatcher.utter_message(text="Please choose one of the options")
            return {"Surmonter_les_frustrations": None}
        else:
            return {"Surmonter_les_frustrations": slot_value}


class ValidateDailyForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_daily_form"

    # async def required_slots(
    #         self,
    #         slots_mapped_in_domain: List[Text],
    #         dispatcher: "CollectingDispatcher",
    #         tracker: "Tracker",
    #         domain: "DomainDict",
    # ) -> Optional[List[Text]]:
    #     additional_slots = [tracker.slots.get("douleurs")]
    #     if tracker.slots.get("douleurs") == "Aucune douleur":
    #         # If the user wants to sit outside, ask
    #         # if they want to sit in the shade or in the sun.
    #         # additional_slots.append("pain_type")
    #         additional_slots.append("bodypart")
    #         additional_slots.append("painkiller_count")
    #         additional_slots.append("alternatives")
    #
    #     # additional_slots.append("painkiller_count")
    #     if tracker.slots.get("painkiller_count") != "0" and tracker.slots.get("painkiller_count") is not None:
    #         # additional_slots.append("painkiller_count")
    #         additional_slots.append("lesquelles")
    #
    #     return additional_slots + slots_mapped_in_domain

    def validate_journee(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout bien",
                   "Pas très bien",
                   "Normalement",
                   "Très bien",
                   "Parfaitement bien"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"journee": None}
        else:
            return {"journee": slot_value}

    def validate_dormi_la_nuit(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout bien",
                   "Pas très bien",
                   "Normalement",
                   "Très bien",
                   "Parfaitement bien"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"dormi_la_nuit": None}
        else:
            return {"dormi_la_nuit": slot_value}

    def validate_humeur(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout bien",
                   "Pas très bien",
                   "Très Bien",
                   "Normaleme",
                   "Très Bonne",
                   "Parfaitement bien"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"humeur": None}
        else:
            return {"humeur": slot_value}

    def validate_globalment(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        if not slot_value.isnumeric():
            dispatcher.utter_message(text="Please enter a number")
            return {"globalment": None}
        else:
            return {"globalment": slot_value}

    def validate_effort_exagéré(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"effort_exagéré": None}
        else:
            return {"effort_exagéré": slot_value}

    def validate_senti_plus_fatigue(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"senti_plus_fatigue": None}
        else:
            return {"senti_plus_fatigue": slot_value}

    def validate_senti_plus_stress(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"senti_plus_stress": None}
        else:
            return {"senti_plus_stress": slot_value}

    def validate_froid_ou_resenti(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"froid_ou_resenti": None}
        else:
            return {"froid_ou_resenti": slot_value}

    def validate_perdu_appetit(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"perdu_appetit": None}
        else:
            return {"perdu_appetit": slot_value}

    def validate_dehydrate(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"dehydrate": None}
        else:
            return {"dehydrate": slot_value}

    def validate_rapidement(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"rapidement": None}
        else:
            return {"rapidement": slot_value}

    def validate_urine(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Très Bien"
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"urine": None}
        else:
            return {"urine": slot_value}

    def validate_douleurs(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Douleur extrême insupportable",
                   "Douleur intense m'empêchant de faire la plupart de mes activités",
                   "Douleur continues supportables",
                   "Douleur transitoires supportables",
                   "Aucune douleur"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"douleurs": None}
        else:
            if slot_value != "Aucune douleur":
                SlotSet("body_part", "N/A")
                SlotSet("painkiller_count", "N/A")
                SlotSet("lesquelles", "N/A")
                SlotSet("alternatives", "N/A")
                # SlotSet("painkillers", "N/A")

            return {"douleurs": slot_value}

    def validate_activites(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout",
                   "Pas vraiment",
                   "Rien d'anormal",
                   "Un peu",
                   "Beaucoup"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"activites": None}
        else:
            return {"activites": slot_value}

    def validate_painkiller_count(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        if not slot_value.isnumeric():
            dispatcher.utter_message(text="Please enter a number")
            return {"painkiller_count": None}
        else:
            if int(slot_value) > 0:
                SlotSet("painkillers", None)
            return {"painkiller_count": slot_value}

    def validate_pouvoir(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout", "Pas vraiment", "Pas sûr", "Un peu", "Totalement"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"pouvoir": None}
        else:
            if slot_value == "Pas du tout":
                SlotSet("porquoi", "N/A")
            return {"pouvoir": slot_value}


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
