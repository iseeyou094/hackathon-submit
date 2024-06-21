import json
import os

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def is_binary_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # 尝试读取文件内容，检查是否包含非文本字符
            if '\0' in file.read(1024):
                return True
    except Exception as e:
        print(f"Cannot read file {file_path} due to {e}, assuming binary.")
        return True
    return False

def should_ignore(path, filename, config):
    for ignore_path in config['ignore_paths']:
        if ignore_path in path.split(os.sep):
            return True
    for ignore_ext in config['ignore_extensions']:
        if filename.endswith(ignore_ext):
            return True
    return False

def format_file_content(file_path, is_binary):
    # 如果文件是二进制文件，只记录文件名
    if is_binary:
        return f"{file_path}\n- BINARY FILE -\n\n"
    else:
        # 文本文件，记录文件路径及内容，并忽略无法解码的字节
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
            content_with_line_numbers = ''.join(f"{idx + 1}: {line}" for idx, line in enumerate(lines))
            formatted_content = f"{file_path}\n{content_with_line_numbers}\n\n"
        except Exception as e:
            # 如果读取文件时发生了未知错误，记录错误并跳过文件
            formatted_content = f"{file_path}\n- ERROR READING FILE: {e} -\n\n"
        return formatted_content

def traverse_and_extract(project_path, output_path, config):
    with open(output_path, 'w', encoding='utf-8') as output_file:  # 指定UTF-8编码
        for root, dirs, files in os.walk(project_path):
            # 过滤掉忽略配置中的目录
            dirs[:] = [d for d in dirs if not should_ignore(root, d, config)]
            for filename in files:
                # 忽略配置中指定要忽略的文件
                if should_ignore(root, filename, config):
                    continue
                # 不被忽略的文件，将其内容写入输出文件
                file_path = os.path.join(root, filename)
                is_binary = is_binary_file(file_path)
                output_file.write(format_file_content(file_path, is_binary))

# 示例配置，默认所有文件都被遍历，除了配置中忽略的文件类型和路径
config = {
    "ignore_paths": [],
    "ignore_extensions": []
}

# 使用示例
config_file_path = 'config.json'  # 更改为你的配置文件路径
output_file_path = 'output.txt'   # 更改为你的输出文件路径
project_path = './'          # 更改为你的项目目录路径

# 加载配置
config = load_config(config_file_path)

# 提取文件内容并写入到输出文件中
traverse_and_extract(project_path, output_file_path, config)