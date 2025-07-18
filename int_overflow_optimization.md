# C# 原子递增整数溢出优化方案

## 问题分析

原始代码：
```csharp
int index = Interlocked.Increment(ref _index);
int threadCount = _executors.Length;
_executors[index % threadCount].Execute(action);
```

### 存在的问题
1. **整数溢出风险**：当 `_index` 达到 `int.MaxValue` (2,147,483,647) 时，再次递增会溢出到负数
2. **负数取模问题**：负数对正数取模在 C# 中可能返回负值，导致数组索引越界异常

## 优化方案

### 方案一：使用 Math.Abs 处理负数（简单但不完美）

```csharp
int index = Interlocked.Increment(ref _index);
int threadCount = _executors.Length;
int safeIndex = Math.Abs(index % threadCount);
_executors[safeIndex].Execute(action);
```

**优点**：代码简单
**缺点**：当 index 为 int.MinValue 时，Math.Abs 仍会溢出

### 方案二：重置计数器（推荐）

```csharp
private int GetNextIndex()
{
    int current, next;
    do
    {
        current = _index;
        next = (current == int.MaxValue) ? 0 : current + 1;
    } while (Interlocked.CompareExchange(ref _index, next, current) != current);
    
    return next;
}

// 使用方式
int index = GetNextIndex();
int threadCount = _executors.Length;
_executors[index % threadCount].Execute(action);
```

### 方案三：使用无符号整数

```csharp
private uint _index = 0;

public void Execute(Action action)
{
    uint index = (uint)Interlocked.Increment(ref _index);
    int threadCount = _executors.Length;
    _executors[index % (uint)threadCount].Execute(action);
}
```

**注意**：需要将 `_index` 字段类型改为 `uint`，并注意 `Interlocked.Increment` 的返回值转换

### 方案四：使用位运算优化（当线程数为2的幂时）

```csharp
// 假设 threadCount 是 2 的幂（如 4, 8, 16）
private readonly int _threadMask;

public Constructor()
{
    // 确保 threadCount 是 2 的幂
    int threadCount = _executors.Length;
    if ((threadCount & (threadCount - 1)) != 0)
        throw new ArgumentException("Thread count must be a power of 2");
    
    _threadMask = threadCount - 1;
}

public void Execute(Action action)
{
    int index = Interlocked.Increment(ref _index);
    _executors[index & _threadMask].Execute(action);
}
```

### 方案五：使用 ThreadLocal 计数器（最高性能）

```csharp
private static readonly ThreadLocal<Random> _threadLocalRandom = 
    new ThreadLocal<Random>(() => new Random());
private readonly int _threadCount;

public void Execute(Action action)
{
    // 使用线程本地的随机数，避免原子操作的开销
    int index = _threadLocalRandom.Value.Next(_threadCount);
    _executors[index].Execute(action);
}
```

## 推荐方案

### 最佳实践（方案二改进版）

```csharp
private volatile int _index = -1;

private int GetNextExecutorIndex()
{
    int threadCount = _executors.Length;
    
    // 使用局部变量避免重复读取 volatile 字段
    int current, next;
    do
    {
        current = _index;
        // 防止溢出，当接近最大值时重置
        if (current >= int.MaxValue - 1000) // 留出安全边界
        {
            next = 0;
        }
        else
        {
            next = current + 1;
        }
    } while (Interlocked.CompareExchange(ref _index, next, current) != current);
    
    return next % threadCount;
}

public void Execute(Action action)
{
    int executorIndex = GetNextExecutorIndex();
    _executors[executorIndex].Execute(action);
}
```

## 性能考虑

1. **原子操作开销**：`Interlocked.Increment` 比普通递增慢，但在多线程环境下必需
2. **取模操作**：对于2的幂，位运算 `&` 比取模 `%` 更快
3. **竞争激烈度**：如果线程数很多，考虑使用 ThreadLocal 或其他分散策略

## 测试建议

```csharp
[Test]
public void TestIndexOverflow()
{
    // 模拟接近溢出的情况
    _index = int.MaxValue - 10;
    
    for (int i = 0; i < 20; i++)
    {
        int executorIndex = GetNextExecutorIndex();
        Assert.IsTrue(executorIndex >= 0 && executorIndex < _executors.Length);
    }
}
```