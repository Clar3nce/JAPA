import xml.etree.ElementTree as ET

class CONFIG:

    local_server_ip = ""
    local_server_port = 6666
    remote_interface = ""
    remote_interface_token = ""
    command_identifier = ""
    priv_level = 2

    def __init__(self):
        self.data = []

def load_Default_Config(configPath):
    c = CONFIG()

    config = ET.parse(configPath)
    config_root = config.getroot()


    c.local_server_ip = config_root.find("./local_serv/local_ip").text
    c.local_server_port = config_root.find("./local_serv/local_port").text

    c.remote_interface = config_root.find("./remote_interface").attrib
    c.remote_interface_token = config_root.find("./remote_interface/bot_token").text
    c.command_identifier = config_root.find("./remote_interface/command_identifier").text

    c.priv_level = config_root.find("./security/priv_level").text

    return c




default_config_path = "configuration/config.xml"

config = load_Default_Config(default_config_path)

print(config.remote_interface_token)
print(config.command_identifier)



