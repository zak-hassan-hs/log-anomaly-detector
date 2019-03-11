class AnomalyFact:
    """
    AnomalyFact

    Core class for anomaly validation
    """

    def __init__(self, predict_id, msg, score=0, anomaly=False):
        """
        Constructor for anomaly fact and listeners that will get triggered if this anomaly is marked as True

        :param msg:
        :param score:
        :param anomaly:
        """
        self._observers = []
        self._predict_id= predict_id
        self._msg=msg
        self._score=score
        self._anomaly=anomaly


    @property
    def predict_id(self):
        return self._predict_id

    @predict_id.setter
    def score(self, predict_id):
        self._predict_id = predict_id


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def anomaly(self):
        return self._anomaly

    @anomaly.setter
    def anomaly(self, anomaly):
        self._anomaly = anomaly
        if self._anomaly == True:
            self.notify(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("error")

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)



class AnomalyFactRecorder:
    def __init__(self,name):
        self.name=name


    def update(self, subject):
        print(" AnomalyFactRecorder {} : {} has score {} is anomaly: {} and predict_id= {} ".format(self.name,subject._msg, subject.score, subject.anomaly, subject.predict_id))
        # TODO: Check Is this really an anomaly?
        #       - HTTP Rest call to anomaly fact-store to see if this was reported as false
        #       - Once it gets a no then we proceed with next step which is

