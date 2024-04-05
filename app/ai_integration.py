import openai

# Set your OpenAI API key
openai.api_key = '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'

# Example function to interact with OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
