from PIL import Image, ImageDraw, ImageFont
import os
import json


def edit_the_New_Year_celebration_painting(
    image_path,
    text,
    font_path,
    font_size,
    font_color,
    expansion_proportion,
    expansion_color,
    save_path,
):
    # 加载图像
    image = Image.open(image_path)

    # 计算新画布尺寸
    expanded_height = int(image.height * expansion_proportion)
    new_canvas = Image.new(
        "RGB", (image.width, expanded_height), expansion_color
    )  # 替换 'your_color_here' 为固定颜色

    # 将原图像复制到新画布的底部
    new_canvas.paste(image, (0, expanded_height - image.height))

    # 添加文本
    draw = ImageDraw.Draw(new_canvas)
    # 设置字体及大小
    font = ImageFont.truetype(font_path, font_size)
    # 设置文本位置
    text_x = new_canvas.width // 15  # 定位到左侧1/15的位置
    text_y = expanded_height - image.height  # 定位到纵向添加块左下角的位置
    draw.text((text_x, text_y), text, fill=font_color, font=font)

    # 保存编辑后的图像
    new_canvas.save(save_path)


def load_variable(config):
    global image_path, font_path, font_size, font_color, save_name, expansion_proportion, expansion_color
    image_path = config["image_path"]
    font_path = config["font_path"]
    font_size = config["font_size"]
    font_color = tuple(config["font_color"])  # JSON中的数组转换为元组
    save_name = config["save_name"]
    expansion_proportion = config["expansion_proportion"]
    expansion_color = tuple(config["expansion_color"])


def load_config():
    default_config = {
        "image_path": "image.pic.jpg",
        "font_path": "原神_达芬奇可识别.ttf",
        "font_size": 55,
        "font_color": [145, 31, 31],
        "save_name": "edited_new_year_greeting_image",
        "expansion_proportion": 1.05,
        "expansion_color": [228, 222, 212],
    }
    try:
        with open("Config.json", "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            # 读取配置文件
            load_variable(config)
    except Exception as e:
        print(f"读取配置文件失败：{e}")
        print("请检查配置文件是否存在或格式是否正确。")
        print("程序将依据默认配置继续执行。")
        print("默认配置：")
        print(default_config)
        print(
            "如需依据默认配置自动覆盖或创建配置文件，请输入'y'，否则输入任意字符不创建配置文件，以默认配置继续程序："
        )
        input_text = input()
        if input_text.lower() == "y":
            with open("Config.json", "w", encoding="utf-8") as config_file:
                json.dump(default_config, config_file, ensure_ascii=False, indent=4)
            print("已覆盖或创建配置文件。")
            load_variable(default_config)
        else:
            print("未覆盖或创建配置文件。")
            print("程序结束。")
            return False
    return True


def input_names():
    # 循环输入人名
    names = []
    while True:
        text = input(
            "请输入要添加的人名，可以空格分割或多行输入，直接按回车继续生成图像："
        )
        if not text:
            print("输入结束。")
            break
        # 将输入的人名按照空格分割并去除可能存在的多余空格
        names = names + text.split()
    return names


def main():
    if not load_config():
        return False
    # 检查image_path是否存在
    if not os.path.exists(image_path):
        print(f"图像文件不存在：{image_path}")
        return False
    # 检查font_path是否存在
    if not os.path.exists(font_path):
        print(f"字体文件不存在：{font_path}")
        return False

    # 输入人名
    names = input_names()
    print("输入的人名为：", names)
    if names:
        # 检查output路径是否存在，不存在就创建
        try:
            if not os.path.exists("output"):
                os.makedirs("output")
        except Exception as e:
            print(f"创建output路径失败：{e}")
            return False
    num = 0
    # 生成图像
    for name in names:
        num += 1
        text = "祝" + name + ":"
        save_path = f"output{os.sep}{num}_{name}_{save_name}.jpg"
        edit_the_New_Year_celebration_painting(
            image_path,
            text,
            font_path,
            font_size,
            font_color,
            expansion_proportion,
            expansion_color,
            save_path,
        )
    return True


global image_path, font_path, font_size, font_color, save_name, expansion_proportion, expansion_color

if __name__ == "__main__":
    if main():
        print("程序执行成功。")
    else:
        print("程序异常结束，请查看报错信息尝试解决或联系开发者。")
    # 让命令行窗口停留
    input("按回车键退出。")
