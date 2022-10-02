## python C 语言扩展

### 1. 使用ctypes访问C代码

**需求**

你有一些C函数已经被编译到共享库或DLL中。你希望可以使用纯Python代码调用这些函数， 而不用编写额外的C代码或使用第三方扩展工具。

**解决方案**

对于需要调用C代码的一些**小的问题**，通常使用Python标准库中的 `ctypes` 模块就足够了。 要使用 `ctypes` ，你首先要确保你要访问的C代码已经被编译到和Python解释器兼容 （同样的架构、字大小、编译器等）的某个共享库中了（.so文件）。实现三部曲：

- sample.c  源码实现 (自己写的)
- sample.so 生成共享库，也叫动态库 (编译生成的) 
- sample.py python包装 （自己写的，也是最终要用的）

**具体实现**

当然并不是说这个共享库就直接能用的，还需要写一个包装它的Python模块。

比如，C代码如下：

```c
#include <math.h>

/* Compute the greatest common divisor */
int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* Divide two numbers */
int divide(int a, int b, int *remainder) {
    int quot = a / b;
    *remainder = a % b;
    return quot;
}
```

编译生成了libsample.so的动态库（怎么编译的？），然后需要我们用python去包装这个模块，如下：

```python
# sample.py
import ctypes
import os

# Try to local the .so file in the same directory as this file.
_file = 'libsample.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
# 加载动态库
_mod = ctypes.cdll.LoadLibary(_path)

# init gcd(int, int)
gcd = _mod.gcd  # 函数初始化
gcd.argtypes = (ctypes.c_int, ctypes.c_int)  # 形参初始化
gcd.restype = ctypes.c_int # 输出初始化

# int divide(int, int, int *)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
    rem = ctypes.c_init()
    quto = _divide(x, y, rem)
    
    return quto, rem.value

```

以上可见，参数的数据类型有一点麻烦的，比如ctypes不支持的一些，所以说只能写一写简单的C函数。

**使用**

这下文件目录中会有三种文件：

- sample.c  源码实现 (自己写的)
- sample.so 生成共享库，也叫动态库 (编译生成的) 
- sample.py python包装 （自己写的，也是最终要用的）

sample.py 才是我们直接使用的，如：

```
import sample
a = sample.gcd(10, 20)
b = sample.divide(10, 20)
print(a, b)
```

**讨论**

**数据类型要对齐**：在这段代码中，`.argtypes` 属性是一个元组，包含了某个函数的输入， 而 `.restype` 就是相应的返回类型。 `ctypes` 定义了大量的类型对象（比如c_double, c_int, c_short, c_float等）， 代表了对应的C数据类型。如果你想让Python能够传递正确的参数类型并且正确的转换数据的话， 那么这些类型签名的绑定是很重要的一步。如果你没有这么做，不但代码不能正常运行， 还可能会导致整个解释器进程挂掉

**不对齐会出BUG：**如果你想让Python能够传递正确的参数类型并且正确的转换数据的话， 那么这些**类型签名的绑定**是很重要的一步。如果你没有这么做，不但代码不能正常运行， 还可能会导致整个解释器进程挂掉。

**缺点**：对于大型库的访问有个主要问题，由于ctypes并不是完全自动化， 那么你就必须花费大量时间来编写所有的类型签名，就像例子中那样。 如果函数库够复杂，你还得去编写很多小的包装函数和支持类

### 2. python API 扩展C模块

**需求**

不依赖任何工具，直接用pyhon 的扩展API来编写一些简单的C扩展模块

**解决方案**

通过编译生成.so文件，然后import导入使用(目前见到的大多数采用的方式)，用到的文件顺序如下：

- sample.h    sample.c
- steup.py
- sample.so

**具体实现**

先写好一个正确的头文件, 且这个头文件对应一个已经编译过的库(不太理解了)

```c
// sample.h
#include <math.h>
extern int gcd(int, int);
ertrrn int dvide(int a, int b, int *remainder);
```

再开始写 pysample.c 

```c
#include "Python.h"
#include "sample.h"

/* int gcd(int, int) */
static PyObject *py_gcd(PyObject *self, PyObject *args){
    int x, y, result;
    
    if(!PyArg_ParseTuple(args, "ii", &x, &y)){
        return NULL;
    }
    result = gcd(x, y);
    return Py_BuildValue("i", result);
}

/* int divide(int, int, int *) */
static PyObject *py_divide(PyObject *self, PyObject *args) {
  int a, b, quotient, remainder;
  if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
    return NULL;
  }
  quotient = divide(a,b, &remainder);
  return Py_BuildValue("(ii)", quotient, remainder);
}
/* Module method table */
static PyMethodDef SampleMethods[] = {
  {"gcd",  py_gcd, METH_VARARGS, "Greatest common divisor"},
  {"divide", py_divide, METH_VARARGS, "Integer division"},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,
  "sample",           /* name of module */
  "A sample module",  /* Doc string (may be NULL) */
  -1,                 /* Size of per-interpreter state or -1 */
  SampleMethods       /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
```

然后写一个setup.py文件去绑定这个模块：

```python
# setup.py
from distutils import setup, Externsion

steup(name='sample',  
     ext_modules=[
         Extension('sample',
                  ['pysample.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['sample'])
     ])
```

接下就是最常见的指令了，每次安装一个工程，基本都有这一步，今天终于知道干啥的了：

```
python3 setup.py build_ext --inplace
```

python setup.py 命令行：

![image-20220504211113669](C:\Users\10428\AppData\Roaming\Typora\typora-user-images\image-20220504211113669.png)

之后就会生成一个 **sample.so** 的共享库。编译完成就可以在python环境中当做一个模块导入了：

```pyhton
import sample
sample.gcd(10, 20)
sample.divide(10, 20)
```



**讨论**

`PyObject` 是一个能表示任何Python对象的C数据类型。 在一个高级层面，一个扩展函数就是一个接受一个Python对象 （在 PyObject [*](https://python3-cookbook.readthedocs.io/zh_CN/latest/c15/p02_write_simple_c_extension_module.html#id5)args中）元组并返回一个新Python对象的C函数。函数的 `self` 参数对于简单的扩展函数没有被使用到， 不过如果你想定义新的类或者是C中的对象类型的话就能派上用场了。比如如果扩展函数是一个类的一个方法， 那么 `self` 就能引用那个实例了。

`PyArg_ParseTuple()` 函数被用来将Python中的值转换成C中对应表示。 它接受一个指定输入格式的格式化字符串作为输入，比如“i”代表整数，“d”代表双精度浮点数， 同样还有存放转换后结果的C变量的地址。 如果输入的值不匹配这个格式化字符串，就会抛出一个异常并返回一个NULL值。 通过检查并返回NULL，一个合适的异常会在调用代码中被抛出。

`Py_BuildValue()` 函数被用来根据C数据类型创建Python对象。 它同样接受一个格式化字符串来指定期望类型。 在扩展函数中，它被用来返回结果给Python。

`SampleMethods` 表。 这个表可以列出C函数、Python中使用的名字、文档字符串。 所有模块都需要指定这个表，因为它在模块初始化时要被使用到。

最后的函数 `PyInit_sample()` 是模块初始化函数，但该模块第一次被导入时执行。

本篇文章只是一个入门，更详细的需要看`PyArg_ParseTuple()` 和 `Py_BuildValue()` 函数的文档， 然后进一步扩展开。

