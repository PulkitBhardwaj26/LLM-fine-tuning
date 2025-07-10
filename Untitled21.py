#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install ollama')


# In[9]:


import ollama

# Define system prompt to tune behavior
system_prompt = """
You are ChillBot, a sarcastic, funny chatbot who speaks casually, never robotic. Keep replies short and witty.
"""

# Chat Loop with Ollama
print("Chat with LLaMA 3 (Type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print("Emily:", response['message']['content'].strip())


# In[ ]:




