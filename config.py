# Duygu ve Motivasyon Analizi için Konfigürasyon Dosyası

MOTIVATION_LEVELS = {
    "low": (0.0, 0.4),
    "medium": (0.4, 0.7),
    "high": (0.7, 1.0)
}

CATEGORY_QUESTIONS = {
    # Akademik Gelişim
    "akademik": {
        "low": [
            "Ders çalışmaya başlamakta neden zorlanıyorsun?",
            "Hangi dersler seni en çok strese sokuyor?",
            "Ödevlerini erteleme nedenlerin neler?",
            "Sınav kaygısıyla başa çıkamadığın durumlar neler?",
            "Motivasyonunu en çok ne düşürüyor?"
        ],
        "medium": [
            "Ders çalışma rutininde en çok zorlandığın nokta nedir?",
            "Hangi öğrenme yöntemi senin için en verimli?",
            "Sınav kaygısıyla nasıl başa çıkıyorsun?",
            "Zaman yönetimi konusunda kendini nasıl geliştirebilirsin?",
            "Ders çalışırken motivasyonunu nasıl koruyorsun?"
        ],
        "high": [
            "En başarılı olduğun ders hangisi ve neden?",
            "Öğrenirken en çok neyden keyif alıyorsun?",
            "Akademik hedeflerine ulaşmak için hangi adımları atıyorsun?",
            "Öğrenme sürecinde en büyük desteği nereden alıyorsun?",
            "Gelecek dönem için akademik planların neler?"
        ]
    },
    
    # Sosyal İlişkiler
    "sosyal": {
        "low": [
            "Sosyal ortamlarda kendini nasıl hissediyorsun?",
            "Yeni insanlarla tanışmak seni neden korkutuyor?",
            "Sosyal medya seni nasıl etkiliyor?",
            "Kalabalık ortamlarda rahatsız olduğun şeyler neler?",
            "Sosyal hayatında değiştirmek istediğin bir şey var mı?"
        ],
        "medium": [
            "Sosyal çevren seni nasıl etkiliyor?",
            "Yeni insanlarla tanışırken en çok neye dikkat ediyorsun?",
            "Sosyal aktivitelerde en çok neyden keyif alıyorsun?",
            "Sosyal becerilerini geliştirmek için neler yapıyorsun?",
            "Sosyal medya kullanımın ilişkilerini nasıl etkiliyor?"
        ],
        "high": [
            "Arkadaşlık ilişkilerinde en çok neye önem veriyorsun?",
            "En yakın arkadaşlarının seni en çok etkileyen özelliği ne?",
            "Ailenle olan ilişkilerini nasıl tanımlarsın?",
            "Sosyal aktivitelerde en çok neyden keyif alıyorsun?",
            "Sosyal hayatında en çok neye minnettarsın?"
        ]
    },
    
    # Kariyer Planlama
    "kariyer": {
        "low": [
            "Kariyer hedeflerin konusunda kendini nasıl hissediyorsun?",
            "İş arama sürecinde en çok ne zorlanıyorsun?",
            "Kariyerinde en çok neyi erteleme eğilimindesin?",
            "Hangi becerileri geliştirmekten korkuyorsun?",
            "Kariyer planlamada en büyük engelin ne?"
        ],
        "medium": [
            "Hayalindeki iş ortamını nasıl hayal ediyorsun?",
            "Kariyer hedeflerine ulaşmak için hangi becerileri geliştirmelisin?",
            "İş-yaşam dengesi konusunda kendini nasıl değerlendiriyorsun?",
            "Hangi sektörler ilgini çekiyor ve neden?",
            "Profesyonel ağını genişletmek için neler yapıyorsun?"
        ],
        "high": [
            "Kariyerinde en çok gurur duyduğun başarın neydi?",
            "5 yıl sonra kendini kariyer basamaklarının neresinde görüyorsun?",
            "Yeteneklerini nasıl daha iyi pazarlayabilirsin?",
            "Mentorluk almak ister misin? Neden?",
            "Kariyerinde şu anda en motive edici şey nedir?"
        ]
    },
    
    # Finansal Okuryazarlık
    "finans": {
        "low": [
            "Para yönetimi konusunda en çok neyi erteliyorsun?",
            "Finansal konularda en büyük korkun ne?",
            "Bütçe yapmakta neden zorlanıyorsun?",
            "Harcama alışkanlıklarında değiştirmek istediğin ne?",
            "Finansal konularda en çok neyi anlamakta zorlanıyorsun?"
        ],
        "medium": [
            "Para yönetimi konusunda kendini nasıl değerlendiriyorsun?",
            "Tasarruf yapmak için hangi yöntemleri kullanıyorsun?",
            "Bütçe planlaması yaparken nelere dikkat ediyorsun?",
            "Finansal hedeflerini nasıl belirliyorsun?",
            "Borç yönetimi konusunda kendini nasıl değerlendiriyorsun?"
        ],
        "high": [
            "Finansal özgürlük senin için ne ifade ediyor?",
            "Yatırım yapmayı düşünüyor musun? Neden?",
            "Pasif gelir kaynakları oluşturmak için neler yapıyorsun?",
            "Finansal okuryazarlığını nasıl geliştirebilirsin?",
            "Uzun vadeli finansal planların neler?"
        ]
    },
    
    # Teknoloji Kullanımı
    "teknoloji": {
        "low": [
            "Teknoloji kullanımında en çok neyi erteliyorsun?",
            "Hangi teknolojik araçlar seni strese sokuyor?",
            "Dijital detoks yapmak ister misin? Neden?",
            "Teknoloji bağımlılığı konusunda endişelerin var mı?",
            "Teknolojik gelişmeler seni korkutuyor mu?"
        ],
        "medium": [
            "Teknolojinin hayatındaki rolü nedir?",
            "Hangi teknolojik araçlar olmadan yapamazsın?",
            "Sosyal medya kullanım süreni nasıl kontrol ediyorsun?",
            "Dijital güvenlik önlemlerini nasıl alıyorsun?",
            "Online eğitim platformlarını kullanıyor musun?"
        ],
        "high": [
            "Yapay zeka hakkında ne düşünüyorsun?",
            "Hangi uygulamalar hayatını kolaylaştırıyor?",
            "Yeni teknolojileri öğrenmek için ne yapıyorsun?",
            "Teknolojiyi nasıl verimli kullanıyorsun?",
            "Gelecekte hangi teknolojileri kullanmayı hayal ediyorsun?"
        ]
    },
    
    # Yaratıcılık
    "yaratıcılık": {
        "low": [
            "Yaratıcılığını engelleyen şeyler neler?",
            "Yaratıcı projeleri neden erteliyorsun?",
            "Yaratıcı çalışmalarını paylaşmaktan çekiniyor musun?",
            "Yaratıcı blokaj yaşadığında ne yapıyorsun?",
            "Yaratıcılık konusunda kendini nasıl görüyorsun?"
        ],
        "medium": [
            "Yaratıcılığını en çok ne tetikliyor?",
            "Yaratıcı projeler üretirken nasıl bir süreç izliyorsun?",
            "Günlük rutininde yaratıcılığa nasıl yer veriyorsun?",
            "İlham kaynakların neler?",
            "Yaratıcılığın zamanla nasıl değişti?"
        ],
        "high": [
            "En sevdiğin sanat dalı nedir ve neden?",
            "Yaratıcı çalışmalarını nasıl sergiliyorsun?",
            "Yaratıcılığını beslemek için neler yapıyorsun?",
            "Disiplinlerarası projeler denedin mi?",
            "Yaratıcılığınla nasıl bir fark yaratıyorsun?"
        ]
    },
    
    # Fiziksel Sağlık
    "fiziksel_saglik": {
        "low": [
            "Sağlık rutininde en çok neyi erteliyorsun?",
            "Egzersiz yapmaktan neden kaçınıyorsun?",
            "Uyku düzeninde en büyük sorunun ne?",
            "Sağlıklı beslenmekte neden zorlanıyorsun?",
            "Vücudunla ilgili en çok neyi değiştirmek istersin?"
        ],
        "medium": [
            "Uyku düzenin nasıl ve kaliteli uyuyor musun?",
            "Beslenme alışkanlıklarını nasıl değerlendiriyorsun?",
            "Düzenli egzersiz yapıyor musun? Nasıl bir programın var?",
            "Sağlık kontrollerini düzenli yaptırıyor musun?",
            "Enerji seviyeni nasıl yükseltiyorsun?"
        ],
        "high": [
            "Vücudunla ilgili genel olarak nasıl hissediyorsun?",
            "Sağlık hedeflerin neler?",
            "Dinlenmiş hissetmek için ne yapıyorsun?",
            "Sağlıklı yaşam için hangi değişiklikleri yaptın?",
            "Fiziksel sağlığın için en önemli rutin nedir?"
        ]
    },
    
    # Zihinsel Sağlık
    "zihinsel_saglik": {
        "low": [
            "Zihinsel olarak en çok ne seni yoruyor?",
            "Stresle başa çıkmakta neden zorlanıyorsun?",
            "Olumsuz düşüncelerle nasıl başa çıkıyorsun?",
            "Mental olarak en zorlandığın dönem neydi?",
            "Zihinsel sağlık konusunda destek almayı düşünür müsün?"
        ],
        "medium": [
            "Zihinsel sağlığını nasıl koruyorsun?",
            "Stresle başa çıkmak için hangi yöntemleri kullanıyorsun?",
            "Meditasyon yapıyor musun? Nasıl bir deneyim?",
            "Zihnini dinlendirmek için ne yapıyorsun?"
        ],
        "high": [
            "Mental olarak en güçlü olduğun anlar ne zaman?",
            "Zihinsel sağlığın için en önemli uygulaman ne?",
            "Minnettarlık günlüğü tutuyor musun?",
            "Olumlu düşünme pratiklerin neler?",
            "Zihinsel sağlığını nasıl daha iyi hale getirirsin?"
        ]
    },
 
    # Aile
    "aile": {
        "low": [
            "Aile içi iletişimde zorlandığın noktalar neler?",
            "Ailenle paylaşmaktan kaçındığın konular neler?",
            "Aile içinde kendini ifade etmekte zorlanıyor musun?",
            "Çocukluk aile deneyimlerin şimdiki seni nasıl etkiliyor?",
            "Ailenle ilişkilerini geliştirmek için ne yapabilirsin?"
        ],
        "medium": [
            "Ailenle ilişkilerini nasıl tanımlarsın?",
            "Ailende en çok kimle anlaşıyorsun? Neden?",
            "Ailen seni en çok neyle motive ediyor?",
            "Aile bağlarını güçlendirmek için ne yapıyorsun?",
            "Ailenle paylaşmaktan en çok keyif aldığın aktivite ne?"
        ],
        "high": [
            "Ailenin sana kattığı en değerli şey ne?",
            "Ailenle en güzel anın neydi?",
            "Gelecekte kurmak istediğin aile nasıl olacak?",
            "Ailen için minnettar olduğun şeyler neler?",
            "Ailenle birlikte yapmaktan en çok keyif aldığın şey ne?"
        ]
    },
    
    # Spiritüel Gelişim
    "spirituel": {
        "low": [
            "Spiritüel konularda kendini nasıl hissediyorsun?",
            "Meditasyon yapmakta neden zorlanıyorsun?",
            "İç huzurunu bulmakta zorlandığın anlar ne zaman?",
            "Hayat amacın hakkında kendini nasıl hissediyorsun?",
            "Maneviyatın hayatında nasıl bir yer tutuyor?"
        ],
        "medium": [
            "Hayat amacın hakkında ne düşünüyorsun?",
            "Meditasyon yapıyor musun? Nasıl bir deneyim?",
            "İç huzurunu nasıl sağlıyorsun?",
            "Doğayla bağlantı kurmak senin için ne ifade ediyor?",
            "Manevi gelişim için neler yapıyorsun?"
        ],
        "high": [
            "En son ne zaman gerçekten huzurlu hissettin?",
            "Hayatın anlamı hakkında ne düşünüyorsun?",
            "Manevi pratiklerin var mı?",
            "Evrenle bağlantı kurduğunu hissettiğin anlar ne zaman?",
            "Spiritüel gelişimin için en önemli şey ne?"
        ]
    },
    
    # Hobiler ve İlgi Alanları
    "hobiler": {
        "low": [
            "Hobilerine zaman ayırmakta neden zorlanıyorsun?",
            "Yeni bir hobi denemekten seni alıkoyan şey ne?",
            "Hobilerinle ilgili bir topluluğa katılmak ister misin?",
            "Çocukken sevdiğin aktiviteleri neden bıraktın?",
            "Hobilerin için bütçe ayırmak ister misin?"
        ],
        "medium": [
            "En sevdiğin hobin nedir ve sana ne katıyor?",
            "Hobilerine ne sıklıkla zaman ayırıyorsun?",
            "Yeni bir hobi edinmek ister misin? Ne?",
            "Hobilerin stresini azaltmanda yardımcı oluyor mu?",
            "Hobilerin kişisel gelişimine nasıl katkı sağlıyor?"
        ],
        "high": [
            "Hobilerinle ilgili bir topluluğa dahil misin?",
            "Hobilerin için bütçe ayırıyor musun?",
            "En son ne zaman yeni bir hobi denedin?",
            "Hobilerinle nasıl bir fark yaratıyorsun?",
            "Hobilerinden ne öğrendin?"
        ]
    },
    
    # Seyahat
    "seyahat": {
        "low": [
            "Seyahat etmekten seni alıkoyan şeyler neler?",
            "Yalnız seyahat etmek seni neden korkutuyor?",
            "Seyahat planı yapmakta neden zorlanıyorsun?",
            "Seyahatlerin bütçeni nasıl etkiliyor?",
            "Seyahat etmek senin için neden önemli?"
        ],
        "medium": [
            "En son nereye seyahat ettin ve seni en çok ne etkiledi?",
            "Seyahat etmek senin için ne ifade ediyor?",
            "Hayalindeki seyahat neresi? Neden?",
            "Seyahatlerin kişisel gelişimine nasıl katkı sağlıyor?",
            "Seyahat planı yaparken en çok neye dikkat ediyorsun?"
        ],
        "high": [
            "Yalnız seyahat etmeyi denedin mi? Nasıl bir deneyimdi?",
            "Seyahatlerinde en çok neyi keşfetmeyi seviyorsun?",
            "Kültürlerarası deneyimler seni nasıl etkiliyor?",
            "Gelecekte hangi ülkelere gitmek istiyorsun?",
            "Seyahatlerinden ne öğrendin?"
        ]
    },
    
    
    
    # Sanat ve Tasarım
    "sanat": {
        "low": [
            "Sanatla ilgilenmekten seni alıkoyan şeyler neler?",
            "Sanat eserlerinden neden etkilenmiyorsun?",
            "Kendini sanatla ifade etmekte neden zorlanıyorsun?",
            "Sanatın günlük hayatındaki yeri nedir?",
            "Sanatçı olmak ister miydin? Neden?"
        ],
        "medium": [
            "Sanat senin için ne ifade ediyor?",
            "En sevdiğin sanat dalı nedir? Neden?",
            "Sanat eserlerinden nasıl etkileniyorsun?",
            "Kendini sanatla ifade ediyor musun? Nasıl?",
            "Son zamanlarda seni en çok etkileyen sanat eseri neydi?"
        ],
        "high": [
            "Sanatın ruh sağlığına etkisini düşünüyor musun?",
            "Yaratıcı süreçte en çok neyden ilham alıyorsun?",
            "Sanatın toplumsal rolü hakkında ne düşünüyorsun?",
            "Sanatla nasıl bir fark yaratıyorsun?",
            "Sanatın hayatındaki en önemli etkisi ne?"
        ]
    }
}

SUGGESTIONS = {
    "akademik": {
        "low": [
            "Küçük adımlarla başla: Günde sadece 15 dakika çalış",
            "Zorlandığın konuları belirle ve yardım iste",
            "Çalışma ortamını düzenleyerek dikkat dağıtıcıları azalt",
            "Gerçekçi hedefler belirle ve başardıkça küçük ödüller ver",
            "Ders çalışma arkadaşı bul"
        ],
        "medium": [
            "Pomodoro tekniğini dene: 25 dakika çalış, 5 dakika mola",
            "Zorlandığın konuları küçük parçalara bölerek çalış",
            "Farklı öğrenme yöntemlerini dene (videolar, podcast'ler)",
            "Haftalık tekrar yaparak bilgilerini pekiştir",
            "Öğrendiklerini başkalarına anlatarak pekiştir"
        ],
        "high": [
            "Yeni bir öğrenme yöntemi keşfet",
            "Akademik projelerde liderlik rolü al",
            "Öğrendiklerini uygulamak için pratik yap",
            "Mentorluk yaparak bilgilerini paylaş",
            "Uzun vadeli akademik hedefler belirle"
        ]
    },
    
    "sosyal": {
        "low": [
            "Küçük sosyal adımlar at (bir selam ver, gülümse)",
            "Sosyal medya kullanımını sınırlandır",
            "Yalnız kalmaya zaman ayır ve kendini dinle",
            "Olumlu insanlarla vakit geçirmeye çalış",
            "İletişim becerilerini geliştirmek için pratik yap"
        ],
        "medium": [
            "Yeni sosyal aktivitelere katılarak çevreni genişlet",
            "Kaliteli zaman geçirdiğin insanlarla daha çok vakit geçir",
            "İletişim becerilerini geliştirmek için kitaplar oku",
            "Arkadaşlarınla düzenli buluşmalar planla",
            "Empati kurmayı ve aktif dinlemeyi pratik et"
        ],
        "high": [
            "Sosyal projelerde liderlik rolü al",
            "Yeni insanlara mentorluk yap",
            "Sosyal becerilerini geliştirmek için eğitim al",
            "Topluluk önünde konuşma pratiği yap",
            "Sosyal ağını stratejik olarak genişlet"
        ]
    },
    
    "kariyer": {
        "low": [
            "Küçük adımlarla başla: CV'ni güncelle",
            "Kariyer hedeflerini yazılı hale getir",
            "Sektörünle ilgili basit makaleler oku",
            "Bir kariyer danışmanıyla görüş",
            "Temel becerilerini geliştirmeye başla"
        ],
        "medium": [
            "LinkedIn profilinizi güncelleyin ve aktif kullanın",
            "Sektörünüzle ilgili en az haftada bir makale okuyun",
            "Networkünüzü genişletmek için ayda bir etkinliğe katılın",
            "Yeni beceriler öğrenmek için online kurslara katılın",
            "Kariyer hedeflerinizi aylık gözden geçirin"
        ],
        "high": [
            "Profesyonel ağınızı stratejik olarak genişletin",
            "Sektör konferanslarında konuşmacı olun",
            "Mentorluk yaparak bilginizi paylaşın",
            "Yüksek profilli projelere katılın",
            "Uzun vadeli kariyer planları yapın"
        ]
    },
    
    "finans": {
        "low": [
            "Harcamalarını bir ay boyunca takip et",
            "Küçük tasarruflar yapmaya başla",
            "Temel finansal terimleri öğren",
            "Otomatik tasarruf ayarı yap",
            "Basit bir bütçe planı oluştur"
        ],
        "medium": [
            "50-30-20 kuralını uygulayın (Zorunlu-Tasarruf-Kişisel)",
            "Harcamalarınızı takip etmek için bir uygulama kullanın",
            "Temel yatırım araçlarını öğrenmeye başlayın",
            "Aylık bütçe toplantıları yapın",
            "Finansal okuryazarlık podcast'leri dinleyin"
        ],
        "high": [
            "Yatırım portföyünüzü çeşitlendirin",
            "Pasif gelir kaynakları oluşturun",
            "Finansal danışmanla görüşün",
            "Uzun vadeli yatırım stratejileri geliştirin",
            "Finansal bağımsızlık planı yapın"
        ]
    },
    
    "teknoloji": {
        "low": [
            "Teknoloji kullanımını gözden geçir",
            "Ekran süreni azaltmak için küçük adımlar at",
            "Basit bir dijital detoks yap",
            "Teknolojiyle ilgili temel bilgileri öğren",
            "Dijital güvenlik önlemlerini gözden geçir"
        ],
        "medium": [
            "Dijital detoks günleri belirleyin",
            "Ekran sürenizi takip etmek için bir uygulama kullanın",
            "Yeni bir yazılım dili öğrenmeye başlayın",
            "Teknoloji haberlerini düzenli takip edin",
            "Sosyal medya kullanım sürelerinizi sınırlandırın"
        ],
        "high": [
            "Yeni teknolojiler geliştirmeye katıl",
            "Teknoloji blogu yazmaya başla",
            "Yazılım projeleri geliştir",
            "Teknoloji etkinliklerinde konuşmacı ol",
            "Dijital ürünler oluştur"
        ]
    },
    
    "yaratıcılık": {
        "low": [
            "Günde 5 dakika yaratıcı bir aktivite yap",
            "Bir fikir defteri tutmaya başla",
            "Çocukken sevdiğin yaratıcı aktivitelere dön",
            "Yaratıcı blokaj için kendine izin ver",
            "Basit sanat malzemeleriyle denemeler yap"
        ],
        "medium": [
            "Günlük yaratıcılık egzersizleri yapın",
            "Farklı sanat dallarını deneyimleyin",
            "Yaratıcı topluluklara katılın",
            "Rutinlerinizi değiştirin (farklı yoldan işe gitmek gibi)",
            "Doğada zaman geçirerek ilham alın"
        ],
        "high": [
            "Yaratıcı projelerde liderlik rolü al",
            "Eserlerini sergilemek için fırsatlar yarat",
            "Disiplinlerarası projeler deneyin",
            "Yaratıcılık workshop'ları düzenleyin",
            "Yaratıcılığını ticari ürünlere dönüştür"
        ]
    },
    
    "fiziksel_saglik": {
        "low": [
            "Günde 10 dakika yürüyüş yap",
            "Su tüketimini artır",
            "Uyku saatlerini düzenlemeye çalış",
            "Fast food tüketimini azalt",
            "Basit egzersizlerle başla"
        ],
        "medium": [
            "Düzenli uyku saatleri belirleyin ve bunlara uyun",
            "Beslenmenize daha fazla meyve-sebze ekleyin",
            "Günde en az 30 dakika hareket edin",
            "Stres seviyenizi kontrol etmek için meditasyon yapın",
            "Düzenli sağlık kontrolleri yaptırın"
        ],
        "high": [
            "Kişisel antrenörle çalış",
            "Maraton gibi zorlu hedefler belirle",
            "Sağlıklı yaşam blogu başlat",
            "Spor müsabakalarına katıl",
            "Sağlıklı yaşam workshop'ları düzenle"
        ]
    },
    
    "zihinsel_saglik": {
        "low": [
            "Günde 5 dakika nefes egzersizi yap",
            "Olumsuz duyguları kabul et ve yargılama",
            "Küçük molalar ver ve zihnini dinlendir",
            "Sevdiğin bir aktiviteye zaman ayır",
            "Profesyonel destek almayı düşün"
        ],
        "medium": [
            "Duygularınızı tanımlamak için günlük tutun",
            "Nefes egzersizleri yaparak stresinizi azaltın",
            "Minnettarlık günlüğü tutun ve her gün minnettar olduğunuz 3 şey yazın",
            "Sevdiklerinizle duygularınızı paylaşın",
            "Kendinize karşı şefkatli olun ve mükemmeliyetçilikten kaçının"
        ],
        "high": [
            "Meditasyon liderliği yap",
            "Zihinsel sağlık workshop'ları düzenle",
            "Mindfulness pratiklerini derinleştir",
            "Zihinsel dayanıklılık eğitimleri al",
            "Başkalarına mentorluk yap"
        ]
    },
    

    
    "aile": {
        "low": [
            "Haftada bir aile yemeği düzenleyin",
            "Aile üyelerine basit teşekkürler ifade edin",
            "Ayda bir aile aktivitesi planlayın",
            "Aile hikayelerini dinleyin ve kaydedin",
            "Birlikte basit gönüllülük aktiviteleri yapın"
        ],
        "medium": [
            "Düzenli aile toplantıları yapın",
            "Birlikte yemek yeme alışkanlığı edinin",
            "Aile hikayelerini paylaşın ve kaydedin",
            "Birlikte yeni aktiviteler deneyin",
            "Aile üyelerinize minnettarlığınızı ifade edin"
        ],
        "high": [
            "Aile gelenekleri oluşturun ve sürdürün",
            "Aile vizyonu ve değerlerini belirleyin",
            "Aile üyeleriyle terapi veya koçluk deneyin",
            "Aile olarak toplumsal projeler yürütün",
            "Aile bireyleriyle kişisel gelişim çalışmaları yapın"
        ]
    },
    
    "spirituel": {
        "low": [
            "Günde 3 dakika nefes egzersizi yapın",
            "Doğada kısa yürüyüşler yapın",
            "Haftada bir minnettarlık listesi yapın",
            "Basit meditasyon denemeleri yapın",
            "Olumlu bir niyetle güne başlayın"
        ],
        "medium": [
            "Günlük meditasyon yapın",
            "Doğada düzenli zaman geçirin",
            "Minnettarlık günlüğü tutun",
            "Manevi okumalar yapın",
            "Derin nefes egzersizleri yapın"
        ],
        "high": [
            "Manevi inzivalara katılın",
            "Spiritüel bir topluluğa dahil olun",
            "Mentorluk veya rehberlik yapın",
            "Spiritüel uygulamalarınızı derinleştirin",
            "Spiritüel bir yolculuk veya hac deneyimi yaşayın"
        ]
    },
    
    "hobiler": {
        "low": [
            "Haftada 1 saat hobinize zaman ayırın",
            "Yeni bir hobi araştırın",
            "Hobinizle ilgili basit videolar izleyin",
            "Hobinizi paylaşabileceğiniz birini bulun",
            "Hobinizle ilgili küçük hedefler belirleyin"
        ],
        "medium": [
            "Haftada en az 2 saat hobinize ayırın",
            "Hobilerinizi paylaşabileceğiniz bir topluluğa katılın",
            "Hobinizle ilgili bir blog veya günlük tutun",
            "Hobinizle ilgili workshoplara katılın",
            "Hobinizi geliştirmek için ekipman alın"
        ],
        "high": [
            "Hobinizi gelir kaynağına dönüştürün",
            "Hobinizle ilgili profesyonel eğitim alın",
            "Hobinizde ustalaşmak için yoğun çalışın",
            "Hobinizle ilgili bir iş veya girişim başlatın",
            "Hobinizde mentorluk yapın"
        ]
    },
    
    "seyahat": {
        "low": [
            "Yakın çevrenizde keşif yapın",
            "Seyahat için küçük bir bütçe ayırın",
            "Seyahat blogları okuyun",
            "Yerel kültür etkinliklerine katılın",
            "Seyahat fotoğrafları albümü oluşturun"
        ],
        "medium": [
            "Yılda en az bir kez yeni bir yere seyahat edin",
            "Seyahat bütçesi oluşturun",
            "Seyahat öncesi araştırma yapın",
            "Yerel kültürleri deneyimlemeye odaklanın",
            "Seyahat günlüğü tutun"
        ],
        "high": [
            "Uzun süreli seyahat planları yapın",
            "Sürdürülebilir seyahat yöntemlerini uygulayın",
            "Seyahat deneyimlerinizi profesyonelce paylaşın",
            "Seyahat rehberliği yapın",
            "Seyahatle ilgili bir iş veya girişim başlatın"
        ]
    },
    
  
    
    "sanat": {
        "low": [
            "Ayda bir sanat etkinliğine katılın",
            "Basit sanat malzemeleriyle denemeler yapın",
            "Sanatla ilgili belgeseller izleyin",
            "Yerel sanat sergilerini ziyaret edin",
            "Yaratıcı yazarlık denemeleri yapın"
        ],
        "medium": [
            "Bir sanat dalını öğrenmeye başlayın",
            "Sanat eserlerini analiz etmeyi öğrenin",
            "Yerel sanatçıları destekleyin",
            "Sanat terapisi deneyin",
            "Sanat tarihi öğrenin"
        ],
        "high": [
            "Profesyonel sanat eğitimi alın",
            "Kendi serginizi açın",
            "Sanat koleksiyonu oluşturun",
            "Sanatla ilgili bir atölye veya okul açın",
            "Sanat alanında mentorluk yapın"
        ]
    }
}

KEYWORD_MAP = {
    "akademik": ["ders", "sınav", "ödev", "tez", "proje", "not", "hoca", "üniversite", "öğrenme", "okul", "eğitim", "mezun", "akademi", "ders çalışma", "sınıf", "üniversite", "öğrenci", "öğretmen", "sınav kaygısı", "mezuniyet", "staj", "araştırma", "makale", "sunum", "seminer", "konferans", "kütüphane", "laboratuvar", "deney", "stajyer"],
    
    "sosyal": ["arkadaş", "aile", "parti", "dışarı", "gezi", "toplantı", "iletişim", "yalnızlık", "sohbet", "dost", "grup", "kulüp", "organizasyon", "etkinlik", "buluşma", "tanışma", "davet", "sosyalleşme", "topluluk", "network", "iletişim", "konuşma", "dinleme", "paylaşım", "diyalog", "ilişki", "bağlantı", "çevre", "sosyal medya", "takipçi"],
    
    "kariyer": ["iş", "mülakat", "terfi", "maaş", "kariyer", "CV", "linkedin", "işsizlik", "kariyer", "meslek", "profesyonel", "şirket", "ofis", "yönetici", "çalışan", "müdür", "pozisyon", "maaş", "terfi", "istifa", "işe alım", "referans", "portföy", "kariyer planlama", "network", "sektör", "endüstri", "kariyer danışmanı", "iş görüşmesi", "staj"],
    
    "finans": ["para", "bütçe", "yatırım", "kredi", "borç", "tasarruf", "harcama", "borsa", "gelir", "gider", "banka", "hesap", "faiz", "döviz", "altın", "emeklilik", "sigorta", "vergi", "bütçe planlama", "finansal özgürlük", "pasif gelir", "yatırım portföyü", "hisse senedi", "fon", "birikim", "nakit", "kredi kartı", "banka hesabı", "finansal planlama"],
    
    "teknoloji": ["bilgisayar", "telefon", "yazılım", "donanım", "internet", "wifi", "uygulama", "app", "programlama", "kod", "dijital", "siber", "veri", "bulut", "yapay zeka", "robot", "algoritma", "sosyal medya", "oyun", "stream", "download", "upload", "hacker", "güvenlik", "şifre", "email", "web site", "domain", "hosting", "program"],
    
    "yaratıcılık": ["tasarım", "sanat", "resim", "müzik", "yazı", "şiir", "roman", "çizim", "fotoğraf", "heykel", "seramik", "dans", "tiyatro", "senaryo", "kurgu", "ilham", "yaratıcı", "yenilikçi", "orijinal", "icat", "keşif", "hayal gücü", "fikir", "proje", "eser", "kompozisyon", "kolaj", "enstalasyon", "performans", "sergi"],
    
    "fiziksel_saglik": ["spor", "egzersiz", "koşu", "yürüyüş", "yoga", "pilates", "fitness", "vücut", "sağlık", "diyet", "beslenme", "vitamin", "mineral", "protein", "karbonhidrat", "yağ", "kalori", "metabolizma", "kilo", "kas", "kemik", "eklem", "nabız", "tansiyon", "şeker", "kolesterol", "check-up", "doktor", "hastane", "ilaç"],
    
    "zihinsel_saglik": ["stres", "kaygı", "depresyon", "panik", "terapi", "psikolog", "psikiyatr", "meditasyon", "mindfulness", "nefes", "rahatlama", "uyku", "dinlenme", "yorgunluk", "tükenmişlik", "motivasyon", "odak", "konsantrasyon", "hafıza", "özgüven", "benlik", "kişisel gelişim", "farkındalık", "duygu", "düşünce", "davranış", "alışkanlık", "değişim", "iyileşme"],
    
    "aile": ["anne", "baba", "kardeş", "çocuk", "torun", "dede", "nine", "amca", "dayı", "hala", "teyze", "kuzen", "yeğen", "aile", "ev", "yuva", "akraba", "soy", "sülale", "miras", "gelenek", "görenek", "bayram", "toplantı", "bir araya gelme", "aile bağları", "aile içi iletişim", "aile terapisi", "aile danışmanlığı", "aile hekimi"],
    
    "spirituel": ["ruh", "maneviyat", "meditasyon", "yoga", "dua", "ibadet", "tanrı", "allah", "evren", "enerji", "karma", "reenkarnasyon", "kader", "kısmet", "şans", "fal", "burç", "astroloji", "numeroloji", "reiki", "şifa", "huzur", "dinginlik", "sükunet", "farkındalık", "varoluş", "anlam", "amaç", "mistisizm", "tasavvuf"],
    
    "hobiler": ["koleksiyon", "pul", "para", "kart", "maket", "lego", "bulmaca", "yapboz", "satranç", "dama", "kitap", "okuma", "yazma", "günlük", "blog", "fotoğrafçılık", "resim", "çizim", "boyama", "heykel", "seramik", "dikiş", "nakış", "örgü", "ahşap", "marangoz", "bahçe", "bitki", "evcil hayvan", "akvaryum"],
    
    "seyahat": ["gezi", "seyahat", "tatil", "otel", "pansiyon", "hostel", "uçak", "tren", "otobüs", "gemi", "vapur", "feribot", "araç kiralama", "pasaport", "vize", "gümrük", "havaalanı", "terminal", "valiz", "bavul", "gezi rehberi", "tur", "rehber", "harita", "navigasyon", "dil", "kültür", "gelenek", "yemek", "alışveriş"],
    
    "sanat": ["resim", "heykel", "seramik", "fotoğraf", "sinema", "tiyatro", "opera", "bale", "dans", "müzik", "enstrüman", "şarkı", "konser", "sergi", "galeri", "müze", "performans", "edebiyat", "şiir", "roman", "öykü", "deneme", "tiyatro oyunu", "senaryo", "koreografi", "kompozisyon", "desen", "renk", "perspektif", "estetik"]
}

MODEL_NAME = "savasy/bert-base-turkish-sentiment-cased"