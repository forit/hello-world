#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime

def is_after_thursday(timestamp_ms=None):
    """
    判断当前毫秒时间戳是否在周四之后
    
    Args:
        timestamp_ms (int, optional): 毫秒时间戳，如果不提供则使用当前时间
        
    Returns:
        bool: 如果是周五、周六或周日则返回True，否则返回False
    """
    if timestamp_ms is None:
        timestamp_ms = int(time.time() * 1000)
    
    # 将毫秒时间戳转换为秒时间戳
    timestamp_s = timestamp_ms / 1000
    
    # 创建datetime对象
    dt = datetime.fromtimestamp(timestamp_s)
    
    # 获取星期几 (0=周一, 1=周二, 2=周三, 3=周四, 4=周五, 5=周六, 6=周日)
    day_of_week = dt.weekday()
    
    # 周四之后意味着周五(4)、周六(5)、周日(6)
    return day_of_week >= 4

def get_day_name(day_of_week):
    """
    获取星期几的中文名称
    
    Args:
        day_of_week (int): 星期几的数字表示 (0=周一)
        
    Returns:
        str: 星期几的中文名称
    """
    days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    return days[day_of_week]

def main():
    """
    主函数 - 检查当前时间是否在周四之后
    """
    now_ms = int(time.time() * 1000)
    current_dt = datetime.fromtimestamp(now_ms / 1000)
    day_of_week = current_dt.weekday()
    day_name = get_day_name(day_of_week)
    
    print(f"当前时间戳: {now_ms}")
    print(f"当前时间: {current_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"今天是: {day_name}")
    
    result = is_after_thursday(now_ms)
    print(f"是否在周四之后: {'是' if result else '否'}")
    
    return result

if __name__ == "__main__":
    main()