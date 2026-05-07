# 极简Agent核心示例 (使用 LangChain + 豆包 API)

# 安装依赖
# pip install langchain langchain-openai langchain-core langchain-community

from langchain.agents import create_agent  # LangChain v0.1+ 通用Agent创建函数
from langchain_openai import ChatOpenAI  # 导入OpenAI模型集成（支持OpenAI兼容API）
from langchain_core.tools import StructuredTool  # 工具定义类

# 1. 定义一个简单的工具
def get_weather(city: str) -> str:
    """获取指定城市天气"""
    # 这里可以替换为真实的天气API调用
    weather_data = {
        "北京": "晴 25°C",
        "上海": "多云 23°C",
        "旧金山": "晴 18°C",
        "纽约": "阴 15°C",
    }
    return f"{city} 的天气是：{weather_data.get(city, '未知')}！"

# 将函数转换为LangChain工具
weather_tool = StructuredTool.from_function(get_weather)
tools = [weather_tool]

# 2. 初始化豆包LLM模型
# 豆包API支持OpenAI兼容格式
model = ChatOpenAI(
    model="doubao-3.5t",  # 豆包3.5T模型
    api_key="XXX",  # 你的豆包API Key
    base_url="https://api.doubao.com/v1",  # 豆包API地址
    temperature=0.1,
    max_tokens=1000,
    timeout=30
)

# 3. 创建Agent（使用简化API）
agent = create_agent(model, tools=tools)

# 4. 调用Agent执行任务
if __name__ == "__main__":
    result = agent.invoke({"input": "旧金山天气如何？"})
    
    # 打印结果
    print("Agent执行结果:")
    print(result)
