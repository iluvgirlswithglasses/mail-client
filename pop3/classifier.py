
from pop3.separator import Separator

class Classifier:
    IMPORTANT = ['urgent', 'asap', 'important', 'action required', 'critical',
                 'priority', 'attention', 'dealine', 'approval required', 'emergency',
                 'important information', 'right now']
    SPAM = ['virus', 'hack', 'crack', 'security alert', 'suspicious activity',
            'unauthorized access', 'account compromise', 'fraud warning', 'phishing attempt',
            'please confirm your identity', 'click here to reset your password', 'verify your account',
            'unusual login activity', 'your account will be suspended', 'bank account verification',
            'important security upadate', 'win a prize', 'win a lottery']
    WORK = ['meeting', 'report', 'project update', 'task', 'collaboration', 'discussion', 'schedule',
            'feedback', 'assignment']
    PROJECT = ['dang@gmail.com']  # can be modify

    @staticmethod
    def contains(response, lst):
        for word in response.split():
            if word in lst:
                return True
        return False

    @staticmethod
    def classify_email(response):
        content, attac = Separator.separate_content(response)

        if Classifier.contains(content, Classifier.PROJECT):
            return "Project"
        if Classifier.contains(content, Classifier.IMPORTANT):
            return "Important"
        if Classifier.contains(content, Classifier.SPAM):
            return "Spam"
        if Classifier.contains(content, Classifier.WORK):
            return "Work"
        return "Inbox"

