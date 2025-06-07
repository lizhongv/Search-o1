# from openai import OpenAI
# import os
# os.environ['DASHSCOPE_API_KEY'] = "sk-8aef464eb019408f94dc3cc5ef63d46e"

# # 初始化OpenAI客户端
# client = OpenAI(
#     # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )

# messages = [{"role": "user", "content": "9.9和9.11谁大"}]

# completion = client.chat.completions.create(
#     model="qwq-plus",  # 您可以按需更换为其它深度思考模型
#     messages=messages,
#     # enable_thinking 参数开启思考过程，QwQ 与 DeepSeek-R1 模型总会进行思考，不支持该参数
#     # extra_body={"enable_thinking": True},
#     stream=True,
#     stop=["首先", "总结"]
# )

# reasoning_content = ""  # 完整思考过程
# answer_content = ""  # 完整回复
# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")

# for chunk in completion:
#     if not chunk.choices:
#         print("\nUsage:")
#         print(chunk.usage)
#         continue

#     delta = chunk.choices[0].delta

#     # 只收集思考内容
#     if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
#         if not is_answering:
#             print(delta.reasoning_content, end="", flush=True)
#         reasoning_content += delta.reasoning_content

#     # 收到content，开始进行回复
#     if hasattr(delta, "content") and delta.content:
#         if not is_answering:
#             print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
#             is_answering = True
#         print(delta.content, end="", flush=True)
#         answer_content += delta.content



from openai import OpenAI
import os
os.environ['DASHSCOPE_API_KEY'] = "sk-8aef464eb019408f94dc3cc5ef63d46e"

# 初始化OpenAI客户端
client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "9.9和9.11谁大"}]

completion = client.chat.completions.create(
    model="qwq-plus",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    # enable_thinking 参数开启思考过程，QwQ 与 DeepSeek-R1 模型总会进行思考，不支持该参数
    # extra_body={"enable_thinking": True},
    stream=True,
    stop=["首先", "总结"]
)

reasoning_content = ""  # 完整思考过程
answer_content = ""  # 完整回复
is_answering = False  # 是否进入回复阶段

for chunk in completion:
    if not chunk.choices:
        continue

    delta = chunk.choices[0].delta

    # 只收集思考内容
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        reasoning_content += delta.reasoning_content

    # 收到content，开始进行回复
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            is_answering = True
        answer_content += delta.content

# 输出思考过程和最终答案
print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")
print(f"[思考过程]：{reasoning_content}")
print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
print(f"[最终答案]：{answer_content}")