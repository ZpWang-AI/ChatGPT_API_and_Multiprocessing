import openai

from api_key import api_key
openai.api_key = api_key  # TODO: set the api key of openai


def openai_api_chatcompletion(
    content=None,
    messages=None,
    
    engine='gpt-3.5-turbo',
    max_tokens=2048,
    n=1,
    temperature=0.0,
    top_p=1.0,
    presence_penalty=0.0,
    frequency_penalty=0.0,
):
    if messages is None and content is None:
        raise "no content"
    if messages is None:
        messages = [{ "role": "user", "content": content}]
        
    chatcompletion = openai.ChatCompletion.create(
        messages=messages,
        model=engine,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature,
        top_p=top_p,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
    )
    
    response = chatcompletion 
    response_content = chatcompletion['choices'][0]['message']['content']  # get the content only
    return response


if __name__ == '__main__':
    response_ = openai_api_chatcompletion('hello, world!')
    print(response_)
    '''
{
  "id": "chatcmpl-7xwhsxp8QiAmKOEBtSyBRzC4qW6Ha",
  "object": "chat.completion",
  "created": 1694521376,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 11,
    "completion_tokens": 9,
    "total_tokens": 20
  }
}
    '''