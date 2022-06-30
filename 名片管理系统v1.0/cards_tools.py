# 记录所有的名片字典
card_list = []


def show_menu():

    print("*"*50)
    print("欢迎使用 [名片管理系统]v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查找名片")
    print("")
    print("0.退出系统")
    print("*"*50)


def new_card():
    """新增名片"""
    print("-"*80)
    print("新增名片")
    usrname = input("请输入姓名:")
    usrphone = input("请输入电话:")
    usrqq = input("请输入QQ:")
    usremail = input("请输入邮箱:")
    card_dict = {"name": usrname,
                 "phone": usrphone,
                 "qq": usrqq,
                 "email": usremail}
    card_list.append(card_dict)
    # print(card_list)
    print("添加 %s 的名片成功!" % usrname)
    print("-"*80)


def show_all():
    """显示所有名片"""
    print("-"*80)
    print("显示所有名片")
    if len(card_list) == 0:
        print("当前没有名片添加记录,请使用新增功能添加名片!")
        return
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")
    print("")
    print("-"*80)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                  card_dict["phone"],
                                  card_dict["qq"],
                                  card_dict["email"]))
    print("-"*80)


def search_card():
    """查找名片"""
    print("-"*80)
    print("查找名片")
    find_name = input("请输入要搜索的姓名:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-"*80)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 对找到的名片进行修改或删除的操作
            deal_card(card_dict)
            # break
    else:
        print("抱歉,没有找到 %s" % find_name)
    print("-"*80)


def deal_card(find_dict):
    """
     # 处理查找到的名片
    :param find_dict: 查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作 -> 1.修改 / 2.删除 / 0.返回上一级菜单:")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:")
        print("修改名片成功!")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功!")
    else:
        pass


def input_card_info(dict_value, tip_message):
    """
     # 输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 提示输入信息
    :return: 如果输入内容,则返回内容,否则返回字典原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
