#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import cards_tools

while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择您需要进行的操作：")
    print("您选择的操作是【%s】" % action_str)

    if action_str in ["1","2","3"]:
        if action_str == "1":
            cards_tools.new_card()
        elif action_str == "2":
            cards_tools.show_all()
        else:
            cards_tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】！")
        break
    else:
        print("您的输入不正确，请重新选择！")