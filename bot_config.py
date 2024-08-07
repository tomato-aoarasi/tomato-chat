# 超级管理员QQ号列表
from datetime import timedelta


super_admin_users = ["114514"]

# 管理员QQ号列表(填写超级管理员自动适配管理员)
admin_users = ["1919810"]

# 开放的群聊
allow_groups = ["893"]

# 模型列表
MODELS = {
    "local": {
        "label": "本地",
        "model": ["llama3.1:latest"],
        "url": "http://localhost:11434", # 填写ollama AI的url
    }
}

# AI的名称
AI_NAME = "tomato"

# 自动水群默认水群概率3%(1-0.97)
SEND_PROBABILITIES = 0.97

# 发表情包的概率
SEND_IMAGE_PROBABILITIES = 0.55

# 情绪图片目录
EMOTION_PIC_PATH = "resources/emotions"

# 脑容量
MAX_MEMORY = 12

# 最大内容
GLOBAL_CTX = 8192
# 不重复率(越高越不重复)
REPEAT_PENALTY = 1.45
# 预测文本段
PREDICT = 128
# 回复是否具有感情(越大感情越丰富)
TEMPERATURE = 0.825

# k,p越大给的答案越百花齐放
TOP = [70, 0.975] # k, p

COMMAND_START = {'y', '!', '！', 'tomato', '/'}

# BOT参数
DEBUG = False
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
# 服务器和端口
HOST = '::'
PORT = 8765
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=1)
SESSION_RUNNING_EXPRESSION = ''
SESSION_RUN_TIMEOUT = timedelta(seconds=1200)