#! /usr/bin/python3.10
import cards_tools

while True:
    # 显示菜单
    cards_tools.show_menu()
    action_str = input("请选择需要执行的操作: ")
    print("您选择的操作是 [%s]" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            # 新增名片
            cards_tools.new_card()
        elif action_str == "2":
            # 显示所有名片
            cards_tools.show_all()
        else:
            # 查找名片
            cards_tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用 [名片管理系统]")
        break
    else:
        print("您输入的不正确,请重新选择!")

