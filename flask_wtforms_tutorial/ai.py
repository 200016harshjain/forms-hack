from os import environ, path
import openai

openai.api_key = environ.get("OPENAI_API_KEY") 

def call_gpt(question, responses):
    joined_responses = ". ".join(responses)

    prompt = f"""
   Given the following responses to the question '{question}':
    {joined_responses}
    Could you provide a one-sentence refined question that would elicit more specific and informative answers?
    """
# Ensure prompt does not contain sensitive user information and is not too large
    if len(prompt) > 2000:
        print("Prompt is too large")
    else:
        # Making API call
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extracting refined question from API response
    refined_question = response.choices[0].text.strip()
    return refined_question