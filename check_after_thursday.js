/**
 * 判断当前毫秒时间戳是否在周四之后
 * @param {number} timestamp - 毫秒时间戳，如果不提供则使用当前时间
 * @returns {boolean} - 如果是周五、周六或周日则返回true，否则返回false
 */
function isAfterThursday(timestamp = Date.now()) {
    // 创建Date对象
    const date = new Date(timestamp);
    
    // 获取星期几 (0=周日, 1=周一, 2=周二, 3=周三, 4=周四, 5=周五, 6=周六)
    const dayOfWeek = date.getDay();
    
    // 周四之后意味着周五(5)、周六(6)、周日(0)
    return dayOfWeek === 0 || dayOfWeek === 5 || dayOfWeek === 6;
}

/**
 * 获取星期几的中文名称
 * @param {number} dayOfWeek - 星期几的数字表示
 * @returns {string} - 星期几的中文名称
 */
function getDayName(dayOfWeek) {
    const days = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
    return days[dayOfWeek];
}

/**
 * 主函数 - 检查当前时间是否在周四之后
 */
function main() {
    const now = Date.now();
    const currentDate = new Date(now);
    const dayOfWeek = currentDate.getDay();
    const dayName = getDayName(dayOfWeek);
    
    console.log(`当前时间戳: ${now}`);
    console.log(`当前时间: ${currentDate.toLocaleString('zh-CN')}`);
    console.log(`今天是: ${dayName}`);
    
    const result = isAfterThursday(now);
    console.log(`是否在周四之后: ${result ? '是' : '否'}`);
    
    return result;
}

// 如果直接运行此文件，则执行主函数
if (require.main === module) {
    main();
}

// 导出函数供其他模块使用
module.exports = {
    isAfterThursday,
    getDayName,
    main
};