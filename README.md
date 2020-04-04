# audible-tools
Scripts pour aider à la gestion des services Audible.


## split_audible
Ce script permet de préparer la ligne de commande FFmpeg qui pourra découper proprement un livre audio récupéré sur Audible.
### Utilisation
```
python split_audible.py <FILE_IN> <CODE | META_DATA_URL> ["ffmpeg options" [OUTPUT_EXT]]
```
FILE_IN : le fichier que vous avez récupéré (avec VideoDownloadHelper par exemple).
CODE : le code du livre tel que vous le voyez dans l'URL.
META_DATA_URL : l'URL qui contient les méta-datas.
"ffmpegs options" : les options que l'on souhaite utiliser dans ffmpeg. Si non renseigné, l'option utilisée sera "-c copy".
OUTPUT_EXT : l'extension que l'on souhaite donner aux fichiers de sortie. Si non renseigné, l'extension sera la même que le fichier d'entrée.


Exemple :  
Pour récupérer le découpage de "Pierre et le loup" qui se trouve à l'URL :
```
https://stories.audible.com/pdp/B00TKSFFJE?ref=adbl_ent_anon_ds_pdp_pc_pg-1-cntr-0-1
```
en ayant déjà téléchargé le fichier "pierre_et_le_loup.mp4", on exécute :
```
python split_audible.py pierre_et_le_loup.mp4 B00TKSFFJE
```
qui est l'équivalent de :
```
python split_audible.py pierre_et_le_loup.mp4 "https://stories.audible.com/audibleapi/1.0/content/B00TKSFFJE/metadata?drm_type=Hls&response_groups=chapter_info" 
```

Le script retournera :
```
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:00:00.000 -t 00:03:00.558 -c copy "000 Chapitre 1.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:03:00.558 -t 00:02:33.112 -c copy "001 Chapitre 2.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:05:33.670 -t 00:02:15.976 -c copy "002 Chapitre 3.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:07:49.646 -t 00:01:42.725 -c copy "003 Chapitre 4.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:09:32.371 -t 00:02:04.691 -c copy "004 Chapitre 5.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:11:37.062 -t 00:03:00.048 -c copy "005 Chapitre 6.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:14:37.110 -t 00:01:28.561 -c copy "006 Chapitre 7.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:16:05.671 -t 00:04:16.302 -c copy "007 Chapitre 8.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:20:21.973 -t 00:02:13.886 -c copy "008 Chapitre 9.mp4" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:22:35.859 -t 00:04:26.379 -c copy "009 Chapitre 10.mp4" & ^
echo Done!
```



Pour faire en sorte que FFmpeg effectue une conversion en MP3 64 kbps, on exécutera :
```
python split_audible.py pierre_et_le_loup.mp4 B00TKSFFJE "-b:a 64k -c:a mp3" mp3
```

Le script retournera :
```
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:00:00.000 -t 00:03:00.558 -b:a 64k -c:a mp3 "000 Chapitre 1.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:03:00.558 -t 00:02:33.112 -b:a 64k -c:a mp3 "001 Chapitre 2.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:05:33.670 -t 00:02:15.976 -b:a 64k -c:a mp3 "002 Chapitre 3.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:07:49.646 -t 00:01:42.725 -b:a 64k -c:a mp3 "003 Chapitre 4.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:09:32.371 -t 00:02:04.691 -b:a 64k -c:a mp3 "004 Chapitre 5.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:11:37.062 -t 00:03:00.048 -b:a 64k -c:a mp3 "005 Chapitre 6.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:14:37.110 -t 00:01:28.561 -b:a 64k -c:a mp3 "006 Chapitre 7.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:16:05.671 -t 00:04:16.302 -b:a 64k -c:a mp3 "007 Chapitre 8.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:20:21.973 -t 00:02:13.886 -b:a 64k -c:a mp3 "008 Chapitre 9.mp3" & ^
ffmpeg -i "pierre_et_le_loup.mp4" -ss 00:22:35.859 -t 00:04:26.379 -b:a 64k -c:a mp3 "009 Chapitre 10.mp3" & ^
echo Done!
``` 


## Installation
### Prérequis
- Python 3.7+ (non testé avec les versions précédentes)
- pip
- Librairies SSL

#### Sous Windows
##### Python
Allez sur ce site :  
https://www.python.org/downloads/windows/  
et suivez les instructions d'installation de Python 3.

##### Pip
- Téléchargez [get-pip.py](https://bootstrap.pypa.io/get-pip.py) dans un répertoire.
- Ouvrez une ligne de commande et mettez vous dans ce répertoire.
- Entrez la commande suivante :  
```
python get-pip.py
```
- Voilà ! Pip est installé !
- Vous pouvez vérifier en tapant la commande :  
```
pip -v
```

##### Librairies SSL
- Vous pouvez essayer de les installer avec la commande :  
```
pip install pyopenssl
```
- Vous pouvez télécharger [OpenSSL pour Windows](http://gnuwin32.sourceforge.net/packages/openssl.htm). 


#### Sous Linux
Si vous êtes sous Linux, vous n'avez pas besoin de moi pour installer Python, Pip ou SSL...  

### Téléchargement
- Vous pouvez cloner le repo git :  
```
git clone https://github.com/izneo-get/audible-tools.git
```
ou  
- Vous pouvez télécharger uniquement le binaire Windows (expérimental).  


### Configuration
(pour la version "script" uniquement)
```
pip install -r requirements.txt
```
