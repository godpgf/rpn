# 符号的优先级
opt_priority = {
    ',': -1,
    '=': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    # 函数
    '@': 100,
}


def get_opt_priority(opt):
    if len(opt) > 1:
        return opt_priority[opt[0]]
    else:
        return opt_priority[opt]


def rpn_encode(line):
    # line中不能有空格
    line = list(line)
    lid, rid = 0, 0
    opt_list = []
    prn_list = []
    # lid一定是指向操作数或者函数的起点
    while rid < len(line):
        if line[rid] in opt_priority:
            if rid > lid:
                # 如果遇到符号，证明lid指向的是操作数，遇到操作数直接输出
                prn_list.append("".join(line[lid:rid]))

            if line[rid] != ',' and (len(opt_list) == 0 or opt_list[-1] == '(' or get_opt_priority(line[rid]) > get_opt_priority(opt_list[-1])):
                # 如果符号堆栈栈顶没有元素或者为“(”，或者自己优先级比栈顶的高，直接存入（“,”不做存入和输出）
                opt_list.append(line[rid])
            else:
                # 不断输出符号堆栈的元素，直到顶上的元素优先级小于当前符号（即栈顶存在运算符的话，优先级一定是小于当前运算符），或者到了“(”
                while len(opt_list) > 0 and opt_list[-1] != '(' and get_opt_priority(opt_list[-1]) >= get_opt_priority(line[rid]):
                    prn_list.append(opt_list.pop())
                if line[rid] != ',':
                    opt_list.append(line[rid])
            lid = rid + 1
            rid = lid
        elif line[rid] == '(':
            if lid == rid:
                # 遇到的是"("符号，直接输出到操作符堆栈
                opt_list.append("(")

            else:
                # 遇到函数调用，输出函数开始调用标记，
                prn_list.append("@")
                # 将函数名和"("存入运算符堆栈
                opt_list.append("@" + "".join(line[lid:rid]))
                opt_list.append("(")
            lid = rid + 1
            rid = lid
        elif line[rid] == '[':
            assert lid == rid
            # 遇到的是数组，当做函数处理
            prn_list.append("@")
            opt_list.append("@array")
            opt_list.append("(")
            lid = rid + 1
            rid = lid
        elif line[rid] == ')' or line[rid] == ']':
            if rid > lid:
                # 遇到")"时说明之前有操作数
                prn_list.append("".join(line[lid:rid]))

            # 将运算符堆栈的元素不断输出，直到遇到“(”时把它丢弃并停止。
            while len(opt_list) > 0 and opt_list[-1] != '(':
                prn_list.append(opt_list.pop())
            if len(opt_list) > 0 and opt_list[-1] == '(':
                opt_list.pop()
            if len(opt_list) > 0 and opt_list[-1].startswith("@"):
                # 如果运算符栈顶是函数符号，再将它输出
                prn_list.append(opt_list.pop())
            lid = rid + 1
            rid = lid
        else:
            rid += 1

    if rid != lid:
        prn_list.append("".join(line[lid:rid]))
    while len(opt_list) > 0:
        prn_list.append(opt_list.pop())
    return prn_list
