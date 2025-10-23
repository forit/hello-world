#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from check_after_thursday import is_after_thursday, get_day_name
from datetime import datetime

def test_after_thursday():
    """
    测试不同日期的周四判断功能
    """
    print('=== 测试周四之后判断功能 ===\n')
    
    # 测试用例：不同星期几的时间戳
    test_cases = [
        # 2025年10月20日 周一
        {'date': '2025-10-20', 'expected': False},
        # 2025年10月21日 周二  
        {'date': '2025-10-21', 'expected': False},
        # 2025年10月22日 周三
        {'date': '2025-10-22', 'expected': False},
        # 2025年10月23日 周四
        {'date': '2025-10-23', 'expected': False},
        # 2025年10月24日 周五
        {'date': '2025-10-24', 'expected': True},
        # 2025年10月25日 周六
        {'date': '2025-10-25', 'expected': True},
        # 2025年10月26日 周日
        {'date': '2025-10-26', 'expected': True},
    ]
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for index, test_case in enumerate(test_cases):
        test_date = datetime.strptime(test_case['date'] + ' 12:00:00', '%Y-%m-%d %H:%M:%S')
        timestamp_ms = int(test_date.timestamp() * 1000)
        day_of_week = test_date.weekday()
        day_name = get_day_name(day_of_week)
        result = is_after_thursday(timestamp_ms)
        passed = result == test_case['expected']
        
        print(f"测试 {index + 1}: {test_case['date']} ({day_name})")
        print(f"  时间戳: {timestamp_ms}")
        print(f"  预期结果: {'是' if test_case['expected'] else '否'}")
        print(f"  实际结果: {'是' if result else '否'}")
        print(f"  测试结果: {'✅ 通过' if passed else '❌ 失败'}\n")
        
        if passed:
            passed_tests += 1
    
    print('=== 测试总结 ===')
    print(f'通过测试: {passed_tests}/{total_tests}')
    print(f'测试成功率: {passed_tests / total_tests * 100:.1f}%')
    
    return passed_tests == total_tests

if __name__ == "__main__":
    test_after_thursday()