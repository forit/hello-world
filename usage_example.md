# 判断当前毫秒时间戳是否周四之后

本项目提供了两个版本的实现来判断给定的毫秒时间戳是否在周四之后（即周五、周六、周日）。

## 文件说明

- `check_after_thursday.js` - JavaScript版本的实现
- `check_after_thursday.py` - Python版本的实现  
- `test_after_thursday.js` - JavaScript版本的测试文件
- `test_after_thursday.py` - Python版本的测试文件

## 使用方法

### JavaScript版本

```bash
# 直接运行，检查当前时间
node check_after_thursday.js

# 在代码中使用
const { isAfterThursday } = require('./check_after_thursday');

// 检查当前时间
const result = isAfterThursday();
console.log(result); // true 或 false

// 检查指定时间戳
const timestamp = 1761307200000; // 2025-10-24 周五
const result2 = isAfterThursday(timestamp);
console.log(result2); // true
```

### Python版本

```bash
# 直接运行，检查当前时间
python3 check_after_thursday.py

# 在代码中使用
from check_after_thursday import is_after_thursday

# 检查当前时间
result = is_after_thursday()
print(result)  # True 或 False

# 检查指定时间戳
timestamp_ms = 1761307200000  # 2025-10-24 周五
result2 = is_after_thursday(timestamp_ms)
print(result2)  # True
```

## 运行测试

```bash
# JavaScript测试
node test_after_thursday.js

# Python测试
python3 test_after_thursday.py
```

## 逻辑说明

- 周四之后指的是：周五、周六、周日
- 周四及之前指的是：周一、周二、周三、周四
- 函数接受毫秒时间戳作为参数，如果不提供则使用当前时间
- 返回布尔值：`true/True` 表示在周四之后，`false/False` 表示在周四及之前

## 当前测试结果

两个版本都通过了全部测试用例，测试成功率100%。