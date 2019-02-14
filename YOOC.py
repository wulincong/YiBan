#coding:utf-8
#___author:wulin___
#date:2019/2/11 0011
import re

def spl(question_All):  #把文件内容按照题目序号进行分割
    dic = re.split('\n\d+[,.]',question_All)
    while '' in dic:
        dic.remove('')
    return dic

def spl_question(question_one,answer):   #传入分割好的题目，答案
    li_question = re.split('\s*[A-D]\.?',question_one)  #按照ABCD选项分割
    answer_dic = {'A':1,'B':2,'C':3,'D':4}
    Answer = '(x)'+li_question.pop(answer_dic[answer])+'\n'   #把答案拿出来，加上(x)
    return '\n( )'.join(li_question)+Answer+'\n'  #返回拼接好的问题

file = input('请输入文件名>>>')
try:
    f = open(file,'r+',encoding='utf-8')  #文件必须是utf-8格式，否则报错
    s = f.read()
    copy_s = s
    f.close()
    f = open('out_'+file,'w',encoding='utf8')  #清空文件方便复写
except FileNotFoundError as F:
    print(F,'没有该文件')
except Exception as e:
    print(e,'请检查文件是否为utf-8编码')
    f.write(copy_s)
    f.close()
print(s)
try:
    copy_s = s  #复制一份，防止报错丢失文件内容
    s = spl(s)
    print('识别到%d个题目'%len(s))
    answer = input('请输入答案>>>')
    assert len(answer) == len(s)  #强制答案长度等于文件题目数量
    lis = []
    for i in range(len(answer)):
        lis.append(spl_question(s[i],answer[i]))  #把所有问题拼接起来
    qu = '+2\n'+'+2\n'.join(lis)
    print(qu)
    f.write(qu)
    f.close()
except AssertionError as A:
    print('答案长度与题目数量不符，请检查题目文件是否符合规范')
    f.write(copy_s)
    f.close()
    print(A)
except Exception as e:  #如果报错，执行复写，防止文件内容丢失
    f.write(copy_s)
    f.close()
    print(e)
#可以增加多编码文件支持
