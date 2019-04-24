import numpy as np
import random
import time
import cllm_utils

# 你的助手已经收集了他们能够找到的所有恐龙名字，并编入了这个数据集,为了构建字符级语言模型来生成新的名称，
# 你的模型将学习不同的名称模式，并随机生成新的名字。希望这个算法能让你和你的团队远离恐龙的愤怒。

# 数据集与预处理
# 获取名称
data = open("dinos.txt", "r").read()
# 转化为小写字符
data = data.lower()
# 转化为无序且不重复的元素列表
chars = list(set(data))
# 获取大小信息
data_size, vocab_size = len(data), len(chars)
print(chars)
print("共计有%d个字符，唯一字符有%d个"%(data_size,vocab_size))

char_to_ix = {ch:i for i, ch in enumerate(sorted(chars))}
ix_to_char = {i:ch for i, ch in enumerate(sorted(chars))}

print(char_to_ix)
print(ix_to_char)
