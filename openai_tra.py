import openai

# 设置您的OpenAI API密钥
openai.api_key = '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'

def translate_text(input_text):
    # 设置您要翻译的源语言和目标语言（从中文到英文）
    source_language = 'zh-CN'
    target_language = 'en'

    # 使用OpenAI进行翻译
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Translate the following {source_language} text to {target_language}:\n\n{input_text}",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        #log_level='info'
    )

    # 提取翻译结果
    translation = response.choices[0].text.strip()

    return translation

# 读取txt文件内容
with open('input.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()
    print("input_text")


# 进行翻译
translated_text = translate_text(input_text)

# 打印翻译结果
print(translated_text)


# Write translated text to file
with open('output.txt', 'w') as file:
    file.write(translated_text)

# Print confirmation message
print('Translation saved to output.txt')

