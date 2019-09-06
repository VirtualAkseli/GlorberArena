## Käyttäjä: Kollektiivin jäsen

Glörber -kollektiivin jäsenenä, haluan päästä käsiksi nopeasti ja helposti vuosien saatossa tekemäämme mediaan.

Tästä syystä Glörber-keskustelupalstalla tulee olla ennen kaikkea tehokkaasti toimiva ja järkeviä tuloksia antava **hakutoiminto**. Viihteellinen selaaminen mielessäpitäen, **järkevä jaottelu aihealueittain** tekee summittaisestakin selaamisesta mukavaa.

Järkevän jaottelun mahdollistavat haut:
- Haetaan Aihealueen otsikot listattavaksi:  
`` SELECT subject.id, subject.name FROM subject
				LEFT JOIN Theme ON Theme.id = subject.theme_id
				WHERE (subject.theme_id = :theme_id)
				GROUP BY subject.id `` 
        
Viestin muokkauksen mahdollistavat haut:        
- Haetaan vastausviestille asiankuuluva otsikko:  
`` SELECT subject.id, subject.name FROM subject
				LEFT JOIN Post ON Post.subject_id = subject.id
				WHERE (subject.id = :topic_id)
				GROUP BY subject.id `` 
     
     
Muuta:     
- Listataan profiilisivulla käyttäjän viestit:  
`` SELECT * FROM Post
   LEFT JOIN account ON account.id = Post.account_id
   WHERE (account_id = :user_id) ``   

Käyttäjätilin luotuani, minulla tulee olla mahdollisuus hypätä jonkinlaisen "omat toiminnot"-**yhteenvetosivun** kautta keskusteluihin joihin osallistun. Sama pätee myös toisinpäin; ellei käyttäjä niin ole erikseen asettanut, voin toisen ihmisen "tiliä" tarkastellessani katsoa hänen kirjoittamiaan viestejä.

Kollektiivin hengen tuntien, edellytän, että jo(i)llekin suodaan ylläpito-oikeudet asiattomuuksien kitkemiseksi ja ylipäätään keskustelupalstan sääntöjen noudattamista valvomaan. Vaikka sisältö voikin olla huonoa, jopa lukukelvotonta, kukaan ei vaivaudu vilkaisemaan sitä, jos foorumilla vallitsevat rajaseudun (olemattomat) lait
