# Mercor_hackthon

# Textbase

✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py` and Textbase will take care of the rest :)

Since it is just Python you can use whatever models, libraries, vector databases and APIs you want.

_Coming soon:_

- [ ] PyPI package
- [ ] SMS integration
- [ ] Easy web deployment via `textbase deploy`
- [ ] Native integration of other models (Claude, Llama, ...)

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry shell
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

```bash
poetry run python textbase/textbase_cli.py test main.py
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.

_Simpler version using PyPI package and CLI coming soon!_

# Features
Natural Language Processing: The chatbot responds in a natural, conversational manner.
Context-Awareness: It understands and maintains context throughout the conversation.
Safe Responses: Guardrails are in place to ensure the chatbot doesn't provide harmful or inappropriate advice.
User-Friendly Interface: The front end allows users to interact seamlessly with the chatbot.
# Dependencies
Python (>= 3.10)
Textbase library (Install using pip install textbase)
OpenAI API Key
# Setup
Clone the repository.
Install the required dependencies.
Set up your OpenAI API key in the code. Replace YOUR_API_KEY with your actual API key.
Run the chatbot using the following command: python main.py
# Disclaimer
Create a chatbot to assist users in asking queries about college admissions, programmes, application procedures, qualifications, and scholarships. To produce responses and be able to recognise user inquiries about various admission themes, the chatbot should employ the GPT-3.5 Turbo model. The trick is getting the chatbot to understand user questions and respond in a clear and useful way while merging its responses with accurate and pertinent information from the college admissions office.

# Contributions
Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.



