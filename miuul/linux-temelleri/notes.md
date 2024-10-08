# Linux Temelleri ve Komut Satırı İşlemleri - Miuul Eğitimi

## Linux Dünyasına Giriş

### Genel Bilgilendirme

- Linux Temelleri ve Komut Satırı İşlemleri eğitimine hoş geldiniz! Eğitimi tamamladığınız zaman aşağıdaki konular hakkında bilgi sahibi olacaksınız:
  - Linux Kurulumları
  - Temel Komutlar
  - Kullanıcılar ve Gruplar
  - Dosya ve Dizin Erişimleri
  - Paket Yönetimi
  - Sistem İzleme Komutları
  - Ağ Komutları

### Linux Düntyasına Giriş

### Linux Hakkında

- Linus Torvalds tarafından 1991 yılında geliştirilen ve günümüzde dünya genelinde en çok kullanılan işletim sistemlerinden biri olan Linux, Unix benzeri bir işletim sistemidir. Git'in mucididir.
- Linux, açık kaynak kodludur. Özelleştirilebilir. Birçok linux dağıtımı vardır. CentOs, Linux Mint, Ubuntu, Fedora, Debian, Red Hat, Suse, Arch Linux, Kali Linux, Gentoo, Slackware, vs. Ücretsizdir. Basit ve hızldıdır. TCP/IP protokolüne desteği vardır. Bu da internet haberleşmesini sağlar.
- Linux, birçok platformda çalışabilir. (x86, x86_64, ARM, MIPS, PowerPC, SPARC, Alpha, Itanium, vs.)

| Linux | Windows |
| --- | --- |
| Open Source | Closed Source |
| Free | Paid |
| Customizable | Not customizable |
| More efficient | Less efficient |
| Case-sensitive | Case-insensitive |
| Root yetkisi | Administrator yetkisi |
| Bash | Powershell |
| No drives | Different drives |

- help komutu ile yardım alabiliriz. `help` veya `help <komut>` şeklinde kullanılabilir.

### Dosya Sistemi Hiyerarşisi

- Filesystem Hierarchical Structure (FHS) - Dosya Sistemi Hiyerarşisi
- root directory (/) - kök dizin
  - bin - binary files, binary files, commands: mv, ls, cat
  - sbin - system binary files, sistemi yeniden başlatma, iptables konfigürasyonları, root yetkisi gerektiren komutlar
  - lib - system libraries, .lib and .so files
  - opt - optional addon apps
  - boot - boot loader files, linux kernel
  - etc - editable text configuration, configuration files, .conf files, Resolv.conf, Crontab
  - home - kullanıcı dizinleri, `/home/<username>`, can be created files in the username
  - root - root user's home directory, root yetkisi gerekir
  - srv - service data, web server script & data files
  - media - removable media, cdrom, usb
  - mnt - mount directory, hard disk
  - tmp - temporary files, reboot sonrası silinir. her kullanıcı erişemez
  - dev - device files, sabit disk, usb gibi
  - proc - process information, virtual file system, /proc/cpuinfo
  - sys - system files, linux 2.6 çekirdeği için oluşturulmuş bir dosya sistemi
  - var - variable files, database files, logs, temporary files
    - lib - uygulamaların durumlarını içeren dosyaları içerir.
    - log - log dosyalarını içerir.
    - tmp - geçici dosyaları içerir. her kullanıcı erişebilir.
  - usr - unix system resources, binary files, libraries, docs. /bin bulunamazsa /usr/local/bin dosyası içinde bulunabilir
  - lost+found - file system check - fsck, dosya sistemi kontrolü sırasında bozuk dosyaların kurtarıldığı dizin.

## Temel Komutlar

- "|" - pipe, komutları birleştirmek için kullanılır. Komutların çıktısını bir sonraki komuta iletir. `ls -l | more` şeklinde kullanılabilir.

### pwd

- `pwd` - print working directory or present working directory, bulunduğunuz dizini gösterir.
- `pwd --help` - yardım almak için kullanılır.

### ls

- `ls` - listeleme komutu, dizin içeriğini listeler.
- `ls --help` - yardım almak için kullanılır.
- `ls -l` - long format, detaylı listeleme
- `ls -a` - all files, gizli dosyaları da listeler
- `ls -la` - long format, all files
- `ls -lh` - human readable, boyutları okunabilir hale getirir
- `ls -r` - reverse order, ters sıralama
- `ls -t` - sort by time, zaman sıralaması
- `ls -lra` - long format, reverse order, all files
- `ls -arlh` - long format, all files, reverse order, human readable
- `ls -l -h -r -a` - long format, human readable, reverse order, all files. Bu şekilde de kullanabiliriz ama tavsiye edilmez ve tek seferde yazmak daha iyidir.
- `ls -R` - recursive, alt dizinleri de listeler

### cd

- `cd` - change directory, dizin değiştirme komutu
- `cd --help` - yardım almak için kullanılır.
- `cd /` - root dizinine gitmek için kullanılır.
- `cd ..` - bir üst dizine gitmek için kullanılır.
- `cd /home/username` - belirtilen dizine gitmek için kullanılır.
- `cd ~` - home dizinine gitmek için kullanılır.

### touch

- `touch` - dosya oluşturma komutu
- `touch --help` - yardım almak için kullanılır.
- `touch filename` - belirtilen isimde dosya oluşturur.

### mkdir

- `mkdir` - dizin oluşturma komutu
- `mkdir --help` - yardım almak için kullanılır.
- `mkdir dirname` - belirtilen isimde dizin oluşturur.
- `mkdir -p dirname/subdirname` - alt dizinlerle birlikte dizin oluşturur.
- `mkdir {dirname1,dirname2,dirname3}` - birden fazla dizin oluşturur.

### rm ve rmdir

- dosya ve dizin silme komutları
- rmdir boş dizinleri siler.
- rm dosyaları siler.
- `rm --help` - yardım almak için kullanılır.
- `rmdir --help` - yardım almak için kullanılır.
- `rm filename` - belirtilen dosyayı siler.
- `rm -i filename` - silme işlemi onaylanır.
- `rm -f filename` - silme işlemi onaylanmaz. Dikkatli kullanılmalıdır.
- `rm -r dirname` - belirtilen dizini ve alt dizinleri siler. Dikkatli kullanılmalıdır.
- `rm -rf dirname` - belirtilen dizini ve alt dizinleri siler, onaylanmaz. Dikkatli kullanılmalıdır.
- `rm -rf *` - tüm dosyaları siler. Dikkatli kullanılmalıdır. Kullanılırken dizine dikkat edilmelidir.
- `rmdir dirname` - belirtilen dizini siler.
- `rmdir dirname -v` - silme işlemi gösterilir.

### cp

- `cp` - dosya kopyalama komutu veya dizin kopyalama komutu
- `cp --help` - yardım almak için kullanılır.
- `cp source target` - belirtilen dosyayı veya dizini kopyalar.
- `cp -i source target` - kopyalama işlemi onaylanır. Eğer hedef dosya varsa onay ister.
- `cp -r source target` - belirtilen dizini ve alt dizinleri kopyalar.
- `cp -v source target` - kopyalama işlemi gösterilir.
- `cp *.txt target` - belirtilen uzantıdaki dosyaları kopyalar.
- `cp filename1 filename2` - dosyayı farklı bir isimle kopyalar.
- `cp -r dirname1 dirname2` - dizini farklı bir isimle kopyalar.

### mv

- `mv` - dosya taşıma komutu veya dosya adı değiştirme komutu
- `mv --help` - yardım almak için kullanılır.
- `mv source target` - belirtilen dosyayı veya dizini taşır.
- `mv -i source target` - taşıma işlemi onaylanır. Eğer hedef dosya varsa onay ister.
- `mv -v source target` - taşıma işlemi gösterilir.
- `mv filename1 filename2` - dosyayı farklı bir isimle değiştirir.
- `mv dirname1 dirname2` - dizini farklı bir isimle değiştirir.

### cat

- `cat` - dosya içeriğini gösterme komutu. Concatenate. Yeni dosya oluşturmak için de kullanılabilir. Var olan dosyaları birleştirmek için de kullanılabilir.
- `cat --help` - yardım almak için kullanılır.
- `cat filename` - belirtilen dosyanın içeriğini gösterir. Üstüne yazdırır.
- `cat > filename` - yeni dosya oluşturur ve içeriği yazmanızı sağlar. `Ctrl + D` ile çıkış yapabilirsiniz.
- `cat >> filename` - dosyanın sonuna ekleme yapar.
- `cat file1 file2 > file3` - file1 ve file2 dosyalarını birleştirerek file3 dosyasına yazar.
- `cat file1 file2 >> file3` - file1 ve file2 dosyalarını file3 dosyasının sonuna ekler.
- `cat <<EOF > filename` - EOF (End Of File) ile dosya oluşturur ve içeriği yazmanızı sağlar. `Ctrl + D` ile çıkış yapabilirsiniz.
- `cat <<EOF >> filename` - EOF (End Of File) ile dosyanın sonuna ekleme yapar.
- `cat -n filename` - dosyanın satırlarını numaralandırır.

### vi ve vim

- `vi` - vi text editor, düzenleme yapma komutu. Yeni dosya oluşturmak için de kullanılabilir.
- `vim` - vi improved, geliştirilmiş vi text editor komutu. Yeni dosya oluşturmak için de kullanılabilir.
- `vi --help` - yardım almak için kullanılır.
- `vim --help` - yardım almak için kullanılır.
- `vi filename` - belirtilen dosyayı düzenler. `i` tuşuna basarak insert moduna geçebilirsiniz. `Esc` tuşuna basarak normal moduna geçebilirsiniz. `:w` ile kaydedebilirsiniz. `:q` ile çıkış yapabilirsiniz. `:wq` ile kaydedip çıkış yapabilirsiniz. `:q!` ile kaydedilmemiş dosyadan çıkabilirsiniz.
- `vim filename` - belirtilen dosyayı düzenler. `i` tuşuna basarak insert moduna geçebilirsiniz. `Esc` tuşuna basarak normal moduna geçebilirsiniz. `:w` ile kaydedebilirsiniz. `:q` ile çıkış yapabilirsiniz. `:wq` ile kaydedip çıkış yapabilirsiniz. `:q!` ile kaydedilmemiş dosyadan çıkabilirsiniz.
- `:set number` - satır numaralarını gösterir.
- `:set nonumber` - satır numaralarını gizler.
- `:5,10d` - 5. satırdan 10. satıra kadar olan satırları siler.
- `:dd` - o anki satırı siler.
- `ZZ` - kaydedip çıkış yapar.

### nano

- `nano` - nano text editor, düzenleme yapma komutu. Yeni dosya oluşturmak için de kullanılabilir.
- `nano --help` - yardım almak için kullanılır.
- `nano filename` - belirtilen dosyayı düzenler. `Ctrl + O` ile kaydedebilirsiniz. `Ctrl + X` ile çıkış yapabilirsiniz.
- Alt satırlarda text editor içinde neler yapabileceğinizi yazmaktadır.
- `nano -l filename` - belirtilen dosyayı düzenler. Satır numaralarını gösterir.

### more

- `more` - dosya içeriğini gösterme komutu. Sayfa sayfa gösterir. Büyük dosyaları okumak için kullanılır.
- `more --help` - yardım almak için kullanılır.
- `more filename` - belirtilen dosyanın içeriğini sayfa sayfa gösterir. `Space` tuşuna basarak bir sonraki sayfaya geçebilirsiniz. `Enter` tuşuna basarak bir sonraki satıra geçebilirsiniz. `q` tuşuna basarak çıkış yapabilirsiniz.
- `more +5 filename` - belirtilen dosyanın 5. satırdan başlayarak içeriğini sayfa sayfa gösterir.
- `more -5 filename` - belirtilen dosyanın içeriğini ilk 5 satırını gösterir.
- `more -s filename` - belirtilen dosyanın içeriğinde boş satırları göstermez.

### less

- `less` - dosya içeriğini gösterme komutu. Sayfa sayfa gösterir. Büyük dosyaları okumak için kullanılır. more komutundan daha gelişmiş bir komuttur. Birden fazla formatı destekler.
- `less --help` - yardım almak için kullanılır.
- `less -N filename` - belirtilen dosyanın içeriğini sayfa sayfa gösterir. Satır numaralarını gösterir. `Space` tuşuna basarak bir sonraki sayfaya geçebilirsiniz. `Enter` tuşuna basarak bir sonraki satıra geçebilirsiniz. `q` tuşuna basarak çıkış yapabilirsiniz.
- `less +5 filename` - belirtilen dosyanın 5. satırdan başlayarak içeriğini sayfa sayfa gösterir.
- less ile açtıktan sonra v ye basınca nano editörüne geçer. Kolaylıkla değişiklik yapabilirsiniz.
- `less -p "word" filename` - belirtilen dosyanın içeriğinde arama yapar ve bulduğu ilk kelimeyi gösterir.

### tail

- `tail` - dosyanın son kısmını gösterme komutu. Log dosyalarını izlemek için kullanılır. Sistem ya da uygulama loglarını izlemek için kullanılır.
- `tail --help` - yardım almak için kullanılır.
- `tail filename` - belirtilen dosyanın son kısmını gösterir. Varsayılan olarak son 10 satırı gösterir.
- `tail -n 5 filename` - belirtilen dosyanın son 5 satırını gösterir.
- `tail -f filename` - belirtilen dosyanın son kısmını gösterir ve dosya güncellendiğinde otomatik olarak günceller. Log dosyalarını izlemek için kullanılır. `Ctrl + C` ile çıkış yapabilirsiniz.

### echo

- `echo` - ekrana yazdırma komutu. Sistem değişkenlerini yazdırmak için de kullanılır. Yeni bir dosya oluşturmak için de kullanılabilir. Dosya veya dizinleri göstermek için kullanılabilir.
- `echo --help` - yardım almak için kullanılır.
- `echo "Hello World"` - belirtilen metni ekrana yazdırır.
- `echo "Hello World" > filename` - belirtilen metni yeni dosyaya yazar. Dosya yoksa oluşturur. Dosya varsa üstüne yazar.
- `echo "Hello World" >> filename` - belirtilen metni dosyanın sonuna ekler.
- `echo 2+3`- belirtilen işlemi yapmaz. Sadece metni ekrana yazdırır. `expr` komutu ile işlem yapılabilir.
- `echo $((2+3))` - belirtilen işlemi yapar ve sonucu ekrana yazdırır.
- `echo -e "Hello\nWorld"` - belirtilen metni alt satıra geçirerek ekrana yazdırır.
- `echo $PATH` - PATH değişkenini ekrana yazdırır.
- `echo $HOME` - HOME değişkenini ekrana yazdırır.
- `echo $USER` - USER değişkenini ekrana yazdırır.
- `echo ~` - home dizinini ekrana yazdırır.
- `echo {1..10}` - 1'den 10'a kadar olan sayıları ekrana yazdırır.
- `arg1="Hello"` - arg1 değişkenine değer atar. `echo $arg1` ile ekrana yazdırabiliriz.

### shutdown ve reboot

- `shutdown` - sistem kapatma komutu. Sistemin ne zaman kapanacağını belirtebiliriz.
- `reboot` - sistem yeniden başlatma komutu. Sistemin ne zaman yeniden başlayacağını belirtebiliriz.
- `shutdown --help` - yardım almak için kullanılır.
- `reboot --help` - yardım almak için kullanılır.
- `shutdown -h now` - sistem hemen kapanır.
- `shutdown` - sistem 1 dakika sonra kapanır. Varsayılan olarak 1 dakika bekler.
- `shutdown -c` - kapatma işlemini iptal eder.
- `shutdown 12:50` - sistem 12:50'de kapanır.
- `shutdown +5` - sistem 5 dakika sonra kapanır.

### hostname

- `hostname` - bilgisayarın adını gösterme komutu. /etc/hostname. Kalıcı ya da geçici olarak isim değiştirebiliriz.
- `hostname --help` - yardım almak için kullanılır.
- `hostname` - bilgisayarın adını ekrana yazdırır.
- `sudo hostname newhostname` - bilgisayarın adını değiştirir. Geçici olarak değiştirir. Yeniden başlatıldığında eski adına döner.
- `sudo hostnamectl set-hostname newhostname` - bilgisayarın adını değiştirir. Kalıcı olarak değiştirir. Yeniden başlatıldığında yeni adı alır.

### date

- `date` - tarih ve saat bilgisini gösterme komutu. Sistem saati ve tarihi hakkında bilgi almak için kullanılır. Farklı format ve opsiyonlarla kullanılabilir.
- `date --help` - yardım almak için kullanılır.
- `date` - tarih ve saati ekrana yazdırır.
- `date +%Y` - yıl bilgisini ekrana yazdırır.
- `date +%m` - ay bilgisini ekrana yazdırır.
- `date +%d` - gün bilgisini ekrana yazdırır.
- `date --date="2 days ago"` - 2 gün önceki tarihi ekrana yazdırır.
- `date --date="2 days"` - 2 gün sonraki tarihi ekrana yazdırır.
- `date --date="2 days" +%Y-%m-%d` - 2 gün sonraki tarihi yıl-ay-gün formatında ekrana yazdırır.
- `TZ="America/New_York" date` - New York saati hakkında bilgi alır.
- `timedatectl list-timezones | wc -l` - kaç farklı zaman dilimi olduğunu ekrana yazdırır.
- `timedatectl list-timezones | grep Istanbul` - İstanbul saati hakkında bilgi alır.

### Yardım Alma Komutları

- Linux komutları hakkında bilgi alınmasını sağlar
- help - Komut hakkında bilgi verir, opsiyonları gösterir. `help <command>`
- whatis - Komutun ne işe yaradığını gösterir. `whatis <command>`
- whereis - Kullanılan komutun hangi dizinde olduğunu gösterir. `whereis <command>`
- man - Komutla ilgili tüm dokümantasyonu gösterir. `man <command>`
- info - Komutun açıklamasını gösterir. `info <command>`

### history

- `history` - komut geçmişini gösterme komutu. Daha önce kullanılan komutları gösterir.
- `history --help` - yardım almak için kullanılır.
- `history` - komut geçmişini ekrana yazdırır.
- `history 5` - son 5 komutu ekrana yazdırır.
- `history | grep <command>` - belirtilen komutu içeren komutları ekrana yazdırır.

### clear ve reset

- Komut satırını temizlemek ve komut satırını tekrar yüklemek için kullanılır.
- `clear` - komut satırını temizler.
- `reset` - komut satırının yeniden yüklenmesini sağlar.
- `clear --help` - yardım almak için kullanılır.
- `reset --help` - yardım almak için kullanılır.

### tar

- `tar` - dosya sıkıştırma ve arşivleme komutu. Birçok opsiyonu vardır. Dosya boyutları azalır.
- `tar --help` - yardım almak için kullanılır.
- `tar --usage` - yardım almak için kullanılır.
- c - arşiv oluşturmak için kullanılır. x - arşivi açmak için kullanılır. f - dosya adını belirtir. v - detaylı şekilde işlemi gösterir. z - gzip ile sıkıştırma yapar.
- `tar -cvf archive.tar file1 file2` - file1 ve file2 dosyalarını archive.tar dosyasına ekler.

## Kullanıcılar ve Gruplar

### root

- superuser. Tüm işlemleri gerçekleştirebilir.
- Paketler yükleyebilir, silebilir ya da güncelleyebilir.
- Kullanıcı ya da gruplar oluşturabilir, kullanıcı ya da grupları silebilir.
- Kullanıcılara 'sudo' yetkisi verebilir.
- /etc/sudoers dosyasında tanımlanır.
- root yetkisiyle çalışmak tehlikelidir. Dikkatli olunmalıdır.
- Root directory (Kök dizin): Dosya sistemi hiyerarşisinde en üstte bulunan dizindir. (/)
- Root home: Root kullanıcısının home dizinidir. (/root). Root kullanıcısının konfigürasyonları ve dosyaları burada bulunur.

### sudo

- superuser do. Yetkisi kısıtlanmış dosyalara erişilmesini ya da komutların çalıştırılmasını sağlamak için kullanılır.
- Her kullanıcıya tam yetki verilmemelidir.
- root olmadan root yetkisi kullanılır. Geçici olarak root yetkisi alınır. Süresi 15 dakikadır.
- root şifresinin paylaşılmasına gerek olmaz.
- Kullanıcılar oluşturulduğunda direkt olarak 'sudo' yetkisini kullanamaz.
- /etc/sudoers dosyasında tanımlanması gerekir. 'visudo' komutu ile düzenlenebilir. Bu şekilde açılmalıdır.
- 'Permission denied', 'Sudoers file busy, try again later' gibi hatalar alınabilir. visudo ile açılaiblir.
- [sudoers file](sudoers_file.png), [sudoers file 1](sudoers_file_1.png)
- `root ALL=(ALL:ALL) ALL` - root kullanıcısına tüm yetkileri verir. [root](root_image.png)
- `NOPASSWD:ALL` - şifre sormadan yetki verir.

### su

- switch user. Kullanıcı değiştirme komutu.
- substitute user (yedek kullanıcı)
- Oturumu kapatmaya gerek yoktur.
- Farklı bir kullanıcı ya da root'a geçiş yapmayı sağlar.
- PATH ve LOGNAME gibi değişkenler değişir.
- exit ile eski kullanıcıya geri dönülebilir.
- `su` - root kullanıcısına geçiş yapar.
- `su --help` - yardım almak için kullanılır.
- `su -` - root kullanıcısına geçiş yapar. `su - <username>` - belirtilen kullanıcıya geçiş yapar. Kullanıcı değişkenlerini değiştirir.
- `sudo su` - root kullanıcısına geçiş yapar.
- Root yerine hangi kullanıcıdaysa o kullanıcının şifresini sorar.
- Geçiş yapmadan önceki dizin hangisiyse değiştirmeden geçiş yapar.

### passwd

- Sistemdeki kullanıcıların şifrelerini değiştirmek için kullanılır.
- /etc/passwd dosyasında kullanıcı bilgileri tutulur. Kullanıcıların okuma yetkisi vardır. [passwd](passwd.png) . Şifre bilgisi sadece x olarak gözükür.
- /etc/shadow dosyasında kullanıcılarla ilgili bilgiler tutulur. Bütün kullanıcılar okuma yetkisine sahip değiştir. Dosyanın okunması için 'sudo' yetkisi gereklidir. [shadow](shadow.png)

### Kullanıcı Oluşturma ve Silme

- adduser: Kullanıcı oluşturma komutu. Kullanıcı oluşturulduğunda home dizini de oluşturulur. `sudo adduser <username>` şeklinde kullanılır. Şifre sorar.
- userdel: Var olan kullanıcıyı siler. `sudo userdel <username>` şeklinde kullanılır. Home dizini silinmez. `sudo userdel -r <username>` veya `sudo deluser --remove <username>` şeklinde kullanılır. Home dizini de silinir.

### Grup Oluşturma ve Silme

- groupadd: Grup oluşturma komutu. `sudo groupadd <groupname>` şeklinde kullanılır.
- usermod -aG: Kullanıcıyı gruba eklemek için kullanılır. `sudo usermod -aG <groupname> <username>` şeklinde kullanılır. a: append, G: group.
- /etc/group dosyasında grup bilgileri tutulur. [group](group.png). [group_file](group_file.png). Şifre girilse de girilmese de x olarak gözükür.
- `groupmod -n` - grup adını değiştirir. `sudo groupmod -n <newgroupname> <oldgroupname>` şeklinde kullanılır.
- groupdel: Grubu siler. `sudo groupdel <groupname>` şeklinde kullanılır.

## Dosya ve Dizin Erişimleri

### Dosya ve Dizin Erişim Yetkileri

- Güvenlik ve gizlilik için dosya ve dizinlere erişim yetkileri tanımlanır ve önemmlidir.
- 3 tür kullanıcı vardır: user (u), group (g), others (o).
- 3 tür yetki vardır: read (r), write (w), execute (x).
- 3 tür dosya vardır: regular file (-), directory (d), symbolic link (l) (windowstaki shortcut gibi).
- [dosya yetkileri](dosya_yetkileri.png)
- rwx: read, write, execute yapabilir. r-x: read and execute yapabilir. rw-: read and write yapabilir. -wx: write and execute yapabilir. r--: read yapabilir. -w-: write yapabilir. --x: execute yapabilir. ---: hiçbir işlem yapamaz. Kullanıcı yetkilerini buradan anlayabiliriz. Bunlar group ve others için de geçerlidir.

### Dosya ve Dizin Erişim Yetkileri Değiştirme

- chmod: Dosya ve dizin erişim yetkilerini değiştirmek için kullanılır.
- 3 tür kullanıcı vardır: user (u), group (g), others (o).
- `chmod u=r filename` - belirtilen dosyanın kullanıcı yetkilerini sadece read yapar.
- `chmod u=r, g=w, o=x filename` - belirtilen dosyanın kullanıcı yetkilerini read, group yetkilerini write, others yetkilerini execute yapar.
- `chmod ugo=rw filename` - belirtilen dosyanın kullanıcı, group ve others yetkilerini read ve write yapar.

| Yetki | Sayısal Değer | Binary |
| --- | --- | --- |
| --- | 0 | 000 |
| --x | 1 | 001 |
| -w- | 2 | 010 |
| -wx | 3 | 011 |
| r-- | 4 | 100 |
| r-x | 5 | 101 |
| rw- | 6 | 110 |
| rwx | 7 | 111 |

- `chmod 777 filename` - belirtilen dosyanın kullanıcı, group ve others yetkilerini read, write ve execute yapar.
- `chmod 755 filename` - belirtilen dosyanın kullanıcı yetkilerini read, write ve execute yapar. Group ve others yetkilerini read ve execute yapar.
- `chmod 000 filename` - belirtilen dosyanın kullanıcı, group ve others yetkilerini hiçbir işlem yapamaz.

### Dosya ve Dizin Kullanıcılarını Değiştirmek

- chown: Dosya ve dizinlerin sahibini veya grubunu değiştirmeyi sağlar.
- `chown <username> filename` - belirtilen dosyanın sahibini değiştirir.
- `chown -R <username>:<groupname> filename` - belirtilen dosyanın sahibini ve grubunu değiştirir.
- `chown -R <username>:<groupname> dirname` - belirtilen dizinin sahibini ve grubunu değiştirir.
- chgrp: Dosya ve dizinlerin grubunu değiştirmeyi sağlar.
- `chgrp <groupname> filename` - belirtilen dosyanın grubunu değiştirir.

## Paket Yönetimi (Debian ve REHL tabanlı dağıtımlar)

### apt

- Advanced Package Tool. Debian tabanlı dağıtımlar için paket yönetim aracıdır. Paket indirmek, silmek, güncellemek için kullanılır.
- Farklı komutlarla kullanılabilir: list,install, remove, update, upgrade, search, show, autoremove, purge vb.
- `apt --help` - yardım almak için kullanılır.
- `sudo apt --version` - apt sürümünü ekrana yazdırır.
- `sudo apt update` - paket listesini günceller.
- `sudo apt upgrade` - güncellenebilir paketleri günceller.
- `sudo apt update -y && sudo apt upgrade -y` - paket listesini günceller ve güncellenebilir paketleri günceller.
- `sudo apt install <package>` - belirtilen paketi yükler. `sudo apt install -y <package>` - onay sormadan yükler. `sudo apt install -y <package1> <package2>` - birden fazla paketi yükler.
- `sudo apt remove <package>` - belirtilen paketi siler. `sudo apt remove -y <package>` - onay sormadan siler. `sudo apt remove -y <package1> <package2>` - birden fazla paketi siler.
- `sudo apt autoremove` - gereksiz paketleri siler. `sudo apt autoremove -y` - onay sormadan siler.
- `sudo apt show <package>` - belirtilen paket hakkında bilgi verir.
- `sudo apt list` - yüklü ve yüklü olmayan paketleri listeler. `sudo apt list --installed` - yüklü paketleri listeler. `sudo apt list --upgradable` - güncellenebilir paketleri listeler. `sudo apt list | less` - sayfa sayfa listeler.
- `sudo apt list | grep <package>` - belirtilen paketi içeren paketleri listeler.
- `sudo apt search <package>` - belirtilen paketi arar.
- `sudo apt depends <package>` - belirtilen paketin bağımlılıklarını listeler.

### yum

- yellowdog updater, modified. RHEL, Fedora tabanlı dağıtımlar için paket yönetim aracıdır. Paket indirmek, silmek, güncellemek için kullanılır.
- `yum --help` - yardım almak için kullanılır.
- `yum info <package>` - belirtilen paket hakkında bilgi verir.
- `yum list` - yüklü ve yüklü olmayan paketleri listeler. `yum list installed` - yüklü paketleri listeler. `yum list updates` - güncellenebilir paketleri listeler. `yum list | less` - sayfa sayfa listeler. `yum list | wc -l` - kaç paket olduğunu ekrana yazdırır.
- `yum search <package>` - belirtilen paketi arar.
- `yum install <package>` - belirtilen paketi yükler. `yum install -y <package>` - onay sormadan yükler. `yum install -y <package1> <package2>` - birden fazla paketi yükler.
- `yum reinstall <package>` - belirtilen paketi yeniden yükler.
- `yum remove <package>` - belirtilen paketi siler. `yum remove -y <package>` - onay sormadan siler. `yum remove -y <package1> <package2>` - birden fazla paketi siler.
- `yum update` - güncellenebilir paketleri günceller. Eski paketler kalır.
- `yum-plugin-versionlock` - /etc/yum/pluginconf.d/versionlock.list dosyasında belirtilen paketlerin güncellenmesini engeller.
- `yum versionlock <package>` - belirtilen paketin güncellenmesini engeller.
- `yum versionlock list` - hangi paketlerin güncellenmesinin engellendiğini listeler.
- `yum versionlock clear` - listeyi temizler.
- `yum upgrade` - güncellenebilir paketleri günceller. Eski paketlerin silinmesini sağlar.
- `yum update --obsoletes` - eski paketleri de günceller. Eski paketlerin silinmesini sağlar.

### rpm

- Paketlerin yüklenmesini, listelemesini, silinmesini sağlar.
- `rpm --help` - yardım almak için kullanılır.
- Offline ortamlarda daha çok kullanılır.
- Öncelikle `yum install --downloadonly <package> --downloaddir=<directory>` ile paketi indiririz.
- `rpm -i v h *.rpm` - belirtilen paketi yükler. v: verbose, h: hash. -i: install.
- `rpm -q a` - yüklü paketleri listeler. -q: query, a: all.
- `rpm -e <package>` - belirtilen paketi siler. -e: erase.

## Sistem İzleme Komutları

### top

- Sistemi izlemek için kullanılır. Çalışan tüm processlelri listeler. Processlere ait id, user, komut, önem, memory, cpu kullanımı gibi bilgileri gösterir.
- Spesifik listeleme yapılabilir: pid, memory vb. Sistemin ne kadar süredir açık olduğu bilgisini ekrana yazar.
- `top --help` - yardım almak için kullanılır.
- `top` - sistemi izler. `q` tuşuna basarak çıkış yapabilirsiniz.
- PID ler unique'dir. Process ID.
- `top -u <username>` - belirtilen kullanıcıya ait processleri listeler.
- `top -p <pid>` - belirtilen processi listeler.

### du

- disk usage. Disk kullanımını gösterir. Dizinlerin boyutunu gösterir.
- `du --help` - yardım almak için kullanılır.
- `du` - dizinlerin boyutunu ekrana yazdırır. 1024 byte = 1 KB.
- `du -h` - insan okunabilir formatta ekrana yazdırır. KB, MB, GB gibi.
- `du -sh` - belirtilen dizinin boyutunu ekrana yazdırır. s: summary, h: human readable.
- `du -sh <dirname>` - belirtilen dizinin boyutunu ekrana yazdırır.
- `du --all` veya `du -a` - tüm dosyaların boyutunu ekrana yazdırır.
- `--exclude <filename>` - belirtilen dosyayı hesaplamaz. `--exclude="*.txt"` - belirtilen uzantıdaki dosyaları hesaplamaz.
- `du -ah --exclude="*.txt"` - insan okunabilir formatta belirtilen uzantıdaki dosyaları hesaplamaz.
- Logrotation: Log dosyalarının boyutunu kontrol etmek için kullanılır. Log dosyaları büyüdüğünde disk dolabilir.

### df

- disk free. Kullanılabilir disk alanını gösterir. Disklerin boyutunu, kullanılan alanı, boş alanı, kullanım yüzdesini gösterir.
- `df --help` - yardım almak için kullanılır.
- `df` - disklerin boyutunu, kullanılan alanı, boş alanı, kullanım yüzdesini ekrana yazdırır.
- `df -h` - insan okunabilir formatta ekrana yazdırır. KB, MB, GB gibi.
- `df -a` - tüm dosyaların boyutunu ekrana yazdırır.

### htop

- Sistemi izlemek için kullanılır. Kullanıcı dostu arayüze sahiptir. Çalışan tüm processlelri listeler. Processlere ait id, user, komut, önem, memory, cpu kullanımı gibi bilgileri gösterir.
- Spesifik listeleme yapılabilir: pid, memory vb. Sistemin ne kadar süredir açık olduğu bilgisini ekrana yazar.
- `htop --help` - yardım almak için kullanılır.
- `sudo apt install htop -y` - htop yüklemek için kullanılır. Yüklü değilse.
- `htop` - sistemi izler. `q` tuşuna basarak çıkış yapabilirsiniz.

### free

- Bellek kullanımını gösterir. Spesifik listeleme yapılabilir: megabyte, gigabyte vb.
- `free --help` - yardım almak için kullanılır.
- `free` - bellek kullanımını ekrana yazdırır. KB cinsinden.
- `free -h` - insan okunabilir formatta ekrana yazdırır. MB, GB gibi.
- `free -m` - megabyte cinsinden ekrana yazdırır.
- `free -th` - toplam bellek kullanımını ekrana yazdırır. t: total, h: human readable.
- `watch free -h` - belirtilen komutu belirtilen saniye aralıklarında ekrana yazdırır.

### ps

- process status. Çalışan processleri listeler. Processlere ait id, user, komut, önem, memory, cpu kullanımı gibi bilgileri gösterir.
- Spesifik listeleme yapılabilir: pid, memory vb.
- `ps --help` - yardım almak için kullanılır.
- `ps` - çalışan processleri listeler.
- `ps -u <username>` - belirtilen kullanıcıya ait processleri listeler.
- `ps -ef` - tüm processleri listeler. e: everyone, f: full.
- `ps -ef | less` - sayfa sayfa listeler. q tuşuna basarak çıkış yapabilirsiniz.
- `ps -ef | grep <process>` - belirtilen processi içeren processleri listeler.

### kill

- Bir processi sonlandırmak için kullanılır. Process ID (PID) ile çalışır.
- `kill --help` - yardım almak için kullanılır.
- `kill <pid>` - belirtilen processi sonlandırır.
- `kill -9 <pid>` - belirtilen processi zorla sonlandırır. 9: SIGKILL.

## Ağ Komutları

### Ağ Arayüzleri

- `ifconfig` - ağ arayüzlerini listeler. IP adresi, MAC adresi, broadcast adresi, netmask gibi bilgileri gösterir.
- `ifconfig --help` - yardım almak için kullanılır.
- `sudo apt install net-tools -y` - ifconfig yüklemek için kullanılır. Yüklü değilse.
- `ifconfig -a` - tüm ağ arayüzlerini listeler.
- `sudo ifconfig <interface> up` - belirtilen ağ arayüzünü aktif hale getirir. up: up.
- `sudo ifconfig <interface> down` - belirtilen ağ arayüzünü pasif hale getirir. down: down.
- `sudo ifconfig <interface> <ip>` - belirtilen ağ arayüzüne belirtilen ip adresini atar.
- ifconfig is deprecated. ip komutu kullanılmalıdır.
- `ip a` - ağ arayüzlerini listeler. a: address.
- `sudo ip link set <interface> up` - belirtilen ağ arayüzünü aktif hale getirir.
- `sudo ip link set <interface> down` - belirtilen ağ arayüzünü pasif hale getirir.
- iwconfig - kablosuz ağ arayüzlerini listeler.
- `iwconfig --help` - yardım almak için kullanılır.
- `sudo apt install wireless-tools -y` - iwconfig yüklemek için kullanılır. Yüklü değilse.
- `iwconfig` - kablosuz ağ arayüzlerini listeler.

### DNS

- Domain Name System. IP adreslerini alan adlarına çevirir. Alan adlarını IP adreslerine çevirir.
- DNS olması daha sonrasında değişiklik yapılacağında IP adresi değişikliğinde kolaylık olması içindir.

### ping

- Bir kontrol komutudur. Belirtilen IP adresine paket gönderir ve cevap alır. Ağ bağlantısını kontrol etmek için kullanılır.
- IP adresinin çözümlenmesini sağlar.
- `ping --help` - yardım almak için kullanılır.
- `sudo apt install iputils-ping -y` - ping yüklemek için kullanılır. Yüklü değilse.
- `ping <ip>` - belirtilen IP adresine paket gönderir ve cevap alır. `Ctrl + C` tuşuna basarak çıkış yapabilirsiniz.

### telnet

- telecommunication network. Uzak sunucuya bağlanmak için kullanılır. Bağlantı sağlar. TCP/IP protokolü kullanır. Güvenli değildir. Şifrelenmez.
- Port:23 üzerinden çalışır.
- `telnet --help` - yardım almak için kullanılır.
- `sudo apt install telnet -y` - telnet yüklemek için kullanılır. Yüklü değilse.
- `sudo apt install openssh-server -y` - ssh yüklemek için kullanılır. Yüklü değilse.
- `sudo systemctl status ssh` - ssh servisinin durumunu kontrol eder.
- `telnet <ip> <port>` - belirtilen IP adresine ve portuna bağlanır. `Ctrl + ]` tuşuna basarak çıkış yapabilirsiniz.

### wget ve curl

- İnternet üzerinden dosya indirmek için kullanılır.
- `wget --help` - yardım almak için kullanılır.
- `curl --help` - yardım almak için kullanılır.
- `sudo apt install wget -y` - wget yüklemek için kullanılır. Yüklü değilse.
- `sudo apt install curl -y` - curl yüklemek için kullanılır. Yüklü değilse.
- `wget <url>` - belirtilen URL'den dosya indirir.
- `wget -O <filename> <url>` - belirtilen URL'den dosyayı belirtilen isimde indirir.
- `wget -P <directory> <url>` - belirtilen URL'den dosyayı belirtilen dizine indirir.
- `curl -O <url>` - belirtilen URL'den dosya indirir.
- `curl -o <filename> <url>` - belirtilen URL'den dosyayı belirtilen isimde indirir.
- wget vs curl: wget sadece http, https, ftp protokollerini destekler. curl ise daha fazla protokolü destekler. curl daha esnek ve güçlüdür.
