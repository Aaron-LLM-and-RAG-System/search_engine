import openai
import os

# Set your OpenAI API key
openai.api_key = "API_KEY_DO_NOT_MODIFY"


def create_message(role, content):
    return {"role": role, "content": content}


def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the most suitable model, modify if necessary
        messages=messages,
        max_tokens=150,
        temperature=0.1
    )
    return response['choices'][0]['message']


def main():
    initial_message = create_message(
        "user", "I plan to visit Rome. Can you recommend a top sightseeing spot?")
    conversation = [initial_message]

    for _ in range(3):
        response_message = get_response(conversation)
        conversation.append(response_message)
        new_user_message = create_message(
            "user", "Can you recommend another sightseeing spot?")
        conversation.append(new_user_message)

    print(conversation)


if __name__ == "__main__":
    main()
