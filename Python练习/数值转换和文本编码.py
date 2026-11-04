
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_base(base):
    """检查进制是否在 2~36 之间"""
    if base < 2 or base > 36:
        raise ValueError("进制必须在 2 到 36 之间")


def decimal_to_base(n, base):
    """十进制整数 n 转成 base 进制字符串"""
    check_base(base)

    if n == 0:
        return "0"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(DIGITS[r])

    return sign + "".join(reversed(result))


def base_to_decimal(s, base):
    """base 进制字符串 s 转成十进制整数"""
    check_base(base)

    s = s.strip().upper()
    if not s:
        raise ValueError("输入不能为空")

    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]

    if not s:
        raise ValueError("输入格式错误")

    value = 0
    for ch in s:
        if ch not in DIGITS:
            raise ValueError(f"非法字符：{ch}")

        digit = DIGITS.index(ch)
        if digit >= base:
            raise ValueError(f"字符 {ch} 不属于 {base} 进制")

        value = value * base + digit

    return sign * value


def text_to_hex(text, encoding):
    """文本编码为十六进制字符串，并返回字节数"""
    data = text.encode(encoding)
    hex_str = data.hex(" ").upper()
    return hex_str, len(data)


def hex_to_text(hex_text, encoding):
    """十六进制字符串解码为文本"""
    clean = "".join(hex_text.split())

    if len(clean) % 2 != 0:
        raise ValueError("十六进制字符串长度必须为偶数")

    data = bytes.fromhex(clean)
    return data.decode(encoding)


def show_ord_chr(text):
    """显示字符的 ord / chr 信息"""
    for ch in text:
        code = ord(ch)
        print(f"字符：{ch!r}  ord={code}  十六进制=0x{code:X}  chr({code})={chr(code)!r}")


def main():
    while True:
        print("\n========== 数制转换与文本编码 ==========")
        print("1. 十进制 -> 其他进制")
        print("2. 其他进制 -> 十进制")
        print("3. 文本编码为十六进制字节")
        print("4. 十六进制字节解码为文本")
        print("5. 查看 ord() / chr() 信息")
        print("0. 退出")

        choice = input("请选择功能：").strip()

        try:
            if choice == "0":
                print("程序结束。")
                break

            elif choice == "1":
                n = int(input("请输入十进制整数：").strip())
                base = int(input("请输入目标进制（2~36）：").strip())
                result = decimal_to_base(n, base)
                print(f"转换结果：{result}")

            elif choice == "2":
                s = input("请输入数字字符串：").strip()
                base = int(input("请输入原进制（2~36）：").strip())
                result = base_to_decimal(s, base)
                print(f"十进制结果：{result}")

            elif choice == "3":
                text = input("请输入文本：")
                encoding = input("请输入编码（utf-8/gbk/ascii，默认 utf-8）：").strip().lower()
                if not encoding:
                    encoding = "utf-8"

                hex_str, byte_count = text_to_hex(text, encoding)
                print(f"编码：{encoding}")
                print(f"字节数：{byte_count}")
                print(f"十六进制字节：{hex_str}")

            elif choice == "4":
                hex_text = input("请输入十六进制字节（可带空格）：").strip()
                encoding = input("请输入编码（utf-8/gbk/ascii，默认 utf-8）：").strip().lower()
                if not encoding:
                    encoding = "utf-8"

                text = hex_to_text(hex_text, encoding)
                print(f"解码结果：{text}")

            elif choice == "5":
                text = input("请输入文本：")
                show_ord_chr(text)

            else:
                print("无效选择，请重新输入。")

        except ValueError as e:
            print(f"输入或转换错误：{e}")
        except UnicodeEncodeError as e:
            print(f"编码错误：{e}")
        except UnicodeDecodeError as e:
            print(f"解码错误：{e}")
        except Exception as e:
            print(f"发生错误：{e}")


if __name__ == "__main__":
    main()
