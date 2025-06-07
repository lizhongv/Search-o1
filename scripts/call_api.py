import os
from openai import OpenAI

os.environ['DASHSCOPE_API_KEY'] = "sk-8aef464eb019408f94dc3cc5ef63d46e"
os.environ['DEEPSEEK_API_KEY'] = "sk-56726d885ca64e959be6dfefc5b39312"
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com/v1"
# )

completion = client.chat.completions.create(
    model="qwq-plus",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    # model = "deepseek-reasoner",
    messages=[
        {'role': 'user', 'content': '9.9和9.11谁大'}
    ], 
    stop = ["首先", "总结"],
    stream=True,
)


# 通过reasoning_content字段打印思考过程
print("[思考过程]：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("[最终答案]：")
print(completion.choices[0].message.content)