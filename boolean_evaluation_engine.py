from regex_routines import RegexRoutines

class BooleanEvaluationEngine:
    def __init__(self, token_dict):
        self.__token_dict = token_dict
        self.__regex_routines = RegexRoutines()