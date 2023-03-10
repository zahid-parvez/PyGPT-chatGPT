# import openai library
import openai

# Set up the OpenAI API client
openai.api_key = "enter_your_secret-API-key_generated_from_openAI_website"

# read the readme.md file to get API key

# this loop will let us ask questions continuously and behave like ChatGPT untill either 'bye' encountered
while True:
    # Set up the model and prompt the user
    model_engine = "text-davinci-003"
    
    prompt = input('Key in the query: ')


    # Generating a response based on prompt
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extracting useful part of response
    response = completion.choices[0].text
    
    # printing response
    print(response)

    #  if this if-cond is placed before geneation of response, the response from openai will not be called 
    # and chat will end up without goobye message 

    if 'bye' in prompt:
        break
