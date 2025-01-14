document.addEventListener('DOMContentLoaded', function () {
    // الحصول على العناصر
    const menuButton = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    // التحقق من وجود العناصر
    if (!menuButton || !sidebar) {
        console.error('Error: Could not find menuButton or sidebar elements.');
        return;
    }

    // إضافة حدث النقر
    menuButton.addEventListener('click', function () {
        console.log('Menu button clicked!'); // للتحقق في وحدة التحكم
        sidebar.classList.toggle('visible'); // إظهار أو إخفاء القائمة
    });

    // اختبار التحميل الناجح
    console.log('JavaScript loaded successfully!');
});
