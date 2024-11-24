---
ID: 352
post_title: passkey 指北
post_name: passkey-guide
author: Xuan
post_date: 2024-11-03 22:51:54
layout: post
link: >
  https://blog.wangxuan.name/2024/11/03/passkey-guide/
published: true
tags:
  - Apple
  - Google
  - Microsoft
  - Passkey
  - Yubikey
categories:
  - Fiddling
  - Internet Freedom
  - Knowhow
---
# 什么是 passkey

Passkey 的官方中文翻译是「通行密钥」，这实在不是个好的翻译。本来推广 passkey 的几大公司起这个名字，是和 password 相对应，password 是「用于通行的口令」，那么 passkey 就是「用于通行的钥匙」，简单好记。但 password 的中文已经约定俗成翻译为「密码」，「密钥」又另有所指，不得不起了这么一个蹩脚的翻译。四字短语永远会在广泛使用后有一个两字的缩写，不知道假以时日，会不会有人用「通钥」来简称 passkey。不过以今日中文网站对 passkey 的冷漠，这一天即使有大概也很遥远。

言归正传。天下人苦密码久矣。这些年有些时兴的 passkey 是又一波试图「消灭」密码的浪潮。

所有人都痛恨用户名－密码验证：总是记不住用户名、密码，试错几次锁帐户……每个月总有几次这样的时候让人想摔电脑。如果还有双因素认证，输完密码还要再输个验证码，人就更暴躁了。什么时候才能让这种证明「我是我」的过程不那么痛苦。

前些年国内网站在逐渐使用短信验证码来替换密码登录，可短信这个东西，仅作为一个验证手段都嫌不安全，作为唯一的登录凭据使用，简直是把脑袋挂在手机上。它成为中国主流的验证方式也是「自有实名制国情在此」。相对而言，公钥私钥验证，在密码学上早已成熟，在实际应用中久经考验，几十年来都被人认为是取代密码的最佳方案之一。在 SSH、PGP、PIV 卡等应用上，公钥认证已经广泛使用很多年。但是在网站登录上，由于易用性的原因，尽管已经有很多免密码登录的业界标准，却一直没有推广开来。

2022 年，Microsoft Google Apple 三大操作系统提供商，以及 Chrome Firefox 浏览器终于开始一致行动，推广免密码登录。虽然本质上是新瓶装旧酒，底层方案仍然是久已有之的东西，但一个好名字显然有助于推广，这个新名字就是 passkey。这之后，支持 passkey 登录的网站慢慢多起来。

Passkey 的目标不仅是取代密码，还要取代传统的两步验证（2FA）。对于两步验证，或者多因素验证来说，登入帐户需要两个凭证，一件是「用户知道的」，比如说密码，一件是「用户持有的」，比如说硬件密钥或者手机。如果有人偷了用户持有的东西，但是不知道密码，自然无法访问。如果有人偷窥到了密码，或者恶意软件记录了密码，只要没有把第二凭证拿到手，还是无法登入。Passkey 既然要取代两步验证，安全性自不能降低，还是要证明用户已经出示了两种凭证。

打个比方来说明一下什么是 passkey ：一个网站或者其它需要验证身份的服务（relying party）（RP）要求用户出示某种凭证来证明身份：

军营前方，一骑快马奔来，军营守卫大喊「来者何人！」。如果用密码的话，来使在马上大喊「天王盖地虎！」守卫回去一看，好像确系皇帝所约定的暗语，于是放行。没想到使者见将军之后一剑刺死将军，大笑三声：「你们天天都是同一个口令，早就被我们密探听得一清二楚！」

如果使用 passkey 的话，只见来使从背后抱出一个沉重的密码箱，左拧右拧，露出一半虎符，将军让守卫传上来，和自己的那半虎符一对，严丝合缝，「果然是真使者！」

虎符只是个比方，实际使用的是更为安全的公钥私钥认证。在前述比喻中，实际发生的是：用户使用 PIN 或者指纹、面容解锁 passkey 设备（也就是上面比喻中的密码箱）之后，passkey 设备使用密码学上的公钥认证向 RP 发出证明：「兹证明，某用户在我这台设备上使用 PIN 解锁成功（既然您对我这款设备熟，您应该知道我只有在用户物理上持有我这台设备的时候才会发出证明，那个啥，第二因素认证就一并免了吧？）」。于是 RP 一方「收到，放行！」

如果要买个特制密码箱（passkey 设备）才能使用 passkey 的话，就不会有几个人用它了。老套的 OTP 验证之所以这两年来获得普及，就是因为在手机上装个 authenticator app 很方便，不需要 U 盾或者动态口令牌之类的专用设备。这次 passkey 的卷土重来，正是三大操作系统提供商陆续在操作系统层面加入了对 passkey 的支持：passkey 不再需要是某个专用设备，而可以是我们已经在使用的手机或电脑。既然手机电脑本来就需要 PIN 或者指纹解锁，又基本不离身，为什么不用作 passkey 呢？这次三家的联合推广使 passkey 成功破圈，以至于在绝大部分第一次听说 passkey 的人眼中，passkey 就是 iPhone 或者 Android 手机上的一个新功能。而那些专门的硬件设备如 Yubikey，在网站上愤愤不平地说：我们十几年前就可以当 passkey 用了！

相对于传统的用户名密码登录，passkey 无论是安全性和便捷性都要好很多。从安全性上来说，网站被拖库不会影响到用户的帐户，因为攻击者没有用户的私钥，即使获得网站数据库也无法假冒用户登入。从便捷性上来说，用户不需要记忆每个网站的密码，只需要记忆解锁 passkey 的密码，记忆负担大大减轻。十分建议本文读者尝试一下 passkey 登录：用过就回不去啦！

## passkey 设备

粗糙地说，你可以把 passkey 设备看作前面比喻中的密码箱，而 passkey 就是密码箱里的虎符。（虽然 passkey 标准说，如果这个虎符没有放在密码箱里，而是随便什么人都能掏得到，它就不可以叫 passkey）由前所述，passkey 设备既可以是手机、电脑，也可以是一个单独的硬件密钥如 Yubikey。前者无疑比后者更便捷，因为手机每天都带在身边，但后者在抵抗网络攻击的安全性上更胜一筹。

Passkey 设备的安全性全系于它如何保护用户登录网站的私钥。如果 passkey 设备感染恶意软件，内部存储的私钥有可能会泄露。专门的外置硬件密钥一般无法被恶意软件感染，安全性更高。

不过，即使是手机、电脑，安全性也没有那么差。一般来说，现代操作系统会使用硬件安全模块来加密用户的私钥。这样的话，至少在用户设备关机之后，只要攻击者没有同时偷到解锁用的 PIN，不能解锁设备，私钥就是安全的。也就是说，一般情况下，已经关机的手机即使丢了也不需要担心。这方面 Windows Android iOS MacOS 没有太大的区别。实际中更可能遇到的风险是，设备在开机状态下感染恶意软件，比如说在访问恶意网站时受到感染。通常来说，恶意软件需要破坏操作系统的完整性才能隐藏输入 PIN 或指纹的弹窗，这种攻击比较困难，但并非没有可能。好在，网络攻击也遵守经济原则。这种「能偷到所有人电脑上所有 passkey」的漏洞的价值极高，攻击者一定会在漏洞被修复之前争分夺秒地攻击高价值目标。只要及时接受操作系统的安全更新，风险是可控的，普通用户不必过于担心。如果安全风险很高的话，三大操作系统厂商不会愿意联手推动系统内置 passkey 普及。

仅说理论上的风险的话，root 过的设备的风险远大于没有 root 过的设备，Windows Android 因为用户广泛，每年被利用的漏洞也多于 MacOS。而外置硬件密钥则还没有软件上被攻破的记录，只有侧信道攻击。这样说来，十分重视「绝对安全」的人，还是应该选择外置硬件密钥。不过，安全性也和线下的风险相关。手机一丢，立刻就会发现，而硬件密钥丢了，却未必见得会马上发现。

## passkey 认证各方

其实，如果要把手机电脑当作 passkey 设备用的话，并不是只有操作系统提供的 passkey 功能可选。许多密码管理器也加入了对 passkey 的支持。如果我们说，passkey 的核心是这个「让用户输入密码或者按指纹之后就用私钥完成认证」的东西，它其实是个在 passkey 设备上运行的软件，在标准中称作 authenticator。如前所述，用户希望登入的网站或者 app 那一边，则叫作 relying party。

## Passkey vs 密码管理器

如果不谈外置硬件密钥的话，完全基于软件的 passkey 和传统密码管理器相似度很高，所以传统密码管理软件也在纷纷加入 passkey 功能。假设某帐户同时提供密码和 passkey 登入选项，面对攻击时，用密码管理软件所管理的密码，会比 passkey 更安全吗？下面分情况讨论不同的威胁：

- 如果网站数据库泄露，所谓的被「拖库」。原则上来说，存储在此网站的所有数据都不算安全，我们只关心我们的其它帐户是否有危险。如果使用密码管理器为每个网站设置单独的强密码，一样可以保证其它帐户的安全。Passkey 的更长的密钥长度在实际中不会有什么区别。可以认为两者在面对这类威胁时同等安全的。一定细究的话，passkey 有更好的防呆设计。如果用户在使用密码管理器时故意为不同网站设置同样的密码，密码管理器拦不住用户这么做。而 passkey 则完全不存在这个问题。
- 如果用户选择将密码库和 passkey 同步到云端，当云端服务被攻破，且加密密钥泄露，无论哪个方案都会导致所有网站帐户陷入危险。攻击者可以很容易地枚举所有帐户并一个个登入。
- 钓鱼网站。当攻击者仅仅在用户计算机以外设立了一个钓鱼网站，密码管理软件和 passkey 的 authenticator 都会校验 RP 一方的域名是否是正确的域名，都可以靠 HTTPS 防范中间人攻击。但如果用户的机器已经感染恶意软件，浏览器已经被篡改的话，两者都无能为力。
- 如果讨论计算机已经被恶意软件感染的情况，事情就比较微妙了。相当一部分传统计算机安全专家认为一旦计算机已经感染恶意软件，一切全完。这种「全或无」的想法在实际中未免有些绝对。
  - 对于传统密码管理软件来说，对于运行于本地计算机的恶意软件的防范比较有限。但许多密码管理器都做了不同程度的防护：浏览器插件配对需要用户确认以免恶意软件冒名顶替，使用模拟键盘自动输入密码时乱序输入来防范 key logger，复制密码到剪贴板之后会定时清空剪贴板，解锁密码库时需要操作系统层面的 FaceID 或者 Windows Hello 授权，凡此等等。具体的实现每家密码管理器各不相同，需要仔细选择。
  - Passkey 相对来说，攻击面要小一些，passkey 根本不可能通过键盘输入，也就无需防范 key logger 和监听剪贴板的恶意程序。但仍然有一些攻击点：如果恶意软件冒充浏览器向 passkey authenticator 发出请求的话，它并不认证浏览器的合法性，而是依赖用户在输入 PIN 或者使用 FaceID 的时候察觉是否有不对劲。所以，即使伪装浏览器，恶意软件还需要有能力绕过操作系统的 PIN 或 FaceID 弹窗才能在用户不知不觉的情况下瞒天过海登入帐户，如前所述，这个难度并不低。有的用户不仔细看系统弹窗的显示内容，稀里糊涂就扫脸通过，那就很麻烦。
- 设备被盗被抢。两者的情况大差不差。Passkey 是强制每次使用都需要解锁，如果使用 PIN 来保护 passkey 的话，在公共场合使用的时候容易被人偷拍到 PIN。而如果用 FaceID 或指纹的话，在被暴力胁迫时会直接解锁设备。而密码管理器也好不到哪里去，虽然提供了一些设置的灵活性，但如果设置每次输密码都要校验 FaceID 的话，就和 passkey 一样；如果一次解锁一直可用的话，如果设备在开机状态下被抢，直接就是裸奔。哪种更好，就要看你是认为自己的设备容易被附近的人在你不在的时候偷偷干点什么，还是更容易被人盯上之后蓄意抢走，还是……

总的来说，passkey 更标准化一些（虽然有很多非标实现），理论上来说更防呆。而密码管理器的可选设置选项更多，适合根据自己的 threat model 来定制。最坏情况下，在十分漠视安全的用户手中，密码管理器肯定更不安全。在最审慎的使用情况下，passkey 的安全性要略好一些，比如说完全免疫剪贴板监视程序。

而如果选择使用外置硬件密钥作为 passkey 设备，会比操作系统或密码管理软件提供的 passkey 功能更安全一些，相应地在便捷性上会有一些取舍。


## passkey 类型

在目前的 passkey 推广过程中，即使是几家主要的厂商也常常对于他们是如何部署 passkey 验证语焉不详。如果对于安全有强迫症一样的追求的话，搞清楚「这家用的 passkey 到底有多安全」不是个容易的活。

反之，如果你只想要一个「比密码更安全的，用起来省心的登录方法」，大可以跳过此节，直接开始使用 passkey。

### discoverable credential 和 non-discoverable credential

其实 passkey 只是 FIDO2 WebAuthn 换了个好听的新名字。对于 FIDO2 WebAuthn 来说，有两种凭证：discoverable credential 和 non-discoverable credential。以前叫作 resident key 和 non-resident key。现在说的 passkey，严格来说，应该只是 discoverable credential。不过也有一些网站比如说 Google 在管 non-discoverable credential 叫作 passkey。

就实际使用体验来说，discoverable credential 理论上连输入用户名都可以免掉。因为用户名、网站域名连同私钥一起存储在 passkey 当中。而 non-discoverable credential 则需要输入用户名之后再进行认证，passkey 设备本身并不存储该网站的登入用私钥。

简略而说，两者的工作模式是这样的：

- 对于 discoverable credential，用户在网站选择使用 passkey 登入之后，网站会向 passkey 设备发出请求，设备检查自己是否存有该网站的登录凭证，如果有的话，就调取内部存储的私钥进行签名认证，没有就拒绝认证。如果有多个用户名的话，浏览器会提示用户选择其中一个用于登录。
- 对于 non-discoverable credential，认证过程很像 FIDO U2F（虽然 U2F 通常用于 2FA 而非 passkey）。用户需要先输入用户名，网站调取记录，找到一段数据，将这个数据包发给 passkey 设备来进行下一步。这个数据（key handle）是和前述 discoverable credential 认证过程中的最大的不同点。它不仅仅包含网站的域名等信息，还包含用户私钥信息！不过它被 passkey 设备的公钥加密，只有 passkey 设备的私钥才能解密，所以网站无法读取或篡改其中的内容（这里说的 passkey 设备的私钥是它的 master 私钥，每个 passkey 设备上的每个 authenticator 只有一个，而非每个网站有不同的私钥）。这个数据解开之后，passkey 设备使用其中的数据重建「该网站认证专用」私钥，再以该私钥签名认证。如果仅仅用作第二因素认证的话，整个过程并不强制要求用户验证 PIN 。但如果是用作免密码登录的 passkey，用户必须要先输入 PIN 或者指纹解锁 passkey 设备，之后 authenticator 才会执行认证。

由上可见，discoverable credential 需要占用 passkey 设备的存储空间，而 non-discoverable credential 不需要。对于手机这样的设备来说，存储密钥所占的空间可以忽略不计，而对于 Yubikey 之类的外置硬件密钥来说，存储空间有限。5.7 版固件之前的 Yubikey 只支持存储 25 组 discoverable credentials，到底把这宝贵的 25 个槽用在哪些网站上就得琢磨一下了。

这两种认证方式的另一个区别是，最坏情况下，当 passkey 设备丢失，且 PIN 泄露，也就是说攻击者可以完全控制 passkey 设备时，攻击者可以直接枚举 passkey 设备中存储的所有 discoverable credential，然后逐一登录用户的每一个帐户。相反，攻击者完全无法获知这个 passkey 设备到底在哪些网站上注册了 non-discoverable credential，更不知道用户名，想控制用户的网络帐户还需要再花一番功夫。也就是说，在最坏情况下，用户有更多的时间去做亡羊补牢的工作。

遗憾的是，对于绝大多数网站来说，用户并没有选择到底是使用 discoverable credential 还是 non-discoverable credential 的自由，只能使用网站所提供的选项。

### 设备绑定的 passkey 和可以跨设备同步的 passkey

对于 passkey 认证来说，最核心的是用户的私钥。不同的私钥存储方式安全性不同。

最安全的私钥存储方式是：私钥在 passkey 设备上创建并只能在 passkey 设备上使用，永远不能离开 passkey 设备。这样做的缺点很明显：如果设备丢失的话，这个 passkey 就没了，需要使用其它方式登录后再创建一个 passkey。如果买了新手机，想在新手机中设置 passkey 的话，每个网站都要重新来一遍。

因此 FIDO2 标准并不禁止 passkey 设备将私钥传到云端。目前苹果设备上创建的 passkey 都会上传到 iCloud Keychain，而 Android 设备的 passkey 默认都会上传到 Google Password Manager。这样做的优点是用户买了新手机之后不需要重新设置，所有网站的登录凭证都自动下载下来立刻可用。但风险也因此增加：任何一个设备被攻击得手，所有存储于 iCloud Keychain 中的 passkey 都会泄露。整体的安全性等同于任何同步了私钥的 passkey 设备中安全性最低的那一个。比如说，如果手机端每次使用 passkey 都需要 FaceID 但 Mac 上只有开机的时候才需要验指纹，使用 passkey 的时候不需要的话，那么这个网站帐户的安全性就等同于它在 Mac 上登录时的安全性——也就是说任何人在 Mac 开机的时候偷走你的 Mac 就可以登入你的帐户 [例子](https://www.reddit.com/r/Passkeys/comments/1fz6cb9/passwordless_pinless_authentication_possible_for/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 。对于最重要的帐户，也许不要传到云端为妙。

目前 Apple 和 Google 默认都使用云端同步。而微软一方较为谨慎，Windows Hello 创建的 passkey 默认只存储在本地。

至少在目前，iCloud Keychain 无法在 Android 设备上使用。这带来了一点小麻烦：如果想在 iPhone 和 Android 上都使用 passkey 登录同一个网站，需要在两台手机上分别创建 passkey。一个办法是使用第三方密码管理器来同步 passkey，比如说 1Password，LastPass 和 Bitwarden，它们都同时支持 iOS 和 Android。但这些密码管理器并非操作系统组件，更容易被恶意软件攻击。

与此相对，外置硬件密钥提供了另一种思路：虽然密钥本身不同步到云端，但可以把硬件密钥插到不同设备上使用。使用 Yubikey 这样的硬件密钥，只需要在登入的时候把 Yubikey 插到（或者贴上）正在用的手机就可以了。因而，它既提供了最强的安全性，同时也提供了操作系统 passkey 所欠缺的一点跨平台同步的便捷性。

## 混乱的命名：passkey 和 security key

严格来说，只有 FIDO2 中的 discoverable credential （DC）才能称为 passkey。然而实际上，包括 Google 在内的网站依然将 non-discoverable credential （NDC）称为 passkey。所以遇到 passkey 一词时，唯一能确定的是，它是一种基于 FIDO2 WebAuthn 的免密码登录方式，可能是 DC 也可能是 NDC。

Security key，严格来说，指的是外接硬件密钥，它们可能支持 FIDO2，可能支持 U2F，也可能只支持老旧的 PIV 标准。这里的混乱要更大一些：在 Google 等许多网站中，security key 被特指为「使用 FIDO U2F 方式提供 2FA 认证的硬件密钥」。如果这个密钥可以被用作免密码登录，就会被改称为 passkey。也就是说，在这些网站上所称的 security key 是实际的 security key 的一个真子集，且和作为 passkey 使用的 security key 在使用场合上完全无重叠（虽然物理上可能是同一个设备）。比如说在 Google 帐户中，同一把 Yubikey，可以同时被登记为一把用于二次验证用的 security key 和一把用于免密码登录的 passkey。

另外一个定义上的混乱是，passkey 到底指的是存有 passkey 的设备（比如说手机、Yubikey）还是里面所存储的私钥？在实际中，passkey 常常模糊地指代两者。既可以看到「将手机用作 passkey」这种描述，也会看到「创建 passkey」这种描述。如果按前者，手机是 passkey，如果按后一种，手机里存储的私钥才是 passkey。准确地说，手机是 passkey 设备，里面存储的私钥是 passkey，而管理认证过程并存储 passkey 的软件，如前所述，是 authenticator。但在不致引起误解的前提下，将 passkey 设备和 authenticator 称作 passkey 似乎也没什么关系。

|                                 | 实际                                 | 在大部分网站中      |
|---------------------------------|--------------------------------------|---------------------|
| 手机、电脑里存储的 passkey      | 是 passkey                           | 被称为 passkey      |
| 硬件密钥作为 2FA 凭证使用时     | 是 security key                      | 被称为 security key |
| 硬件密钥作为 passkey 设备使用时 | 既是 passkey 设备，也是 security key | 被称为 passkey      |
| 设备中存储的 NDC 凭证           | 不是 passkey                         | 可能被称为 passkey  |
| 任何使用 DC 免密码认证的设备    | 是 passkey                           | 被称为 passkey      |

对于普通用户来说，没有必要搞清楚这些名词的区分。不过对于一些较真且在安全性上不愿意妥协的用户来说，本来这些网站在描述 passkey 时就常常语焉不详，这些名称上的混乱进一步增加了搞清楚问题的难度。

# passkey 使用

本节可能会随各网站对 passkey 的支持情况而更新。最近一次更新于 2024 年 10 月。

## 可以用作 passkey 的设备

### Windows

Windows 10 和 Windows 11 现在把 passkey 功能内置到了 Windows Hello 里，操作系统可以创建和管理 passkey。解锁 passkey 时可以使用 Windows Hello 所支持的任何 Windows 登录凭证，如 PIN，指纹等。

当在 Windows 设备上需要绑定 Yubikey 等外置硬件密钥时，需要注意弹出的提示到底是 Windows Hello 还是 Yubikey。通常 Windows Hello 会先弹出来，点击取消之后才会询问是否要绑定 Yubikey。使用外置硬件密钥来登入帐户倒没什么坑，不会有 Windows Hello 跳出来干扰。

### iOS 设备

iOS 也已经支持 passkey 的创建和管理，系统创建的 passkey 会同步到 iCloud Keychain 中。在支持 passkey 登录的网站创建 passkey 之后，所有 iPhone iPad Mac 都可以用同一把 passkey 登录。支持使用 PIN，FaceID 或 TouchID 解锁 passkey。

iOS 设备的 Safari 似乎不能为外置硬件密钥创建 passkey，但使用外置硬件密钥登入帐户的体验是很丝滑的，无论是用 NFC 还是 USB 接口。偶尔在系统更新之后会有一些问题，比如说 iOS 18.1 就有许多人反映 NFC passkey 不好用。

### Android 设备

Android 同样已经支持创建和管理 passkey。系统创建的 passkey 会同步到 Google Password Manager 中。不过 Google Password Manager 曾经有许多十分糟糕的安全设计，在密码管理器当中只能算三流产品，不知道以前的老问题现在是否都已经修正。

同样，Android 系统也支持使用外置硬件密钥。

### Yubikey 等外置硬件密钥

任何支持 FIDO2 的硬件密钥都可以用作 passkey。不过，它们只能存储有限个 discoverable credentials。

固件版本 5.7 之前的 Yubikey 支持 25 个 passkey，5.7 及之后的版本支持 100 个 passkey。目前的冠军是 token 2 的 PIN+ Release2 系列，支持存储 300 个 passkey。最新的 Google Titan Security Key 支持 250 个 passkey 但并未提供删除替换旧 passkey 的功能，所以不一定好用。当然，这里说的 passkey 都是 discoverable credential。对于 non-discoverable credential，如前所述，则没有数目上的限制。

## 支持 passkey 登录的网站

[passkey.directory](https://passkeys.directory/) 可能是目前最全面的 passkey 支持网站列表，对于一些网站还有当前支持的情况说明。

下面汇总一些常见网站设置和使用 passkey 的体验，会比 passkey.directory 写的详细一些。

### Microsoft

在操作系统御三家中，Microsoft 对免用户名密码登录的支持最早，也最全面。不过很长时间里一直在测试，时灵时不灵。目前来看已经比较完善可用，对于各种 passkey 设备都有所支持。微软只支持 discoverable credential 登录。即使在当年 Yubikey 只能作为 2FA security key 使用的时候，也会创建一个 discoverable credential。如果当年已经将 YUbikey 作为 2FA 凭证登记，之后会自动升级成 passkey。

如果要使用 passkey 登录，登入时不可填写用户名，而需要点击下方的 Sign-in Option 按钮，再选择「Face, fingerprint, PIN or security key」。

综上，微软对 passkey 的支持最为规范全面，几乎没有什么坑。总结：只支持 discoverable credential，不需要输入用户名，支持所有类型 passkey，支持所有浏览器。

微软旗下的不少网站，如 GitHub 等，对 passkey 的支持和微软自家网站相当。

### Google

Google 对 2FA security key 的支持很早，但 passkey 功能上线之后有相当长的时间里这个功能极度混乱。目前 Google 的实现也是比较奇怪的。

如果使用操作系统内置 passkey 功能创建 passkey 的话，Google 应该创建的是 discoverable credential。而如果使用 Yuibkey 作为 passkey 设备的话，大部分情况下会创建 non-discoverable credential，虽然也有人说他们创建了 discoverable credential 但我从未成功过。什么时候是 discoverable credential 什么时候是 non discoverable credential 有些难以捉摸。Google 应该是为数不多的可以使用 non-discoverable credential 进行免密码登录的网站。遗憾的是这并不是 Google 文档中明文提供的选项，所以这种行为并不稳定，实际登记 passkey 的时候到底发生什么就 YMMV 了。

在登录 Google 帐户时，免用户名登录的选项比较隐蔽。如果浏览器支持 passkey，当光标停在用户名输入框的时候，会有一个小下拉菜单「Use a passkey」。不然的话，在输入用户名之后还有一次选择 passkey 登录的机会。如果用的是 non-discoverable credential，只能在输入用户名之后才可以用 passkey 登录。

Google 也是主流服务里少见的允许用户将一把硬件密钥同时登记为 2FA security key 和 passkey 的网站，当然这样也没什么用。目前来看，似乎只有在很久以前就在 Google 帐户中登记的 2FA security key 可以和 passkey 共存。如果用最新的硬件和最新的浏览器，一把硬件密钥只能在 2FA security key 和 passkey 中二选一。

在今天，如果想把 Yubikey 仅用于 2FA security key 的话，办法是先禁用 Yubikey 的 FIDO2 功能，再作为 security key 登记（否则会被登记为 passkey）。

一些小提示：

- 如果帐户中既有 2FA security key 又有 passkey 的话，有些环节的交互逻辑会有些令人迷惑：比如说，在已经登入帐户的情况下，如果要访问一些敏感信息，仍然需要再次验证密码或 passkey，此时 2FA security key 不可以用于验证身份，必须使用密码或 passkey。如果用的 key 仅注册为 2FA security key 的话，用户可能会对验证失败的结果有些迷惑。

- 在 Google 网页上创建 passkey 时，如果使用 create a passkey 选项，则只能使用操作系统内置 passkey 功能。如果需要注册外置硬件密钥，需要使用 Use another device 选项。

总结：支持免用户名登录，对外置硬件密钥支持有些奇怪，支持所有类型 passkey，支持所有浏览器。

### Apple

Apple 对 passkey 的支持是御三家里最迟缓的。很长时间里，苹果即使对于 2FA 也是坚持使用自家平台的验证码推送。对于 passkey 来说，苹果同样选择尽可能把用户困在自己的生态环境里。

目前，没有任何办法为 Apple ID 手工创建 passkey。使用 iOS 17 以上的设备登录 Apple ID 时，会自动为用户创建 passkey，这个 passkey 在设置中不可见，无法删除。

在使用浏览器登入 Apple ID 时，在输入用户名之后有一个使用 passkey 登入的选项，然后可以使用 iPhone 扫码登入。这似乎是使用 passkey 登入苹果帐户的唯一途径。目前不支持 Firefox。

苹果支持使用 Yubikey 作为 2FA security key 但不支持将 Yubikey 用作 passkey。更讨厌的是，目前用 Yubikey 做 2FA 也很令人痛苦：许多旧设备和 Windows 客户端、Android 客户端会被踢下来无法登录。目前在非苹果平台上的客户端，只有 iCloud for Windows 已经明确支持 security key，其它的支持状态仍然不明，许多人反映，一旦启用 security key，Apple Music 无法在非苹果平台登录。往好里说，苹果至少做对了一点：如果你希望用 security key 来加强安全性，那么所有更不安全的登录方式都必须被禁用。但苹果迟缓的的软件开发进度使得 security key 目前体验不佳。

总结：没有免用户名登录，只能使用苹果设备，无法绑定第三方 passkey，不支持 Firefox。即使是 security key 的支持也有很多限制。

### GitHub

作为微软旗下网站，对 passkey 的支持是一流的。如果之前已经把 Yubike 登记为 2FA security key 的话，在创建 passkey 时会提供「升级」为 passkey 的选项。在 Firefox 上，这个升级过程有一定概率出错，如果出错的话需要删除重加一下。和 Google 不同，同一把硬件密钥在帐户里只会显示为一把，要么是 2FA security key，要么是 passkey。

和其它微软服务一样，如果使用 passkey 登录的话，不要填写用户名，直接点下方的「Sign in with a passkey」。

总结：只支持 discoverable credential，不需要输入用户名，支持所有类型 passkey，支持所有浏览器。

### Amazon 

Amazon 对 passkey 的支持吧，说是不支持，它倒也支持。但这个支持实在是实现的脑洞清奇。

首先，amazon 对 passkey 的理解就很成问题。它的帮助文档里认为 passkey 「仅仅」是可以在云端漫游的 passkey ，所以你只需要一个 Apple 的，一个 Google 的，不需要更多了。视 Microsoft 和 Yubikey 为无物。虽然实际上也完全可以用 Windows Hello 和 Yubikey 绑定 passkey 。

其次，amazon 无法使用 passkey 绕过 2FA。passkey 只能省去输密码的麻烦，形同一个密码管理器（参见上文，可能它的技术团队真的觉得 passkey 和你把 amazon 密码存在 iCloud Keychain 里没什么区别）。如果你的 amazon 帐户开启了 2FA，那么你每次登入 amazon 需要解锁 passkey 之后再输入 2FA 验证码。这纯属脱了裤子放屁。2FA TOTP 验证码唯一的作用就是证明用户持有一个可以生成验证码的设备。如果按 amazon 的理解，passkey 就存在手机上，TOTP 也是手机上的 app, 多这一道手续不会增加任何安全性。

最后，amazon 创建的是 discoverable credential，但它依然要求输入用户名登录，无法实现免用户名登录。

综上，在 amazon 上使用 passkey 的唯一用途大概是「不输密码，避免被键盘监听软件偷密码」吧。

### Adobe

Adobe 对 passkey 的支持也是比较奇特的。像 Google 一样，它在登录的时候在输用户名的地方有一个下拉框可以选择 passkey，此时只能使用 DC 登入，而输入用户名之后，还有一个使用 NDC passkey 登入的按钮。不过我只成功地创建 NDC passkey，不知道它到底支持不支持创建 DC passkey。

和 Amazon 一样，用 passkey 登入 Adobe 时不能跳过两步验证，登入过程十分麻烦。

最后，它甚至不提供为 passkey 重命名的功能！如果 passkey 丢失之后想删除的话，大概只能把所有 passkey 都一股脑删掉了帐。

总的来说，这个支持确实很差，和 Amazon 一样，唯一的用途就是「不输密码」。

### NVidia

NVidia 对 passkey 的支持很早，但支持很奇特。登录的时候必须选择“Login with Secure Device”，之后可以用 passkey 免用户名登录，却仍然需要输入 2FA TOTP 验证码。

总结：使用 discoverable credential 支持免用户名登录，但仍然需要 TOTP 验证码。

### Passkey 支持十分糟糕的网站

有一些网站，说是支持 passkey 吧，确实是支持的，但有些致命的问题。

- CVS: CVS 的网站做的奇差无比。它只能登记一把 passkey 且不提供删除 passkey 的选项！你最好指望你的 passkey 永远不会丢……
