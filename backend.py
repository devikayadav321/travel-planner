import requests 

key=""
def travel_planner():
        landmark = input("Enter a landmark: ")
        destination = input("Enter a destination: ")
        trip_type = input("Enter a trip type (e.g., solo, couple, family): ")

        system_prompt = f"""
        Generate a travel plan for a {trip_type} trip from {landmark} to {destination}. Include recommended activities, places to visit, and any important  tips for travelers with budget.
        """
        url="https://openrouter.ai/api/v1/chat/completions"

        headers = {
                "Authorization":f"Bearer {key}",
                "Content-type":"application/json"
            }

        payload = {
                "model":"deepseek/deepseek-chat",
                "messages":[
                    {"role":"system","content":system_prompt},
                    {"role":"user","content":f"Generate a travel plan for a {trip_type} trip from {landmark} to {destination}. Include recommended activities, places to visit, and any important  tips for travelers with budget."}
                ],
                "temperature":0.7,
            }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
                result  = response.json()
                print(result['choices'][0]['message']['content'])
                    
                      
                    
        else:
                print("error")
      