import json, os

from revChatGPT.revChatGPT import Chatbot


class Chatter:
    def __init__(self):
        """Chatter is a wrapper of acheong08's excellent Reverse Engineered ChatGPT"""
        config = {
            "Authorization": str(os.environ.get("OPENAI_AUTH")),
            "session_token": str(os.environ.get("CHATGPT_SESSION1"))+str(os.environ.get("CHATGPT_SESSION2"))
        }
        self.chatbot = Chatbot(config, conversation_id=None)
        return None

    def get_response(self, prompt):
        """Basic ChatGPT query. Give a prompt, get a response.

        Parameters
        ----------
        prompt : str
            the instructions/dialogue provided to ChatGPT
        """
        message = self.chatbot.get_chat_response(prompt)["message"]
        return message

    def parse_job(self, job):
        """Creates a prompt from a job dict

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        prompt = "An example of ".format(tone=job["tone"])

        if job["tone"] in ["excited", "angry"]:
            prompt += "an %s email " % job["tone"]
        elif job["tone"] in ["happy", "sad"]:
            prompt += "a %s email " % job["tone"]
        else:  # includes "neutral"
            prompt += "an email "
        if job["sender"] != "":
            prompt += "from %s " % job["sender"]
        if job["recipient"] != "":
            prompt += "to %s " % job["recipient"]
        if job["subject"] != "":
            prompt += "with the subject line '%s' " % job["subject"]
        if job["topic"] != "":
            prompt += "about %s " % job["topic"]

        while prompt[-1] == " ":
            prompt = prompt[:-1]
        return prompt

    def email_from_job(self, job):
        """Given a job dict, generates an email.

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        prompt = self.parse_job(job)
        message = self.get_response(prompt)
        return message
