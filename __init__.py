from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'artificial'

LOGGER = getLogger(__name__)


class TravelAssistantSkill(MycroftSkill):

    def __init__(self):
        super(TravelAssistantSkill, self).__init__(name="TravelAssistantSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        find_intent = IntentBuilder("HotelSearchIntent").\
            require("VeniceHotelKeywords").build()
        self.register_intent(find_intent, self.handle_find_intent)

    def handle_find_intent(self, message):
        self.speak_dialog("Splendid.Venice.Venezia.Starhotels.Collezione.Price.285.Dollars.Located.in.Venices.designer.shopping.district.this.hotel.is.500.meters.from.Piazza.San.Marco.Address.San.Marco.Mercerie.760.Venice.30124.   
Best Western Titian Inn Hotel Venice Airport Price 127 Dollars Situated near the airport, this hotel is 1 kilometer from Forte Bazzera and 3 and a half kilometers from Ca'Noghera Casino Address Via Orlanda 240 Mestre 30173
Antony Hotel Price 88 Dollars is located 10 minutes by car from the city center and Port of Venice cruise terminal Address Via Orlanda 182 Mestre 30173  
Hilton Molino Stucky Venice Price 538 dollars is located at Isola Della Giudecca 820 Venice 30133 This modern luxurious hotel offers unique panoramic views over Venice and the lagoon and is located on a peaceful surrounding in Venice
Hotel Dei Dragomanni Price 192 is located at San Marco 2711 Venice 30124 Located in San Marco, this hotel is steps from Santa Maria del Giglio and Basilica of Saint Mary of Health.
Best Western Hotel Montecarlo Price 200 is located at Calle Specchieri 463 San Marco Venice 30124 This modernized 17th century building in Venice formerly a convent and a palazzo is 50 meters from Piazza San Marco.
")

    def stop(self):
        pass


def create_skill():
return TravelAssistantSkill()
