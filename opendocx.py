import docx
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
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
        #log_level='info'
    )

    # 提取翻译结果
    translation = response.choices[0].text.strip()

    return translation

# 打开Word文档
doc = docx.Document('2.docx')

# 遍历所有段落并输出文本,并翻译成英文
for para in doc.paragraphs:
    translated_text = translate_text(para.text)
    print(translated_text)
