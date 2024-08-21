import tensorflow as tf
import numpy as np
import json
from transformers import BertTokenizer, GPT2LMHeadModel,TextGenerationPipeline
import opencc


def poem_generate(name):
    tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-poem")  # 下載 GPT2 模型
    model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-poem")
    text_generator = TextGenerationPipeline(model, tokenizer)   
    temp = text_generator(name, max_length=50, do_sample=True)  # 輸出長度為 50 的句子
    converter = opencc.OpenCC('s2t.json')
    poem = converter.convert(temp[0]['generated_text'])  # 轉成繁體中文

    return poem