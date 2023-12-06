
from pop3.separator import Separator
from config import Config

class Classifier:
    conf = Config.load()['keywords']

    @staticmethod
    def contains(response, lst):
        for word in response.split():
            if word in lst:
                return True
        return False

    @staticmethod
    def classify_email(response):
        content, attac = Separator.separate_content(response)

        if Classifier.contains(content, Classifier.conf['project']):
            return "Project"
        if Classifier.contains(content, Classifier.conf['important']):
            return "Important"
        if Classifier.contains(content, Classifier.conf['spam']):
            return "Spam"
        if Classifier.contains(content, Classifier.conf['work']):
            return "Work"
        return "Inbox"

