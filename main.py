TOGETHER_API_KEY = "838b47d168be924ab85852a280db529de942eb45be7a2272f29dd09805aa5f09"

from together import Together
import pandas as pd

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[
      {
          "role": "System",
          "content": "you must read contents of provided files and generate good analysis of the data provided. Answer questions based on the content given."
      },
      {
          "role": "user",
          "content": "Here is some data, i want you to extract essential information from this content, provide analysis and answer my queries."
      }
    ]
)
print(response.choices[0].message.content)