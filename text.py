# from the txt file, print the result

import openai


openai.api_key = "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"
filename = 'input.txt'

# store the result from the txt file
with open(filename, 'r') as f:
    text = f.read()
    print(text)

# print(text)
# reset the result.txt file
with open('result.txt', 'w') as f:
    f.write("")

response = openai.Completion.create(
model="text-davinci-003",
prompt=text,
temperature=0,
max_tokens=1000,
top_p=1,
frequency_penalty=0.2,
presence_penalty=0
)
with open('result.txt', 'w') as f:
    f.write(response["choices"][0]["text"] + "\n")


# reset the input.txt file
with open('input.txt', 'w') as f:
    f.write("")




