#pylint: disable = all
from ollama import chat

MODEL_NAME = 'codellama:latest'

def verify_model(prompt):
    try:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            )

        print(response.message.content)
        return True

    except Exception as e:
        print(f'Model verfication failed: {e}')
        return False

if __name__ == '__main__':
    verify_model()