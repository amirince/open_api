import openai


openai.api_key = "" # Insert your personal API key here

def open_ai_query(prompt):
        
    # sending promp to LLM via API
    completion = openai.Completion.create( 
        engine='text-davinci-003', # which model of the LLMs to use
        # engine = "gpt-3.5-turbo-0301",
        # model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1024, # number of max tokens supported by the query 
        n=1, # number of responses to return 
        stop=None,
        temperature=0.6, # controls how creative or random the LLM can be with its response higher temp => more randomness and creativity
    )
    message = completion.choices[0].text # getting string reponse from data returned by API
    return message

test = open_ai_query("How many planets are there?")
print(test)