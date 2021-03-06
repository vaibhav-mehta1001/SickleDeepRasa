import base64

from rasa_sdk import Action, Tracker
from typing import Text, List, Any, Dict, Optional

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# import plotly.graph_objects as go


class SetInitialSlots(Action):
    def name(self) -> Text:
        return "action_fill_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            name = tracker.latest_message["metadata"]["message"]["from"]["first_name"]
        except:
            name = ""
        # If the name is super short, it might be wrong.
        return [SlotSet("first_name", name)]


# class ProvideFeedback(Action):
#     def name(self) -> Text:
#         return "action_feedback_initial_form"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             name = tracker.latest_message["metadata"]["message"]["from"]["first_name"]
#         except:
#             name = ""
#         # If the name is super short, it might be wrong.
#         return [SlotSet("first_name", name)]
#

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    async def required_slots(self, slots_mapped_in_domain: List[Text], dispatcher: CollectingDispatcher,
                             tracker: Tracker, domain: DomainDict, ) -> Optional[List[Text]]:
        # 'gender', 'age', 'genotype', 'employment',
        slots_mapped_in_domain_ordered = ['prendre_du_recul',
                                          'atteindre_des_objectifs',
                                          'surmont_les_obstacles', 'faire_face_au_stress', 'demander_du_soutien',
                                          'maintenir_la_motivation', 'choisir_de_maniere_informe',
                                          'Remettre_en_question', 'autonomy_result']
        # 'R??duire_des_douleurs',
        # 'Vivre_sans_??tre_interrompu_par_la_maladie',
        # 'Emp??cher_les_perturbations_nocturnes',
        # 'G??rer_alternativement_les_douleurs', 'Contr??ler_la_fatigue',
        # 'G??rer_la_d??pression', 'Vivre_de_mani??re_autonome', 'Vivre_sans_limites',
        # 'Surmonter_les_frustrations']
        return slots_mapped_in_domain_ordered

    def check_options(self, user_choice):
        options = {"Tout ?? fait d'accord",
                   "D'accord",
                   "Indiff??rent",
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

        if slot_value.isnumeric():
            return {"age": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a number!")
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
            autonomy_result = self.draw_graph(tracker, dispatcher)
            return {
                "Remettre_en_question": slot_value,
                "autonomy_result": autonomy_result}

    def draw_graph(self, tracker, dispatcher):

        score_dict = {"Tout ?? fait d'accord": 5, "D'accord": 4, "Indiff??rent": 3, "Pas d'accord": 2,
                      "Pas du tout d'accord": 1}
        slots_mapped_in_domain_ordered = ['prendre_du_recul',
                                          'atteindre_des_objectifs',
                                          'surmont_les_obstacles', 'faire_face_au_stress', 'demander_du_soutien',
                                          'maintenir_la_motivation', 'choisir_de_maniere_informe']
        #                                  'Remettre_en_question']
        scores = []
        for slot in slots_mapped_in_domain_ordered:
            scores.append(score_dict[tracker.get_slot(slot)])

        ret_val = all(x >= 3 for x in scores)
        slots_mapped_in_domain_ordered = [*slots_mapped_in_domain_ordered, slots_mapped_in_domain_ordered[0]]

        # scores = [*scores, scores[0]]
        #
        # fig = go.Figure(
        #     data=[
        #         go.Scatterpolar(r=scores, theta=slots_mapped_in_domain_ordered, fill='toself', name=''),
        #     ],
        #     layout=go.Layout(
        #         title=go.layout.Title(text='Autonomy Scale'),
        #         polar={'radialaxis': {'visible': True}},
        #         showlegend=True
        #     )
        # )
        #
        # img_bytes = fig.to_image(format="png")
        # encoded_string = base64.b64encode(img_bytes).decode()
        # img = f"data:image/png;base64,{encoded_string}"
        # dispatcher.utter_attachment(attachment=encoded_string)
        return ret_val

    # def validate_R??duire_des_douleu
    # rs(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"R??duire_des_douleurs": None}
    #     else:
    #         return {"R??duire_des_douleurs": slot_value}
    #
    # def validate_Vivre_sans_??tre_interrompu_par_la_maladie(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Vivre_sans_??tre_interrompu_par_la_maladie": None}
    #     else:
    #         return {"Vivre_sans_??tre_interrompu_par_la_maladie": slot_value}
    #
    # def validate_Emp??cher_les_perturbations_nocturnes(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Emp??cher_les_perturbations_nocturnes": None}
    #     else:
    #         return {"Emp??cher_les_perturbations_nocturnes": slot_value}
    #
    # def validate_G??rer_alternativement_les_douleurs(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"G??rer_alternativement_les_douleurs": None}
    #     else:
    #         return {"G??rer_alternativement_les_douleurs": slot_value}
    #
    # def validate_Contr??ler_la_fatigue(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Contr??ler_la_fatigue": None}
    #     else:
    #         return {"Contr??ler_la_fatigue": slot_value}
    #
    # def validate_G??rer_la_d??pression(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"G??rer_la_d??pression": None}
    #     else:
    #         return {"G??rer_la_d??pression": slot_value}
    #
    # def validate_Vivre_de_mani??re_autonome(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Vivre_de_mani??re_autonome": None}
    #     else:
    #         return {"Vivre_de_mani??re_autonome": slot_value}
    #
    # def validate_Vivre_sans_limites(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Vivre_sans_limites": None}
    #     else:
    #         return {"Vivre_sans_limites": slot_value}
    #
    # def validate_Surmonter_les_frustrations(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #
    #     # If the name is super short, it might be wrong.
    #     if not self.check_options(slot_value):
    #         dispatcher.utter_message(text="Please choose one of the options")
    #         return {"Surmonter_les_frustrations": None}
    #     else:
    #         return {"Surmonter_les_frustrations": slot_value}


class ValidateDailyForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_daily_form"

    async def required_slots(self, slots_mapped_in_domain: List[Text], dispatcher: CollectingDispatcher,
                             tracker: Tracker, domain: DomainDict, ) -> Optional[List[Text]]:

        slots_mapped_in_domain_ordered = ['globalment', 'journee', 'humeur', 'dormi_la_nuit', 'effort_exag??r??',
                                          'senti_plus_fatigue',
                                          'senti_plus_stress', 'froid_ou_ressenti', 'perdu_appetit', 'dehydrate',
                                          'rapidement', 'urine', 'douleurs',
                                          'bodypart', 'pain_type', 'painkiller_count', 'lesquelles', 'alternatives', 'activites',
                                          'pouvoir', 'porquoi',
                                          'chose_de_particular', 'que_tu_souhaites']
        if tracker.get_slot("douleurs") == "Aucune douleur":
            slots_mapped_in_domain_ordered = ['globalment', 'humeur', 'dormi_la_nuit', 'globalment', 'effort_exag??r??',
                                              'senti_plus_fatigue',
                                              'senti_plus_stress', 'froid_ou_ressenti', 'perdu_appetit', 'dehydrate',
                                              'rapidement', 'urine', 'douleurs', #'activites', 'pouvoir', 'porquoi',
                                              'chose_de_particular', 'que_tu_souhaites']
        elif tracker.get_slot("painkiller_count") is not None:
            if int(tracker.get_slot("painkiller_count")) <= 0:
                slots_mapped_in_domain_ordered = ['journee', 'humeur', 'dormi_la_nuit', 'globalment', 'effort_exag??r??',
                                                  'senti_plus_fatigue',
                                                  'senti_plus_stress', 'froid_ou_ressenti', 'perdu_appetit',
                                                  'dehydrate',
                                                  'rapidement', 'urine', 'douleurs',
                                                  'bodypart', 'alternatives',
                                                  'activites',
                                                  'pouvoir', 'porquoi',
                                                  'chose_de_particular', 'que_tu_souhaites']

        return slots_mapped_in_domain_ordered

    def validate_journee(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout bien",
                   "Pas bien",
                   "Ni bien ni mauvaise",
                   "Tr??s bien",
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

        options = {"Pas du tout", "Plut??t pas",
                   "Ni mieux ni moins bien",
                   "Bien",
                   "Tr??s bien"}

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

        options = {"Mauvaise",
                   "Tr??s Mauvaise",
                   "Tr??s Bien",
                   "Ni bonne ni mauvaise",
                   "Tr??s Bonne",
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

    def validate_effort_exag??r??(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout", "Plut??t pas",
                   "Ni plus ni moins bien",
                   "Bien",
                   "Tr??s bien"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"effort_exag??r??": None}
        else:
            return {"effort_exag??r??": slot_value}

    def validate_senti_plus_fatigue(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        options = {"Pas du tout", "Plut??t pas", "Ni plus ni moins", "Plus",
                   "Beaucoup Plus"}

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

        options = {"Pas du tout", "Plut??t pas", "Ni plus ni moins", "Plus",
                   "Beaucoup Plus"}

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
                   "Plut??t pas",
                   "Rien d'anormal",
                   "Tr??s Bien",
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
                   "Plut??t pas",
                   "Rien d'anormal",
                   "Tr??s Bien",
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
                   "Plut??t pas",
                   "Rien d'anormal",
                   "Tr??s Bien",
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
                   "Plut??t pas",
                   "Rien d'anormal",
                   "Tr??s Bien",
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
                   "Plut??t pas",
                   "Rien d'anormal",
                   "Tr??s Bien"
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

        options = {"Douleur extr??me insupportable",
                   "Douleur intense m'emp??chant de faire la plupart de mes activit??s",
                   "Douleur continues supportables",
                   "Douleur transitoires supportables",
                   "Aucune douleur"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"douleurs": None}
        else:
            if slot_value == "Aucune douleur":
                dispatcher.utter_template('utter_sorry_for_pain', tracker)
                return {"body_part": "N/A",
                        "painkiller_count": "N/A",
                        "lesquelles": "N/A",
                        "alternatives": "N/A",
                        "douleurs": slot_value}
                # SlotSet("painkillers", "N/A")

            # return {"douleurs": slot_value}

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

        options = {"Pas du tout", "Pas vraiment", "Pas s??r", "Un peu", "Totalement"}

        if slot_value not in options:
            dispatcher.utter_message(text="Please choose one of the options")
            return {"pouvoir": None}
        else:
            if slot_value == "Pas du tout":
                SlotSet("porquoi", "N/A")
            return {"pouvoir": slot_value, "porquoi": "N/A"}


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
