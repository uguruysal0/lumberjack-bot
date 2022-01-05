from abc import ABC, abstractmethod


class IoProvider(ABC):
    """
    Simplest abstracion for taking screen shot and interaction with keyboard
    """
    @abstractmethod
    def get_screenshot(self):
        pass
    
    @abstractmethod
    def hit_key(self, key, sleep_time):
        """
        Method for hitting keyboard key, it also puts fixed delay between press and rlease events, 
        """
        pass

