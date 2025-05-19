from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if sep is None:
        return split_by_step(data,maxsplit)
    else:
        return split_by_sep(data,sep,maxsplit)


def split_by_step(data,maxsplit=-1,sep=" "):
    result = []
    build_str = ""

    if maxsplit == -1:
        for i in range(len(data)):
            if (data[i] == sep):
                if build_str != "":
                    result.append(build_str)
                    build_str = ""
                else:
                    continue
            else:
                build_str += str(data[i]) 
        
        if build_str != "":
            result.append(build_str)
        return result
    
    elif maxsplit == 0:
        for i in range(len(data)):
            if data[i] == sep:
                if build_str != "":
                    result.append(build_str+f"{data[i:]}")
                    return result
                else:
                    continue
            else:
                build_str += str(data[i])   
        return result   

    elif maxsplit > 0:
        for i in range(len(data)):
            if data[i] == sep:
                if build_str != "":
                    if maxsplit == 0:
                        result.append(build_str+f"{data[i:]}")
                        return result
                    else:
                        result.append(build_str)
                        build_str = ""
                        maxsplit -= 1
                else:
                    continue
            else:
                build_str += str(data[i])   
        return result  

    return result

def split_by_sep(data,sep,maxsplit=-1):
    result = []
    build_str = ""
    sep_len = len(sep)
    splits_done =0

    if maxsplit == 0:
        return [data]
    
    elif maxsplit == -1:
        for i in range(len(data)):
            if i + sep_len <= len(data) - 1:
                if data[i:i+sep_len] == sep:
                    if build_str != "":
                        result.append(build_str)
                        build_str = ""
                    result.append('')
                else:
                    build_str += data[i:i+sep_len]
            else:
                if data[i:] == sep:
                    if build_str != "":
                        result.append(build_str)
                    result.append("")
                    return result
                else:
                    if build_str != "":
                        result.append(build_str+data[i:])
                    else:
                        result.append(data[i:])
                    return result

    elif maxsplit > 0:
        i = 0
        while i < len(data):
            if data[i:i+sep_len] == sep and (maxsplit == -1 or splits_done < maxsplit):
                result.append(build_str)
                build_str =""
                i += sep_len
                splits_done += 1
            else:
                build_str += data[i]
                i += 1
        result.append(build_str)
        return result
    return result    

if __name__ == '__main__':
    assert split('') == []
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
    assert split('adf<>5', sep='<>', maxsplit=0) == ['adf<>5']
