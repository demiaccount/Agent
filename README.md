# LangChain Agent Demo

这是一个极简的LangChain Agent示例，展示了如何快速创建一个具有工具调用能力的AI Agent。

## 核心概念

### LangChain 是什么？
LangChain 是一个用于构建LLM应用的框架，提供了：
- 强大的Agent系统 (`initialize_agent`)
- 丰富的工具集成
- 灵活的提示词管理
- 支持多种大语言模型

## 快速开始

### 1. 安装依赖
```bash
pip install langchain langchain-openai
```

### 2. 设置API Key

**方法一：使用环境变量（推荐）**
```bash
# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

**方法二：直接在代码中设置**
```python
llm = ChatOpenAI(model="gpt-4o-mini", api_key="your-api-key-here")
```

### 3. 运行示例
```bash
python agent.py
```

## 代码解析

```python
# 1. 定义工具函数
def get_weather(city: str) -> str:
    """获取指定城市天气"""
    return f"{city} 的天气是晴天！"

# 2. 转换为LangChain工具
weather_tool = StructuredTool.from_function(get_weather)

# 3. 创建Agent
agent = initialize_agent(
    tools=[weather_tool],  # 工具列表
    llm=llm,               # 大语言模型
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)

# 4. 调用Agent
result = agent.run("旧金山天气如何？")
```

## ReAct 工作原理

Agent内部执行流程：
1. **思考**：分析用户问题，决定是否需要调用工具
2. **行动**：调用合适的工具获取信息
3. **观察**：接收工具返回的结果
4. **总结**：基于观察结果生成最终回答

## 扩展建议

1. **添加更多工具**
```python
def search_web(query: str) -> str:
    """搜索互联网信息"""
    return f"搜索结果关于: {query}"

search_tool = StructuredTool.from_function(search_web)

agent = initialize_agent(
    tools=[weather_tool, search_tool],
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)
```

2. **支持多轮对话**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

# 多轮对话
agent.run("北京天气如何？")
agent.run("那上海呢？")  # 记得上下文
```

## 注意事项

- 需要有效的OpenAI API Key才能运行
- 确保网络连接正常
- 注意API调用成本

## 相关资源

- LangChain 官方文档: https://python.langchain.com/
- OpenAI API: https://platform.openai.com/