#IOC collection
from OTXv2 import OTXv2, IndicatorTypes
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import json
otx = OTXv2("3e1d17b591d8e946c88e4dd05919eecba708d60c674ab796490d184bfd96e0a1")

# Get the latest pulse in the 'Manufacturing' industry category
# manufacturing_pulses = otx.search_pulses("manufacturing")
# pulse_details = otx.get_pulse_details('63d78854ff0f2e48acb6ab50')

pulses = otx.getall()


with open("ICS_IOCs_updated.json", "w") as f:
    json.dump(pulses, f, indent=4)