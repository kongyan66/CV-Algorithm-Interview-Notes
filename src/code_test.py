from functools import wraps
# 装饰器
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

f(2)
print(f.__name__)      # 输出 'f'
print (f.__doc__)       # 输出 'does some math'