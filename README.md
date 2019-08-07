# 将中缀表达式转化成逆波兰表达式，并特殊的支持函数和数组

> 可以把数组看成是特殊的函数，[1,2,3,4]等价于array(1,2,3,4)

## 一、将中缀表达式转换成后缀表达式算法

### 1、从左至右扫描一中缀表达式。
### 2、如果遇到操作数就直接输出
### 3、如果遇到运算符
#### 3.1、如果运算符是“(”，直接存入运算符堆栈
#### 3.2、如果运算符是“)”
##### 3.2.1、将运算符堆栈的元素不断输出，直到遇到“(”时把它丢弃并停止。
##### 3.2.2、如果运算符栈顶是函数符号，再将它输出
#### 3.3、如果运算符是非括号运算符
##### 3.3.1、如果符号堆栈栈顶没有元素或者为“(”，或者自己优先级比栈顶的高，直接存入（“,”不做存入和输出）
##### 3.3.2、否则，将栈顶所有优先级大于等于自己的符号全部输出，直到没有或者直到“(”。然后再将自己入栈（“,”不入栈）
### 4、如果遇到函数调用
#### 4.1、直接输出函数开始标记“@”，并将“@函数名”和“（”都存入运算符堆栈



```python
from rpn import prn_encode
line = "loss = a + 0.4 * b + fun((a + b) * c, d, e) + concat([a, b, c, d, e], 1)"
print(prn_encode(line.replace(" ","")))
```

> 输出：['loss', 'a', '0.4', 'b', '*', '+', '@', 'a', 'b', '+', 'c', '*', 'd', 'e', '@fun', '+', '@', '@', 'a', 'b', 'c', 'd', 'e', '@array', '1', '@concat', '+', '=']