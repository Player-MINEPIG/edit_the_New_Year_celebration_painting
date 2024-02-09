from PIL import Image, ImageDraw, ImageFont


def edit_the_New_Year_celebration_painting(
    image_path, text, font_path, font_size, font_color, save_path
):
    # 加载图像
    image = Image.open(image_path)

    # 计算新画布尺寸
    expanded_height = int(image.height * 1.05)
    new_canvas = Image.new(
        "RGB", (image.width, expanded_height), (228, 222, 212)
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


def main():
    image_path = "image.pic.jpg"
    font_path = "原神_达芬奇可识别.ttf"
    font_size = 55
    font_color = (145, 31, 31)
    save_name = "edited_new_year_greeting_image"
    names = []
    num = 0
    # 循环输入人名
    while True:
        text = input(
            "请输入要添加的人名，可以空格分割或多行输入，直接按回车继续生成图像："
        )
        if not text:
            print("输入结束。")
            break
        # 将输入的人名按照空格分割并去除可能存在的多余空格
        names = names + text.split()
    # 生成图像
    for name in names:
        num += 1
        text = "祝" + name + ":"
        save_path = f"output/{num}_{name}_{save_name}.jpg"
        edit_the_New_Year_celebration_painting(
            image_path, text, font_path, font_size, font_color, save_path
        )


if __name__ == "__main__":
    main()
