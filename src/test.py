import re

from lib.config import ConfigManager

config = ConfigManager()
config.get_user_config()
print(config.paths)

print("Test still working")
