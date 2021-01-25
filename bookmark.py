BOOKMARK = {}


def show_bookmark_douyu():
    print("斗鱼收藏夹：A_CS:GO_刘坤，B_东北乱炖，C_狂拽酷炫，D_小U，F_坦克世界黑鹰, E_杜比4k")
    global BOOKMARK
    BOOKMARK = {'A': 52319,
                'B': 30191,
                'C': 252802,
                'D': 96577,
                'F': 4722447,
                'E': 9249162
                }

def show_bookmark_bili():
    print("哔哩哔哩收藏夹：A_胖丁，B_乌帕下士", 'C_沙鹰')
    global BOOKMARK
    BOOKMARK = {'A': 1620209,
                'B': 92137,
                'C': 14246602
                }

def choose_rid(rid):
    test_id = BOOKMARK.get(rid)
    # if test_id:
    #     return test_id
    # else:
    #     return rid
    # test_id ? test_id : rid 传统三目运算符 与 Python三目运算符
    return test_id if test_id else rid
