def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("*" * 50)

# 记录所有的名片字典
card_list = []

def new_card():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")

    card_man = {"name":name,
                "phone":phone,
                "qq":qq,
                "email":email}

    card_list.append(card_man)

    print("添加 %s 的名片成功！" % name)

def show_all():
    if len(card_list) == 0:
        print("当前名片无记录，请添加名片！")
        return
    for tag in ["姓名","电话","QQ","邮箱"]:
        print(tag, end="\t\t")
    print("")
    print("=" * 50)
    for person in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (person["name"],
                                        person["phone"],
                                        person["qq"],
                                        person["email"]))
    print("=" * 50)

def search_card():
    find_name = input("请输入要搜索的姓名：")
    for man in card_list:
        if man["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (man["name"],
                                            man["phone"],
                                            man["qq"],
                                            man["email"]))
            print("=" * 50)
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(man)
            break
    else:
        print("很抱歉没有找到用户 %s " % find_name)

def deal_card(find_man):
    """处理查找到的名片

    :param find_man: 查找到的名片
    """
    deal_str = input("请选择要执行的操作 1 修改 2 删除 0 返回上级菜单")
    if deal_str in ["1", "2"]:
        if deal_str == "1":
            find_man["name"] = input_card_info(find_man["name"], "姓名[回车不修改]：")
            find_man["phone"] = input_card_info(find_man["phone"], "电话[回车不修改]：")
            find_man["qq"] = input_card_info(find_man["qq"], "QQ[回车不修改]：")
            find_man["email"] = input_card_info(find_man["email"], "邮箱[回车不修改]：")
            print("%s 的信息修改成功！" % find_man["name"])
        else:
            card_list.remove(find_man)
            print("删除 %s 成功！" % find_man["name"])
    elif deal_str == "0":
        return
    else:
        print("您选择执行的操作有误！")
        return

def input_card_info(old_value, tip_message):
    """输入名片信息

    :param old_value: 字典中原有的值
    :param tip_message: 输入的提示语
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    new_value = input(tip_message)
    if new_value.strip() == "":
        return old_value
    else:
        return new_value.strip()