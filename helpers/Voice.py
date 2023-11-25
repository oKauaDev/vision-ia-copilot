import pyttsx3
from typing import Optional, Callable

class Voice: 
  engine = pyttsx3.init()
  
  def __init__(self):
    self.engine.connect('finished-utterance', self.on_utterance_finished)
  
  def speak(self, text, callback: Optional[Callable] = None):
    self.callback = callback
    self.engine.say(text)
    self.engine.runAndWait()
  
  def on_utterance_finished(self, name, completed):
    if self.callback is not None:
      if completed and hasattr(self, 'callback') and callable(self.callback):
        self.callback()
        del self.callback