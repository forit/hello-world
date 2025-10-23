const { isAfterThursday, getDayName } = require('./check_after_thursday');

/**
 * 测试不同日期的周四判断功能
 */
function testAfterThursday() {
    console.log('=== 测试周四之后判断功能 ===\n');
    
    // 测试用例：不同星期几的时间戳
    const testCases = [
        // 2025年10月20日 周一
        { date: '2025-10-20', expected: false },
        // 2025年10月21日 周二  
        { date: '2025-10-21', expected: false },
        // 2025年10月22日 周三
        { date: '2025-10-22', expected: false },
        // 2025年10月23日 周四
        { date: '2025-10-23', expected: false },
        // 2025年10月24日 周五
        { date: '2025-10-24', expected: true },
        // 2025年10月25日 周六
        { date: '2025-10-25', expected: true },
        // 2025年10月26日 周日
        { date: '2025-10-26', expected: true },
    ];
    
    let passedTests = 0;
    let totalTests = testCases.length;
    
    testCases.forEach((testCase, index) => {
        const testDate = new Date(testCase.date + 'T12:00:00');
        const timestamp = testDate.getTime();
        const dayOfWeek = testDate.getDay();
        const dayName = getDayName(dayOfWeek);
        const result = isAfterThursday(timestamp);
        const passed = result === testCase.expected;
        
        console.log(`测试 ${index + 1}: ${testCase.date} (${dayName})`);
        console.log(`  时间戳: ${timestamp}`);
        console.log(`  预期结果: ${testCase.expected ? '是' : '否'}`);
        console.log(`  实际结果: ${result ? '是' : '否'}`);
        console.log(`  测试结果: ${passed ? '✅ 通过' : '❌ 失败'}\n`);
        
        if (passed) passedTests++;
    });
    
    console.log(`=== 测试总结 ===`);
    console.log(`通过测试: ${passedTests}/${totalTests}`);
    console.log(`测试成功率: ${(passedTests / totalTests * 100).toFixed(1)}%`);
    
    return passedTests === totalTests;
}

// 运行测试
if (require.main === module) {
    testAfterThursday();
}