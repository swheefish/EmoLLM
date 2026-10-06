import os
from langchain_openai import ChatOpenAI


def get_glm(
        model_name='deepseek-chat',              # ← 改模型
        api_base="https://api.deepseek.com",     # ← 改地址
        temprature=0.7,
        streaming=False,
    ):
    """用 DeepSeek 替代智谱"""

    llm = ChatOpenAI(
        model_name=model_name,
        openai_api_base=api_base,
        openai_api_key=os.getenv("DEEPSEEK_API_KEY"),  # ← 用环境变量
        streaming=streaming,
        temperature=temprature
    )

    return llm