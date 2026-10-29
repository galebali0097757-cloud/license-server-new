# iOS Install Hub — مركز تثبيت iOS

واجهة عربية مفتوحة المصدر لإنشاء ملف `manifest.plist` وربط تثبيت **تطبيق iOS موقّع ومصرّح بتوزيعه** عبر HTTPS. هذا ليس ESign ولا يولّد شهادة Apple ولا يوقّع ملفات IPA.

## الميزات

- صفحة RTL للهاتف، بدون مكتبات خارجية أو تتبع.
- إنشاء `manifest.plist` داخل المتصفح، من بيانات التطبيق ورابط IPA الموقّع.
- فتح `itms-services` من Safari عند توفير رابط HTTPS إلى manifest.
- استضافة مجانية عبر GitHub Pages (إذا كانت مفعّلة).
- لا يُرفع IPA ولا شهادات ولا بيانات تسجيل دخول من خلال الصفحة.

## النشر

هذا المشروع محفوظ داخل مجلد `ios-installer/` حتى لا يؤثر على ملفات المستودع الأصلية. يوجد workflow في `.github/workflows/deploy-ios-installer.yml` ينشر هذا المجلد على GitHub Pages.

إذا لم تعمل GitHub Pages تلقائياً، افتح **Settings → Pages → Build and deployment → Source = GitHub Actions** في المستودع. رابط الموقع عند تفعيل Pages:

https://galebali0097757-cloud.github.io/license-server-new/

## التثبيت

1. احصل بشكل مشروع على تطبيقك IPA موقّع بشهادة Apple وتصريح provisioning يسمح بالتثبيت على الجهاز (مثل Ad Hoc للأجهزة المدرجة).
2. استضف IPA الموقّع على HTTPS يدعم تنزيل الملف.
3. افتح الموقع واستعمل النموذج لإنشاء `manifest.plist` مطابق لـ CFBundleIdentifier وCFBundleVersion.
4. ارفع `manifest.plist` على رابط HTTPS عام، ثم ضعه في حقل التثبيت وافتحه من Safari على جهاز مسموح.

وجود رابط لا يتجاوز سياسة Apple. الموقع لا يستطيع فحص الشهادة أو ضمان التثبيت. شهادة HTTPS للموقع مختلفة عن شهادة توقيع التطبيق. DNS لا يوفر شهادة Apple ولا يصلح شهادة ملغاة.

## الأمان

**لا تضع** ملفات `.p12` أو مفاتيح خاصة أو كلمات مرور أو رموز Apple في المستودع أو صفحة عامة. تجنّب الشهادات المجهولة. هذه الواجهة لا تستبدل Xcode أو اعتماد Apple.

## روابط رسمية

- https://developer.apple.com/help/account/provisioning-profiles/create-an-ad-hoc-provisioning-profile
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://developer.apple.com/support/apps-in-the-eu
