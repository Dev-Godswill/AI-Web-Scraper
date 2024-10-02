# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# template = (
#     "You are tasked with extracting specific information from the following text content: {dom_content}. "
#     "Please follow these instructions carefully: \n\n"
#     "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
#     "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
#     "3. **Empty Response:** If no information matches the description, return an empty string ('')."
#     "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
# )

# model = OllamaLLM(model="mistral")


# def parse_with_ollama(dom_chunks, parse_description):
#     prompt = ChatPromptTemplate.from_template(template)
#     chain = prompt | model

#     parsed_results = []

#     for i, chunk in enumerate(dom_chunks, start=1):
#         response = chain.invoke(
#             {"dom_content": chunk, "parse_description": parse_description}
#         )
#         print(f"Parsed batch: {i} of {len(dom_chunks)}")
#         parsed_results.append(response)

#     return "\n".join(parsed_results)



import openai

# Set your OpenAI API key
openai.api_key = ''

# Define the template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Function to parse content using OpenAI API
def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        # Construct the prompt using the template
        prompt_text = template.format(dom_content=chunk, parse_description=parse_description)

        # Call the OpenAI API for each chunk using the correct 'openai.ChatCompletion.create' method
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can also use 'gpt-3.5-turbo' for faster/cheaper results
            messages=[{"role": "system", "content": prompt_text}]
        )

        # Extract the response content
        result = response['choices'][0]['message']['content']
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(result.strip())

    return "\n".join(parsed_results)

# Example usage
dom_chunks = [
    "Some content from a webpage to be parsed.",
    "More text content that might contain useful information."
]
parse_description = "Extract all dates mentioned in the content."

# Call the function
parsed_data = parse_with_openai(dom_chunks, parse_description)
print(parsed_data)
