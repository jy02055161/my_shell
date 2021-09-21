def list_to_bin(data, is_reversal=None):
    bin_list=[2**i for i in range(32)]
    index = 0
    res = 0
    if is_reversal:
        re_data = []
        for i in data:
            if i:
                re_data.append(0)
            else:
                re_data.append(1)
        data = re_data
    for i in data:
        if i:
            res |= bin_list[index]
        index += 1
    return res

def bin_to_list(data,bit=8):
    if isinstance(data,int):
        bin_list=[2**i for i in range(32)]
        res=[]
        for i in range(bit):
            temp=data&bin_list[bit-i-1] #为了结果方便阅读，从最后一位加入列表
            if(temp):res.append(1)
            else:res.append(0)
    else:
        res=data
    return res


