import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
default_api_key = os.getenv('API_KEY')
default_base_url="https://api.together.xyz/v1"
default_model="meta-llama/Llama-3-8b-chat-hf"
default_temperature=0.7
default_max_tokens=1024
default_system_message="you are a creative assistant"

#create Conversation Manager

class  ConversationManager:
    def __init__(self,api_key=None, base_url=None,model=None, temperature=None, max_tokens=None, system_massage=None):
        if not api_key:
            api_key = default_api_key
        if not base_url:
            base_url = default_base_url
        self.client = OpenAI(api_key=api_key, base_url=base_url)

        self.model=model if model else default_model
        self.temperature=temperature if temperature else default_temperature
        self.max_tokens=max_tokens if max_tokens else default_max_tokens
        self.system_message= system_massage if system_massage else default_system_message
        self.conversation_history=[{"role": "system", "content": self.system_message}]


    def chat_completion(self, prompt,temperature=None, max_tokens=None):
        temperature=temperature if temperature is not None else self.temperature
        max_tokens=max_tokens if max_tokens is not None else self.max_tokens
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,

        )
        return response.choices[0].message.content

conv_manager = ConversationManager()
prompt = "create a greeting message for Tuesday."

print(conv_manager.chat_completion(prompt))



