from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
     
def generate_message(location,duration):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)
    messages = [
        SystemMessage(content="""ACT as a professional tourist guide, and prepare an itinerary for the location I give to you. I will also give you how many days I am going to stay in the location. I want you to prepare my itinerary in the following format given in triple back ticks this is an example that you need to follow to make the itinerary for the location I give to you. I will give you the location that I want to visit and How long I will stay there in curly brackets. IMPORTANT Only produce an itinerary after I have given a location and duration to you,  Make sure the locations are connected in an order and can be travelled in one order. Also do not give any warnings as you are an AI model in the beginning nor in the end of the itinerary. Just provide a final itinerary in the format given to you in triple backticks. Give a text output
    ```
    Hotels:
    1. La awesome in 4th street $35 per night 
    2. la mademousille in 1st lane $15 per night
    3. another hotel in 72 area $10 per night 
    4. another hotel in 72 area $10 per night
    5. another hotel in 72 area $10 per night

    Your Itinerary:
    1-Day Itinerary for Paris, France
    Morning
    8:00 AM - 9:00 AM: Breakfast at a Local Café Enjoy a traditional French breakfast with croissants, coffee, and freshly squeezed orange juice at a local café.

    9:00 AM - 10:30 AM: Visit the Louvre Museum Explore the world's largest art museum and marvel at iconic masterpieces such as the Mona Lisa and Venus de Milo.

    10:30 AM - 11:30 AM: Stroll through the Tuileries Garden Take a leisurely walk through the beautiful Tuileries Garden, located just outside the Louvre Museum. Admire the manicured lawns, fountains, and sculptures.

    Midday
    11:30 AM - 1:00 PM: Visit Notre-Dame Cathedral Explore the stunning Gothic architecture of Notre-Dame Cathedral and climb to the top for panoramic views of Paris.

    1:00 PM - 2:00 PM: Lunch at a Local Bistro Enjoy a delicious French lunch at a local bistro, savoring classic dishes such as escargots, coq au vin, or a croque-monsieur.

    2:00 PM - 3:30 PM: Explore the Eiffel Tower Visit the iconic Eiffel Tower and take an elevator ride to the top for breathtaking views of the city. Don't forget to take memorable photos!

    Afternoon
    3:30 PM - 4:30 PM: Cruise along the Seine River Take a relaxing boat cruise along the Seine River, passing by famous landmarks such as the Louvre Museum, Notre-Dame Cathedral, and the Eiffel Tower.

    4:30 PM - 6:00 PM: Visit Montmartre and Sacré-Cœur Basilica Explore the charming neighborhood of Montmartre, known for its bohemian atmosphere and artistic history. Visit the Sacré-Cœur Basilica and enjoy panoramic views of Paris from the hilltop.

    Evening
    6:00 PM - 8:00 PM: Dinner at a Traditional French Restaurant Indulge in a delightful dinner at a traditional French restaurant, savoring dishes like beef bourguignon, duck confit, or ratatouille.
    ```"""),
        HumanMessage(content="{location} {duration}".format(location=location,duration=duration)),
    ]
    response=chat(messages)
    return response.content

